
from constants import *
from game.casting.stats import Stats
from game.services.raylib.raylib_video_service import RaylibVideoService
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.scripting.change_scene_action import ChangeSceneAction
from game.casting.text import Text 
from game.casting.point import Point
from game.casting.label import Label
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.play_sound_action import PlaySoundAction,PlayBackGroundSound
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.casting.hero import Hero
from game.casting.image import Image
from game.casting.body import Body
from game.scripting.draw_hero_action import DrawHeroAction
from game.casting.animation import Animation
from game.scripting.draw_ghost_action import DrawGhostAction
from game.scripting.control_hero_action import ControlHeroAction
from game.scripting.move_hero_action import MoveHeroAction
from game.scripting.colide_ghost_action import ColideGhostAction
from game.services.raylib.raylib_physics_service import RaylibPhysicsService




class SceneManager:

    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    AUDIO_SERVICE = RaylibAudioService()
    PHYSICS_SERVICE = RaylibPhysicsService()

    MUSIC         = PlayBackGroundSound(AUDIO_SERVICE, LOOP_SOUND)
    KEYBOARD_SERVICE = RaylibKeyboardService()

    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_HERO_ACTION = DrawHeroAction(VIDEO_SERVICE)
    DRAW_GHOST_ACTION = DrawGhostAction(VIDEO_SERVICE)
    CONTROL_HERO_ACTION = ControlHeroAction(KEYBOARD_SERVICE)
    MOVE_HERO_ACTION    = MoveHeroAction()
    COLIDE_GHOST_ACTION = ColideGhostAction(PHYSICS_SERVICE,AUDIO_SERVICE)

    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    
    
    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):

        print(f"Prepare Scene: {scene}")

        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        #elif scene == NEXT_LEVEL:
        #    self._prepare_next_level(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script) 
       
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)

        
    def _prepare_new_game(self, cast, script):
        
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_hero(cast)

        self._add_ghost(cast)
        self._add_dialog(cast, ENTER_TO_START)
        
        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 4))
        #script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        script.add_action(OUTPUT,PlaySoundAction(self.AUDIO_SERVICE, INTRO_SOUND))


    def _prepare_try_again(self, cast, script):
        self._add_hero(cast)
        self._add_ghost(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

        
    def _prepare_game_over(self, cast, script):
        self._add_ghost(cast)
        self._add_hero(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        #script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    def _prepare_in_play(self,cast,script):

        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_HERO_ACTION)

        self._add_update_script(script)
        self._add_output_script(script)
        

        script.add_action(OUTPUT,self.MUSIC)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _add_stats(self, cast):

        ''' Manage the information in the game'''
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_hero(self, cast):
        cast.clear_actors(HERO_GROUP)
        position = Point(HERO_INIT_X, HERO_INIT_Y)
        size = Point(HERO_WIDTH, HERO_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(HERO_IMAGE)

        #Animation, open/close
        animation = Animation([
            HERO_IMAGE_U,
            HERO_IMAGE_O
        ], HERO_RATE, HERO_DELAY)

        hero = Hero(body, animation, image, True)
        cast.add_actor(HERO_GROUP, hero)      


    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)


    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)


    def _add_ghost(self,cast):
        cast.clear_actors(GHOST_GROUP)
        x = (CENTER_X - HERO_WIDTH / 2) 
        y = (SCREEN_HEIGHT / 2 )   
        position = Point(x, y)
        size = Point(GHOST_WIDTH, GHOST_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(GHOST_RED)




        #Animation, 
        animation = Animation([
            GHOST_RED,
            GHOST_RED
        ], HERO_RATE, HERO_DELAY)

        heror = Hero(body, animation, image, True)
        x = (CENTER_X - HERO_WIDTH / 2) - GHOST_WIDTH
      
        position = Point(x, y)
        body = Body(position, size, velocity)

        image = Image(GHOST_BLUE)
        animation = Animation([
            GHOST_BLUE,
            GHOST_BLUE
        ], HERO_RATE, HERO_DELAY)

        herob = Hero(body, animation, image, True)

        x = (CENTER_X - HERO_WIDTH / 2) +  GHOST_WIDTH
        position = Point(x, y)
        body = Body(position, size, velocity)

        image = Image(GHOST_ORANGE)
        animation = Animation([
            GHOST_ORANGE,
            GHOST_ORANGE
        ], HERO_RATE, HERO_DELAY)
        heroo = Hero(body, animation, image, True)


        x = (CENTER_X - HERO_WIDTH / 2) 
        y = (SCREEN_HEIGHT / 2 ) - GHOST_HEIGHT
        position = Point(x, y)
        body = Body(position, size, velocity)

        image = Image(GHOST_PINK)
        animation = Animation([
            GHOST_PINK,
            GHOST_PINK
        ], HERO_RATE, HERO_DELAY)
        herop = Hero(body, animation, image, True)

        

        cast.add_actor(GHOST_GROUP, heror)      
        cast.add_actor(GHOST_GROUP, herob)      
        cast.add_actor(GHOST_GROUP, heroo) 
        cast.add_actor(GHOST_GROUP, herop) 
    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)



    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    

    def _add_output_script(self, script):
        print("output script")
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_HERO_ACTION)
        script.add_action(OUTPUT, self.DRAW_GHOST_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
       
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)
        
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        
        script.add_action(UPDATE, self.MOVE_HERO_ACTION)
        script.add_action(UPDATE, self.COLIDE_GHOST_ACTION)



    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
     