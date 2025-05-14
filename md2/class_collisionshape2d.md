# CollisionShape2D

**Inherits:** Node2D < CanvasItem < Node < Object

A node that provides a Shape2D to a CollisionObject2D parent. Used for collision detection in 2D physics.

## Description
- Provides a Shape2D to a CollisionObject2D parent
- Enables editing of collision shapes
- Can be used for:
  - Detection shape for Area2D
  - Making PhysicsBody2D solid

## Tutorials
- Physics introduction: [Physics introduction](../tutorials/physics/physics_introduction)
- 2D Dodge The Creeps Demo: [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)
- 2D Pong Demo: [2D Pong Demo](https://godotengine.org/asset-library/asset/2728)
- 2D Kinematic Character Demo: [2D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2719)

## Properties

- **debug_color**: Color (default: Color(0, 0, 0, 0))
- **disabled**: bool (default: false)
- **one_way_collision**: bool (default: false)
- **one_way_collision_margin**: float (default: 1.0)
- **shape**: Shape2D (no default)

## Property Descriptions

### debug_color
- **Set/Get**: set_debug_color(value: Color), get_debug_color()
- **Description**: Collision shape color displayed in editor. Default is ProjectSettings.debug/shapes/collision/shape_color.

### disabled
- **Set/Get**: set_disabled(value: bool), is_disabled()
- **Description**: Disables collision effects. Use Object.set_deferred() for changes.

### one_way_collision
- **Set/Get**: set_one_way_collision(value: bool), is_one_way_collision_enabled()
- **Description**: Enables one-sided collision detection (top/bottom). No effect if parent is Area2D.

### one_way_collision_margin
- **Set/Get**: set_one_way_collision_margin(value: float), get_one_way_collision_margin()
- **Description**: Margin for one-way collision (in pixels). Higher values increase shape thickness.

### shape
- **Set/Get**: set_shape(value: Shape2D), get_shape()
- **Description**: The actual collision shape associated with this node.