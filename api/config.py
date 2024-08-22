import yaml

with open('../config.yaml', 'r') as file:
    PLUGINS = yaml.safe_load(file)['plugins']
