from AM.core.bot import Alone
from AM.core.dir import dirr
from AM.core.git import git
from AM.core.userbot import Userbot
from AM.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Alone()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
