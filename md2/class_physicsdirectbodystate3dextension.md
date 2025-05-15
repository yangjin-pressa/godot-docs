Here is a detailed documentation for the `PhysicsDirectBodyState3DExtension` class, based on the method names and parameters provided:

---

### **PhysicsDirectBodyState3DExtension**

This class provides access to the state and properties of a physics body in a 3D environment, including its transform, velocity, forces, and interaction with the physics space.

---

### **Methods**

#### **_get_transform()**
**Returns:** `Transform3D`  
**Description:**  
Retrieves the current transform (position and rotation) of the body. This is a read-only property used to query the body's position and orientation in the physics world.

---

#### **_get_velocity_at_local_position(local_position: Vector3)**
**Returns:** `Vector3`  
**Description:**  
Calculates the velocity of the body at a specified local position relative to the body's origin. This is useful for determining the motion of different points on the body, especially in rigid body dynamics.

---

#### **_integrate_forces()**
**Description:**  
Updates the body's state based on applied forces and torques. This method is part of the physics simulation loop, integrating forces to compute the body's acceleration, velocity, and position over time.

---

#### **_set_transform(transform: Transform3D)**
**Description:**  
Sets the body's transform (position and rotation). This method directly assigns the body's state, overriding any previous values. Note that this is typically used in conjunction with the physics engine's update logic.

---

#### **_is_sleeping()**
**Returns:** `bool`  
**Description:**  
Checks if the body is in a "sleeping" state. A sleeping body is inactive and not affected by physics calculations. This is a read-only property.

---

#### **_set_sleep_state(enabled: bool)**
**Description:**  
Sets whether the body is in a sleeping state. Enabling this state may stop the body's physics updates, while disabling it will awaken the body.

---

#### **_set_angular_velocity(velocity: Vector3)**
**Description:**  
Sets the body's angular velocity (rotation speed). This directly modifies the body's rotation rate, overriding any previous values.

---

#### **_set_constant_force(force: Vector3)**
**Description:**  
Applies a constant force to the body. This is used to simulate continuous forces, such as gravity or user input, during the physics simulation.

---

#### **_set_constant_torque(torque: Vector3)**
**Description:**  
Applies a constant torque to the body. This affects the body's rotational motion, similar to how forces affect linear motion.

---

#### **_set_linear_velocity(velocity: Vector3)**
**Description:**  
Sets the body's linear velocity (movement speed). This directly modifies the body's translational motion.

---

#### **_get_contact_count()**
**Returns:** `int`  
**Description:**  
Returns the number of contact points the body has with other objects. This is used for collision detection and response.

---

#### **_get_contact_normal(contact_index: int)**
**Returns:** `Vector3`  
**Description:**  
Retrieves the normal vector at a specified contact point. This is used to determine the direction of the contact force during collisions.

---

#### **_get_contact_point(contact_index: int)**
**Returns:** `Vector3`  
**Description:**  
Returns the position of a specific contact point. This is useful for debugging or calculating contact forces.

---

#### **_get_contact_point_derivative(contact_index: int)**
**Returns:** `Vector3`  
**Description:**  
Returns the derivative (rate of change) of the contact point position. This is used in advanced collision response calculations.

---

#### **_get_total_angular_damp()**
**Returns:** `float`  
**Description:**  
Returns the total angular damping applied to the body. This controls how quickly the body slows down rotation.

---

#### **_get_total_linear_damp()**
**Returns:** `float`  
**Description:**  
Returns the total linear damping applied to the body. This controls how quickly the body slows down translation.

---

#### **_get_total_gravity()**
**Returns:** `Vector3`  
**Description:**  
Returns the combined gravity vector acting on the body. This is the sum of all gravitational forces from different sources in the environment.

---

#### **_get_step()**
**Returns:** `float`  
**Description:**  
Returns the time step used in the physics simulation. This determines how frequently the physics engine updates the body's state.

---

#### **_get_space_state()**
**Returns:** `PhysicsDirectSpaceState3D`  
**Description:**  
Returns the space state associated with the body. This is used for querying or modifying the physics space's state related to this body.

---

### **Key Notes**
- **Sleeping State:** The `_is_sleeping()` and `_set_sleep_state()` methods control whether the body is active in the physics simulation.
- **Forces and Damping:** Methods like `_set_constant_force()` and `_get_total_angular_damp()` allow precise control over the body's motion and energy dissipation.
- **Transform Management:** The `_get_transform()` and `_set_transform()` methods are critical for updating or querying the body's position and rotation in the world.

This class is essential for customizing and debugging physics behavior in a 3D environment, particularly when integrating with a physics engine that supports direct body state manipulation.