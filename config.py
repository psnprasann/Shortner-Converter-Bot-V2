# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "15432910"))
API_HASH = os.environ.get("API_HASH", "bf3b5a92497cf5744e6310f309b5490a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6356613407:AAFd5nLh7iNIq1Xe55e-38EjzrpAZB7gb6k")
ADMINS = [int(i.strip()) for i in os.environ.get("5234476249").split("Owner Id")] if os.environ.get("5234476249") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Paramathma")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Paramathma:Paramathma@cluster0.qno5wbm.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5234476249")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Updates Channel User name Without @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
