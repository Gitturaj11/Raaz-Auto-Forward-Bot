from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "136b7d8c2c5fbb04a3ea88182b02aed4")
      API_ID = int(getenv("API_ID", "26386383"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6349359474:AAEb3h1LSg9SjjYRnzna5xtgtCD4C0g-FQ4")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002021034685:-1001942056256").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
