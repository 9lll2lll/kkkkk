## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBDimEmaLMf6g0t57HVbto876EudE31jevuyRxtcWlPhZv76vn6qrcOpvssgYMUCIBoaoLeZouN9DQHX5lIv9Y_9_NyHYhiArHHXNLlMVUw91F70yosstLE3B6XJjy8vx55xbgQeLG-VXcS0rABMW3MUykUebfKpeAFSyr_lFySxEdFlv7i55-KoV1AaAnnZdQAbJLk9LAifaJVa5DwsXDCKvlP7vTZyvGNYJBjQ-zzAbK5oEbMfsPx5zRyI0oGR2d9nTJ9L9hXyIggs-zhdbVc7HKuj2SnL-tWI24xHveEXRLdSRA_c1epNDFOx6HfuBKitM6CJcAVXgfpqfMIu0-4NOA0PwA")
BOT_TOKEN = getenv("BOT_TOKEN", "5454692767:AAFHj6GgGAGwa7Q9sbnjfR4SpboAiknnA84")
BOT_NAME = getenv("BOT_NAME", "G3X66")
API_ID = int(getenv("API_ID", "6817364"))
API_HASH = getenv("API_HASH", "b2aea0b75ceca34bf5333107ac526c02")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ii321")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "G3X66bot")
OWNER_ID = getenv("OWNER_ID", "887108671")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "k_6_6")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ll2ll3")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ll2ll3")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "887108671").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
