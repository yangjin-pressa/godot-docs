# Control Class Documentation

The `Control` class in Godot is the base class for all visual node types, providing essential methods for positioning, sizing, and handling user input. Below is a detailed guide to its key methods and their usage.

---

## **Key Methods and Usage**

### **1. Drag-and-Drop Customization**
#### **_get_drag_data(position: Vector2) → Variant**
- **Purpose**: Returns the data to be dragged when a user initiates a drag operation.
- **Example**:
  ```gdscript
  func _get_drag_data(position):
      var cpb = ColorPickerButton.new()
      cpb.color = color
      cpb.size = Vector2(50, 50)
      set_drag_preview(cpb)
      return color
  ```
  - **Note**: The control (`cpb`) must not be in the scene tree and is deleted after the drag.

#### **set_drag_forwarding(drag_func: Callable, can_drop_func: Callable, drop_func: Callable)**
- **Purpose**: Customizes drag-and-drop behavior by replacing default virtual methods.
- **Parameters**:
  - `drag_func`: Callable for drag data retrieval.
  - `can_drop_func`: Callable to check if a drop is possible.
  - `drop_func`: Callable to handle the drop.
- **Example (C#)**:
  ```csharp
  public override Variant _GetDragData(Vector2 atPosition)
  {
      var cpb = new ColorPickerButton();
      cpb.Color = _color;
      cpb.Size = new Vector2(50, 50);
      SetDragPreview(cpb);
      return _color;
  }
  ```

#### **set_drag_preview(control: Control)**
- **Purpose**: Displays a custom control as the drag preview.
- **Important**: The control must not be in the scene tree and is deleted after the drag.

---

### **2. Positioning and Sizing**
#### **set_position(position: Vector2, keep_offsets: bool = false)**
- **Purpose**: Sets the control's position relative to its parent.
- **Parameters**:
  - `keep_offsets`: If `true`, anchors are updated instead of offsets.

#### **set_size(size: Vector2, keep_offsets: bool = false)**
- **Purpose**: Sets the control's size.
- **Note**: Use with `keep_offsets` to adjust anchors instead of offsets.

#### **set_global_position(position: Vector2, keep_offsets: bool = false)**
- **Purpose**: Sets the global (scene) position of the control.
- **Example**: Directly sets the position in the world coordinate system.

#### **set_end(position: Vector2) / set_begin(position: Vector2)**
- **Purpose**: Sets the end/begin position for layout (e.g., for `Preset_LEFT` layout).
- **Example**: `set_end(Vector2(100, 100))` sets the bottom-right corner.

#### **update_minimum_size()**
- **Purpose**: Invalidates the size cache, ensuring `get_minimum_size()` returns the correct value.
- **Note**: Automatically called when `custom_minimum_size` is set.

---

### **3. Layout Management**
#### **set_offset(side: Side, offset: float)**
- **Purpose**: Adjusts the offset for a specific side (e.g., left, right).
- **Example**: `set_offset(SIDE_LEFT, 10)` adds a 10-pixel left margin.

#### **set_offsets_preset(preset: LayoutPreset, resize_mode: int = 0, margin: int = 0)**
- **Purpose**: Applies a layout preset (e.g., `PRESET_LEFT_WIDE`).
- **Parameters**:
  - `resize_mode`: Determines how the control resizes (e.g., `LAYOUT_PRESET_NONE`).
  - `margin`: Gap between the control and edges.

#### **set_focus_neighbor(side: Side, neighbor: NodePath)**
- **Purpose**: Sets the focus neighbor for navigation (e.g., Tab key behavior).
- **Example**: `set_focus_neighbor(SIDE_BOTTOM, "ButtonInstance")`.

---

### **4. Global Position and Anchors**
#### **warp_mouse(position: Vector2)**
- **Purpose**: Moves the mouse cursor to the specified position relative to the control.
- **Note**: Supported only on Windows, macOS, and Linux.

#### **get_minimum_size() → Vector2**
- **Purpose**: Returns the calculated minimum size based on the control's properties and layout.

---

### **5. Internal and Custom Methods**
#### **has_custom_minimum_size() → bool**
- **Purpose**: Checks if the custom minimum size is enabled.

#### **_can_drop_data(position: Vector2, data: Variant) → bool**
- **Purpose**: Internal method to check if a drop is possible (customizable via `set_drag_forwarding`).

#### **_drop_data(position: Vector2, data: Variant)**
- **Purpose**: Internal method to handle the drop (customizable via `set_drag_forwarding`).

---

## **Important Notes**
- **Drag Preview**: The control passed to `set_drag_preview()` must not be in the scene tree.
- **Platform Support**: `warp_mouse()` is only supported on Windows, macOS, and Linux.
- **Layout Presets**: Use `set_offsets_preset()` for layout adjustments, e.g., `PRESET_LEFT` for left-aligned controls.
- **Anchors vs. Offsets**: Use `keep_offsets` to avoid directly modifying offset values when adjusting position.

---

## **Example Use Case**
```gdscript
# Custom drag-and-drop for a button
func _get_drag_data(position):
    var preview = Button.new()
    preview.text = "Drag Me"
    set_drag_preview(preview)
    return "Dragged Data"
```

This example creates a custom drag preview and returns data for the drag operation.

---

By leveraging these methods, developers can create flexible, interactive UI elements in Godot, tailored to specific layout and user interaction requirements.