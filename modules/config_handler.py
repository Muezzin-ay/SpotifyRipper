
import json
import os


STD_CONFIG_FILE = '''
{
    "api_client" : "", 
    "api_secret" : "", 
    "spotify_username" : "", 
    "album_id" : ""
}
'''


class ConfigHandler :

    @staticmethod
    def check_settings_file() :
        if not os.path.isfile('./config.json') :
            with open('./config.json', 'w') as file:
                file.write(STD_CONFIG_FILE)
                return False
        return True

    @staticmethod
    def load_settings() :
        with open('./config.json') as file:
            settings = json.load(file)
            file.close()
        return settings