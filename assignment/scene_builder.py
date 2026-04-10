"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]

# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# Object 2: Tower (cylinder)
# ---------------------------------------------------------------------------
tower_height = 10
tower_radius = 1
tower_x = 2
tower_z = -4

tower = cmds.polyCylinder(
    name="tower_01",
    height=tower_height,
    radius=tower_radius,
)[0]

# Raise the tower so its base sits on the ground plane.
cmds.move(tower_x, tower_height / 2.0, tower_z, tower)

# ---------------------------------------------------------------------------
# Object 3: Globe (sphere)
# ---------------------------------------------------------------------------
globe_radius = 1
globe_x = 2
globe_z = 3

globe = cmds.polySphere(
    name="globe_01",
    radius=globe_radius,
)[0]

# Raise the globe so its base sits on the ground plane.
cmds.move(globe_x, globe_radius, globe_z, globe)

# ---------------------------------------------------------------------------
# Object 4: Courtyard (torus)
# ---------------------------------------------------------------------------
courtyard_radius = 4
courtyard_section_radius = 1
courtyard_x = 2
courtyard_z = 3

# Primitive Type: Torus
courtyard = cmds.polyTorus(
    name="courtyard_01",
    radius=courtyard_radius,
    sectionRadius=courtyard_section_radius,
)[0]

# Raise the courtyard so its base sits on the ground plane.
cmds.move(courtyard_x, courtyard_section_radius, courtyard_z, courtyard)

# ---------------------------------------------------------------------------
# Object 5: Tent (cone)
# ---------------------------------------------------------------------------
tent_height = 2
tent_radius = 3
tent_x = -5
tent_z = -4

# Primitive Type: Cone
tent = cmds.polyCone(
    name="tent_01",
    height=tent_height,
    radius=tent_radius,
)[0]

# Raise the tent so its base sits on the ground plane.
cmds.move(tent_x, tent_height / 2.0, tent_z, tent)

# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
