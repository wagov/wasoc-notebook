#!/usr/bin/env python3
from subprocess import run

# Basic setup for pulling in useful shared deps in a The Littlest Jupyter Hub environment
run("sudo -E conda install pandas numpy", shell=True)
run("sudo -E pip install -r requirements.txt", shell=True)
