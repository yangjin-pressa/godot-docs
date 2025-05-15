# PolygonPathFinder

## Inheritance
- `Resource`
- `RefCounted`
- `Object`

---

## Methods

### `find_path(from: Vector2, to: Vector2) -> PackedVector2Array`
- **Description**: Missing documentation.
- **Parameters**:
  - `from`: Starting point as a `Vector2`.
  - `to`: Destination point as a `Vector2`.
- **Return**: A `PackedVector2Array` representing the path.

### `get_bounds() -> Rect2`
- **Description**: Missing documentation.
- **Return**: A `Rect2` defining the bounding rectangle.

### `get_closest_point(point: Vector2) -> Vector2`
- **Description**: Missing documentation.
- **Parameters**:
  - `point`: A `Vector2` to find the closest point to.
- **Return**: The closest `Vector2` point.

### `get_closest_point_on_edge(edge: Edge, point: Vector2) -> Vector2`
- **Description**: Missing documentation.
- **Parameters**:
  - `edge`: An `Edge` object.
  - `point`: A `Vector2` to find the closest point on the edge.
- **Return**: The closest `Vector2` point on the edge.

### `is_point_inside(point: Vector2) -> bool`
- **Description**: Checks if a given point is inside the polygon.
- **Parameters**:
  - `point`: A `Vector2` to check.
- **Return**: `true` if the point is inside, `false` otherwise.
- **Example**:
  ```gdscript
  var is_inside = polygon.is_point_inside(Vector2(10, 10))
  ```
  ```csharp
  bool isInside = polygon.IsPointInside(new Vector2(10, 10));
  ```

### `setup(points: Array[Vector2], connections: Array[int])`
- **Description**: Initializes the polygon with vertices and edges.
- **Parameters**:
  - `points`: An array of `Vector2` points defining the polygon.
  - `connections`: An array of integers representing edge connections.
- **Note**: The `connections` array must have an even length to form a closed polygon.

---

## Example Usage

### Initialize Polygon
```gdscript
var polygon = PolygonPathFinder.new()
var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
var connections = [0, 1, 1, 2, 2, 0]
polygon.setup(points, connections)
```

### Check Point Inside
```gdscript
var isInside = polygon.is_point_inside(Vector2(0.5, 0.5))
```

---

## Notes
- Methods like `find_path`, `get_bounds`, and `get_closest_point` lack descriptions.
- The `setup` method requires valid connections to form a closed polygon.