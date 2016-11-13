# -*- coding: utf-8 -*-
# Gunicorn WSGI compatible Service

import os
import sys

path = os.getcwd()
sys.path.append(path)

# noinspection PyUnresolvedReferences
from pandaservice import app as application