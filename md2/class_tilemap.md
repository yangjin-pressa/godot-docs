Here's a detailed explanation of the **TileMap** class methods in Godot, organized by their purpose and usage:

---

### **1. Layer Control**
- **`set_layer_enabled(layer: int, enabled: bool)`**  
  Enables or disables a layer. Disabled layers are not rendered or processed.  
  **Example:**  
  ```gdscript
  tile_map.set_layer_enabled(0, true)  # Enable the first layer
  ```

- **`get_layer_enabled(layer: int) -> bool`**  
  Checks if a layer is enabled.  
  **Example:**  
  ```gdscript
  if tile_map.get_layer_enabled(1): print("Layer 1 is enabled")
  ```

- **`set_layer_name(layer: int, name: String)`**  
  Sets a layer's name for the editor (e.g., "Background").  
  **Example:**  
  ```gdscript
  tile_map.set_layer_name(0, "Background")
  ```

---

### **2. Color Modulation**
- **`set_layer_modulate(layer: int, modulate: Color)`**  
  Sets a color multiplier for a layer. This is applied to the layer's tiles.  
  **Example:**  
  ```gdscript
  tile_map.set_layer_modulate(1, Color(1, 0, 0, 1))  # Red tint for layer 1
  ```

---

### **3. Navigation Settings**
- **`set_layer_navigation_enabled(layer: int, enabled: bool)`**  
  Enables or disables built-in navigation regions for a layer.  
  **Example:**  
  ```gdscript
  tile_map.set_layer_navigation_enabled(0, true)  # Enable navigation for layer 0
  ```

- **`set_layer_navigation_map(layer: int, map: RID)`**  
  Assigns a navigation map to a layer.  
  **Example:**  
  ```gdscript
  var nav_map = NavigationServer2D.get_map("nav_map")
  tile_map.set_layer_navigation_map(1, nav_map)
  ```

---

### **4. Y-Sorting (Z-Order)**
- **`set_layer_y_sort_enabled(layer: int, y_sort_enabled: bool)`**  
  Enables or disables Y-sorting for a layer. Y-sorting sorts tiles by Y-coordinate.  
  **Example:**  
  ```gdscript
  tile_map.set_layer_y_sort_enabled(0, true)
  ```

- **`set_layer_y_sort_origin(layer: int, y_sort_origin: int)`**  
  Sets the Y-sort origin for a layer, allowing height-based sorting.  
  **Example:**  
  ```gdscript
  tile_map.set_layer_y_sort_origin(0, 100)
  ```

- **`set_layer_z_index(layer: int, z_index: int)`**  
  Sets the Z-index for a layer (used for rendering order).  
  **Example:**  
  ```gdscript
  tile_map.set_layer_z_index(1, 50)
  ```

---

### **5. Pattern Creation**
- **`set_pattern(layer: int, position: Vector2, pattern: TileMapPattern)`**  
  Paste a `TileMapPattern` into a specific position and layer.  
  **Example:**  
  ```gdscript
  var pattern = TileMapPattern.new()
  pattern.add_tile(0, 0, 1)  # Add a tile to the pattern
  tile_map.set_pattern(0, Vector2(10, 10), pattern)
  ```

---

### **6. Forced Update**
- **`update_internals()`**  
  Forces the TileMap to update its internal state (e.g., when data changes).  
  **Example:**  
  ```gdscript
  tile_map.update_internals()
  ```

---

### **7. Navigation Map (Deprecated)**
- **`set_navigation_map(map: RID)`**  
  Assigns a navigation map to the entire TileMap (not per-layer).  
  **Example:**  
  ```gdscript
  var nav_map = NavigationServer2D.get_map("nav_map")
  tile_map.set_navigation_map(nav_map)
  ```

---

### **Example: Full TileMap Usage**
```gdscript
# Create a TileMap node
var tile_map =.TileMap.new()

# Add layers
tile_map.add_layer(0)
tile_map.add_layer(1)

# Enable layer 0 and set its name
tile_map.set_layer_enabled(0, true)
tile_map.set_layer_name(0, "Background")

# Disable layer 1
tile_map.set_layer_enabled(1, false)

# Set Y-sort for layer 1
tile_map.set_layer_y_sort_enabled(1, true)

# Create and apply a pattern
var pattern = TileMapPattern.new()
pattern.add_tile(0, 0, 1)  # Add a tile at position (0,0)
tile_map.set_pattern(1, Vector2(10, 10), pattern)

# Force update
tile_map.update_internals()
```

---

### **Key Notes**
- **Layers** are used for separating different elements (e.g., background, foreground, UI).  
- **Navigation** settings are essential for pathfinding in 2D games.  
- **Y-sorting** and **Z-index** control the rendering order of layers.  
- **Patterns** can be used for procedural generation or custom tile placement.  

This covers the primary methods of the `TileMap` class, enabling you to manage layers, navigation, and visual properties in Godot.