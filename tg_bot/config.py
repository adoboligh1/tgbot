from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 504913071  # my telegram ID
    OWNER_USERNAME = "whereareyoufrom"  # my telegram username
    API_KEY = "1133019257:AAHg0eoN279ZL9dWcfqmEc_re7_g7zbVs3E"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://joey:YounG.,12j@localhost:5432/joey'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [504913071]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
