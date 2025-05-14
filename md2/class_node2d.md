# Godot Node2D Class Explanation

The `Node2D` class in Godot is a fundamental component in 2D game development, serving as a container for 2D nodes and enabling complex transformations through properties like position, rotation, scale, and skew. Below is a detailed breakdown of its properties, methods, and key considerations.

---

## **1. Core Properties**

### **Position**
- **Description**: Represents the local position of the node relative to its parent. 
- **Usage**: Directly controls the node's position in local coordinates.
- **Example**: `position = Vector2(100, 200)`.

### **Rotation**
- **Description**: The rotation angle of the node in radians.
- **Usage**: Rotates the node around its origin. A positive value rotates it clockwise.
- **Note**: Rotation is applied after scaling and skewing.

### **Scale**
- **Description**: A `Vector2` representing the scaling factors along the X and Y axes.
- **Usage**: Scales the node's size. A value of `(1, 1)` is unscaled.
- **Note**: Negative scales on the X axis are not decomposable and may alter the transformation matrix, potentially introducing unintended rotations.

### **Skew**
- **Description**: A `float` representing the skew angle (in radians) along the X axis.
- **Usage**: Skews the node, creating a slanted effect. Skew is applied between rotation and scaling.
- **Note**: Skew is measured in degrees in the editor but must be converted to radians in code using `deg_to_rad()`.

### **Transform**
- **Description**: A `Transform2D` object combining all transformations (position, rotation, scale, skew) relative to the parent.
- **Usage**: Encapsulates the cumulative effect of all transformations, useful for complex calculations.
- **Example**: `transform = get_global_transform()`.

### **Global Transform**
- **Description**: The global transformation of the node, combining its own transformations with those of its parent.
- **Usage**: Used for determining the absolute position and orientation of the node in the world.

### **Global Position**
- **Description**: The absolute position of the node in the world coordinate system.
- **Usage**: Derived from `transform.origin`.

### **Global Rotation**
- **Description**: The absolute rotation angle of the node in radians.
- **Usage**: Derived from `transform.basis.get_rotation()`.

### **Global Scale**
- **Description**: The absolute scale factors along the X and Y axes.
- **Usage**: Derived from `transform.basis.get_scale()`.

### **Global Skew**
- **Description**: The absolute skew angle of the node in radians.
- **Usage**: Derived from `transform.basis.get_skew()`.

---

## **2. Key Methods**

### **apply_scale(ratio: Vector2)**
- **Description**: Multiplies the current scale by the `ratio` vector.
- **Example**: `apply_scale(Vector2(2, 1))` doubles the X scale and keeps Y scale the same.

### **get_angle_to(point: Vector2) -> float**
- **Description**: Calculates the angle between the node and a given point in radians.
- **Note**: The angle is measured from the node's local X-axis to the line connecting the node to the point.

### **get_relative_transform_to_parent(parent: Node) -> Transform2D**
- **Description**: Returns the transformation relative to the node's parent.
- **Usage**: Useful for calculating relative positions or orientations.

### **global_translate(offset: Vector2)**
- **Description**: Adds the `offset` vector to the node's global position.
- **Usage**: Directly modifies the node's position in the world space.

### **look_at(point: Vector2)**
- **Description**: Rotates the node so its local X-axis points toward the given point (in global coordinates).
- **Note**: The point should not be the node's own position, as this would cause the node to always face right.

### **move_local_x(delta: float, scaled: bool = false)**
- **Description**: Moves the node along its local X-axis by `delta`. If `scaled` is `false`, movement is normalized.
- **Usage**: Useful for precise movement in the scene, often used in `._process()` methods.

### **move_local_y(delta: float, scaled: bool = false)**
- **Description**: Moves the node along its local Y-axis by `delta`. If `scaled` is `false`, movement is normalized.
- **Usage**: Similar to `move_local_x`, but for vertical movement.

### **rotate(radians: float)**
- **Description**: Applies a rotation to the node, in radians, relative to its current rotation.
- **Example**: `rotate(90.0)` rotates the node 90 degrees clockwise.

### **to_global(local_point: Vector2) -> Vector2**
- **Description**: Converts a local position to global coordinates.
- **Note**: Correctly transforms child node positions but not the node's own position (as it includes its own transformation).

### **to_local(global_point: Vector2) -> Vector2**
- **Description**: Converts a global position to local coordinates.
- **Usage**: Useful for determining the position of child nodes relative to the node.

### **translate(offset: Vector2)**
- **Description**: Translates the node by the given `offset` in local coordinates.
- **Note**: This method is often used in conjunction with movement logic in the scene.

---

## **3. Important Considerations**

- **Local vs Global Coordinates**: 
  - **Local**: Relative to the node's parent.
  - **Global**: Absolute in the world space. Use `to_global()` and `to_local()` to convert between them.

- **Negative Scales**: 
  - A negative X scale inverts the node's X-axis, but this can affect the transformation matrix. For example, a negative X scale combined with a rotation might result in unexpected orientation.

- **Skew and Rotation**: 
  - Skew is applied between rotation and scaling. Avoid using skew in conjunction with complex rotations to prevent unexpected visual effects.

- **Transform Calculations**: 
  - The `transform` property is a combination of all transformations. It is essential for tasks like collision detection, rendering, and physics calculations.

- **Editor Behavior**: 
  - The editor automatically adjusts the transform when properties like position, rotation, scale, or skew are modified. This includes updating the `transform` property.

---

## **4. Conclusion**

The `Node2D` class is the backbone of 2D game development in Godot, enabling precise control over the position, rotation, scale, and skew of nodes. Understanding the distinction between local and global coordinates, as well as the interplay between these transformations, is crucial for creating complex 2D scenes and animations. By leveraging the provided properties and methods, developers can achieve a wide range of visual effects and interactions in their games.