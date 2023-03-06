# Actual test script called from test_app Test Suite.
import bpy
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from util import *

def main():
    
    p, w, h = get_args()
    # create logger for this module.
    log_path = p / 'test_simple.log'
    logger = get_logger('test_simple', log_path)
    # logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)
    logger.info('run test')
    
    delete_defaults()
    create_solar_system()
    if not 'Camera' in bpy.data.objects:
        logger.error(f"Error: no Camera in blender scene")
    
    if not 'Earth' in bpy.data.objects:
        logger.error(f"Error: no Earth in blender scene")
    
    add_light('Light', -14.4, 0, 0)

    path = p / 'test_simple.png'
    save_to_file(path, w, h)
    if not path.exists:
        logger.error(f"No result png file at: {path}")
    bpy.ops.wm.quit_blender()

main()