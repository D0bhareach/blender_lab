# Actual test script called from test_app Test Suite.
import bpy
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from util import create_solar_system, save_to_file, get_args

def main():
    
    p, w, h = get_args()
    # create logger for this module.
    log_path = p / 'test_simple.log'
    logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)
    
    create_solar_system()
    if not 'Camera' in bpy.data.objects:
        logging.error(f"Error: no Camera in blender scene")
    
    if not 'Earth' in bpy.data.objects:
        logging.error(f"Error: no Earth in blender scene")

    path = p / 'test_simple.png'
    save_to_file(path, w, h)
    if not path.exists:
        logging.error(f"No result png file at: {path}")
    bpy.ops.wm.quit_blender()

main()