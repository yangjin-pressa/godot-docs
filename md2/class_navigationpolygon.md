# NavigationPolygon Class Documentation

## Overview
The `NavigationPolygon` class in Godot is used to define a 2D navigation area with custom polygons and outlines. It provides methods to manage vertex data, outlines, and polygons, and it supports generating a navigation mesh that can be used with the `NavigationServer3D` for 3D navigation.

---

## Properties

### `agent_radius`: `float`
The radius of the navigation agent (in world units) that this polygon is designed for. This affects how the agent navigates around obstacles.

### `agent_height`: `float`
The height of the navigation agent (in world units). This is used to determine how the agent interacts with the navigation mesh, such as climbing slopes or avoiding obstacles.

### `max_slope`: `float`
The maximum slope angle (in radians) that the agent can handle. This defines the steepness of the terrain the agent can traverse.

### `max_hopping`: `float`
The maximum vertical distance (in world units) that the agent can hop over obstacles.

### `agent_half_height`: `float`
The half-height of the navigation agent. This is used for collision detection and height-based navigation.

### `collision_layer`: `int`
The collision layer this navigation polygon is associated with. This determines which layers of the scene are considered when generating the navigation mesh.

### `collision_mask`: `uint32`
A bitmask representing which layers the navigation polygon should collide with. This is used for visibility and collision checks.

### `parsed_collision_mask`: `uint32`
A bitmask that specifies which layers are considered for collision during parsing. This is used to filter which layers are included in the navigation mesh.

---

## Methods

### `add_outline(outline: PackedVector2Array)`
Adds an outline (a list of vertices) to the navigation polygon. This outline is used to define areas that should be avoided or treated as obstacles.

### `add_outline_at_index(outline: PackedVector2Array, index: int)`
Inserts an outline at a specific index in the list of outlines. This allows for dynamic modification of the outline list.

### `add_polygon(polygon: PackedInt32Array)`
Adds a polygon using vertex indices from the `vertices` array. The indices are based on the vertices defined by `get_vertices()`.

### `clear()`
Clears all vertices and polygons from the navigation polygon, resetting it to an empty state.

### `clear_outlines()`
Removes all outlines but retains the vertices and polygons. This is useful when you want to modify the outline list without re-creating the polygons.

### `clear_polygons()`
Removes all polygons but retains the outlines and vertices. This is useful when you want to redefine the polygons without removing the outlines.

### `get_navigation_mesh() -> NavigationMesh`
Returns the navigation mesh generated from this polygon. This mesh can be used to update a region in the `NavigationServer3D` for 3D navigation.

### `get_outline(idx: int) -> PackedVector2Array`
Retrieves a specific outline by index. This is useful for modifying or inspecting outlines added via the editor or script.

### `get_outline_count() -> int`
Returns the total number of outlines currently in the navigation polygon.

### `get_parsed_collision_mask_value(layer_number: int) -> bool`
Checks if a specific layer (1–32) is enabled in the `parsed_collision_mask`. This is used to determine which layers are considered during parsing.

### `get_polygon(idx: int) -> PackedInt32Array`
Retrieves a specific polygon by index. This is useful for inspecting or modifying the structure of the navigation mesh.

### `get_polygon_count() -> int`
Returns the number of polygons defined in the navigation polygon.

### `get_vertices() -> PackedVector2Array`
Returns all the vertices used to create the polygons. These vertices are the base for building the navigation mesh.

### `make_polygons_from_outlines()`
Generates polygons from the outlines added to the navigation polygon. This is necessary before using the polygon data in navigation logic.

### `remove_outline(idx: int)`
Removes an outline by index. This is useful for cleaning up the outline list.

### `set_outline(idx: int, outline: PackedVector2Array)`
Replaces an outline at a specific index. This allows for dynamic modification of the outline list.

### `set_parsed_collision_mask_value(layer_number: int, value: bool)`
Enables or disables a specific layer in the `parsed_collision_mask`. This is used to control which layers are included in the navigation mesh.

### `set_vertices(vertices: PackedVector2Array)`
Sets the vertices that will be used to create polygons. These vertices are then indexed by `add_polygon()` to form the navigation mesh.

---

## Deprecated Method

### `make_polygons_from_outlines()`
**Deprecated:** This method is no longer recommended. Instead, use `NavigationServer2D.parse_source_geometry_data()` and `NavigationServer2D.bake_from_source_geometry_data()` to generate navigation meshes from source geometry.

---

## Notes

- This class is part of the 2D navigation system but uses the 3D `NavigationServer3D` underneath, making it suitable for 3D navigation in 2D environments.
- The `NavigationMesh` returned by `get_navigation_mesh()` can be used to update regions in the `NavigationServer3D` for 3D pathfinding.
- Outlines and polygons are separate entities. Outlines define areas, while polygons define the actual mesh structure.

---

## Example Usage

```gdscript
# Create a new navigation polygon
var poly = NavigationPolygon()

# Set vertices for the polygon
poly.set_vertices(PackedVector2Array([
    Vector2(0, 0),
    Vector2(10, 0),
    Vector2(10, 10),
    Vector2(0, 10)
]))

# Add an outline
poly.add_outline(PackedVector2Array([
    Vector2(5, 5),
    Vector2(15, 5),
    Vector2(15, 15),
    Vector2(5, 15)
]))

# Generate polygons from outlines
poly.make_polygons_from_outlines()

# Get the navigation mesh
var mesh = poly.get_navigation_mesh()
```

---

## See Also

- [NavigationServer3D](https://docs.godotengine.org/en/latest/classes/navigationserver3d.html)
- [NavigationMesh](https://docs.godotengine.org/en/latest/classes/navigationmesh.html)
- [NavigationServer2D](https://docs.godotengine.org/en/latest/classes/navigationserver2d.html)