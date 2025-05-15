**Signal Class Documentation**

The `Signal` class in Godot is used to represent and manage signals, which are events that can be emitted by objects and connected to functions. This class provides methods to connect, disconnect, and emit signals, as well as retrieve information about connected callables.

---

### **Constructors**

1. **`Signal()`**  
   Constructs an empty signal with no object or signal name bound.  
   *Example:*  
   ```gdscript
   var empty_signal = Signal()
   ```

2. **`Signal(from: Signal)`**  
   Constructs a copy of an existing signal.  
   *Example:*  
   ```gdscript
   var copied_signal = Signal(from: some_signal)
   ```

3. **`Signal(object: Object, signal: StringName)`**  
   Creates a signal that references a signal named `signal` in the specified `object`.  
   *Example:*  
   ```gdscript
   var button_pressed = Signal($Button, "pressed")
   ```

---

### **Methods**

#### **`connect(callable: Callable, flags: int = 0)`**  
Connects the specified `callable` to this signal. Optional `flags` can be used to configure the connection (e.g., `Object.CONNECT_REFERENCE_COUNTED`).  
- **Parameters:**  
  - `callable`: The function or method to connect.  
  - `flags`: Connection flags (e.g., `CONNECT_REFERENCE_COUNTED`).  
- **Returns:**  
  - An integer representing the connection ID.  
- **Note:**  
  - A signal can be connected to the same callable only once unless using `CONNECT_REFERENCE_COUNTED`.  
  - If the callable’s object is freed, the connection is lost.  
  - Use `Callable.bind()` to pass additional arguments to the callable.  
  *Example:*  
  ```gdscript
  for button in $Buttons.get_children():
      button.pressed.connect(_on_pressed.bind(button))
  ```

#### **`disconnect(callable: Callable)`**  
Disdisconnects the specified `callable` from this signal.  
- **Note:**  
  - If the connection does not exist, an error is generated.  
  - Use `is_connected()` to check for existing connections before calling this method.

#### **`emit(...)`**  
Emits the signal, triggering all connected callables.  
- **Parameters:**  
  - Variable number of arguments (parameters passed to the connected callable).  
  *Example:*  
  ```gdscript
  signal.emit("pressed", 123)
  ```

#### **`get_connections()`**  
Returns an array of all connections for this signal. Each connection is a dictionary with entries for the signal, callable, and flags.  
*Example:*  
```gdscript
var connections = signal.get_connections()
```

#### **`get_name()`**  
Returns the name of the signal.  
*Example:*  
```gdscript
var name = signal.get_name()
```

#### **`get_object()`**  
Returns the object that emits this signal.  
*Example:*  
```gdscript
var obj = signal.get_object()
```

#### **`get_object_id()`**  
Returns the ID of the object emitting this signal (e.g., `Object.get_instance_id()`).  
*Example:*  
```gdscript
var id = signal.get_object_id()
```

#### **`has_connections()`**  
Returns `true` if any callable is connected to this signal.  
*Example:*  
```gdscript
var has_connections = signal.has_connections()
```

#### **`is_connected(callable: Callable)`**  
Returns `true` if the specified callable is connected to this signal.  
*Example:*  
```gdscript
var is_connected = signal.is_connected(_on_pressed)
```

#### **`is_null()`**  
Returns `true` if the signal has no object and an empty name (equivalent to `signal == Signal()`).  
*Example:*  
```gdscript
var is_null = signal.is_null()
```

---

### **Operators**

#### **`!=` (Signal)`**  
Returns `true` if the signals do not share the same object and name.  
*Example:*  
```gdscript
var result = signal1 != signal2
```

#### **`==` (Signal)`**  
Returns `true` if both signals share the same object and name.  
*Example:*  
```gdscript
var result = signal1 == signal2
```

---

### **Key Notes**
- **Reference Counting:** Use `CONNECT_REFERENCE_COUNTED` to prevent the signal’s object from being freed while connected.
- **Callable Binding:** Use `Callable.bind()` to pass additional arguments to a callable when connecting it to a signal.
- **Safety:** Always check for existing connections with `is_connected()` before calling `disconnect()`.

---

### **Example Usage**
```gdscript
# Connect a signal to a function
$Button.pressed.connect(_on_button_press)

# Emit a signal with arguments
my_signal.emit("action", "pressed")

# Check if a signal is connected
if my_signal.is_connected(_on_button_press):
    print("Signal is connected!")
```

This documentation covers the essential aspects of the `Signal` class, enabling developers to manage events and interactions in Godot effectively.