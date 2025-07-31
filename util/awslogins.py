#! /usr/bin/env python3
import configparser
import os

config_path = os.path.expanduser('~/.aws/config')
config = configparser.ConfigParser()
config.read(config_path)

for section in config.sections():
    sso_start_url = config[section].get('sso_start_url')
    sso_session = config[section].get('sso_session')
    if sso_start_url:
        profile = section.replace('profile ', '')
        print(f"{profile}: {sso_start_url} ({sso_session})")