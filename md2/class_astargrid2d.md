# AStarGrid2D Class Documentation

A 2D grid-based pathfinding system using the A* algorithm. This class provides methods to define a grid, set point properties, and find paths between points.

## Properties

### `region`: `Rect2`
The region that defines the grid's bounds. Points outside this region are considered invalid.

### `cell_size`: `Vector2`
The size of each grid cell in world coordinates. Determines how the grid is mapped to the actual world space.

### `offset`: `Vector2`
An offset that shifts the grid's origin. Used to adjust the position of grid points relative to the world.

### `dirty`: `bool`
Indicates whether the grid parameters have changed and need to be updated. This is automatically set when parameters like `region`, `cell_size`, or `offset` are modified.

## Methods

### `__construct()`
Constructor. Initializes the grid with default parameters.

### `update()`
Updates the internal state of the grid according to the parameters. Must be called after changing parameters like `region`, `cell_size`, or `offset`. This method clears all point data (solidity and weight scale).

### `is_dirty() const`
Returns `true` if the grid parameters have changed and an update is needed.

### `is_in_bounds(x: int, y: int) const`
Returns `true` if the given grid coordinates (x, y) are within the grid's bounds. Equivalent to `region.has_point(Vector2i(x, y))`.

### `is_in_boundsv(id: Vector2i) const`
Returns `true` if the given grid ID is within the grid's bounds. Equivalent to `region.has_point(id)`.

### `is_point_solid(id: Vector2i) const`
Returns `true` if the point at the given ID is disabled for pathfinding. By default, all points are enabled.

### `set_point_solid(id: Vector2i, solid: bool = true)`
Disables or enables the specified point for pathfinding. Useful for creating obstacles. By default, all points are enabled.

### `get_point_solid(id: Vector2i) const`
Returns the solidity status of the point at the given ID.

### `get_point_position(id: Vector2i) const`
Returns the world position of the point associated with the given ID.

### `get_point_weight_scale(id: Vector2i) const`
Returns the weight scale of the point at the given ID. The weight scale is multiplied by the result of `_compute_cost()` when determining the overall cost of traveling across a segment.

### `set_point_weight_scale(id: Vector2i, weight_scale: float)`
Sets the `weight_scale` for the point with the given ID. The `weight_scale` is multiplied by the result of `_compute_cost()` when determining the overall cost of traveling across a segment.

### `get_point_data_in_region(region: Rect2) const`
Returns an array of dictionaries with point data (id, position, solid, weight_scale) within the specified region.

### `get_id_path(from_id: Vector2i, to_id: Vector2i, allow_partial_path: bool = false)`
Returns an array of point IDs that form the path found by AStar2D between the given points. The array is ordered from the starting point to the ending point of the path. If there is no valid path and `allow_partial_path` is `true`, returns a path to the point closest to the target.

### `get_point_path(from_id: Vector2i, to_id: Vector2i, allow_partial_path: bool = false)`
Returns an array of points that are in the path found by AStarGrid2D between the given points. The array is ordered from the starting point to the ending point of the path. If there is no valid path and `allow_partial_path` is `true`, returns a path to the point closest to the target.

**Note:** This method is not thread-safe. If called from a thread, it will return an empty array and print an error message.

### `get_id_path(from_id: Vector2i, to_id: Vector2i, allow_partial_path: bool = false)`
Returns an array of point IDs that form the path found by AStar2D between the given points. The array is ordered from the starting point to the ending point of the path. If there is no valid path and `allow_partial_path` is `true`, returns a path to the point closest to the target.

**Note:** When `allow_partial_path` is `true` and `to_id` is solid, the search may take an unusually long time to finish.

## Notes

- **Updating the Grid:** After changing parameters like `region`, `cell_size`, or `offset`, call `update()` to prepare the grid for pathfinding.
- **Thread Safety:** The `get_point_path()` method is not thread-safe. Avoid calling it from a thread.
- **Partial Paths:** When `allow_partial_path` is `true` and the target is solid, the search may take longer to find a valid path.
- **Dirty Flag:** The `dirty` flag is automatically set when parameters are changed, indicating that `update()` needs to be called.
- **Point Data:** The `update()` method clears all point data (solidity and weight scale) when called.

This class provides a flexible and efficient way to implement pathfinding in 2D environments, with options to customize grid behavior and point properties.