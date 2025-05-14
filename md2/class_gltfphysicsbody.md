**Class Name**: GLTFPhysicsBody  
**Inheritance**: Resource → Object  

---

### **Overview**  
Represents physics data for 3D models in the OMI_physics_body glTF extension format.  
- Acts as an intermediary between glTF geometry and Godot physics systems.  
- Supports future extensions for physics properties.  

---

### **Tutorials**  
1. [GLTF Physics Basics](#)  
2. [OMI_physics_body glTF extension](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_physics_body)  

---

### **Properties**  
- **angular_velocity**: Vector3(0, 0, 0)  
- **linear_velocity**: Vector3(0, 0, 0)  
- **mass**: 1.0  
- **inertia_diagonal**: (deprecated) Basis(0, 0, 0, 0, 0, 0, 0, 0, 0)  
- **inertia_tensor**: (deprecated) Basis(0, 0, 0, 0, 0, 0, 0, 0, 0)  
- **inertia_orientation**: Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)  
- **body_type**: (default: "rigid")  

---

### **Methods**  
- **from_dictionary(dictionary: Dictionary)** → GLTFPhysicsBody  
  - Parses glTF physics data from a Dictionary.  
- **from_node(body_node: CollisionObject3D)** → GLTFPhysicsBody  
  - Creates a physics body from a Godot CollisionObject3D.  
- **to_dictionary()** → Dictionary  
  - Serializes physics data into a Dictionary.  
- **to_node()** → CollisionObject3D  
  - Converts physics data into a Godot CollisionObject3D.  

---

### **Key Features**  
- **Physics Properties**: Mass, velocity, inertia.  
- **Extensibility**: Supports future physics property extensions.  
- **Conversion**: Converts between glTF and Godot physics systems.  

---

### **Deprecated**  
- **inertia_tensor**: Use inertia_diagonal and inertia_orientation instead.