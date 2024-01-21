import os
import json

def load_config():
    scrip_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(scrip_dir, 'config.json')
    with open(config_path, 'r') as file:
        info = json.load(file)
    return info

data = load_config()
