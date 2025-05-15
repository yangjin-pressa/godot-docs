# PhysicsServer3D Class Documentation

This class provides the interface to the 3D physics engine in Godot. It includes methods for creating and managing physics bodies, spaces, shapes, and simulation parameters.

## Methods

### Body Management

#### `body_create(type: int, position: Vector3, velocity: Vector3) -> RID`
Creates a new physics body.  
**Parameters**:
- `type`: The type of body (e.g., `PhysicsBody3D` or `KinematicBody3D`).
- `position`: The initial position of the body.
- `velocity`: The initial velocity of the body.

#### `body_get_state(body: RID, state: BodyState) -> Variant`
Retrieves the state of a physics body.  
**Parameters**:
- `body`: The RID of the body.
- `state`: The state to retrieve (e.g., `BODY_STATE_LINEAR_VELOCITY`).
**Notes**: Certain states (like `BODY_STATE_SLEEPING`) are not supported in the default physics implementation.

#### `body_get_transform(body: RID) -> Transform3D`
Returns the global transform of a physics body.
**Returns**: A `Transform3D` representing the body's position and rotation.

#### `body_set_state(body: RID, state: BodyState, variant: Variant) -> void`
Sets a specific state for a physics body.  
**Parameters**:
- `body`: The RID of the body.
- `state`: The state to set (e.g., `BODY_STATE_LINEAR_VELOCITY`).
- `variant`: A variant containing the state data.

#### `body_set_transform(body: RID, transform: Transform3D) -> void`
Sets the global transform of a physics body.  
**Note**: This may not be necessary for dynamic bodies, as their transforms are updated automatically by the physics engine.

---

### Soft Body Management

#### `soft_body_create(mass: float, simulation_precision: int) -> RID`
Creates a new soft body.  
**Parameters**:
- `mass`: The total mass of the soft body.
- `simulation_precision`: The simulation precision (higher values improve accuracy but may impact performance).

#### `soft_body_get_points(body: RID) -> Array<Vector3>`
Returns the current positions of the soft body's points.

#### `soft_body_get_transform(body: RID) -> Transform3D`
Returns the global transform of a soft body.

#### `soft_body_set_total_mass(body: RID, total_mass: float) -> void`
Sets the total mass of a soft body.

#### `soft_body_update_rendering_server(body: RID, rendering_server_handler: PhysicsServer3DRenderingServerHandler) -> void`
Requests the physics server to update the rendering server with the latest positions of the soft body's points.

---

### Space Management

#### `space_create() -> RID`
Creates a new physics space.  
**Note**: A space is a collection of parameters for the physics engine. It can be assigned to an area or body.

#### `space_get_direct_state(space: RID) -> PhysicsDirectSpaceState3D`
Returns the state of a space for collision/intersection queries.  
**Returns**: A `PhysicsDirectSpaceState3D` object.

#### `space_get_param(space: RID, param: SpaceParameter) -> float`
Retrieves a parameter value from a space.  
**Parameters**:
- `space`: The RID of the space.
- `param`: The parameter to retrieve (e.g., `SPACE_PARAMETER_GRAVITY`).

#### `space_is_active(space: RID) -> bool`
Checks if a space is active.

#### `space_set_active(space: RID, active: bool) -> void`
Sets the active state of a space.

#### `space_set_param(space: RID, param: SpaceParameter, value: float) -> void`
Sets a parameter value for a space.  
**Parameters**:
- `space`: The RID of the space.
- `param`: The parameter to set.
- `value`: The new value.

---

### Shape Creation

#### `sphere_shape_create() -> RID`
Creates a new sphere shape.  
**Note**: No description is available for this method. Please contribute to the documentation.

#### `world_boundary_shape_create() -> RID`
Creates a world boundary shape.  
**Note**: No description is available for this method. Please contribute to the documentation.

---

### Notes
- **`const` Methods**: Methods marked `const` (e.g., `body_get_state`) do not modify the object and are typically used for querying data.
- **`void` Methods**: Methods returning `void` (e.g., `body_set_state`) perform actions but do not return values.
- **Enums**: Use the `BodyState` and `SpaceParameter` enums for parameter values. For example, `BODY_STATE_LINEAR_VELOCITY` or `SPACE_PARAMETER_GRAVITY`.

This documentation provides a comprehensive overview of the `PhysicsServer3D` class, including its core methods for managing physics bodies, spaces, and shapes in Godot.