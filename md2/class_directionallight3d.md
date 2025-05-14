**DirectionalLight3D Overview**  
A directional light in Godot that simulates light coming from an infinite distance, casting shadows. It is ideal for simulating sunlight or other distant light sources.

---

**Key Features**  
- **Shadow Rendering**: Supports shadow casting with options for shadow mode (Orthographic, Parallel, etc.).  
- **Sky Interaction**: Can be visible in the sky, in the scene, or both.  
- **Distance Control**: Adjusts shadow visibility and detail based on distance parameters.  

---

**Properties**  
1. **directional_shadow_mode**  
   - **Type**: `ShadowMode` (enum)  
   - **Default**: `2` (SHADOW_PARALLEL_4_SPLITS)  
   - **Description**: Controls the algorithm for rendering directional shadows. Options include:  
     - `0` (SHADOW_PARALLEL_2_SPLITS)  
     - `1` (SHADOW_PARALLEL_4_SPLITS)  
     - `2` (SHADOW_PARALLEL_2_SPLITS)  

2. **directional_shadow_max_distance**  
   - **Type**: `float`  
   - **Default**: `100.0`  
   - **Description**: The maximum distance for shadow splits. Increasing this value extends shadow visibility but reduces detail and performance.  

3. **directional_shadow_fade_start**  
   - **Type**: `float`  
   - **Default**: `0.8`  
   - **Description**: Proportion of `directional_shadow_max_distance` at which shadow begins to fade. A higher value prevents fading in distant areas.  

4. **directional_shadow_pancake_size**  
   - **Type**: `float`  
   - **Default**: `20.0`  
   - **Description**: Adjusts the shadow camera frustum to improve depth resolution. A higher value may cause artifacts in large objects.  

5. **directional_shadow_split_1**  
   - **Type**: `float`  
   - **Default**: `0.1`  
   - **Description**: Distance from the camera to the first shadow split. Used when shadow mode is `SHADOW_PARALLEL_2_SPLITS` or `SHADOW_PARALLEL_4_SPLITS`.  

6. **directional_shadow_split_2**  
   - **Type**: `float`  
   - **Default**: `0.2`  
   - **Description**: Distance between shadow splits 1 and 2. Used when shadow mode is `SHADOW_PARALLEL_4_SPLITS`.  

7. **directional_shadow_split_3**  
   - **Type**: `float`  
   - **Default**: `0.5`  
   - **Description**: Distance between shadow splits 2 and 3. Used when shadow mode is `SHADOW_PARALLEL_4_SPLITS`.  

8. **sky_mode**  
   - **Type**: `SkyMode` (enum)  
   - **Default**: `0` (SKY_VISIBLE)  
   - **Description**: Controls visibility in the sky and scene. Options include:  
     - `0` (SKY_VISIBLE)  
     - `1` (SKY_IN_VISIBLE)  
     - `2` (SKY_NOT_VISIBLE)  

---

**Enumerations**  
1. **ShadowMode**  
   - **Values**:  
     - `0` (SHADOW_PARALLEL_2_SPLITS)  
     - `1` (SHADOW_PARALLEL_4_SPLITS)  
     - `2` (SHADOW_PARALLEL_2_SPLITS)  

2. **SkyMode**  
   - **Values**:  
     - `0` (SKY_VISIBLE)  
     - `1` (SKY_IN_VISIBLE)  
     - `2` (SKY_NOT_VISIBLE)  

---

**Notes**  
- **Shadow Detail**: Adjust `directional_shadow_pancake_size` to balance depth resolution and artifacts.  
- **Performance**: Increasing `directional_shadow_max_distance` reduces shadow detail and performance.  
- **Fade Control**: Lower `directional_shadow_fade_start` for fast-moving cameras to reduce visible fade.  

This structure organizes the properties, enumerations, and key features of the `DirectionalLight3D` class for clarity and usability.