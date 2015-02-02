#!/usr/bin/env python
from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()

dist_name = config['configurations']['nslcd-config']['distinguished.name']
groups_name = config['configurations']['nslcd-config']['groups.name']
users_name = config['configurations']['nslcd-config']['users.name']
