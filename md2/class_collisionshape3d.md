# CollisionShape3D

**Inherits:** Node3D → Node → Object

A node that provides a Shape3D to a CollisionObject3D parent.

---

## Description

A node that provides a Shape3D to a CollisionObject3D parent and allows to edit it. This can give a detection shape to an Area3D or turn a PhysicsBody3D into a solid object.

**Warning:** A non-uniformly scaled CollisionShape3D will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its shape resource instead.

---

## Tutorials

- Physics introduction: [../tutorials/physics/physics_introduction](../tutorials/physics/physics_introduction)
- 3D Kinematic Character Demo: [https://godotengine.org/asset-library/asset/2739](https://godotengine.org/asset-library/asset/2739)
- 3D Platformer Demo: [https://godotengine.org/asset-library/asset/2748](https://godotengine.org/asset-library/asset/2748)
- Third Person Shooter (TPS) Demo: [https://godotengine.org/asset-library/asset/2710](https://godotengine.org/asset-library/asset/2710)

---

## Properties

- **debug_color**: Color = Color(0, 0, 0, 0)
- **debug_fill**: bool = true
- **disabled**: bool = false
- **shape**: Shape3D

---

## Methods

- **make_convex_from_siblings()**: Sets the collision shape's shape to the addition of all its convexed MeshInstance3D siblings geometry.
- **resource_changed(resource: Resource)**: **Deprecated**. Use Resource.changed instead. This method does nothing.

---

## Property Descriptions

### debug_color
- **set_debug_color(value: Color)**: Sets the collision shape color displayed in the editor.
- **get_debug_color()**: Gets the collision shape color displayed in the editor.
- **Note:** Default value is ProjectSettings.debug/shapes/collision/shape_color. The documented Color(0, 0, 0, 0) is a placeholder.

### debug_fill
- **set_enable_debug_fill(value: bool)**: Enables/disables solid fill color when shape is displayed.
- **get_enable_debug_fill()**: Gets the debug fill state.

### disabled
- **set_disabled(value: bool)**: Disables the collision shape (no effect in the world).
- **is_disabled()**: Checks if the collision shape is disabled.

### shape
- **set_shape(value: Shape3D)**: Sets the actual shape owned by this collision shape.
- **get_shape()**: Gets the actual shape owned by this collision shape.

---

## Method Descriptions

### make_convex_from_siblings()
- Sets the collision shape's shape to the addition of all its convexed MeshInstance3D siblings geometry.

### resource_changed(resource: Resource)
- **Deprecated**: Use Resource.changed instead. This method does nothing.