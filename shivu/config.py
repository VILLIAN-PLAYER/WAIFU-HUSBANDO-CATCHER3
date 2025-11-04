class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1813373023"
    sudo_users = "1813373023"
    GROUP_ID = -1003208855424
    TOKEN = "6513221042:AAEOYACtqIz52dDwg9p67XPCRMQsgH52iBo"
    mongo_url = "mongodb+srv://indonesiatata07_db_user:<db_password>@cluster0.pgglnny.mongodb.net/?appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "infvibe"
    UPDATE_CHAT = "waifu_private"
    BOT_USERNAME = "ZERO_TWO_R0BOT"
    CHARA_CHANNEL_ID = "-1002074617147"
    api_id = 21846639
    api_hash = "2cebc99bd8378b5237b31ea8e7496d79"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
