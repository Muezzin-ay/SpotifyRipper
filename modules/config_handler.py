
import json
import os


def check_settings_file() :
    if not os.path.isfile('./config.json') :
        with open('./config.json', 'w') as file:
            file.write('{"api_client" : "", "api_secret" : "", "spotify_username" : "", "album_id" : ""}')
            return False
    return True


def load_settings() :
    with open('./config.json') as file:
        settings = json.load(file)
        file.close()
    return settings