from dotenv import load_dotenv

load_dotenv()  # This will load the variables from .env into os.environ

import os


class BOT:
    """
    TOKEN: Bot token generated from @BotFather
    """

    TOKEN = os.environ.get("TOKEN", "")


class API:
    """
    HASH: Telegram API hash from https://my.telegram.org
    ID = Telegram API ID from https://my.telegram.org
    """

    HASH = os.environ.get("API_HASH", "42a60d9c657b106370c79bb0a8ac560c")
    ID = int(os.environ.get("API_ID","14050586"))


class OWNER:
    """
    ID: Owner's user id, get it from @userinfobot
    """

    ID = int(os.environ.get("OWNER","5738579437"))


class WEB:
    """
    PORT: Specific port no. on which you want to run your bot, DON'T TOUCH IT IF YOU DON'T KNOW WHAT IS IT.
    """

    PORT = int(os.environ.get("PORT", 8000))
