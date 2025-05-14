**Class: GLTFLight**  
**Inherits:** Resource → RefCounted → Object  

---

### **Description**  
Represents a light as defined by the `KHR_lights_punctual` glTF extension.  

---

### **Tutorials**  
- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving)  
- [KHR_lights_punctual glTF extension spec](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_lights_punctual)  

---

### **Properties**  
- **color**: `Color(1, 1, 1, 1)`  
- **inner_cone_angle**: `0.0`  
- **intensity**: `1.0`  
- **light_type**: `""`  
- **outer_cone_angle**: `0.785398`  
- **range**: `inf`  

---

### **Methods**  
1. **from_dictionary(dictionary: Dictionary)**  
   Creates a GLTFLight instance from a Dictionary.  

2. **from_node(light_node: Light3D)**  
   Creates a GLTFLight instance from a Godot `Light3D` node.  

3. **get_additional_data(extension_name: StringName)**  
   Retrieves additional data (no description available).  

4. **set_additional_data(extension_name: StringName, additional_data: Variant)**  
   Sets additional data (no description available).  

5. **to_dictionary() → Dictionary**  
   Serializes the GLTFLight instance into a Dictionary.  

6. **to_node() → Light3D**  
   Converts the GLTFLight instance to a Godot `Light3D` node.  

---

### **Property Details**  
- **color**: Linear space; converted to sRGB when needed.  
- **intensity**: Measured in candelas (cd).  
- **light_type**: Can be `"point"`, `"spot"`, or `"directional"`.  
- **range**: Infinite by default; clamped to `4096.0` in Godot.  

---

### **Cone Angles**  
- **inner_cone_angle**: Determines the light's "spot" center.  
- **outer_cone_angle**: Defines the spotlight's angular radius.  
- A half-turn (`π` radians) makes the spotlight emit in all directions.  

---

### **Notes**  
- `range` in glTF corresponds to physical light behavior (infinite range).  
- `light_type` maps to Godot's `Light3D` node types.  
- `get_additional_data` and `set_additional_data` lack descriptions.