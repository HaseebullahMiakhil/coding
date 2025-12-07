import bpy

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create car body
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0.5))
car_body = bpy.context.object
car_body.name = "CarBody"
bpy.ops.transform.resize(value=(1, 0.5, 0.5))  # Adjust dimensions

# Create car roof
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 1.2))
car_roof = bpy.context.object
car_roof.name = "CarRoof"
bpy.ops.transform.resize(value=(0.5, 0.5, 0.5))  # Adjust dimensions

# Create wheels
wheel_locations = [(1.1, 0.7, 0.2), (-1.1, 0.7, 0.2), (1.1, -0.7, 0.2), (-1.1, -0.7, 0.2)]
wheels = []
for loc in wheel_locations:
    bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=0.2, location=loc)
    wheel = bpy.context.object
    wheel.name = "Wheel"
    wheels.append(wheel)

# Group the car body, roof, and wheels
bpy.ops.object.select_all(action='DESELECT')
car_body.select_set(True)
car_roof.select_set(True)
for wheel in wheels:
    wheel.select_set(True)

# Join into a single object
bpy.context.view_layer.objects.active = car_body
bpy.ops.object.join()
bpy.context.object.name = "Car"

# Set smooth shading
bpy.ops.object.shade_smooth()

# Optional: Add a simple material
material = bpy.data.materials.new(name="CarMaterial")
material.diffuse_color = (0.1, 0.2, 0.8, 1)  # Blue color
bpy.context.object.data.materials.append(material)