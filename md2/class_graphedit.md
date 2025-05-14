Here's a structured explanation of the `GraphEdit` class in Godot, covering its key components, methods, theme properties, and usage scenarios:

---

### **Overview**
The `GraphEdit` class is a graph editor tool in Godot, designed for creating and managing node-based graphs. It handles node placement, port connections, grid interactions, snapping, and visual styling. It is commonly used in games or applications that require visual scripting or data flow systems.

---

### **Key Methods**

#### **Connection Management**
- **`get_connection()`**  
  Retrieves the current active connection being drawn.
- **`get_connections()`**  
  Returns a list of all existing connections.
- **`get_current_connection()`**  
  Gets the current connection being interacted with (e.g., during drag operations).
- **`get_dragged_connection()`**  
  Returns the connection being dragged by the user.
- **`get_snapped_point()`**  
  Returns the snapped point for alignment with grid or snapping settings.
- **`get_zoom()`**  
  Gets the current zoom level of the graph.
- **`get_zoomed_rect()`**  
  Returns the rectangle area currently zoomed into.

#### **Node and Port Interactions**
- **`get_selected_nodes()`**  
  Returns the list of selected nodes.
- **`get_selected_node()`**  
  Retrieves the currently selected node.
- **`get_selected_node_port()`**  
  Gets the selected port on the current node.
- **`get_selected_port()`**  
  Returns the selected port (e.g., being dragged or hovered).
- **`get_selected_port_connection()`**  
  Gets the connection associated with the selected port.
- **`on_connection_dragged()`**  
  Called when a connection is being dragged.
- **`on_connection_dragged_end()`**  
  Triggered when a connection drag ends (e.g., connection is finalized).
- **`on_connection_dragged_start()`**  
  Called when a connection drag begins.
- **`on_connection_hover()`**  
  Handles hover events over a connection.
- **`on_connection_terminated()`**  
  Called when a connection is terminated (e.g., drag ends without completing).
- **`on_connection_unhover()`**  
  Called when the mouse leaves a connection.
- **`on_node_dragged()`**  
  Handles node drag events.
- **`on_node_dragged_end()`**  
  Triggered when a node drag ends.
- **`on_node_dragged_start()`**  
  Called when a node drag begins.
- **`on_node_hover()`**  
  Handles hover events over a node.
- **`on_node_terminated()`**  
  Called when a node drag is terminated.
- **`on_node_unhover()`**  
  Called when the mouse leaves a node.
- **`on_node_unselected()`**  
  Handles when a node is unselected.
- **`on_port_hover()`**  
  Called when a port is hovered.
- **`on_port_terminated()`**  
  Triggered when a port drag ends.
- **`on_port_unhover()`**  
  Called when the mouse leaves a port.
- **`on_port_unselected()`**  
  Handles when a port is unselected.
- **`on_port_selected()`**  
  Called when a port is selected.

**Note:** Some method names are duplicates (e.g., `on_port_selected` appears multiple times), which may be a typo or error. Ensure consistency in method naming when implementing.

---

### **Theme Properties**
These control visual styles and colors for the graph editor:

#### **Connection & Hover Effects**
- **`activity`**  
  Color for connection lines when active (e.g., during set_connection_activity).
- **`connection_hover_tint_color`**  
  Tint color for connections when the mouse hovers over them.
- **`connection_rim_color`**  
  Rim color for connection lines to distinguish overlapping lines.
- **`connection_valid_target_tint_color`**  
  Tint color for connections when hovering over valid target ports.

#### **Grid & Snapping**
- **`grid_major`**  
  Color of major grid lines.
- **`grid_minor`**  
  Color of minor grid lines.
- **`connection_hover_thickness`**  
  Percentage increase in line width when the mouse hovers over a connection.

#### **UI Icons**
- **`grid_toggle`**  
  Icon for the grid toggle button.
- **`layout`**  
  Icon for the layout button to auto-arrange nodes.
- **`minimap_toggle`**  
  Icon for the minimap toggle.
- **`snapping_toggle`**  
  Icon for the snapping toggle.
- **`zoom_in`, `zoom_out`, `zoom_reset`**  
  Icons for zoom controls.

#### **Style Props**
- **`menu_panel`**  
  Background style for the UI panel (e.g., for the menu bar).
- **`panel`**  
  Background under the grid.
- **`panel_focus`**  
  Style for the graph editor when focused (e.g., for accessibility).

---

### **Usage Scenarios**

#### **1. Connecting Nodes**
- Use `get_current_connection()` to track the active connection.
- Call `on_connection_dragged()` to handle drag events and `on_connection_dragged_end()` to finalize the connection.

#### **2. Customizing Visuals**
- Modify `activity` to change the color of active connections.
- Adjust `grid_major` and `grid_minor` for grid line visibility.

#### **3. Handling User Interaction**
- Override methods like `on_node_hover()` to add custom hover effects (e.g., tooltips).
- Use `get_snapped_point()` to enforce snapping to grid or other points.

#### **4. Snapping & Grid**
- Enable snapping by adjusting `snapping_toggle` and using `get_snapped_point()`.
- Use `get_zoom()` and `get_zoomed_rect()` to scale the graph view.

#### **5. Node & Port Management**
- Select nodes with `get_selected_node()` and manage ports via `get_selected_port()`.
- Use `on_port_selected()` to trigger actions when a port is clicked.

---

### **Potential Issues**
- **Duplicate Methods:** Methods like `on_port_selected` are listed multiple times. This may be a formatting error in the original documentation. Review and ensure each method is unique.
- **Theme Property Overriding:** Ensure theme properties are correctly applied in the `GraphEdit` node's style settings.
- **Event Handling:** Verify that event handlers (e.g., `on_connection_dragged`) are correctly connected to signals or custom logic.

---

### **Example Implementation**
```gdscript
func _ready():
    # Example: Change connection activity color
    theme.get_stylebox("activity").set_color(Color(1, 0, 0, 0.8))

    # Example: Handle node hover
    connect("on_node_hover", self, "_on_node_hover")

func _on_node_hover(node):
    print("Node hovered:", node.name)
```

---

This documentation provides a comprehensive guide to using the `GraphEdit` class, focusing on its core functionality, visual customization, and interaction handling. Developers can extend it to build custom graph editors for games, workflows, or data visualization tools.