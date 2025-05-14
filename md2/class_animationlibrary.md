**AnimationLibrary class in Godot**

**Inherits from:**  
- `Resource` → `RefCounted` → `Object`

---

### **Description**  
The `AnimationLibrary` class stores animations accessible via `StringName` keys for use with `AnimationPlayer` nodes. It provides methods to manage animations, including adding, retrieving, and removing them.

---

### **Tutorials**  
- [Animation tutorial index](../tutorials/animation/index)

---

### **Methods**  
- **`add_animation`**: Returns an `Error`. Parameters: `name` (StringName), `animation` (Animation).  
  Note: `|const|`  
- **`get_animation`**: Returns an `Animation`. Parameters: `name` (StringName).  
  Note: `|const|`  
- **`get_animation_list`**: Returns an `Array<StringName>`. No parameters.  
  Note: `|const|`  
- **`get_animation_list_size`**: Returns an `int`. No parameters.  
  Note: `|const|`  
- **`has_animation`**: Returns a `bool`. Parameters: `name` (StringName).  
  Note: `|const|`  
- **`remove_animation`**: No return value. Parameters: `name` (StringName).  
- **`rename_animation`**: No return value. Parameters: `name` (StringName), `newname` (StringName).  

---

### **Signals**  
- **`animation_added`**: Emitted when an animation is added, under the key `name`.  
- **`animation_changed`**: Emitted when an animation is changed (e.g., tracks added, moved, or paths changed). `name` is the key of the animation.  
- **`animation_removed`**: Emitted when an animation is removed.  
- **`animation_renamed`**: Emitted when the key of an animation is changed from `name` to `to_name`.  

---

### **Detailed Method Descriptions**  
- **`add_animation`**: Adds an animation to the library.  
- **`get_animation`**: Retrieves the animation associated with the specified key.  
- **`get_animation_list`**: Returns a list of all animations in the library.  
- **`get_animation_list_size`**: Returns the number of animations in the library.  
- **`has_animation`**: Checks if an animation exists with the given key.  
- **`remove_animation`**: Removes the animation associated with the specified key.  
- **`rename_animation`**: Renames the key of an existing animation.