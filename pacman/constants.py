# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------

from game.casting.color import Color

# GAME
GAME_NAME = "Pac-man"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 980
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = (SCREEN_HEIGHT / 2) - 100

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "pacman/assets/fonts/lot.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
INTRO_SOUND = "pacman/assets/sounds/pacman_beginning.wav"
OVER_SOUND = "pacman/assets/sounds/pacman_death.wav"
LOOP_SOUND = "pacman/assets/sounds/wakawaka.mp3"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
RED = Color(255, 0, 0)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"


# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4


# --------------------------------------------------------------------------------------------------
# SCRIPTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# --------------------------------------------------------------------------------------------------
# CASTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5


# BOARD
BOARD_GROUP = "Board"
BOARD_FILE = "pacman/assets/data/board.txt"
BOARD_IMG_PATH = "pacman/assets/images/"
BRICK_WIDTH = 31
BRICK_HEIGHT = 31


# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "READY!"
PREP_TO_LAUNCH = "READY!"
WAS_GOOD_GAME = "GAME OVER"


# HERO

HERO_GROUP = "hero"
HERO_IMAGE_U = "pacman/assets/images/hero_u.png"
HERO_IMAGE_R = "pacman/assets/images/hero_r.png"
HERO_IMAGE_L = "pacman/assets/images/hero_l.png"
HERO_IMAGE_D = "pacman/assets/images/hero_d.png"
HERO_IMAGE_O = "pacman/assets/images/hero_0.png"

HERO_IMAGES = {
    "up": HERO_IMAGE_U,
    "right": HERO_IMAGE_R,
    "left": HERO_IMAGE_L,
    "down": HERO_IMAGE_D,
    "o": HERO_IMAGE_O
}

HERO_IMAGE = "pacman/assets/images/hero_u.png"
HERO_DELAY = 0
HERO_RATE = 10
HERO_WIDTH = 28
HERO_HEIGHT = 28
HERO_VELOCITY = 6

HERO_INIT_X = CENTER_X - HERO_WIDTH / 2
HERO_INIT_Y = SCREEN_HEIGHT - 277


# GHOST

GHOST_GROUP = "ghost"
GHOST_RED = "pacman/assets/images/ghost_red.png"
GHOST_BLUE = "pacman/assets/images/ghost_blue.png"
GHOST_ORANGE = "pacman/assets/images/ghost_orange.png"
GHOST_PINK = "pacman/assets/images/ghost_pink.png"
GHOST_WIDTH = 31
GHOST_HEIGHT = 31
GHOST_INIT_Y = SCREEN_HEIGHT - 385
GHOST_INIT_X = CENTER_X - GHOST_WIDTH / 2
