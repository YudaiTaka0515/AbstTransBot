# coding: utf-8
import yaml


def load_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as yml:
        config = yaml.load(yml, Loader=yaml.SafeLoader)
        return config
