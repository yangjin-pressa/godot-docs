The `CPUParticles3D` class in Godot is a CPU-based particle system, ideal for smaller simulations or when you need more control over particle behavior. Below is a breakdown of its key features and how to use them:

---

### **Key Properties**
1. **`visibility_aabb`**  
   - **Purpose**: Defines an axis-aligned bounding box (AABB) that determines when the particle system is active.  
   - **Usage**: If particles suddenly appear/disappear when the node enters/exits the screen, adjust this AABB. Use the **Particles → Generate AABB** tool in the editor to expand it dynamically.  
   - **Example**:  
     ```gdscript
     visibility_aabb = AABB(0, 0, 0, 100, 100, 100)  # Adjust based on your scene
     ```

2. **`use_fixed_seed`**  
   - **Purpose**: Ensures the same random seed is used for reproducible simulations.  
   - **Usage**: Set to `true` for consistent results across replays or playback.  
   - **Example**:  
     ```gdscript
     use_fixed_seed = true
     ```

3. **`seed`**  
   - **Purpose**: The random seed used for particle generation.  
   - **Usage**: Useful for debugging or ensuring predictable behavior.  
   - **Example**:  
     ```gdscript
     seed = 12345
     ```

4. **`param_max` and `param_min`**  
   - **Purpose**: Control the range of values for particle properties (e.g., velocity, lifetime).  
   - **Usage**: Adjust these to fine-tune particle behavior.  
   - **Example**:  
     ```gdscript
     param_max = 10.0  # Maximum velocity
     param_min = 0.0   # Minimum velocity
     ```

---

### **Key Methods**
1. **`capture_aabb()`**  
   - **Purpose**: Returns the AABB containing all active particles in the current frame.  
   - **Usage**: Useful for collision detection or determining if particles are visible.  
   - **Example**:  
     ```gdscript
     var active_aabb = capture_aabb()
     ```

2. **`restart(keep_seed: bool = false)`**  
   - **Purpose**: Resets the particle emitter.  
   - **Usage**: Use `keep_seed = true` to preserve the current seed for seeking/playing back.  
   - **Example**:  
     ```gdscript
     restart(keep_seed = true)
     ```

3. **`request_particles_process(process_time: float)`**  
   - **Purpose**: Requests extra processing time for particle simulation.  
   - **Usage**: Useful for slowing down or speeding up playback.  
   - **Example**:  
     ```gdscript
     request_particles_process(0.5)  # Process for 0.5 seconds
     ```

4. **`set_particle_flag(flag: ParticleFlags, enable: bool)`**  
   - **Purpose**: Enables or disables particle flags (e.g., gravity, collision).  
   - **Usage**: Control particle behavior via flags.  
   - **Example**:  
     ```gdscript
     set_particle_flag(ParticleFlags.GRAVITY, true)
     ```

---

### **Common Use Cases**
- **Reproducible Simulations**: Set `use_fixed_seed = true` and `seed` to a specific value for consistent results.  
- **Visibility Control**: Adjust `visibility_aabb` to ensure particles are only active when the node is in the scene.  
- **Dynamic Parameters**: Use `param_max` and `param_min` to control properties like velocity or scale.  
- **Playback**: Use `restart(keep_seed = true)` and `request_particles_process()` for smooth playback.  

---

### **Troubleshooting Tips**
- **Particles Not Showing**: Check `visibility_aabb` and ensure particles are emitted within the AABB.  
- **No Movement**: Verify `use_fixed_seed` is set correctly and adjust `param_max`/`param_min` for velocity.  
- **Performance Issues**: Use CPU-based systems for small particle counts; GPU systems (GPUParticles3D) are better for large-scale simulations.  

---

### **Example Scenario**
To create a reproducible particle system that follows gravity and is visible only when the node is in the scene:
```gdscript
# Set up the CPUParticles3D node
var particles = Node3D.new()
particles.name = "Particles"

# Configure parameters
particles.param_max = 10.0  # Max velocity
particles.param_min = 0.0   # Min velocity
particles.use_fixed_seed = true
particles.seed = 42         # Fixed seed for reproducibility

# Set visibility AABB
particles.visibility_aabb = AABB(0, 0, 0, 100, 100, 100)

# Enable gravity
particles.set_particle_flag(ParticleFlags.GRAVITY, true)

# Add to scene
get_tree().root_node.add_child(particles)
```

This setup ensures particles are active only when the node is in the scene, use a fixed seed for reproducible results, and are influenced by gravity.