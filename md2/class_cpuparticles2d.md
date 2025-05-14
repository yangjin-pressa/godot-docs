### CPUParticles2D Class Overview

The `CPUParticles2D` class represents a CPU-based particle system for 2D simulations, offering fine-grained control over particle behavior, motion, and rendering. It includes properties for defining particle parameters, flags for enabling/disabling specific behaviors, and methods to dynamically adjust these values or reset the simulation. This class is ideal for scenarios requiring deterministic or seed-based particle behavior, such as replays or animations.

---

### **Properties**

1. **Motion Parameters**  
   - **radial_velocity**: Controls the outward velocity of particles.  
   - **radial_acceleration**: Determines how quickly particles accelerate radially.  
   - **tangential_velocity**: Specifies the rotational velocity component of particles.  
   - **tangential_acceleration**: Governs the rate of change of tangential velocity.  
   - **angular_velocity**: Defines the rotational speed of particles.  
   - **angular_acceleration**: Controls the rate of change of angular velocity.  

2. **Simulation Control**  
   - **use_fixed_seed**: Enables fixed random seeding for consistent particle behavior across simulations.  
   - **seed**: The seed value used for random number generation (effective only when `use_fixed_seed` is enabled).  

3. **Rendering**  
   - **texture**: The texture applied to particles. If `null`, particles are displayed as squares.  
   - **texture_offset**: A 2D offset for the texture, allowing for tiling or shifting.  
   - **texture_scale**: Scale factor for the texture.  

4. **Particle Behavior Flags**  
   - **particle_flags**: Bitfield controlling particle behavior (e.g., gravity, rotation, collision).  
   - **flags**: Specific flags (e.g., `ParticleFlags::ROTATE`, `ParticleFlags::GRAVITY`).  

5. **Miscellaneous**  
   - **random_seed**: Internal seed value for random generation.  
   - **max_particle_count**: Maximum number of particles the system can handle.  

---

### **Methods**

1. **`convert_from_particles(nodes: Node)`**  
   - **Purpose**: Copies properties from a `GPUParticles2D` node to this CPU particle system.  
   - **Use Case**: Migrate particle configurations from GPU-based systems to CPU.  

2. **`get_param_curve(param: Parameter) -> Curve`**  
   - **Purpose**: Returns the curve associated with a specific particle parameter.  
   - **Example**: Retrieve a curve for `Parameter::RADIAL_VELOCITY`.  

3. **`get_param_max(param: Parameter) -> float`**  
   - **Purpose**: Gets the maximum value for a given parameter.  
   - **Example**: `get_param_max(Parameter::TANGENTIAL_ACCELERATION)`  

4. **`get_param_min(param: Parameter) -> float`**  
   - **Purpose**: Retrieves the minimum value for a parameter.  

5. **`get_particle_flag(flag: ParticleFlags) -> bool`**  
   - **Purpose**: Checks if a specific particle flag is enabled.  
   - **Example**: `get_particle_flag(ParticleFlags::ROTATE)`  

6. **`request_particles_process(process_time: float)`**  
   - **Purpose**: Requests extra processing time for particles during a frame.  
   - **Use Case**: Extend simulation time for playback or complex animations.  

7. **`restart(keep_seed: bool = false)`**  
   - **Purpose**: Resets the particle emitter.  
   - **Flags**:  
     - `keep_seed = true`: Preserves the current seed for consistent replay.  

8. **`set_param_curve(param: Parameter, curve: Curve)`**  
   - **Purpose**: Sets the curve for a parameter.  
   - **Note**: Curves must be normalized (unit curves).  

9. **`set_param_max(param: Parameter, value: float)`**  
   - **Purpose**: Sets the maximum value for a parameter.  

10. **`set_param_min(param: Parameter, value: float)`**  
    - **Purpose**: Sets the minimum value for a parameter.  

11. **`set_particle_flag(flag: ParticleFlags, enable: bool)`**  
    - **Purpose**: Enables or disables a specific particle flag.  

---

### **Enums and Constants**

- **`Parameter`**: Defines particle parameters (e.g., `RADIAL_VELOCITY`, `ANGULAR_ACCELERATION`).  
- **`ParticleFlags`**: Bitfield for enabling/disabling behaviors (e.g., `ROTATE`, `GRAVITY`).  

---

### **Key Notes**

- **Seed Management**:  
  - `use_fixed_seed` ensures consistent particle behavior across runs.  
  - `seed` is used when `use_fixed_seed` is enabled.  

- **Curve Usage**:  
  - Curves (e.g., `set_param_curve`) must be normalized for correct parameter interpolation.  

- **Performance**:  
  - CPU-based systems are suitable for deterministic simulations but may be slower than GPU-based alternatives.  

- **Playback**:  
  - `restart(keep_seed = true)` is essential for seeking or replaying particle sequences.  

---

### **Example Usage**

```gdscript
var particles = CPUParticles2D.new()
particles.texture = Texture2D.load("res://particle_texture.png")
particles.radial_velocity = 10.0
particles.use_fixed_seed = true
particles.seed = 42
particles.restart(keep_seed = true)
```

This initializes a particle system with a texture, radial velocity, and fixed seed, then restarts it to replay the simulation.