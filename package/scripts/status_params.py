#!/usr/bin/env python
from resource_management import *

config = Script.get_config()
nslcd_template_config = config['configurations']['nslcdconf-env']['content']

