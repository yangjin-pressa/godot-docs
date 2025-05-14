**Class: OccluderPolygon2D**

**Inherits From:**  
- `Resource`  
- `RefCounted`  
- `Object`  

**Description:**  
An editor facility for drawing a 2D polygon used for `LightOccluder2D`.  

---

### **Properties**  
1. **`closed`**  
   - **Type:** `bool`  
   - **Default Value:** `true`  
   - **Methods:**  
     - `set_closed(value: bool)`  
     - `get_closed(): bool`  

2. **`cull_mode`**  
   - **Type:** `CullMode`  
   - **Default Value:** `0` (CULL_DISABLED)  
   - **Methods:**  
     - `set_cull_mode(value: CullMode)`  
     - `get_cull_mode(): CullMode`  

3. **`polygon`**  
   - **Type:** `PackedVector2Array`  
   - **Default Value:** Empty  
   - **Methods:**  
     - `set_polygon(value: PackedVector2Array)`  
     - `get_polygon(): PackedVector2Array`  

---

### **Enumerations**  
- **`CullMode`**  
  - `CULL_DISABLED`  
  - `CULL_CLOCKWISE`  
  - `CULL_COUNTER_CLOCKWISE`  

---

### **Notes**  
- The `polygon` property is a `PackedVector2Array`, which stores coordinates for the 2D polygon.  
- The `cull_mode` determines how the polygon is rendered (e.g., whether to cull back-facing polygons).