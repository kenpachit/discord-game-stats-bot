import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    
    def __init__(self):
        self.bot_token = os.getenv('BOT_TOKEN')
        self.api_keys = {
            'game_platform_1': os.getenv('GAME_PLATFORM_1_API_KEY'),
            'game_platform_2': os.getenv('GAME_PLATFORM_2_API_KEY'),
        }

    def get_bot_token(self):
        return self.bot_token
    
    def get_api_key(self, platform_name):
        return self.api_keys.get(platform_name)

config = Config()
bot_token = config.get_bot_token()
game_platform_1_api_key = config.get_api_key('game_platform_1')