#!/usr/bin/env python
from resource_management import *

# server configurations
config = Script.get_config()

dist_name = config['configurations']['nslcd-config']['distinguished.name']
groups_name = config['configurations']['nslcd-config']['groups.name']
users_name = config['configurations']['nslcd-config']['users.name']
ldap_url = config['configurations']['nslcd-config']['ldap.url']
nslcd_template_config = config['configurations']['nslcdconf-env']['content']
#nslcd_template_config = config['configurations']['nslcd-config']['content']

nsswitch_template_config = config['configurations']['nsswitch-env']['content']

