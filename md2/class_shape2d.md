### Shape2D Class Overview

#### Inheritance
- **Resource**  
- **RefCounted**  
- **Object**  

#### Inherited Classes
- **CircleShape2D**  
- **PolygonShape2D**  
- **ConcavePolygonShape2D**  
- **CustomShape2D**  
- **RectangleShape2D**  
- **EdgeShape2D**  

---

### Description
- **Purpose**: Abstract base class for 2D shapes used in physics simulations.
- **Performance Note**: 
  - `CircleShape2D`: Fast collision detection.
  - `PolygonShape2D`: Moderate performance.
  - `ConcavePolygonShape2D`: High computational cost.
  - `CustomShape2D`: Custom implementations vary in efficiency.
  - `RectangleShape2D`: Fast.
  - `EdgeShape2D`: Fast.

---

### Tutorials
- **Physics Introduction**: [Link to Godot Physics Documentation](https://godotengine.org/manual/en/standalone/physics.html)

---

### Properties
- **custom_solver_bias** (float): Default value `0.0`.  
  - **Description**: Controls the solver's bias in collision resolution.

---

### Methods

1. **collide(local_xform, other_shape, shape_mask, motion, collision_object)**  
   - **Return**: `bool`  
   - **Description**: Checks if a collision occurs between two shapes. Parameters include transformation, other shape, collision mask, motion, and collision object.

2. **collide_and_get_contacts(local_xform, other_shape, shape_mask, motion, collision_object)**  
   - **Return**: `PackedVector2Array`  
   - **Description**: Detects collisions and returns contact points. Similar to `collide`, but provides contact information.

3. **collide_with_motion(local_xform, local_motion, other_shape, shape_mask, shape_xform, shape_motion, collision_object)**  
   - **Return**: `bool`  
   - **Description**: Tests for collisions with movement. Parameters include transformation, motion, other shape, collision mask, and movement for the other object.

4. **collide_with_motion_and_get_contacts(local_xform, local_motion, other_shape, shape_mask, shape_xform, shape_motion, collision_object)**  
   - **Return**: `PackedVector2Array`  
   - **Description**: Detects collisions with movement and returns contact points. Similar to `collide_with_motion`.

5. **draw(canvas_item, color)**  
   - **Return**: `void`  
   - **Description**: Draws the shape on a canvas using the RenderingServer API. The drawing method depends on the specific shape.

6. **get_rect()**  
   - **Return**: `Rect2`  
   - **Description**: Returns the bounding rectangle of the shape.

---

### Key Notes
- **Virtual Methods**: Methods like `collide` and `draw` are virtual and should be overridden by subclasses for custom behavior.
- **Const Methods**: `get_rect` is a const method and does not modify the object.
- **Varargs**: Some methods accept variable arguments, but this is not explicitly noted in the documentation.