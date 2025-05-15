The `Tween` class in Godot is used to create animated sequences of properties, methods, or nested tweens. Below is a structured summary of its key methods, with explanations, parameters, and examples in both GDScript and C#:

---

### **1. `tween_property`**
**Purpose**: Animates a property of an object between an initial value and a final value over a duration.  
**Parameters**:  
- `object`: The target object.  
- `property`: The property path (e.g., `"position:x"`).  
- `final_val`: The final value to animate to.  
- `duration`: Animation duration in seconds.  

**Example (GDScript)**:
```gdscript
var tween = create_tween()
tween.tween_property($Sprite, "position", Vector2(100, 200), 1.0)
```
**Example (C#)**:
```csharp
Tween tween = CreateTween();
tween.TweenProperty(GetNode("Sprite"), "position", new Vector2(100.0f, 200.0f), 1.0f);
```

**Notes**:  
- The initial value is the object's current property value unless `from()` or `from_current()` is used.  
- Use `"property:component"` for component-level control (e.g., `"position:x"`).

---

### **2. `tween_method`**
**Purpose**: Calls a method with a value that is tweened between `from` and `to`.  
**Parameters**:  
- `method`: A `Callable` to the method (e.g., `look_at.bind(Vector3.UP)`).  
- `from`: Starting value.  
- `to`: Ending value.  
- `duration`: Duration in seconds.  

**Example (GDScript)**:
```gdscript
var tween = create_tween()
tween.tween_method(look_at.bind(Vector3.UP), Vector3(-1, 0, -1), Vector3(1, 0, -1), 1.0)
```
**Example (C#)**:
```csharp
Tween tween = CreateTween();
tween.TweenMethod(Callable.From((Vector3 target) => LookAt(target, Vector3.Up)), new Vector3(-1.0f, 0.0f, -1.ainted), new Vector3(1.0f, 0.0f, -1.0f), 1.0f);
```

**Notes**:  
- Use `Callable.Bind()` to bind additional arguments.  
- Can combine with `set_delay()` to delay the tween.

---

### **3. `tween_callback`**
**Purpose**: Calls a callback function over time.  
**Parameters**:  
- `callback`: A `Callable` to the function.  
- `from`: Starting value (optional).  
- `to`: Ending value (optional).  
- `duration`: Duration in seconds.  

**Example (GDScript)**:
```gdscript
var tween = create_tween()
tween.tween_callback(my_callback, 0, 10, 1.0).set_delay(1.0)
```

---

### **4. `tween_subtween`**
**Purpose**: Nests a `Tween` within another, allowing complex sequences.  
**Parameters**:  
- `subtween`: The nested `Tween` to add.  

**Example (GDScript)**:
```gdscript
var subtween = create_tween()
subtween.tween_property(self, "rotation_degrees", 45.0, 1.0)
subtween.tween_property(self, "rotation_degrees", 0.0, 1.0)

var tween = create_tween()
tween.tween_property(self, "position:x", 500, 3.0)
tween.tween_subtween(subtween)
tween.tween_property(self, "position:x", 300, 2.0)
```

**Notes**:  
- Parent and subtween settings (e.g., `pause()`, `set_process_mode()`) can override each other.  
- Subtween must be fully defined before being added to the parent.

---

### **5. `set_trans()` / `set_ease()`**
**Purpose**: Control the easing and transition type of the tween.  
**Parameters**:  
- `trans`: Transition type (e.g., `Tween.TRANS_SINE`, `Tween.TRANS_EXPO`).  
- `ease`: Easing function (e.g., `Tween.EASE_IN`, `Tween.EASE_OUT`).  

**Example (GDScript)**:
```gdscript
tween.set_trans(Tween.TRANS_SINE).set_ease(Tween.EASE_OUT)
```

---

### **6. `set_loops()`**
**Purpose**: Repeats the tween a specified number of times.  
**Parameters**:  
- `loops`: Number of loops (e.g., `3` for 3 repetitions).  

**Example (GDScript)**:
```gdscript
tween.set_loops(3)
```

---

### **7. `pause()` / `stop()`**
**Purpose**: Pause or stop the tween.  
**Example (GDScript)**:
```gdscript
tween.pause()
tween.stop()
```

---

### **Key Considerations**:
- **Property Paths**: Use `NodePath` for object properties (e.g., `"position:x"` for x-component).  
- **Nested Tweens**: Use `tween_subtween` to create complex animations.  
- **Timing and Easing**: Combine `set_trans()` and `set_ease()` for smooth transitions.  
- **Synchronization**: Ensure subtweens are fully defined before adding them to a parent tween.  

This structure allows developers to create dynamic, reusable animations in Godot, whether for simple property changes or complex sequences involving multiple objects and methods.