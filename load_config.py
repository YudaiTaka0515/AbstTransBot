import yaml


def load_config(config_file):
    with open(config_file, 'r') as yml:
        config = yaml.load(yml, Loader=yaml.SafeLoader)
        return config
