import bpy
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from util import create_solar_system, save_to_file, get_args

def add_light(name, x, y, z):
    light_data = bpy.data.lights.new(name=name, type='POINT')
    light_data.energy = 3000.0
    light_data.color = (0.993, 1.0, 0.012)

    light_object = bpy.data.objects.new(name=name, object_data=light_data)
    light_object.location = [x, y, z]
    bpy.context.collection.objects.link(light_object)
    return light_object


def main():
    
    p, w, h = get_args()
    # create logger for this module.
    log_path = p / 'test_light.log'
    logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)
    
    create_solar_system()
    # remove standard light
    original = bpy.data.objects.get('Light')
    if original != None:
        bpy.data.objects.remove(original)

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
    
    lights = [l for l in bpy.data.objects if l.name.find('ight_') != -1]
    if len(lights) != 12:
        logging.error(f"There are {len(lights)} in scene, must be 12")
    


    path = p / 'test_light.png'
    save_to_file(path, w, h)
    if not path.exists:
        logging.error(f"No result png file at: {path}")
    bpy.ops.wm.quit_blender()

main()