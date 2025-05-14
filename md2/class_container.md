Container  
--------------------------  
**Inherits**: Control < CanvasItem < Node < Object  
**Inherited By**:  
- class_Container  
- class_Control  
- class_CanvasItem  
- class_Node  
- class_Object  

**Description**:  
A base class for GUI containers that automatically arranges child controls.  

**Tutorials**:  
[Using Containers](../tutorials/ui/gui_containers)  

**Properties**:  
- `MouseFilter (mouse_filter)`: 1 (overrides Control's mouse_filter)  

**Methods**:  
- `_get_allowed_size_flags_horizontal`: Implement to return allowed horizontal SizeFlags for child nodes.  
- `_get_allowed_size_flags_vertical`: Implement to return allowed vertical SizeFlags for child nodes.  
- `_get_allowed_size_flags_horizontal`: (Note: duplicated entry, likely a mistake in the original text)  
- `_get_allowed_size_flags_vertical`: (Note: duplicated entry, likely a mistake in the original text)  

**Signals**:  
- `pre_sort_children`: Emitted when children are about to be sorted.  
- `sort_children`: Emitted after children have been sorted.  

**Constants**:  
- `NOTIFICATION_PRE_SORT_CHILDREN`: 1 (notifies before sorting children)  
- `NOTIFICATION_SORT_CHILDREN`: 2 (notifies after sorting children)  

**Method Descriptions**:  
- `_get_allowed_size_flags_horizontal`: Returns the horizontal SizeFlags that can be applied to child nodes. The value is derived from the `mouse_filter` property.  
- `_get_allowed_size_flags_vertical`: Returns the vertical SizeFlags that can be applied to child nodes. The value is derived from the `mouse_filter` property.  
- `pre_sort_children`: Triggered before sorting child nodes, allowing for pre-processing.  
- `sort_children`: Triggered after sorting child nodes, allowing for post-processing.  
- `NOTIFICATION_PRE_SORT_CHILDREN`: A constant used to trigger pre-sorting logic.  
- `NOTIFICATION_SORT_CHILDREN`: A constant used to trigger post-sorting logic.