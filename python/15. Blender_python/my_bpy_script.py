import bpy
import math

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Parameters for the spiral tower
segments = 50  # Number of segments
height = 5.0   # Total height of the tower
radius = 1.0   # Radius of the base
twist = 5      # Number of twists

# Create a new mesh and a new object
mesh = bpy.data.meshes.new("SpiralTowerMesh")
tower_object = bpy.data.objects.new("SpiralTower", mesh)
bpy.context.collection.objects.link(tower_object)

# Create vertices and faces for the spiral tower
verts = []
faces = []

for i in range(segments):
    angle = i * (2 * math.pi / twist)
    z_value = (i / segments) * height
    x_value = radius * math.cos(angle)
    y_value = radius * math.sin(angle)
    verts.append((x_value, y_value, z_value))

    # Create faces between segments (except the last one)
    if i > 0:
        face = (i - 1, i, i, i - 1)  # Create a quad
        faces.append(face)

# Define the last segment to close the tower
verts.append(verts[0])  # Connect to the first segment to create a closed shape

# Update the mesh with vertices and faces
mesh.from_pydata(verts, [], faces)

# Calculate normals
mesh.update()

# Add a simple material
material = bpy.data.materials.new(name="ColorfulMaterial")
material.use_nodes = True
bsdf = material.node_tree.nodes.get("Principled BSDF")
bsdf.inputs['Base Color'].default_value = (0.1, 0.5, 0.8, 1)  # A nice blue color

# Assign the material to the tower object
tower_object.data.materials.append(material)

# Set smooth shading
bpy.ops.object.shade_smooth()

# Optionally set the viewport shading to 'Rendered'
bpy.context.space_data.shading.type = 'RENDERED'