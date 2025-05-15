**RefCounted Class**  
**Description**  
The `RefCounted` class manages reference counting for objects. It is used to track the number of active references to an object, ensuring proper memory management. This class is primarily for advanced users, with methods that should be used cautiously to avoid issues like memory leaks.  

**Tutorials**  
- [When and how to avoid using nodes for everything](../tutorials/best_practices/node_alternatives)  

**Methods**  
- `get_reference_count()`: Returns the current reference count.  
- `init_ref()`: Initializes the internal reference counter. Use only if you understand the implications.  
- `reference()`: Increments the internal reference counter.  
- `unreference()`: Decrements the internal reference counter.  

**Method Descriptions**  
- **get_reference_count()**  
  Returns the current reference count.  

- **init_ref()**  
  Initializes the internal reference counter. Use only if you understand the implications. Returns `true` if successful.  

- **reference()**  
  Increments the internal reference counter. Returns `true` if the increment was successful, `false` otherwise.  

- **unreference()**  
  Decrements the internal reference counter. Returns `true` if the object should be freed after the decrement, `false` otherwise.  

**Note**  
In C#, reference-counted objects are not immediately freed. Garbage collection will periodically remove unused objects, leading to potential memory retention.  

**Inherits**  
Object class_Object  

**Key Points**  
- Avoid cyclic references to prevent memory leaks.  
- Use `@GlobalScope.weakref()` to break cycles.  
- Advanced users should handle reference counting carefully.