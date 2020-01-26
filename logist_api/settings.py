import pathlib
import yaml
import os

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = os.path.join(BASE_DIR, 'config', 'logist_api.yml')


def get_config(path):
    with open(path) as f:
        config_file = yaml.safe_load(f)
        return config_file


config = get_config(config_path)
