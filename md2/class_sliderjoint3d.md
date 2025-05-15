### Class Documentation: `SliderJoint3D`

---

#### **Properties**

##### **Linear Motion**
- **linear_motion/damping**  
  - **Type**: `float`  
  - **Description**: The amount of damping inside the slider limits.  
  - **Parameters**: None  

- **linear_motion/restitution**  
  - **Type**: `float`  
  - **Description**: The amount of restitution inside the slider limits.  
  - **Parameters**: None  

- **linear_motion/softness**  
  - **Type**: `float`  
  - **Description**: A factor applied to the movement across the slider axis as long as the slider is in the limits. The lower, the slower the movement.  
  - **Parameters**: None  

- **linear_ortho/damping**  
  - **Type**: `float`  
  - **Description**: The amount of damping when movement is across axes orthogonal to the slider.  
  - **Parameters**: None  

- **linear_ortho/restitution**  
  - **Type**: `float`  
  - **Description**: The amount of restitution when movement is across axes orthogonal to the slider.  
  - **Parameters**: None  

- **linear_ortho/softness**  
  - **Type**: `float`  
  - **Description**: A factor applied to the movement across axes orthogonal to the slider.  
  - **Parameters**: None  

- **linear_limit/damping**  
  - **Type**: `float`  
  - **Description**: The amount of damping once the limits are surpassed. The lower, the more velocity-energy gets lost.  
  - **Parameters**: None  

- **linear_limit/restitution**  
  - **Type**: `float`  
  - **Description**: The amount of restitution once the limits are surpassed. The lower, the more velocity-energy gets lost.  
  - **Parameters**: None  

- **linear_limit/softness**  
  - **Type**: `float`  
  - **Description**: A factor applied to the movement across the slider axis once the limits get surpassed. The lower, the slower the movement.  
  - **Parameters**: None  

- **linear_limit/upper_distance**  
  - **Type**: `float`  
  - **Description**: The maximum difference between the pivot points on their X axis before damping happens.  
  - **Parameters**: None  

- **linear_limit/lower_distance**  
  - **Type**: `float`  
  - **Description**: The minimum difference between the pivot points on their X axis before damping happens.  
  - **Parameters**: None  

---

##### **Angular Motion**
- **angular_velocity**  
  - **Type**: `float`  
  - **Description**: The angular velocity of the joint.  
  - **Parameters**: None  

- **angular_motion/damping**  
  - **Type**: `float`  
  - **Description**: The amount of damping inside the angular limits.  
  - **Parameters**: None  

- **angular_motion/restitution**  
  - **Type**: `float`  
  - **Description**: The amount of restitution inside the angular limits.  
  - **Parameters**: None  

- **angular_motion/softness**  
  - **Type**: `float`  
  - **Description**: A factor applied to the movement across the angular axis as long as the joint is in the limits. The lower, the slower the movement.  
  - **Parameters**: None  

- **angular_limit/damping**  
  - **Type**: `float`  
  - **Description**: The amount of damping once the angular limits are surpassed. The lower, the more velocity-energy gets lost.  
  - **Parameters**: None  

- **angular_limit/restitution**  
  - **Type**: `float`  
  - **Description**: The amount of restitution once the angular limits are surpassed. The lower, the more velocity-energy gets lost.  
  - **Parameters**: None  

- **angular_limit/softness**  
  - **Type**: `float`  
  - **Description**: A factor applied to the movement across the angular axis once the limits get surpassed. The lower, the slower the movement.  
  - **Parameters**: None  

---

##### **Other Properties**
- **pivot**  
  - **Type**: `Vector3`  
  - **Description**: The pivot point of the joint.  
  - **Parameters**: None  

- **joint_axis**  
  - **Type**: `Vector3`  
  - **Description**: The axis of the joint.  
  - **Parameters**: None  

---

#### **Methods**

- **get_param(Param param)**  
  - **Return Type**: `float`  
  - **Description**: Returns the value of the given parameter (see `Param` constants).  
  - **Parameters**:  
    - `param`: `Param` – The parameter to retrieve.  

- **set_param(Param param, float value)**  
  - **Return Type**: `void`  
  - **Description**: Assigns `value` to the given parameter (see `Param` constants).  
  - **Parameters**:  
    - `param`: `Param` – The parameter to update.  
    - `value`: `float` – The new value for the parameter.  

---

### Notes
- **`Param` Constants**: The properties use values from the `Param` enum to reference specific parameters (e.g., `linear_motion/damping`, `angular_velocity`).  
- **Virtual Method**: The `set_param` method is marked as `virtual`, indicating it should be overridden by subclasses if needed.  
- **Const Method**: The `get_param` method is `const`, meaning it does not modify the object's state.  

This documentation provides a structured overview of the `SliderJoint3D` class, including its properties, methods, and related parameters.