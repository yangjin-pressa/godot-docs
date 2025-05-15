**Range Class Overview**  
A base class for controls that represent a numerical value within a range. Inherited by classes like `ScrollBar`, `Slider`, etc.

---

### **Key Features**  
- **Abstract Base Class**: Provides common functionality for range-related UI elements.  
- **Value Range**: Defined by `min_value` and `max_value`.  
- **Sharing**: Supports grouping multiple `Range` instances for synchronized values.  

---

### **Properties**  
| Name         | Type    | Default | Description                                                                 |
|--------------|---------|---------|-----------------------------------------------------------------------------|
| `min_value`  | `float` | `0.0`   | Minimum value in the range. Clamps the value if it goes below this.         |
| `max_value`  | `float` | `100.0` | Maximum value in the range. Clamps the value if it goes above this.         |
| `step`       | `float` | `0.01`  | Rounding precision. Values are rounded to multiples of this value.          |
| `rounded`    | `bool`  | `false` | If `true`, values are rounded to integers.                                |
| `page`       | `float` | `0.0`   | Page size for scroll-based controls (e.g., `ScrollBar`).                  |
| `ratio`      | `float` | —       | Normalized value between 0 (min) and 1 (max).                              |
| `value`      | `float` | `0.0`   | Current value. Changing this triggers the `value_changed` signal.          |
| `allow_greater` | `bool` | `false` | If `true`, allows value to exceed `max_value`.                            |
| `allow_lower` | `bool` | `false` | If `true`, allows value to go below `min_value`.                          |

---

### **Methods**  
- **`_value_changed(new_value: float)`**  
  Virtual method called when the value is updated (e.g., via user interaction).  

- **`set_value_no_signal(value: float)`**  
  Sets the value without emitting the `value_changed` signal.  

- **`share(with: Node)`**  
  Groups this `Range` with another, synchronizing their values and properties.  

- **`unshare()`**  
  Stops sharing with other `Range` instances.  

---

### **Signals**  
- **`value_changed`**  
  Emitted when the `value` property changes (e.g., user interaction).  

- **`changed`**  
  Emitted when `min_value`, `max_value`, or `step` changes.  

---

### **Important Notes**  
1. **Clamping**: Values are automatically clamped between `min_value` and `max_value`.  
2. **Ratio**: `ratio` is a normalized value (0–1) for proportional UI elements.  
3. **Sharing**: `share()` binds multiple `Range` instances; `unshare()` breaks the link.  
4. **Debouncing**: Direct value changes (e.g., via code) may require `set_value_no_signal()` to avoid signal emission.  

---

### **Inherited By**  
- `ScrollBar`  
- `Slider`  
- `RangeSlider`  
- Other range-based UI controls.