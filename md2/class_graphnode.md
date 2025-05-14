# GraphNode Class Documentation

## Methods

### get_resizer_color
**Description:** Returns the color modulation applied to the resizer icon.  
**Return Type:** `Color`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

### get_port_h_offset
**Description:** Returns the horizontal offset for the ports.  
**Return Type:** `int`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

### get_separation
**Description:** Returns the vertical distance between ports.  
**Return Type:** `int`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

### get_port_icon
**Description:** Returns the icon used for representing ports.  
**Return Type:** `Texture2D`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

### get_slot_panel
**Description:** Returns the default background for the slot area of the GraphNode.  
**Return Type:** `StyleBox`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

### get_slot_panel_focus
**Description:** Returns the StyleBox used when the GraphNode is focused.  
**Return Type:** `StyleBox`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

### get_slot_panel_selected
**Description:** Returns the StyleBox used for the slot area when selected.  
**Return Type:** `StyleBox`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

### get_slot_style
**Description:** Returns the StyleBox used for each slot of the GraphNode.  
**Return Type:** `StyleBox`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

### get_slot_style_selected
**Description:** Returns the StyleBox used when the slot is focused.  
**Return Type:** `StyleBox`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

### get_titlebar_style
**Description:** Returns the StyleBox used for the title bar of the GraphNode.  
**Return Type:** `StyleBox`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

### get_titlebar_style_selected
**Description:** Returns the StyleBox used for the title bar when the GraphNode is selected.  
**Return Type:** `StyleBox`  
**Note:** This method is virtual and should be overridden by the user if custom behavior is needed.

---

## Theme Properties

### resizer_color
**Type:** `Color`  
**Default Value:** `Color(0.875, 0.875, 0.875, 1)`  
**Description:** The color modulation applied to the resizer icon. This property controls the visual appearance of the resizer icon in the GraphNode.

### port_h_offset
**Type:** `int`  
**Default Value:** `0`  
**Description:** Horizontal offset for the ports. This property determines the horizontal positioning of ports relative to the GraphNode's boundaries.

### separation
**Type:** `int`  
**Default Value:** `2`  
**Description:** The vertical distance between ports. This property controls the spacing between ports along the vertical axis.

### port
**Type:** `Texture2D`  
**Description:** The icon used for representing ports. This property defines the visual representation of ports in the GraphNode.

### panel
**Type:** `StyleBox`  
**Description:** The default background for the slot area of the GraphNode. This property sets the base styling for the slot area.

### panel_focus
**Type:** `StyleBox`  
**Description:** The StyleBox used when the GraphNode is focused. This property provides the visual feedback for focused state.

### panel_selected
**Type:** `StyleBox`  
**Description:** The StyleBox used for the slot area when selected. This property defines the styling for selected slots.

### slot
**Type:** `StyleBox`  
**Description:** The StyleBox used for each slot of the GraphNode. This property sets the base styling for individual slots.

### slot_selected
**Type:** `StyleBox`  
**Description:** The StyleBox used when the slot is focused. This property provides the visual feedback for focused slots.

### titlebar
**Type:** `StyleBox`  
**Description:** The StyleBox used for the title bar of the GraphNode. This property defines the styling for the title bar.

### titlebar_selected
**Type:** `StyleBox`  
**Description:** The StyleBox used for the title bar when the GraphNode is selected. This property defines the styling for the title bar in selected state.