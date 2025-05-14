To effectively use the `CharacterBody3D` node in Godot, follow these steps and best practices to create a character or object that interacts with the environment:

---

### **1. Basic Setup**
- **Create a `CharacterBody3D` node** in your scene hierarchy. This node will handle physics movement and collision detection.
- **Add a `KinematicBody3D`** (if needed) for non-kinematic movement, or use `CharacterBody3D` directly for physics-based movement.

---

### **2. Physics Properties**
- **Set `gravity`** to control the downward force (e.g., `gravity = -9.81` for Earth-like gravity).
- **Adjust `collision_shape`** (e.g., a capsule or box) to define the character's collision area.
- **Configure `friction` and `bounce`** in the physics material for interactions with surfaces.

---

### **3. Movement with `move_and_slide`**
- **Use `move_and_slide`** to move the character based on velocity, handling collisions automatically:
  ```gdscript
  func _process(delta):
      if Input.is_action_pressed("Move Forward"):
          velocity.z = 5.0
      if Input.is_action_pressed("Move Backward"):
          velocity.z = -5.0
      if Input.is_action_pressed("Jump") and is_on_floor():
          velocity.y = 10.0
      move_and_slide(velocity, 1.0)  # 1.0 is the friction coefficient
  ```

- **Modify velocity** if a slide collision occurs. For example, adjust direction when hitting a wall:
  ```gdscript
  if is_on_wall():
      velocity.x *= -1  # Reverse horizontal movement
  ```

---

### **4. Collision Detection**
- **Check collision states** using methods like `is_on_floor()`, `is_on_wall()`, or `is_on_ceiling()` to trigger actions:
  ```gdscript
  if is_on_floor():
      print("Character is on the floor!")
  if is_on_wall():
      print("Character hit a wall!")
  ```

- **Get detailed collision info** with `get_last_slide_collision()` or `get_slide_collision()` for debugging:
  ```gdscript
  var last_collision = get_last_slide_collision()
  if last_collision.get_fixture():
      print("Last collision with: ", last_collision.get_fixture().get_name())
  ```

---

### **5. Advanced Features**
- **Move platforms**: Use `move_and_slide` to let the character follow a moving platform:
  ```gdscript
  if is_on_floor() and platform_velocity.is_valid():
      velocity = platform_velocity
  ```

- **Custom physics**: Override `__body_entered` or `__body_exited` to handle custom interactions with other bodies.

---

### **6. Example: Simple Jumping Character**
```gdscript
extends CharacterBody3D

var velocity = Vector3.ZERO
var jump_power = 10.0

func _process(delta):
    # Horizontal movement
    if Input.is_action_pressed("Move Forward"):
        velocity.z = 5.0
    elif Input.is_action_pressed("Move Backward"):
        velocity.z = -5.0
    else:
        velocity.z = 0

    # Jump
    if Input.is_action_pressed("Jump") and is_on_floor():
        velocity.y = jump_power

    # Apply movement
    move_and_slide(velocity, 1.0)
```

---

### **Key Notes**
- **`move_and_slide`** handles collisions by sliding along surfaces, not stopping abruptly.
- **Collision detection** methods (e.g., `is_on_floor()`) use the `up_direction` and `floor_max_angle` properties to determine surface type.
- **Friction** and **bounciness** can be adjusted in physics materials for realistic interactions.

By combining these elements, you can create dynamic, physics-based characters that interact with the environment and other objects in Godot.