import bpy
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from util import *
from test_material import color_planets

def main():
    
    p, w, h = get_args()
    # print(f'in light p = {p}')
    log_path = p / 'test_light.log'
    logger = get_logger('test_light', log_path)
    logger.info('run test')
    # create logger for this module.
    # logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)
    # logging.info('log from light test')
    delete_defaults()
    create_solar_system()
    color_planets()

    add_light('Light_1', -14.5, 0, 0)    
    add_light('Light_2', -20.5, 0, 50)    
    add_light('Light_3', -25, 0, -50)

    add_light('Light_4', -34.5, 50, 50)    
    add_light('Light_5', -26.5, 50, 0)    
    add_light('Light_6', -34.5, 50, -50)

    add_light('Light_7', -34.5, -50, 50)    
    add_light('Light_8', -25.5, -50, 0)    
    add_light('Light_9', -37.5, -50, -50)

    add_light('Light_10', -24.5, -25.0, 50)    
    add_light('Light_11', -15.5, -25.0, 0)    
    add_light('Light_12', -25.5, -25.0, -50)
    
    lights = [l for l in bpy.data.objects if l.name.find('Light_') != -1]
    if len(lights) != 12:
        logger.error(f"There are {len(lights)} in scene, must be 12")
    


    path = p / 'test_light.png'
    save_to_file(path, w, h)
    if not path.exists:
        logging.error(f"No result png file at: {path}")
    bpy.ops.wm.quit_blender()

main()