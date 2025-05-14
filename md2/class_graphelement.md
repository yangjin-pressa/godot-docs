**GraphElement**  
A class representing an element in a UI system, with properties for interaction and visual customization.  

---

### **Description**  
The `GraphElement` class is used to manage interactive elements in a UI system. It provides properties for controlling visual behavior, such as resizability, and includes signals for user interactions.  

---

### **Properties**  
- **type**: `bool`  
  **name**: `draggable`  
  **default**: `true`  
  **description**: Controls whether the element can be dragged.  

- **type**: `Vector2`  
  **name**: `position_offset`  
  **default**: `Vector2(0, 0)`  
  **description**: Offset for positioning the element.  

- **type**: `bool`  
  **name**: `resizable`  
  **default**: `false`  
  **description**: Determines if the element can be resized.  

- **type**: `Texture2D`  
  **name**: `resizer`  
  **default**: `null`  
  **description**: Icon used for the resizer when `resizable` is enabled.  

---

### **Theme Properties**  
- **type**: `Texture2D`  
  **name**: `resizer`  
  **description**: The icon used for the resizer, visible when `resizable` is enabled.  

---

### **Signals**  
- **delete_request()**:  
  Emitted when the element is removed.  

- **dragged(pos: Vector2)**:  
  Emitted when the element is dragged.  

- **node_deselected()**:  
  Emitted when the element is deselected.  

- **resized(size: Vector2)**:  
  Emitted when the element is resized.  

---

### **Property Descriptions**  
- **draggable**: A boolean property that determines if the element can be dragged.  

- **position_offset**: A vector2 property that defines the offset for positioning the element.  

- **resizable**: A boolean property that controls whether the element can be resized.  

- **resizer**: A texture2d property that sets the icon for the resizer when `resizable` is enabled.  

---

### **Theme Property Descriptions**  
- **resizer**: The icon used for the resizer, visible when `resizable` is enabled.  

--- 

**Notes**:  
- `draggable` and `resizable` are boolean properties that control interaction behaviors.  
- `resizer` is a texture property that customizes the resizer appearance.  
- Signals are emitted during user interactions (drag, resize, etc.).