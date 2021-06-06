import yaml


def load_config():
    with open('config.yml', 'r') as yml:
        config = yaml.load(yml, Loader=yaml.SafeLoader)
        return config
