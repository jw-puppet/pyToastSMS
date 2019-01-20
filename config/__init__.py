import yaml

_CONFIG_PATH = './config/config.yml'
_API_MAP_PATH = './config/secret.yml'

with open(_CONFIG_PATH, 'r') as f:
    secret = yaml.load(f)

with open(_API_MAP_PATH, 'r') as f:
    api = yaml.load(f)
