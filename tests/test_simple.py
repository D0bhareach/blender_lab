# Actual test script called from test_app Test Suite.
import bpy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from util import creat_solar_system, save_to_file

def main():
    creat_solar_system()
    save_to_file('test_simple.png')
    bpy.ops.wm.quit_blender()


main()