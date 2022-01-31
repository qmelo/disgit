import os

import dotenv

dotenv.load_dotenv()

SECRET_KEY = os.environ['SECRET_KEY']
DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']
