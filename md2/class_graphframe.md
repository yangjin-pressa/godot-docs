**GraphFrame Class Documentation**

---

### **Description**
The `GraphFrame` class is used to represent a frame in a graph editor, allowing for the addition and management of nodes and edges. It includes a title bar, support for shrinking, and styling options.

---

### **Properties**
- **autoshrink_enabled**  
  **Type:** `bool`  
  **Default:** `true`  
  Whether the frame is shrinkable.  

- **autoshrink_margin**  
  **Type:** `int`  
  **Default:** `0`  
  The margin for shrinking.  

- **title**  
  **Type:** `String`  
  **Default:** `""`  
  Title of the frame.  

---

### **Methods**
- **get_titlebar_hbox()**  
  **Return Type:** `HBoxContainer`  
  Returns the `HBoxContainer` used for the title bar, containing a `Label` for the title.  
  *Can be used to add custom controls to the title bar.*

---

### **Signals**
- **autoshrink_changed**  
  Emitted when **[autoshrink_enabled](class_GraphFrame_property_autoshrink_enabled)** or **[autoshrink_margin](class_GraphFrame_property_autoshrink_margin)** changes.  

---

### **Theme Properties**
- **resizer_color**  
  **Type:** `Color`  
  **Default:** `Color(0.875, 0.875, 0.875, 1)`  
  The color modulation applied to the resizer icon.  

- **panel**  
  **Type:** `StyleBox`  
  The default `StyleBox` used for the background of the `GraphFrame`.  

- **panel_selected**  
  **Type:** `StyleBox`  
  The `StyleBox` used for the background of the `GraphFrame` when it is selected.  

- **titlebar**  
  **Type:** `StyleBox`  
  The `StyleBox` used for the title bar of the `GraphFrame`.  

- **titlebar_selected**  
  **Type:** `StyleBox`  
  The `StyleBox` used for the title bar of the `GraphFrame` when it is selected.  

---

### **Property Descriptions**
- **autoshrink_enabled**  
  If `true`, the frame can be shrunk.  

- **autoshrink_margin**  
  The amount of space to leave when shrinking the frame.  

- **title**  
  A string representing the title displayed in the title bar.  

---

### **Method Descriptions**
- **get_titlebar_hbox()**  
  Returns the `HBoxContainer` for the title bar, which includes a `Label` to display the title.  
  *Custom controls can be added to the title bar via this method.*  

---

### **Theme Property Descriptions**
- **resizer_color**  
  Modifies the color of the resizer icon (e.g., for resizing the frame).  

- **panel**  
  Defines the visual style for the background of the `GraphFrame`.  

- **panel_selected**  
  Defines the visual style for the selected `GraphFrame`.  

- **titlebar**  
  Defines the visual style for the title bar of the `GraphFrame`.  

- **titlebar_selected**  
  Defines the visual style for the title bar when the `GraphFrame` is selected.  

---

### **Key Notes**
- **virtual**  
  Methods should typically be overridden by the user to have any effect.  

- **const**  
  Methods have no side effects and do not modify instance variables.  

- **vararg**  
  Methods accept any number of arguments after the ones described.  

- **constructor**  
  Used to create an instance of the `GraphFrame` class.  

- **static**  
  Methods can be called directly using the class name without an instance.  

- **operator**  
  Describes valid operators for use with the `GraphFrame` class.  

- **bitfield**  
  Values are integers composed as a bitmask of flags.  

- **void**  
  Methods return no value.  

--- 

This documentation provides a concise overview of the `GraphFrame` class, including its properties, methods, signals, and theme-related settings.