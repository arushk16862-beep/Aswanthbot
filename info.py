import re
from os import environ
from Script import script 

# ============================================================
# 🔹 REGEX PATTERN
# ============================================================
id_pattern = re.compile(r'^.\d+$')


# ============================================================
# 🔹 BOT INFORMATION
# ============================================================
SESSION = environ.get('SESSION', 'MyselfNeon')
API_ID = int(environ.get('API_ID', '21383441'))
API_HASH = environ.get('API_HASH', '62141d4cefa2756e4059cbdeac6ab46b')
BOT_TOKEN = environ.get('BOT_TOKEN', "7404094434:AAGisz2Uvj5dMSexmS8cBgivPNjkz0GiVl4")

# Keep-Alive URL
KEEP_ALIVE_URL = environ.get(
    "KEEP_ALIVE_URL",
    "https://aswanthbot.onrender.com"
)

# ============================================================
# 🔹 START PICTURES
# ============================================================

PICS = (
    environ.get(
        'PICS',
        'https://graph.org/file/856dedf2392bcc1f951ae-e69106494a12b6fd64.jpg '
        'https://graph.org/file/896e7de09b9b82a462b5d-57ada1a4e3c0e78edb.jpg '
        'https://graph.org/file/1b7d6ae759fe855473976-d92758327173dfce8c.jpg '
        'https://graph.org/file/eeaa288b0427c3a6823b9-7bbd05058b3d8cdf5d.jpg '
        'https://graph.org/file/4c95d72f9444c38f52bad-6a184f9fe5bc25a801.jpg '
        'https://graph.org/file/ab6a797daf50e79d95f2c-5e82a5874dddafa1d9.jpg '
        'https://graph.org/file/4112e27f4274c9e854084-6f2d50a7d477e5c949.jpg '
        'https://graph.org/file/5be655c4840f56462ead6-830918119cd9e9ce8b.jpg '
        'https://graph.org/file/ba697d84d93bd8b3fa53c-b55579f4b148d0aad3.jpg '
        'https://graph.org/file/adcffaa2028eb96c541ff-cc15dbdef2fcb4e41f.jpg '
        'https://graph.org/file/bea1103d928d2c49483af-4198216e69b4b22bdb.jpg '
        'https://graph.org/file/0ccacd8754076d74cd7d6-944bf809ce3b45f8be.jpg '
        'https://graph.org/file/859acb2a7be4604b9d586-a1fbaa80ac5eaa3dcb.jpg'
    )
).split()

# ============================================================
# 🔹 ADMINS & USERS
# ============================================================
ADMINS = [int(admin) if id_pattern.search(admin) else admin
          for admin in environ.get('ADMINS', '8587405600').split()]  # Multiple IDs separated by space

auth_users = [int(user) if id_pattern.search(user) else user
              for user in environ.get('AUTH_USERS', '').split()]  # Multiple IDs separated by space

AUTH_USERS = (auth_users + ADMINS) if auth_users else []


# ============================================================
# 🔹 CHANNELS AND GROUPS
# ============================================================
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003359134437'))
# This Channel Is For When User Start Your Bot Then Bot Send That User Name And Id In This Log Channel, Same For Group Also.

CHANNELS = [int(ch) if id_pattern.search(ch) else ch
            for ch in environ.get('CHANNELS', '-1002658908912 -1002312303135 -1003370992067').split()]
# This Is File Channel Where You Upload Your File Then Bot Automatically Save It In Database

REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False))  # True → request to join FSUB
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False))                # Retry button for FSUB

# Force Subscribe Channel
auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# File request channel
reqst_channel = environ.get('REQST_CHANNEL', '-1003359134437')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None

# Index request channel
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

# Bot support group
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1003254934811')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# File store channel (/batch command)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1003359134437')).split()]

# Delete channel(s)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch
                   for dch in environ.get('DELETE_CHANNELS', '-1002231967338').split()]


# ============================================================
# 🔹 DATABASE
# ============================================================
DATABASE_URI = environ.get(
    'DATABASE_URI',
    "mongodb+srv://ASMOVIE_DD:ASMOVIE_DDD@cluster0.1riyjj1.mongodb.net/?appName=Cluster0"
)

DATABASE_NAME = environ.get('DATABASE_NAME', "NeonFilter")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'neoncollection')

MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', False))

# Separate DBs if MULTIPLE_DATABASE = True
O_DB_URI = environ.get('O_DB_URI', "")  # This Db Is For Other Data Store
F_DB_URI = environ.get('F_DB_URI', "")  # This Db Is For File Data Store
S_DB_URI = environ.get('S_DB_URI', "")  # This Db is for File Data Store When First Db Is Going To Be Full

if not MULTIPLE_DATABASE:
    USER_DB_URI = OTHER_DB_URI = FILE_DB_URI = SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = O_DB_URI
    FILE_DB_URI = F_DB_URI
    SEC_FILE_DB_URI = S_DB_URI


# ============================================================
# 🔹 PREMIUM AND REFERAL 
# ============================================================
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', False)) # Set Ture Or False

