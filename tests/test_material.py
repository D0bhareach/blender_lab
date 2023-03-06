# Actual test script called from test_app Test Suite.
import bpy
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from util import *

def add_material(obj, material_name, r, g, b):
    material = bpy.data.materials.get(material_name)
    if material is None:
        material = bpy.data.materials.new(material_name)
    material.use_nodes = True
    principled_bsdf = material.node_tree.nodes['Principled BSDF']
    if principled_bsdf is not None:
        principled_bsdf.inputs[0].default_value = (r, g, b, 1)  
    obj.active_material = material

def color_planets():
    s = bpy.data.objects['Sun']
    add_material(s, "Sun", 1, 0.991, 0.163)

    
    e = bpy.data.objects['Earth']
    add_material(e, "Earth", 0.201, 0.342, 1)

    v = bpy.data.objects['Venus']
    add_material(v, "Venus", 1, 0.048, 0.092)

    me = bpy.data.objects['Mercury']
    add_material(me, "Mercury", 1, 0.297, 0.043)

    ma = bpy.data.objects['Mars']
    add_material(ma, "Mars", 1, 0.007, 0.062)


def main():
    
    p, w, h = get_args()
    log_path = p / 'test_material.log'
    logger = get_logger('test_material', log_path)
    logger.info('test run')
    # create logger for this module.
    # logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)
    
    delete_defaults()
    create_solar_system()
    if not 'Camera' in bpy.data.objects:
        logger.error(f"Error: no Camera in blender scene")
    
    if not 'Earth' in bpy.data.objects:
        logger.error(f"Error: no Earth in blender scene")

    # create materials and assign them to spheres
    color_planets()

    add_light('Light', -14.4, 0, 0)

    path = p / 'test_material.png'
    save_to_file(path, w, h)
    if not path.exists:
        logger.error(f"No result png file at: {path}")
    bpy.ops.wm.quit_blender()

main()
