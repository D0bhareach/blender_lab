import bpy
import mathutils
import time
import os
import sys
from pathlib import PurePath, Path
import logging
from logging.handlers import RotatingFileHandler


# docs: https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cube_add
# def add_cube(
#         name,
#         size = 1.0,
#         location = [0.0, 0.0, 0.0],
#         rotation = [0.0, 0.0, 0.0],
#         scale = [1.0, 1.0, 1.0]):
#     bpy.ops.mesh.primitive_cube_add(
#         size=size,
#         calc_uvs=True,
#         enter_editmode=False,
#         align='WORLD',
#         location=location,
#         rotation=rotation,
#         scale=scale,
#     )
#     c = bpy.context.scene.objects['Cube']
#     c.name = name
# 
#     obj = bpy.context.object
#     obj.color = (0, 0, 1, 1)
#     # Create a material
#     mat = bpy.data.materials.new("Blue")
# 
#     # Activate its nodes
#     mat.use_nodes = True
# 
#     # Get the principled BSDF (created by default)
#     principled = mat.node_tree.nodes['Principled BSDF']
# 
#     # Assign the color
#     principled.inputs['Base Color'].default_value = (0,0,1,1)
# 
#     # Assign the material to the object
#     obj.data.materials.append(mat)


def add_light(name, x, y, z):
    light_data = bpy.data.lights.new(name=name, type='POINT')
    light_data.energy = 2500.0
    light_data.color = (0.993, 1.0, 0.012)

    light_object = bpy.data.objects.new(name=name, object_data=light_data)
    light_object.location = [x, y, z]
    bpy.context.collection.objects.link(light_object)
    return light_object



def add_sphere(
    name,
    subdivisions = 4,
    radius = 1.0,
    location = [0.0, 0.0, 0.0],
    rotation = [0.0, 0.0, 0.0],
    scale = [1.0, 1.0, 1.0]
    ):
    bpy.ops.mesh.primitive_ico_sphere_add(
        subdivisions=subdivisions,
        radius=radius,
        calc_uvs=True,
        enter_editmode=False,
        align='WORLD',
        location=location,
        rotation=rotation,
        scale=scale
    )
    o = bpy.data.objects['Icosphere']
    o.name = name

# docs: https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cone_add
# def add_cone(
#     vertices = 4,
#     radius1 = 1.0,
#     radius2 = 0.0,
#     depth = 2.0,
#     location = [0.0, 0.0, 0.0],
#     rotation = [0.0, 0.0, 0.0],
#     scale = [1.0, 1.0, 1.0]
# ):
#     bpy.ops.mesh.primitive_cone_add(
#         vertices=vertices,
#         radius1=radius1,
#         radius2=radius2,
#         depth=depth,
#         end_fill_type='NGON',
#         calc_uvs=True,
#         enter_editmode=False,
#         align='WORLD',
#         location=location,
#         rotation=rotation,
#         scale=scale
#     )


def create_solar_system():
    """Create simple solar with only four planets and the Sun."""

    add_sphere('Sun', location=[-115.0, 0,  0], subdivisions=6, radius = 100.0)
    add_sphere('Mercury', location=[-14.0, -36.0, -6.], subdivisions=4, radius = 0.40)
    add_sphere('Venus', location=[-5.256, -16.42, -2.577], subdivisions=4, radius = 2.40)
    add_sphere('Earth', location=[0.3409, 0.349, 3.157], subdivisions=4, radius = 1.8)
    add_sphere('Mars',location=[-10.22, 8.689, 1.168], subdivisions=4, radius = 0.8)

    _O = bpy.data.objects
    camera = _O.get('Camera')
    constraint = camera.constraints.new(type='TRACK_TO')
    constraint.target = _O['Venus']
    camera.location = [0, -85.0, -2.0]

    

def save_to_file(path, width, height):
    """Must get path with dir and file_name"""

    file_name = path.stem
    bpy.ops.image.new(name=file_name, width=width, height=height, color=(1.0, 1.0, 1.0, 1.0), alpha=True, generated_type='BLANK', float=False, use_stereo_3d=False, tiled=False)
    image = bpy.data.images[file_name]
    image.alpha_mode = 'STRAIGHT'
    image.file_format = 'PNG'

    scene=bpy.context.scene
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)

def get_args():
    # always receive list of three. Because of default values in main.py
    argv = sys.argv
    path, x, y = argv[argv.index('--') + 1:]
    path = Path(path).resolve()
    return [path, int(x), int(y)]

def delete_default_cube():
    _O = bpy.data.objects
    c = _O.get('Cube')
    if c != None:
        _O.remove(c, do_unlink=True)

def delete_default_light():
    _O = bpy.data.objects
    c = _O.get('Light')
    if c != None:
        _O.remove(c, do_unlink=True)


def delete_defaults():
    delete_default_cube()
    delete_default_light()

def get_logger(name, log_file):
    logging._srcfile = None
    logging.logThreads = 0
    logging.logProcesses = 0
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fh = RotatingFileHandler(log_file, mode='a', maxBytes=500, backupCount=3)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger