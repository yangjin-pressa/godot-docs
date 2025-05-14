# LookAtModifier3D Class Description

The `LookAtModifier3D` class is designed to modify the rotation of a skeletal mesh to look at a specified target node. It supports various properties for controlling the behavior of the look-at operation, including angle limitations, transition types, and secondary rotation.

## Properties

### 1. **target_node**
- **Type:** `NodePath`
- **Description:** The node path to the target node that the look-at modification will rotate the bone to. This node determines the direction the bone should face.

### 2. **use_angle_limitation**
- **Type:** `bool`
- **Description:** If `true`, limits the degree of rotation. This helps prevent excessive rotation, such as a character's neck rotating 360 degrees. Note that some transition types (e.g., `Back`, `Elastic`, `Spring`) may exceed limitations, potentially leading to results that don't respect the bone rest.

### 3. **symmetry_limitation**
- **Type:** `bool`
- **Description:** If `true`, the angle limitations are applied symmetrically to both sides of the bone. If `false`, limitations can be specified separately for each side.

### 4. **transition_type**
- **Type:** `TransitionType` (from `Tween`)
- **Description:** The type of time-based interpolation. Options include `Linear`, `Back`, `Elastic`, `Spring`, etc. This affects how the interpolation between target positions is executed.

### 5. **use_secondary_rotation**
- **Type:** `bool`
- **Description:** If `true`, provides rotation along two axes (e.g., yaw and pitch). This allows more complex rotation behavior compared to single-axis rotation.

### 6. **primary_positive_limitation**, **primary_negative_limitation**
- **Type:** `float`
- **Description:** Limits the maximum positive and negative rotation angles for the primary axis (e.g., pitch). These values control how far the bone can rotate in this direction.

### 7. **secondary_positive_limitation**, **secondary_negative_limitation**
- **Type:** `float`
- **Description:** Similar to the primary limits but for the secondary axis (e.g., yaw). These values control the rotation range for the secondary axis.

### 8. **primary_rotation_axis**, **secondary_rotation_axis**
- **Type:** `int` (euler angle axis)
- **Description:** Specifies the axes for primary and secondary rotation. These determine which directions the rotation will occur.

## Methods

### 1. **get_interpolation_remaining()**
- **Return Type:** `float`
- **Description:** Returns the remaining time (in seconds) for the time-based interpolation. This is useful for tracking how much time is left in the current interpolation process.

### 2. **is_interpolating()**
- **Return Type:** `bool`
- **Description:** Returns `true` if time-based interpolation is currently running. This can be used to determine if the modifier is in the middle of an interpolation cycle, which is useful for safely removing the modifier when it's done.

### 3. **is_target_within_limitation()**
- **Return Type:** `bool`
- **Description:** Checks if the target node is within the defined angle limitations. This is helpful for deciding when to reset the target node if it's outside the allowed rotation range. Note that this value is updated after the `SkeletonModifier3D._process_modification()` method, so it's recommended to use the `SkeletonModifier3D.modification_processed` signal for accurate retrieval.

## Key Notes

- **Angle Limitation Interaction:** The `use_angle_limitation` property affects how the primary and secondary rotation limits are applied. If enabled, the rotation is constrained within the specified ranges.
  
- **Transition Type Behavior:** Certain transition types (e.g., `Back`, `Elastic`, `Spring`) may cause overshooting of the angle limitations, which could lead to results that don't respect the bone's rest position.

- **Signal Usage:** The `is_target_within_limitation()` method's value is updated after processing. For accurate results, use the `SkeletonModifier3D.modification_processed` signal to trigger updates.

- **Secondary Rotation:** Enabling `use_secondary_rotation` allows for more complex rotation behavior, but it requires careful management of the primary and secondary limits.

This class is essential for creating natural-looking animations where a skeletal mesh needs to look at a specific target, with control over rotation behavior and interpolation.