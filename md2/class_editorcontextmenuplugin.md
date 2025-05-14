### EditorContextMenuPlugin

**Inherits from:** `RefCounted`

---

### Description
The `EditorContextMenuPlugin` class is used to add custom context menu items to the Godot editor. It allows users to register actions, shortcuts, and submenus in various editor docks (e.g., FileSystem, SceneTree, etc.).

---

### Enumerations

**ContextMenuSlot**  
| Value | Description |
|-------|-------------|
| `POPUP_MENU` | Represents the main context menu. |
| `SCENE_TREE` | Context menu for the SceneTree dock. |
| `EDITOR` | General editor context menu. |
| `FILE_SYSTEM` | Context menu for the FileSystem dock. |

---

### Methods

1. **`_popup_menu(paths)`**  
   - **Parameters:** `paths` (Array of strings).  
   - **Description:** Called when the context menu is popped up. This is where you add items, submenus, or handle interactions.  

2. **`add_context_menu_item(name, shortcut, icon)`**  
   - **Parameters:** `name` (String), `shortcut` (Shortcut), `icon` (Texture2D).  
   - **Description:** Adds a contextual menu item with a shortcut.  

3. **`add_context_submenu_item(name, menu, icon)`**  
   - **Parameters:** `name` (String), `menu` (PopupMenu), `icon` (Texture2D).  
   - **Description:** Adds a submenu to the context menu. The submenu must be managed manually.  

4. **`add_menu_shortcut(shortcut, callback)`**  
   - **Parameters:** `shortcut` (Shortcut), `callback` (Callable).  
   - **Description:** Registers a shortcut associated with the plugin's context menu.  

---

### Method Descriptions

**`_popup_menu(paths)`**  
This method is called when the context menu is displayed. Use it to add items, submenus, or handle interactions. Example:  
```gdscript
func _popup_menu(paths):
    var popup_menu = PopupMenu.new()
    popup_menu.add_item("Blue")
    popup_menu.add_item("White")
    popup_menu.id_pressed.connect(_on_color_submenu_option)
    
    add_context_submenu_item("Set Node Color", popup_menu)
```

**`add_context_menu_item(name, shortcut, icon)`**  
Adds a menu item with an associated shortcut. Example:  
```gdscript
func _init():
    add_menu_shortcut(SHORTCUT, handle)
    
func _popup_menu(paths):
    add_context_menu_item_from_shortcut("File Custom options", SHORTCUT, ICON)
```

**`add_context_submenu_item(name, menu, icon)`**  
Adds a submenu that requires manual management (e.g., connecting signals). Example:  
```gdscript
func _popup_menu(paths):
    var popup_menu = PopupMenu.new()
    popup_menu.add_item("Blue")
    popup_menu.add_item("White")
    popup_menu.id_pressed.connect(_on_color_submenu_option)
    
    add_context_submenu_item("Set Node Color", popup_menu)
```

**`add_menu_shortcut(shortcut, callback)`**  
Registers a shortcut for the plugin. Example:  
```gdscript
func _init():
    add_menu_shortcut(SHORTCUT, handle)
```

---

### Key Notes
- **`_popup_menu`** is the primary method for customizing context menus.
- **Submenus** must be created and managed manually.
- **Shortcuts** are tied to specific context menus (e.g., FileSystem, SceneTree).