import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("Internal"):
    load_dotenv("Internal")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCRh2NShX4Ak3r736nfbD62ktcDawRzEkt6bmfYUyJ9ADQCwDArxi1AozRAchk0kK0JUu-dbKl1L08OxaX1aTX7CEdX87RVDYAaKhy5vYW0hEsPIi6e9k8VX7RPoIErry9I9lmpnDiV68lhQKoPlhQRlVde3Ly9v8azFssEDMBCcvF6WXIrG3PE4rn03nd-pCYRLyk9GhWOL_gkwvZsUJQDsWFxbScqdZRuBZcaXKX-KzokAThoNH3ZIV3p9xhwHPMYGZv9fJAoL4lQaRD8IaNXzhK1iCk3PgyUzPt_eO77H66L6naGffMxr1g-8YbdEEG32-MOd7pp9n5aqMpHPVOGAAAAAWCsG3gA")
BOT_TOKEN = getenv("BOT_TOKEN", "5894209648:AAF1waPORM1VIJ_J7XSTywlVf7JOoKOoBIU")
BOT_NAME = getenv("BOT_NAME", "Sopia ᴍᴜsɪᴄ")
API_ID = int(getenv("API_ID", "12227067"))
API_HASH = getenv("API_HASH", "b463bedd791aa733ae2297e6520302fe")
OWNER_NAME = getenv("OWNER_NAME", "AM_YTBOTT")
ALIVE_NAME = getenv("ALIVE_NAME", "Sopia ᴍᴜsɪᴄ")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "am_bot12313")
BOT_USERNAME = getenv("BOT_USERNAME", "Defulter4_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", ".")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AM_YTSUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AMBOTYT")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6204761408").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/62a110de948ea71bf071f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SatyamMusic/SophiaMusic")
IMG = getenv("IMG", "https://telegra.ph/file/62a110de948ea71bf071f.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/62a110de948ea71bf071f.jpg")
