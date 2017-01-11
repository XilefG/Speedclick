import sys #system tools
import os

VERSION = '0.0'
PLATFORM = sys.platform
BASE_PATH = os.path.dirname(os.getcwd())
# Use platform to determine which button is right-click.
RIGHT_BTN_NUM = 2 if PLATFORM == 'darwin' else 3 #darwin is mac
# Boolean - check if app is running from exe package.
IN_EXE = hasattr(sys, 'frozen')
BIG = 1e10

##Button states
# Must be a negative integer for use in integer numpy array representing the
# board.
UNCLICKED = -101
MINE = -100
FLAGGED = 'flagged'
CLICKED = 'clicked'

##Drag-select flagging type
UNFLAG = 'unflag'
FLAG = 'flag'

##Game states
READY = 'ready'
ACTIVE = 'active'
WON = 'won'
LOST = 'lost'
INACTIVE = 'inactive'
CREATE = 'create'

##Minefield origins
OFFICIAL = 'official'
REGULAR = 'regular'
KNOWN = 'known'

default_settings = {
    'dims': (8, 8),
    'mines': 10,
    'drag_select': False,
    'btn_size': 16 #pixels
    }
