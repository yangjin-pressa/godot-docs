**PhysicsDirectBodyState3D Class Documentation**

**Overview**  
The `PhysicsDirectBodyState3D` class represents the state of a rigid body in a 3D physics simulation. It provides access to the body's position, velocity, forces, and contact information. This class is used in conjunction with the PhysicsDirectSpaceState3D to manage and query the state of bodies in a space.

---

### **Properties**

1. **body_state**  
   - **Type**: `PhysicsDirectSpaceState3D`  
   - **Description**: The current state of the space, useful for queries and spatial operations.  
   - **Access**: Getter (`get_space_state()`)

2. **contact_count**  
   - **Type**: `int`  
   - **Description**: The number of contacts this body has with other bodies.  
   - **Note**: By default, returns 0 unless bodies are configured to monitor contacts.  
   - **Access**: Getter (`get_contact_count()`)

3. **contact_impulse**  
   - **Type**: `Vector3`  
   - **Description**: The impulse created by the contact.  
   - **Access**: Getter (`get_contact_impulse()`)

4.endid

5. **contact_local_normal**  
   - **Type**: `Vector3`  
   - **Description**: The local normal at the contact point.  
   - **Access**: Getter (`get_contact_local_normal()`)

6. **contact_local_position**  
   - **Type**: `Vector3`  
   - **Description**: The position of the contact point on the body in the global coordinate system.  
   - **Access**: Getter (`get_contact_local_position()`)

7. **contact_local_shape**  
   - **Type**: `int`  
   - **Description**: The local shape index of the collision.  
   - **Access**: Getter (`get_contact_local_shape()`)

8. **velocity**  
   - **Type**: `Vector3`  
   - **Description**: The body's velocity at a given local position, including both translation and rotation.  
   - **Access**: Getter (`get_velocity_at_local_position()`)

---

### **Methods**

1. **get_space_state()**  
   - **Return Type**: `PhysicsDirectSpaceState3D`  
   - **Description**: Returns the current state of the space, useful for queries.  
   - **Note**: This method is typically used to retrieve spatial information for collision detection or spatial queries.

2. **get_contact_collider(contact_idx)**  
   - **Parameters**:  
     - `contact_idx`: `int` (index of the contact)  
   - **Return Type**: `RID`  
   - **Description**: Returns the collider's RID (Resource Identifier) for the specified contact.  
   - **Note**: This is useful for identifying which collider is involved in a contact.

3. **get_contact_collider_id(contact_idx)**  
   - **Parameters**:  
     - `contact_idx`: `int` (index of the contact)  
   - **Return Type**: `int`  
   - **Description**: Returns the collider's object ID for the specified contact.  
   - **Note**: This helps in identifying the unique ID of the collider involved in the contact.

4. **get_contact_collider_object(contact_idx)**  
   - **Parameters**:  
     - `contact_idx`: `int` (index of the contact)  
   - **Return Type**: `Object`  
   - **Description**: Returns the collider object for the specified contact.  
   - **Note**: This can be used to access the underlying node or resource of the collider.

5. **get_contact_collider_position(contact_idx)**  
   - **Parameters**:  
     - `contact_idx`: `int` (index of the contact)  
   - **Return Type**: `Vector3`  
   - **Description**: Returns the position of the contact point on the collider in the global coordinate system.  
   - **Note**: Useful for determining the exact location of the contact on the collider.

6. **get_contact_collider_shape(contact_idx)**  
   - **Parameters**:  
     - `contact_idx`: `int` (index of the contact)  
   - **Return Type**: `int`  
   - **Description**: Returns the collider's shape index for the specified contact.  
   - **Note**: This helps in identifying which shape (e.g., sphere, box) is involved in the contact.

7. **get_contact_impulse(contact_idx)**  
   - **Parameters**:  
     - `contact_idx`: `int` (index of the contact)  
   - **Return Type**: `Vector3`  
   - **Description**: Returns the impulse created by the contact.  
   - **Note**: Impulse is the force applied over a time interval, useful for calculating the effect of the contact.

8. **get_contact_local_normal(contact_idx)**  
   - **Parameters**:  
     - `contact_idx`: `int` (index of the contact)  
   - **Return Type**: `Vector3`  
   - **Description**: Returns the local normal at the contact point.  
   - **Note**: The normal vector indicates the direction of the contact surface.

9. **get_contact_local_position(contact_idx)**  
   - **Parameters**:  
     - `contact_idx`: `int` (index of the contact)  
   - **Return Type**: `Vector3`  
   - **Description**: Returns the position of the contact point on the body in the global coordinate system.  
   - **Note**: Useful for determining the exact location of the contact on the body.

10. **get_contact_local_shape(contact_idx)**  
    - **Parameters**:  
      - `contact_idx`: `int` (index of the contact)  
    - **Return Type**: `int`  
    - **Description**: Returns the local shape index of the collision.  
    - **Note**: This is used to identify the specific shape (e.g., face, edge) involved in the contact.

11. **get_contact_local_velocity_at_position(contact_idx)**  
    - **Parameters**:  
      - `contact_idx`: `int` (index of the contact)  
    - **Return Type**: `Vector3`  
    - **Description**: Returns the linear velocity vector at the body's contact point.  
    - **Note**: This helps in analyzing the motion of the body at the contact point.

12. **get_contact_velocity_at_position(contact_idx)**  
    - **Parameters**:  
      - `contact_idx`: `int` (index of the contact)  
    - **Return Type**: `Vector3`  
    - **Description**: Returns the linear velocity vector at the collider's contact point.  
    - **Note**: This is useful for determining the relative motion of the collider at the contact point.

13. **integrate_forces()**  
    - **Return Type**: `void`  
    - **Description**: Updates the body's linear and angular velocity by applying gravity and damping for the equivalent of one physics tick.  
    - **Note**: This method is essential for simulating the body's motion based on the forces applied.

14. **set_constant_force(force)**  
    - **Parameters**:  
      - `force`: `Vector3` (force to apply to the body)  
    - **Description**: Applies a constant force to the body.  
    - **Note**: This is used to simulate forces like gravity or user input.

15. **set_constant_torque(torque)**  
    - **Parameters**:  
      - `torque`: `Vector3` (torque to apply to the body)  
    - **Description**: Applies a constant torque to the body.  
    - **Note**: Torque affects the rotational motion of the body.

---

### **Notes**
- **Contact Monitoring**: The `contact_count` property only returns non-zero values if the body is configured to monitor contacts.  
- **Space State**: The `body_state` property is used for spatial queries, such as checking for overlaps or intersections with other bodies.  
- **Velocity Calculation**: The `velocity` method calculates the velocity at a local position, considering both translation and rotation.  
- **Force Integration**: The `integrate_forces()` method is critical for updating the body's state in the physics simulation.  

This class is fundamental for managing the dynamics of a 3D physics simulation, allowing developers to access and manipulate the state of rigid bodies accurately.