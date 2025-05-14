Here's a structured overview of the `AnimationNodeBlendSpace2D` class in Godot, detailing its properties, methods, and usage:

---

### **Overview**
The `AnimationNodeBlendSpace2D` class is used to create a 2D blend space for animating between multiple animation nodes. It allows defining points (representing animation nodes) and triangles (defining blending regions) to interpolate between animations based on 2D coordinates.

---

### **Key Properties**

1. **`snap`**  
   - **Type**: `Vector2`  
   - **Default**: `(0.1, 0.1)`  
   - **Purpose**: Snaps the position of a point when moving it. This helps in aligning points for precise blending.

2. **`sync`**  
   - **Type**: `bool`  
   - **Default**: `false`  
   - **Purpose**: If `true`, the blended animations continue playing even when the blend value is `0`. If `false`, they stop.

3. **`x_label`**  
   - **Type**: `String`  
   - **Default**: `"x"`  
   - **Purpose**: Label for the X-axis of the blend space.

4. **`y_label`**  
   - **Type**: `String`  
   - **Default**: `"y"`  
   - **Purpose**: Label for the Y-axis of the blend space.

5. **`auto_generate`**  
   - **Type**: `bool`  
   - **Default**: `false`  
   - **Purpose**: If `true`, automatically generates triangles based on the points' positions.

---

### **Key Methods**

- **`add_blend_point(node: AnimationRootNode, pos: Vector2, at_index: int = -1)`**  
  Adds a new blend point (representing an animation node) at a specific position. If `at_index` is not provided, the point is added to the end.

- **`add_triangle(x: int, y: int, z: int, at_index: int = -1)`**  
  Adds a triangle using three points. Triangles can overlap, and can be inserted at a specific index.

- **`get_blend_point_count()`**  
  Returns the number of blend points in the space.

- **`get_blend_point_node(point: int)`**  
  Returns the animation node referenced by the point at the given index.

- **`get_blend_point_position(point: int)`**  
  Returns the position of the point at the given index.

- **`get_triangle_count()`**  
  Returns the number of triangles in the space.

- **`get_triangle_point(triangle: int, point: int)`**  
  Returns the index of the point in the triangle at the given index.

- **`remove_blend_point(point: int)`**  
  Removes the point at the specified index.

- **`remove_triangle(triangle: int)`**  
  Removes the triangle at the specified index.

- **`set_blend_point_node(point: int, node: AnimationRootNode)`**  
  Updates the animation node referenced by the point.

- **`set_blend_point_position(point: int, pos: Vector2)`**  
  Updates the position of the point.

---

### **Usage Example**

```gdscript
# Create a new blend space node
var blend_space = AnimationNodeBlendSpace2D.new()
blend_space.auto_generate = true  # Enable automatic triangle generation

# Add blend points
blend_space.add_blend_point(anim_node1, Vector2(0, 0))
blend_space.add_blend_point(anim_node2, Vector2(1, 0))
blend_space.add_blend_point(anim_node3, Vector2(0, 1))
blend_space.add_blend_point(anim_node4, Vector2(1, 1))

# Set labels
blend_space.x_label = "Horizontal"
blend_space.y_label = "Vertical"

# Add triangles (if auto_generate is false)
blend_space.add_triangle(0, 1, 2)
blend_space.add_triangle(1, 2, 3)
```

---

### **Important Notes**
- **Triangle Generation**: If `auto_generate` is `true`, the engine automatically creates triangles based on the points' positions. This is useful for simple blend spaces.
- **Sync Behavior**: The `sync` property ensures that animations continue playing when the blend value is `0`, which is essential for smooth transitions.
- **Snap Behavior**: The `snap` property helps in aligning points for precise blending, especially when manually adjusting the blend space.

---

### **Common Use Cases**
- **Animation Blending**: Blend between multiple animations (e.g., walking, running, jumping) based on 2D coordinates.
- **Custom Interpolation**: Define custom triangles for non-uniform blending behavior.
- **Dynamic Adjustment**: Modify points and triangles during runtime to adjust blending behavior.

---

This class is fundamental for creating complex animation systems in Godot, allowing for precise control over how animations interpolate between different states.