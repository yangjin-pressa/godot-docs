**AnimationNodeOneShot Overview**  
- **Inherits from**: AnimationNode  
- **Purpose**: Controls a single animation with fade-in/fade-out transitions and auto-restart functionality.  

---

### **Description**  
- Manages a single animation with options for fade-in, fade-out, and automatic restart.  
- Auto-restart is triggered after the animation finishes, with optional delays and random variation.  
- Supports cross-fading between animations using curves for easing.  

---

### **Tutorials**  
- [Tutorial 1: Using AnimationNodeOneShot](external-link)  
- [Tutorial 2: Advanced Fade Controls](external-link)  

---

### **Properties**  
1. **autorestart**  
   - **Type**: bool  
   - **Default**: `true`  
   - If `true`, the sub-animation restarts automatically after finishing.  
   - Auto-restart is disabled by `ONE_SHOT_REQUEST_ABORT`, but the property remains enabled.  

2. **autorestart_delay**  
   - **Type**: float  
   - **Default**: `1.0`  
   - Delay in seconds before auto-restart is triggered.  

3. **autorestart_random_delay**  
   - **Type**: float  
   - **Default**: `0.0`  
   - Random additional delay (0–value) added to `autorestart_delay`.  

4. **break_loop_at_end**  
   - **Type**: bool  
   - **Default**: `false`  
   - If `true`, breaks the loop at the end of the animation, even if it's looping.  

5. **fadein_curve**  
   - **Type**: Curve  
   - **Default**: empty  
   - Determines easing for fade-in transitions. If empty, transition is linear.  

6. **fadein_time**  
   - **Type**: float  
   - **Default**: `0.0`  
   - Duration of fade-in. Example: `1.0` for a 5s animation creates a fade-in from 0–1s.  
   - **Note**: Scaled by downstream nodes (e.g., `TimeScale` with value `2.0` halves the actual time).  

7. **fadeout_curve**  
   - **Type**: Curve  
   - **Default**: empty  
   - Determines easing for fade-out transitions. If empty, transition is linear.  

8. **fadeout_time**  
   - **Type**: float  
   - **Default**: `0.0`  
   - Duration of fade-out. Example: `1.0` for a 5s animation creates a fade-out from 4–5s.  
   - **Note**: Scaled by downstream nodes.  

9. **mix_mode**  
   - **Type**: MixMode  
   - **Default**: `0`  
   - Blend type:  
     - `0` = Blend (linear interpolation)  
     - `1` = Crossfade (easing between animations)  

---

### **Enumerations**  
- **MixMode**:  
  - `0` = Blend  
  - `1` = Crossfade  

---

### **Key Notes**  
1. **Fade Timing Scaling**:  
   - Fade-in/fade-out times are scaled by downstream nodes (e.g., `TimeScale`).  
   - Example: A `fadein_time` of `1.0` with a `TimeScale` of `2.0` results in a 0.5s fade-in.  

2. **Auto-Reset Behavior**:  
   - Auto-restart is triggered by `ONE_SHOT_REQUEST_FIRE`.  
   - `ONE_SHOT_REQUEST_ABORT` stops the animation but does not disable auto-restart.  

3. **Curve Requirements**:  
   - Fade curves must be unit curves (values between 0 and 1).  

--- 

This summary provides a concise, structured overview of the `AnimationNodeOneShot` class, including its properties, enums, and important behaviors.