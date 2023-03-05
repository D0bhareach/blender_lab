# Actual test script called from test_app Test Suite.
import bpy
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from util import creat_solar_system, save_to_file, get_args

def add_material(obj, material_name, r, g, b):
    material = bpy.data.materials.get(material_name)
    if material is None:
        material = bpy.data.materials.new(material_name)
    material.use_nodes = True
    principled_bsdf = material.node_tree.nodes['Principled BSDF']
    if principled_bsdf is not None:
        principled_bsdf.inputs[0].default_value = (r, g, b, 1)  
    obj.active_material = material

def main():
    
    p, w, h = get_args()
    # create logger for this module.
    log_path = p / 'test_material.log'
    logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)
    
    # Create stub
    creat_solar_system()
    if not 'Camera' in bpy.data.objects:
        logging.error(f"Error: no Camera in blender scene")
    
    if not 'Earth' in bpy.data.objects:
        logging.error(f"Error: no Earth in blender scene")

    # create materials and assign them to spheres
    s = bpy.data.objects['Sun']
    add_material(s, "Sun", 255, 255, 153)
    mat = bpy.data.materials.get("Sun")
    logging.info("Sun is white")
    
    e = bpy.data.objects['Earth']
    add_material(e, "Earth", 0, 51, 103)
    logging.info("Earth is blue")

    v = bpy.data.objects['Venus']
    add_material(v, "Venus", 0, 153, 0)
    logging.info("Venus is green")

    me = bpy.data.objects['Mercury']
    add_material(me, "Mercury", 0, 0, 0)
    logging.info("Mercury is black")

    ma = bpy.data.objects['Mars']
    add_material(ma, "Mars", 204, 0, 0)
    logging.info("Mars is red")

    path = p / 'test_material.png'
    save_to_file(path, w, h)
    if not path.exists:
        logging.error(f"No result png file at: {path}")
    bpy.ops.wm.quit_blender()

main()
