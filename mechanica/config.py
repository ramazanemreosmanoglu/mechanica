from pathlib import Path
import os
import json

CONFIG_FOLDER = Path(os.environ['HOME']) / ".config/mechanicalkeyboard"
CONFIG_FILE = CONFIG_FOLDER / "config.json"
EMPTY_JSON = {
    "packs": {},
}

def config_wrapper(fn):
    if not os.path.exists(CONFIG_FOLDER):
        os.mkdir(CONFIG_FOLDER)
    
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump(EMPTY_JSON, f, indent=4)

    return fn

@config_wrapper
def read_config(config_file):
    with open(config_file) as f:
        data = json.load(f)
    
    return data

@config_wrapper
def save_new_pack(name, path):
    # TODO
    pass