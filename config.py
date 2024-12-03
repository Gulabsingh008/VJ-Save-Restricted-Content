import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24519654"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1ccea9c29a420df6a6622383fbd83bcd")

#Database 
DB_URI = os.environ.get("DB_URI", "")
