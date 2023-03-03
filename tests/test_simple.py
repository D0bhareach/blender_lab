import bpy
import time

def clear_scene():
    oo = bpy.context.scene.objects
    for o in oo:
        bpy.data.objects.remove(o, do_unlink=True)
    # bpy.data.objects['Cube'].select_set(True)
    # bpy.ops.object.delete()
    # if bpy.context.object.mode == 'EDIT':
    #     bpy.ops.object.mode_set(mode='OBJECT')
    # bpy.ops.object.select_all(action='DESELECT')

# docs: https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cube_add
def add_cube(
        name,
        size = 1.0,
        location = [0.0, 0.0, 0.0],
        rotation = [0.0, 0.0, 0.0],
        scale = [2.0, 2.0, 2.0]):
    bpy.ops.mesh.primitive_cube_add(
        size=size,
        calc_uvs=True,
        enter_editmode=False,
        align='WORLD',
        location=location,
        rotation=rotation,
        scale=scale,
    )
    c = bpy.context.scene.objects['Cube']
    c.name = name


# docs: https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_ico_sphere_add
def add_sphere(
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

# docs: https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cone_add
def add_cone(
    vertices = 4,
    radius1 = 1.0,
    radius2 = 0.0,
    depth = 2.0,
    location = [0.0, 0.0, 0.0],
    rotation = [0.0, 0.0, 0.0],
    scale = [1.0, 1.0, 1.0]
):
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=radius1,
        radius2=radius2,
        depth=depth,
        end_fill_type='NGON',
        calc_uvs=True,
        enter_editmode=False,
        align='WORLD',
        location=location,
        rotation=rotation,
        scale=scale
    )
# use subprocess
def main() -> None:
    # remove initials
    clear_scene()
    # print('Running main test')
    add_cube("c_1", location=[10, 0, 0])
    add_sphere(location=[-20, 0, 3])
    add_sphere(location=[20, 0, 3])
    add_sphere(location=[-10, 0, 3])
    add_cone(vertices=4, location=[0, 20, 6])
    add_sphere(location=[10, 0, 3])
    oo = bpy.context.scene.objects
    for  o in oo:
        print(f"{o.name}")
    c = bpy.context.scene.objects.get('c_1')
    assert c.location[0] == 10.0
    print(f'cube location: {c.location}')
    clear_scene()
    bpy.ops.wm.quit_blender()

main()