# CallbackTweener

**Inherits:** Tweener → RefCounted → Object

### Description
A tweener used to call a method in a tweening sequence. See [Tween.tween_callback](#class_tween_method_tween_callback) for usage details.  
The tweener will automatically finish if the callback's target object is freed.

**Note:** [Tween.tween_callback](#class_tween_method_tween_callback) is the only valid way to create a CallbackTweener. Manual creation will not function.

---

### Methods

- `set_delay(delay: float)`  
  Delays the callback by the specified time in seconds.  

**Example:**  
```  
var tween = get_tree().create_tween()  
tween.tween_callback(queue_free).set_delay(2)  
```

---

### Key References
- [Tween.tween_callback](#class_tween_method_tween_callback)  
- [Node.queue_free](#class_node_method_queue_free)