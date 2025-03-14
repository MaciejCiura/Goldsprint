
# Bike
class Bike:
    BIKE_WIDTH = 50
    BIKE_HEIGHT = 50
    MOVE_INCREMENT = 100

# Colors
class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GOLD = (255, 215, 0)


class Screen:
    FRAMERATE = 60
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400
    MAX_DISTANCE = SCREEN_WIDTH - Bike.BIKE_WIDTH - 20
    STARTING_POSITION = 50
    PROGRESSBAR_WIDTH = SCREEN_WIDTH - 40
    PROGRESSBAR_HEIGHT = 20
    BIKE1_Y = 20
    BIKE2_Y = 170
    PROGRESSBAR1_Y = 100
    PROGRESSBAR2_Y = 120
    PROGRESSBAR_INITIAL_VALUE = 20
    WINDOW_CAPTION="Goldsprint"
    FONT_SIZE=74