#!/usr/bin/env python
"""
pytest plugin script.

This script is an extension to py.test which
installs SQLAlchemy's testing plugin into the local environment.

"""
import sys
import os

for pth in ['../lib']:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), pth))


# use bootstrapping so that test plugins are loaded
# without touching the main library before coverage starts
bootstrap_file = os.path.join(
    os.path.dirname(__file__), "..", "lib", "sqlalchemy",
    "testing", "plugin", "bootstrap.py"
)

with open(bootstrap_file) as f:
    code = compile(f.read(), "bootstrap.py", 'exec')
    to_bootstrap = "pytest"
    exec(code, globals(), locals())
    from pytestplugin import *  # noqa
