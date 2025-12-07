import bpy

bpy.ops.mesh.primitive_cube_add(size=4)
cube_obj = bpy.context.active_object
cube_obj.location.z = 3
cube.obj.location.x = 100
cube.obj.location.y = 11