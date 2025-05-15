# ThemeDB

### Overview
A singleton that provides access to static information about Theme resources used by the engine and by your project.

---

### Key Information

#### **Properties**
- **fallback_base_scale** (float): 1.0  
  Fallback base scale factor for Control nodes and Theme resources.  
  Methods: `set_fallback_base_scale(value: float)`, `get_fallback_base_scale()`

- **fallback_font** (Font):  
  Fallback font for Control nodes and Theme resources.  
  Methods: `set_fallback_font(value: Font)`, `get_fallback_font()`

- **fallback_font_size** (int): 16  
  Fallback font size for Control nodes and Theme resources.  
  Methods: `set_fallback_font_size(value: int)`, `get_fallback_font_size()`

- **fallback_icon** (Texture2D):  
  Fallback icon for Control nodes and Theme resources.  
  Methods: `set_fallback_icon(value: Texture2D)`, `get_fallback_icon()`

- **fallback_stylebox** (StyleBox):  
  Fallback stylebox for Control nodes and Theme resources.  
  Methods: `set_fallback_stylebox(value: StyleBox)`, `get_fallback_stylebox()`

---

#### **Methods**
- **get_default_theme()** → Theme  
  Returns the default engine Theme. Cannot be overridden.

- **get_project_theme()** → Theme  
  Returns the custom project Theme. Configure via `ProjectSettings.gui/theme/custom`.

---

#### **Signals**
- **fallback_changed()**  
  Emitted when a fallback value is modified. Use to refresh UI elements relying on fallback themes.

---

#### **Property Descriptions**
- **fallback_base_scale**  
  Scales all Control nodes and Theme resources when no specific value is available.  
  See also: `Theme.default_base_scale`.

- **fallback_font**  
  Default font used by controls when no specific font is defined.  
  See also: `Theme.default_font`.

- **fallback_font_size**  
  Default font size for controls when no specific size is defined.  
  See also: `Theme.default_font_size`.

- **fallback_icon**  
  Default icon used by controls when no specific icon is defined.

- **fallback_stylebox**  
  Default stylebox for controls when no specific stylebox is defined.

---

#### **Related Concepts**
- **fallback_changed signal**: Triggers when fallback values are updated.  
- **ThemeDB inherits from Object**: Provides access to static theme data.  
- **ThemeDB is a singleton**: Ensures a single instance for global theme access.