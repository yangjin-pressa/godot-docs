**GLTFCamera Class**  
**Inherits**: Resource → RefCounted → Object  

---

### **Description**  
Represents a camera as defined by the base glTF spec.  

---

### **Tutorials**  
- glTF camera detailed specification: [https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-camera](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-camera)  
- glTF camera spec and example file: [https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_015_SimpleCameras.md](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_015_SimpleCameras.md)  

---

### **Properties**  
- **depth_far**: float = 4000.0  
- **depth_near**: float = 0.05  
- **fov**: float = 45.0  
- **aspect_ratio**: float = 1.0  
- **near_clip**: float = 0.1  
- **far_clip**: float = 1000.0  

---

### **Methods**  
- **from_dictionary**: static method that takes a Dictionary.  
- **to_dictionary**: method that returns a Dictionary.  
- **to_node**: method that returns a Camera3D node.  
- **to_node**: method that returns a Camera3D node.  

---

### **Property Descriptions**  
- **depth_far**: Specifies the far clipping plane distance.  
- **depth_near**: Specifies the near clipping plane distance.  
- **fov**: Field of view in degrees.  
- **aspect_ratio**: Aspect ratio of the camera.  
- **near_clip**: Near clipping plane distance.  
- **far_clip**: Far clipping plane distance.  

---

### **Method Descriptions**  
- **from_dictionary**: Serializes this GLTFCamera instance into a Dictionary.  
- **to_dictionary**: Converts this GLTFCamera instance into a Dictionary.  
- **to_node**: Converts this GLTFCamera instance into a Godot Camera3D node.