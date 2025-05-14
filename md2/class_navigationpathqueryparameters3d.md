# NavigationPathQueryParameters3D

A class used to configure parameters for 3D pathfinding queries in Godot. This class allows setting start and target positions, navigation layers, map, pathfinding algorithm, and other properties that influence the pathfinding behavior.

## Properties

### `start_position`
```gdscript
var start_position: Vector3 = Vector3(0, 0, 0)
```
**Description:** The pathfinding start position in global coordinates.

**Methods:**
- `set_start_position(position: Vector3)`: Sets the start position.
- `get_start_position(): Vector3`: Retrieves the start position.

---

### `target_position`
```gdscript
var target_position: Vector3 = Vector3(0, 0, 0)
```
**Description:** The pathfinding target position in global coordinates.

**Methods:**
- `set_target_position(position: Vector3)`: Sets the target position.
- `get_target_position(): Vector3`: Retrieves the target position.

---

### `map`
```gdscript
var map: RID = RID()
```
**Description:** The navigation map `RID` used in the path query. This must be a valid `NavigationMap` instance.

**Methods:**
- `set_map(map: RID)`: Sets the map.
- `get_map(): RID`: Retrieves the map.

---

### `navigation_layers`
```gdscript
var navigation_layers: int = 1
```
**Description:** The navigation layers the query will use (as a bitmask). This determines which areas of the map are considered valid for pathfinding.

**Methods:**
- `set_navigation_layers(layers: int)`: Sets the navigation layers.
- `get_navigation_layers(): int`: Retrieves the navigation layers.

---

### `metadata_flags`
```gdscript
var metadata_flags: bitfield<PathMetadataFlags> = 7
```
**Description:** A bitmask of flags that control additional information included with the navigation path (e.g., waypoints, costs, etc.).

**Methods:**
- `set_metadata_flags(flags: bitfield<PathMetadataFlags>)`: Sets the metadata flags.
- `get_metadata_flags(): bitfield<PathMetadataFlags>`: Retrieves the metadata flags.

---

### `pathfinding_algorithm`
```gdscript
var pathfinding_algorithm: PathfindingAlgorithm = PathfindingAlgorithm.ASTAR
```
**Description:** The pathfinding algorithm used in the path query. Options include A*, Dijkstra, etc.

**Methods:**
- `set_pathfinding_algorithm(algorithm: PathfindingAlgorithm)`: Sets the pathfinding algorithm.
- `get_pathfinding_algorithm(): PathfindingAlgorithm`: Retrieves the pathfinding algorithm.

---

### `path_postprocessing`
```gdscript
var path_postprocessing: PathPostprocessing = PathPostprocessing.NONE
```
**Description:** The postprocessing applied to the raw path corridor. Options include simplification, smoothing, etc.

**Methods:**
- `set_path_postprocessing(postprocessing: PathPostprocessing)`: Sets the postprocessing.
- `get_path_postprocessing(): PathPostprocessing`: Retrieves the postprocessing.

---

### `simplify_epsilon`
```gdscript
var simplify_epsilon: float = 0.0
```
**Description:** The path simplification amount in world units. Controls how much of the path is simplified.

**Methods:**
- `set_simplify_epsilon(epsilon: float)`: Sets the simplification epsilon.
- `get_simplify_epsilon(): float`: Retrieves the simplification epsilon.

---

### `simplify_path`
```gdscript
var simplify_path: bool = false
```
**Description:** If `true`, a simplified version of the path is returned with fewer critical points. This is useful for efficiency and avoiding issues with certain agent types.

**Methods:**
- `set_simplify_path(enable: bool)`: Enables or disables path simplification.
- `get_simplify_path(): bool`: Retrieves the simplify path flag.

---

## Example Usage

```gdscript
var query = NavigationPathQueryParameters3D.new()
query.start_position = Vector3(0, 0, 0)
query.target_position = Vector3(10, 10, 10)
query.map = navigation_server.get_map()  # Assuming navigation_server is a NavigationServer3D instance
query.navigation_layers = 3  # Example bitmask
query.simplify_path = true
query.simplify_epsilon = 2.0

var path = navigation_server.query_path(query)
```

## Notes

- The `included_regions` and `excluded_regions` properties are not directly exposed here but are managed via the map's region settings.
- The returned arrays (e.g., `included_regions`) are copies, so modifications to them do not affect the original property. To update the value, modify the array and reassign it.
- This class is used in conjunction with `NavigationServer3D` to perform path queries. Ensure the map and layers are properly configured before use.