# If PREMIUM_AND_REFERAL_MODE is True Then Fill Below Variable, If False Then No Need To Fill.
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', False))

REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '5'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://files.catbox.moe/tc8drk.jpg')
PAYMENT_TEXT = environ.get(
    'PAYMENT_TEXT',
    '<b><blockquote>‣ 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐏𝐋𝐀𝐍𝐒 📝</blockquote>\n'
    '<i>• 30Rs - 01 Week\n• 50Rs - 01 Month\n• 120Rs - 03 Months\n• 220Rs - 06 Months</i>\n\n'
    '<blockquote>‣ 𝐏𝐋𝐀𝐍 𝐁𝐄𝐍𝐄𝐅𝐈𝐓𝐒 ✨</blockquote>\n'
    '<i>• No Need To Verify\n• No Need To Open Links\n• Direct Files\n• Ad-Free Experience\n'
    '• High Speed Download\n• Multiplayer Streaming Links\n• Unlimited Movies, Animes & Series\n'
    '• 24×7 Admin Support\n• Requests Will Be Completed Within 01 Hour Of Submission If Available</i>\n\n'
    '<blockquote>‣ 𝐔𝐏𝐈 𝐈𝐃 🆔</blockquote> - <code>neonan23@ibl</code>\n\n'
    '<i>• Click /myplan To Check Your Plan\n• Send Screenshots After Payment\n'
    '• After Sending Screenshot Give Us Some Time To Add You In Premium</i></b>'
)

# ============================================================
# 🔹 CLONE SETTINGS
# ============================================================
# Clone Information : If Clone Mode Is True Then Bot Clone Other Bots.
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', "") # Necessary If clone mode is true
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', 'AnimeZerox') # Public Channel Username Without @ or without https://t.me/ and Bot Is Admin With Full Right.


# ============================================================
# 🔹 LINKS
# ============================================================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Cinema_Lokam_Movies_Group')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Cinema_Updates_OTT')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Cinema_Clone_BOT_Support') # Support Chat Link Without https:// or @
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/Ascreator_10')


# ============================================================
# 🔹 FEATURES (True/False Switches)
# ============================================================
AI_SPELL_CHECK = bool(environ.get('AI_SPELL_CHECK', True))
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
BUTTON_MODE = bool(environ.get('BUTTON_MODE', True))
MAX_BTN = bool(environ.get('MAX_BTN', True))
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
IMDB = bool(environ.get('IMDB', False))
AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", False))
SPELL_CHECK_REPLY = bool(environ.get("SPELL_CHECK_REPLY", True))
MELCOW_NEW_USERS = bool(environ.get('MELCOW_NEW_USERS', True))
PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', False))
PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', True))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))


# ============================================================
# 🔹 TOKEN VERIFICATIONS
# ============================================================
VERIFY = bool(environ.get('VERIFY', False))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', '')

# If You Fill Second Shortner Then Bot Attach Both First And Second Shortner And Use It For Verify.
VERIFY_SECOND_SHORTNER = bool(environ.get('VERIFY_SECOND_SHORTNER', False))
# if verify second shortner is True then fill below url and api
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')


# ============================================================
# 🔹 SHORTLINK SETTINGS
# ============================================================
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
TUTORIAL = environ.get('TUTORIAL', '')


# ============================================================
# 🔹 MISCELLANEOUS SETTINGS
# ============================================================
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
MAX_B_TN = environ.get("MAX_B_TN", "10")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Powered by @Aswanthcreator ❤️✨')

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)


# ============================================================
# 🔹 FILTER OPTIONS
# ============================================================
LANGUAGES = ["malayalam", "mal", "tamil", "tam", "english", "eng", "hindi", "hin",
             "telugu", "tel", "kannada", "kan"]

SEASONS = [f"season {i}" for i in range(1, 11)]

EPISODES = [f"E{i:02}" for i in range(1, 41)]

QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]

YEARS = [str(year) for year in range(1900, 2026)]


# ============================================================
# 🔹 STREAMING & DOWNLOAD
# ============================================================
STREAM_MODE = bool(environ.get('STREAM_MODE', True))

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = True
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 min

ON_HEROKU = 'DYNO' in environ
URL = environ.get("URL", "https://aswanthbot.onrender.com/").rstrip("/") + "/"


# ============================================================
# 🔹 RENAME
# ============================================================
RENAME_MODE = bool(environ.get('RENAME_MODE', False)) # Set True or False
# Rename Info : If True Then Bot Rename File Else Not


# ============================================================
# 🔹 AUTO APPROVE
# ============================================================
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False))  # Set True or False
# Auto Approve Info : If True Then Bot Approve New Upcoming Join Request Else Not


# ============================================================
# 🔹 START COMMAND REACTIONS
# ============================================================
REACTIONS = [
    "🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩",
    "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡",
    "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]
# Don't add unsupported emojis because Telegram reactions have limits


# Dont remove Credits
# Developer Telegram @MyselfNeon
# Update channel - @NeonFiles















