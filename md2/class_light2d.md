Here's a structured explanation of the **Light2D** class in Godot, covering its properties, methods, and key behaviors:

---

### **Key Properties**
1. **Color**  
   - **Type:** `Color`  
   - **Default:** `(1, 1, 1, 1)`  
   - **Description:** The main color of the light. Adjusts the hue, saturation, and brightness.

2. **Shadow Color**  
   - **Type:** `Color`  
   - **Default:** `(0, 0, 0, 0)`  
   - **Description:** The color of shadows cast by the light. A transparent color `(0, 0, 0, 0)` means no shadows.

3. **Shadow Enabled**  
   - **Type:** `bool`  
   - **Default:** `false`  
   - **Description:** If `true`, the light casts shadows. Disabled by default.

4. **Shadow Filter**  
   - **Type:** `ShadowFilter` (Enum)  
   - **Default:** `NONE`  
   - **Options:**  
     - `NONE`: No shadow filtering.  
     - `PCF5`: Soft shadows using a 5-point filter.  
     - `PCF13`: Soft shadows using a 13-point filter.  
   - **Note:** `PCF5` and `PCF13` require `shadow_filter_smooth` for softness.

5. **Shadow Filter Smooth**  
   - **Type:** `float`  
   - **Default:** `0.0`  
   - **Description:** Controls the softness of shadows when using `PCF5` or `PCF13`. Higher values create softer shadows but may introduce streaks.

6. **Shadow Item Cull Mask**  
   - **Type:** `int`  
   - **Default:** `1`  
   - **Description:** Mask for objects that cast shadows. Only objects with a matching `CanvasItem.light_mask` cast shadows.

7. **Range Item Cull Mask**  
   - **Type:** `int`  
   - **Default:** `1`  
   - **Description:** Mask for objects that receive light. Only objects with a matching `CanvasItem.light_mask` are affected by the light.  
   - **Note:** `DirectionalLight2D` ignores this mask.

8. **Range Layer Min/Max**  
   - **Type:** `int`  
   - **Default:** `0`  
   - **Description:** Define the minimum and maximum layer values for objects affected by the light. Useful for layer-based lighting.

9. **Range Z Min/Max**  
   - **Type:** `int`  
   - **Default:** `-1024` (min) and `1024` (max)  
   - **Description:** Define the minimum and maximum `z` values for objects affected by the light. Useful for depth-based lighting.

10. **Height**  
    - **Type:** `float`  
    - **Default:** `1.0`  
    - **Description:** Used in 2D normal mapping. Adjusts how the light interacts with surface normals. Relevant for `PointLight2D` and `DirectionalLight2D`.

---

### **Key Methods**
1. **`get_height()`**  
   - **Return Type:** `float`  
   - **Description:** Retrieves the current height value for 2D normal mapping.

2. **`set_height(float height)`**  
   - **Description:** Sets the height value for 2D normal mapping. Adjusts how the light interacts with surface normals.

---

### **Important Notes**
- **Light vs Shadow Cull Masks:**  
  - `range_item_cull_mask` determines which objects **receive** light.  
  - `shadow_item_cull_mask` determines which objects **cast** shadows.  
  - These masks are checked against `CanvasItem.light_mask` to filter objects.

- **DirectionalLight2D Behavior:**  
  - Ignores `range_item_cull_mask` and `range_z_min`/`max`.  
  - Always lights objects regardless of their `CanvasItem.light_mask`.

- **Shadow Filtering:**  
  - `shadow_filter_smooth` only affects `PCF5` and `PCF13` filters.  
  - Higher values create softer shadows but may introduce visible artifacts.

- **2D Normal Mapping:**  
  - The `height` property affects how light interacts with surface normals. Use it for advanced effects like terrain lighting.

---

### **Use Cases**
- **Basic Lighting:** Adjust color, layer ranges, and cull masks to control which objects are lit.  
- **Shadow Effects:** Enable shadows, set the shadow filter, and adjust smoothness for soft shadows.  
- **2D Normal Mapping:** Modify the `height` property to simulate light interaction with 2D surfaces (e.g., terrain, objects with normals).

This structure allows you to fine-tune lighting behavior for 2D scenes, whether for simple illumination or advanced effects like shadows and normal mapping.