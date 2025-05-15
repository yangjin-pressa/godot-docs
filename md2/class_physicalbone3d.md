The `PhysicalBone3D` class is a key component in a physics engine, designed to represent a rigid body with properties and behaviors related to physics simulation. Below is a structured breakdown of its properties, methods, and usage considerations:

---

### **Key Properties**
1. **Mass (`mass`)**  
   - **Type:** `float`  
   - **Description:** Represents the physical mass of the object, influencing its inertia and response to forces. Default is `1.0`.

2. **Linear Velocity (`linear_velocity`)**  
   - **Type:** `Vector3`  
   - **Description:** The object's translational velocity in units per second. Use this to set movement, but avoid updating it every frame to prevent instability.

3. **Angular Velocity (`angular_velocity`)**  
   - **Type:** `Vector3`  
   - **Description:** The object's rotational velocity in radians per second. Controls how it spins.

4. **Linear Damping (`linear_damp`)**  
   - **Type:** `float`  
   - **Description:** Damps the object's linear motion. Default is `0.0`. Combined with `linear_damp_mode`, it can override or add to the default damping.

5. **Angular Damping (`angular_damp`)**  
   - **Type:** `float`  
   - **Description:** Damps the object's rotation. Default is `0.0`.

6. **Joint Type (`joint_type`)**  
   - **Type:** `JointType`  
   - **Description:** Defines how the bone connects to other bodies (e.g., pivot, slider, etc.). Common values include `JOINT_PIVOT`, `JOINT_SLIDER`, or `JOINT_FREE`.

7. **Joint Rotation (`joint_rotation`)**  
   - **Type:** `Vector3`  
   - **Description:** Specifies the rotation of the joint in radians. Used to align the bone's orientation.

8. **Joint Position (`joint_position`)**  
   - **Type:** `Vector3`  
   - **Description:** Defines the position of the joint in global coordinates.

9. **Custom Integrator (`custom_integrator`)**  
   - **Type:** `bool`  
   - **Description:** Enables or disables custom physics integration. When `true`, the `_integrate_forces` method is used instead of the default physics engine logic.

10. **Simulate Physics (`simulate_physics`)**  
    - **Type:** `bool`  
    - **Description:** Controls whether the object is part of the physics simulation. Default is `true`.

---

### **Key Methods**
1. **`_integrate_forces(state: PhysicsDirectBodyState3D)`**  
   - **Type:** `virtual`  
   - **Description:** A virtual method for custom physics integration. This allows developers to override the default physics behavior, such as adding custom forces or modifying the object's state before simulation.

2. **`apply_central_impulse(impulse: Vector3)`**  
   - **Type:** `void`  
   - **Description:** Applies an impulse at the object's center of mass, affecting only linear motion. Useful for sudden, directional forces (e.g., collisions).

3. **`apply_impulse(impulse: Vector3, position: Vector3 = Vector3(0, 0, 0))`**  
   - **Type:** `void`  
   - **Description:** Applies an impulse at a specified global position, affecting both linear and rotational motion. Use this for localized forces (e.g., pushing an object at a pivot point).

4. **`get_bone_id()`**  
   - **Type:** `int`  
   - **Description:** Returns a unique identifier for the bone, useful for tracking or debugging.

5. **`get_simulate_physics()`**  
   - **Type:** `bool`  
   - **Description:** Returns whether the object is currently part of the physics simulation.

---

### **Usage Considerations**
- **Avoid Frequent Velocity Updates:**  
  Do not set `linear_velocity` or `angular_velocity` every frame. Physics engines are designed to update these values during simulation, and manual updates can cause instability or incorrect behavior.

- **Custom Physics Integration:**  
  Use the `_integrate_forces` method when implementing custom physics logic (e.g., adding gravity, friction, or constraints). This method is called during the physics step, allowing precise control over the object's state.

- **Impulse Application:**  
  Use `apply_impulse` or `apply_central_impulse` for one-time forces (e.g., collisions, explosions). These methods bypass the default physics integration, ensuring forces are applied as intended.

- **Joint Behavior:**  
  The `joint_type`, `joint_rotation`, and `joint_position` properties define how the bone connects to other bodies. For example, a `JOINT_PIVOT` allows rotation around a fixed point, while a `JOINT_SLIDER` restricts movement along an axis.

---

### **Example Use Case**
```gdscript
# Apply a force to a bone at a specific position
var impulse = Vector3(100, 0, 0)
var position = Vector3(0, 0, 0)  # Position relative to the bone's origin
bone.apply_impulse(impulse, position)

# Enable custom physics integration
bone.custom_integrator = true

# Override the default physics behavior
func _integrate_forces(state: PhysicsDirectBodyState3D) -> void:
    # Custom logic here (e.g., add friction, apply forces)
    state.velocity += Vector3(1, 0, 0) * 0.1
```

---

### **Summary**
The `PhysicalBone3D` class is a versatile component for simulating rigid bodies in a physics engine. By leveraging its properties and methods, developers can create complex systems involving movement, rotation, forces, and joint constraints. Proper use of the custom integrator allows for advanced physics behavior, while avoiding frequent manual updates ensures stability and correctness.