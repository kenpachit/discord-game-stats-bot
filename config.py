import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

class Config:
    
    def __init__(self):
        self.bot_token = self._get_env_variable('BOT_TOKEN')
        self.api_keys = {
            'game_platform_1': self._get_env_variable('GAME_PLATFORM_1_API_KEY'),
            'game_platform_2': self._get_env_variable('GAME_PLATFORM_2_API_KEY'),
        }

    def _get_env_variable(self, var_name):
        value = os.getenv(var_name)
        if value is None:
            logging.error(f'Missing required environment variable: {var_name}')
        return value

    def get_bot_token(self):
        return self.bot_token
    
    def get_api_key(self, platform_name):
        api_key = self.api_keys.get(platform_name)
        if api_key is None:
            logging.error(f'API key for {platform_name} not found.')
        return api_key

config = Config()
bot_token = config.get_bot_token()
game_platform_1_api_key = config.get_api_key('game_platform_1')

if bot_token:
    logging.info('Bot token retrieved successfully.')
else:
    logging.error('Bot token could not be retrieved. Check your environment variables.')

if game_platform_1_api_key:
    logging.info('Game platform 1 API key retrieved successfully.')
else:
    logging.error('Game platform 1 API key could not be retrieved. Check your environment variables.')