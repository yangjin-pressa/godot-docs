# SoftBody3D Class Documentation

A flexible 3D soft body physics simulation node in Godot, allowing for dynamic deformation and interaction with the environment.

## Properties

### `collision_layer` (int)
The layer this body is registered on for collision detection. Values range from 1 to 32.

### `collision_mask` (int)
A bitmask defining which layers this body can collide with. Values range from 1 to 32.

### `simulation_precision` (int)
Controls the simulation accuracy. Higher values improve visual quality but may impact performance. Default is 5.

### `total_mass` (float)
The mass of the soft body. Default is 1.0.

### `ray_pickable` (bool)
Determines if the body responds to raycasting. Default is true.

### `pressure_coefficient` (float)
Controls internal pressure simulation. Higher values increase the strength of this effect. Default is 0.0.

### `parent_collision_exception` (NodePath)
A `CollisionObject3D` to avoid clipping with. Default is an empty path.

## Methods

### `add_collision_exception_with(body: Node)`
Adds a body to the list of bodies this soft body cannot collide with.

### `get_collision_exceptions() -> Array[PhysicsBody3D]`
Returns an array of nodes that are collision exceptions for this body.

### `get_collision_layer_value(layer_number: int) -> bool`
Checks if a specific layer is enabled in the collision layer. Returns true if enabled.

### `get_collision_mask_value(layer_number: int) -> bool`
Checks if a specific layer is enabled in the collision mask. Returns true if enabled.

### `get_physics_rid() -> RID`
Returns the internal RID used by the PhysicsServer3D for this body.

### `get_point_transform(point_index: int) -> Vector3`
Returns the local translation of a surface vertex at the given index.

### `is_point_pinned(point_index: int) -> bool`
Checks if a surface vertex is pinned. Returns true if pinned.

### `remove_collision_exception_with(body: Node)`
Removes a body from the collision exception list.

### `set_collision_layer_value(layer_number: int, value: bool)`
Enables or disables a specific layer in the collision layer.

### `set_collision_mask_value(layer_number: int, value: bool)`
Enables or disables a specific layer in the collision mask.

### `set_point_pinned(point_index: int, pinned: bool, attachment_path: NodePath = "", insert_at: int = -1)`
Sets a surface vertex to be pinned. If pinned is true, the optional attachment path defines a Node3D to attach to.

## Notes

- **Collision Layers/掩码:** Use values 1-32 for layer numbers. The collision layer determines which layers this body is registered on, while the collision mask determines which layers it can interact with.
  
- **Simulation Precision:** Increasing this value improves simulation quality but may degrade performance. Use with caution in real-time applications.

- **Pressure Coefficient:** This value controls how "internal pressure" affects the soft body. Higher values make the body more resistant to compression.

- **Ray Pickable:** When enabled, the soft body can be selected via raycasting, useful for interactive simulations.

- **Pinned Points:** Pinned vertices can be attached to other nodes, creating constraints in the soft body simulation. This is useful for creating fixed points or attaching to environments.