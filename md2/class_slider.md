### Slider Class Documentation

**Inheritance:**
- `Slider` inherits from `Range` and `Control`.

---

#### **Description**
A slider widget for controlling values within a range. It supports horizontal or vertical orientation and can be used for input or visual feedback.

---

#### **Properties**

- **tick_count**:  
  Type: `int`  
  Default: `0`  
  Description: Number of ticks (marks) on the slider.  
  Methods:  
  - `set_tick_count(value)`: Sets the number of ticks.  
  - `get_tick_count()`: Retrieves the current tick count.

- **value**:  
  Type: `float`  
  Default: `0`  
  Description: Current value of the slider.  
  Methods:  
  - `set_value(value)`: Sets the slider's value.  
  - `get_value()`: Retrieves the current value.

- **min**:  
  Type: `float`  
  Default: `0`  
  Description: Minimum value of the slider range.  
  Methods:  
  - `set_min(value)`: Sets the minimum value.  
  - `get_min()`: Retrieves the minimum value.

- **max**:  
  Type: `float`  
  Default: `100`  
  Description: Maximum value of the slider range.  
  Methods:  
  - `set_max(value)`: Sets the maximum value.  
  - `get_max()`: Retrieves the maximum value.

---

#### **Theme Properties**

- **slider**:  
  Type: `StyleBox`  
  Description: Background style for the entire slider. Affects the height/width of the grabber area.

- **grabber_area**:  
  Type: `StyleBox`  
  Description: Background of the area to the left or bottom of the grabber.

- **grabber_area_highlight**:  
  Type: `StyleBox`  
  Description: Highlight background for the grabber area on hover/focus.

- **grabber**:  
  Type: `Texture`  
  Description: Texture for the grabber (slider handle).

- **grabber_disabled**:  
  Type: `Texture`  
  Description: Texture for the grabber when the slider is disabled.

- **grabber_highlight**:  
  Type: `Texture`  
  Description: Texture for the grabber when focused.

- **tick**:  
  Type: `Texture`  
  Description: Texture for the ticks (marks) on the slider.

---

#### **Signals**

- **drag_ended**:  
  Description: Emitted when the slider is released after being dragged.  
  Parameters: None.

- **drag_started**:  
  Description: Emitted when the slider is clicked and begins to be dragged.  
  Parameters: None.

---

#### **Methods**

- **_notification(int)`:  
  Description: Called when the widget receives a notification from the engine.  
  Parameters: `notification` (int).

- **_process(float)`:  
  Description: Called every physics frame.  
  Parameters: `delta` (float).

- **_ready()`:  
  Description: Called once the node is added to the scene graph.  
  Parameters: None.

---

This documentation provides a concise overview of the `Slider` class, its properties, theme-related settings, signals, and methods.