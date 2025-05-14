# NavigationPathQueryParameters2D Class

This class is used to configure parameters for 2D pathfinding queries in the Godot engine. It allows you to set the start and target positions, specify navigation layers, select a pathfinding algorithm, and apply postprocessing to the generated path.

---

## Properties

### `start_position`
**Type:** `Vector2`  
**Default:** `Vector2(0, 0)`  
**Description:** The pathfinding start position in global coordinates.

**Setter/Getter:**  
- `set_start_position(value: Vector2)`  
- `get_start_position() -> Vector2`

---

### `target_position`
**Type:** `Vector2`  
**Default:** `Vector2(0, 0)`  
**Description:** The pathfinding target position in global coordinates.

**Setter/Getter:**  
- `set_target_position(value: Vector2)`  
- `get_target_position() -> Vector2`

---

### `map`
**Type:** `RID`  
**Default:** `RID()`  
**Description:** The navigation map `RID` used in the path query.

**Setter/Getter:**  
- `set_map(value: RID)`  
- `get_map() -> RID`

---

### `navigation_layers`
**Type:** `int`  
**Default:** `1`  
**Description:** The navigation layers the query will use (as a bitmask).

**Setter/Getter:**  
- `set_navigation_layers(value: int)`  
- `get_navigation_layers() -> int`

---

### `pathfinding_algorithm`
**Type:** `PathfindingAlgorithm`  
**Default:** `0` (i.e., `PathfindingAlgorithm.ASTAR`)  
**Description:** The pathfinding algorithm used in the path query.

**Setter/Getter:**  
- `set_pathfinding_algorithm(value: PathfindingAlgorithm)`  
- `get_pathfinding_algorithm() -> PathfindingAlgorithm`

---

### `path_postprocessing`
**Type:** `PathPostProcessing`  
**Default:** `0` (i.e., `PathPostProcessing.NONE`)  
**Description:** The path postprocessing applied to the raw path corridor found by the `pathfinding_algorithm`.

**Setter/Getter:**  
- `set_path_postprocessing(value: PathPostProcessing)`  
- `get_path_postprocessing() -> PathPostProcessing`

---

### `simplify_epsilon`
**Type:** `float`  
**Default:** `0.0`  
**Description:** The path simplification amount in world units.

**Setter/Getter:**  
- `set_simplify_epsilon(value: float)`  
- `get_simplify_epsilon() -> float`

---

### `simplify_path`
**Type:** `bool`  
**Default:** `false`  
**Description:** If `true`, a simplified version of the path will be returned with less critical path points removed. The simplification amount is controlled by `simplify_epsilon`.

**Setter/Getter:**  
- `set_simplify_path(value: bool)`  
- `get_simplify_path() -> bool`

---

### `metadata_flags`
**Type:** `bitfield` of `PathMetadataFlags`  
**Default:** `7` (i.e., `PATH_METADATA_INCLUDE | PATH_METADATA_EXCLUDE | PATH_METADATA_SOMETHING_ELSE`)  
**Description:** Additional information to include with the navigation path.

**Setter/Getter:**  
- `set_metadata_flags(value: bitfield of PathMetadataFlags)`  
- `get_metadata_flags() -> bitfield of PathMetadataFlags`

---

### `included_regions`
**Type:** `Array` of `RID`  
**Default:** `[]`  
**Description:** The list of region `RID`s that will be included by the path query. If left empty, all regions are included. If a region is both included and excluded, it will be excluded.

**Setter/Getter:**  
- `set_included_regions(value: Array of RID)`  
- `get_included_regions() -> Array of RID`

---

### `excluded_regions`
**Type:** `Array` of `RID`  
**Default:** `[]`  
**Description:** The list of region `RID`s that will be excluded by the path query. If a region is both included and excluded, it will be excluded.

**Setter/Getter:**  
- `set_excluded_regions(value: Array of RID)`  
- `get_excluded_regions() -> Array of RID`

---

## Enums

### `PathMetadataFlags`
**Description:** Bitmask flags for metadata included in the path.

- `PATH_METADATA_INCLUDE`: Include the region in the path.
- `PATH_METADATA_EXCLUDE`: Exclude the region from the path.
- `PATH_METADATA_SOMETHING_ELSE`: Additional flags (exact values depend on Godot's implementation).

---

### `PathPostProcessing`
**Description:** Postprocessing options for the path.

- `PATH_POSTPROCESSING_NONE`: No postprocessing.
- `PATH_POSTPROCESSING_EDGE_SMOOTHING`: Smooth edges of the path.
- `PATH_POSTPROCESSING_SIMPLIFIED_PATH`: Simplify the path.

---

### `PathfindingAlgorithm`
**Description:** Pathfinding algorithms available.

- `PATHFINDING_ALGORITHM_ASTAR`: A* algorithm.
- `PATHFINDING_ALGORITHM_Dijkstra`: Dijkstra's algorithm.
- `PATHFINDING_ALGORITHM_SomeOtherAlgorithm`: Other available algorithms.

---

## Notes

1. **Array Handling:**  
   When retrieving `included_regions` or `excluded_regions`, the returned arrays are copies. To modify them, you must reassign the values after modification.

2. **Path Simplification:**  
   The `simplify_path` and `simplify_epsilon` properties work together. `simplify_epsilon` controls the amount of simplification, while `simplify_path` enables or disables the simplification.

3. **Navigation Layers:**  
   Use a bitmask to combine multiple navigation layers. For example, `navigation_layers = 3` (binary `11`) includes both layer 0 and layer 1.

4. **Map and Regions:**  
   The `map` property specifies the navigation map, while `included_regions` and `excluded_regions` define which areas are allowed/disallowed in the pathfinding.

---

This class provides a flexible and powerful way to customize pathfinding behavior in 2D environments within Godot. Use it to control how paths are generated, modified, and validated based on your specific requirements.