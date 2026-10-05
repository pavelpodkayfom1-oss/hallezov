import os
import sys
import runpy

base = os.path.dirname(os.path.abspath(__file__))
bot_dir = os.path.join(base, "test")
os.chdir(bot_dir)
sys.path.insert(0, bot_dir)
runpy.run_path(os.path.join(bot_dir, "main.py"), run_name="__main__")
