Here's a step-by-step guide to creating and customizing a `PopupMenu` in Godot, including checkboxes, radio buttons, separators, and theme customization:

---

### **1. Basic Popup Menu Setup**
Create a `PopupMenu` node in your scene and add items:

```gdscript
# In your script
var menu = PopupMenu.new()
menu.add_item("Item 1")
menu.add_item("Item 2")
menu.add_check_item("Check Item")
menu.add_radio_item("Radio Item")
menu.add_separator()
menu.set_item_text(0, "Custom Item 1")
menu.set_item_icon(0, load("res://icon.png"))  # Use new method
```

---

### **2. Customizing Appearance with Themes**
Use the `Theme` system to customize the popup menu's look:

#### **a. Set Fonts and Colors**
```gdscript
var theme = get_theme()
theme.set_font("font", Font.new())  # Custom font
theme.set_font_size("font_size", 16)
theme.set_color("color", Color(0.2, 0.5, 0.8))  # Text color
```

#### **b. Set Icons**
```gdscript
theme.set_icon("unchecked", load("res://checkbox_unchecked.png"))
theme.set_icon("checked", load("res://checkbox_checked.png"))
theme.set_icon("submenu", load("res://submenu_arrow.png"))
```

#### **c. Set Style Boxes**
```gdscript
theme.set_stylebox("panel", StyleBox.new("rounded", 8, Color(0.3, 0.3, 0.3)))
theme.set_stylebox("hover", StyleBox.new("outlined", 2, Color(0.5, 0.5, 0.5)))
```

---

### **3. Handling User Interaction**
Connect the `item_selected` signal to handle selections:

```gdscript
func _ready():
    menu.connect("item_selected", self, "_on_item_selected")

func _on_item_selected(item_index):
    print("Selected item:", menu.get_item_text(item_index))
```

---

### **4. Advanced Features**
- **Checkboxes/Radio Buttons**:
  ```gdscript
  menu.add_check_item("Checkbox Item")
  menu.add_radio_item("Radio Item")
  menu.set_check_item_checked(0, true)  # Enable checkbox
  ```

- **Separator Customization**:
  ```gdscript
  theme.set_stylebox("separator", StyleBox.new("beveled", 2, Color(0.4, 0.4, 0.4)))
  ```

- **Item Positioning**:
  ```gdscript
  menu.set_item_offset(0, Vector2(10, 0))  # Offset first item
  menu.set_item_height(0, 30)  # Custom height for first item
  ```

---

### **5. Deprecated vs New Methods**
- **Deprecated**: `set_item_icon()`  
  **Use**: `set_item_icon_from_texture()` or set the theme icon property.

---

### **6. Example: Custom Popup with Themes**
```gdscript
func _ready():
    var menu = PopupMenu.new()
    menu.add_check_item("Check Item")
    menu.add_radio_item("Radio Item")
    menu.add_separator()

    # Customize theme
    var theme = get_theme()
    theme.set_icon("unchecked", load("res://checkbox_unchecked.png"))
    theme.set_icon("checked", load("res://checkbox_checked.png"))
    theme.set_stylebox("panel", StyleBox.new("rounded", 8, Color(0.3, 0.3, 0.3)))

    menu.connect("item_selected", self, "_on_item_selected")

    # Show the popup
    menu.popup()
```

---

### **7. Tips**
- Use the **Godot Theme Editor** to adjust themes visually.
- For complex UIs, consider using `Control` and `LineEdit` inside the popup for dynamic content.
- Test layout with `set_item_offset()` and `set_item_height()` to align items properly.

This setup allows you to create a fully customizable popup menu with interactive elements and a polished appearance.