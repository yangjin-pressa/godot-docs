**CameraFeed Class**  

**Inherits:** `RefCounted`  

---

### **Overview**  
- **Purpose:** Provides access to a physical camera.  
- **Notes:**  
  - YCbCr images require shader-based combination for proper display.  
  - Platform support: Works on most systems, but external libraries may be needed for texture handling.  

---

### **Properties**  
1. **`feed_is_active`**  
   - **Type:** `bool`  
   - **Default:** `false`  
   - **Description:** Indicates whether the camera feed is active.  

2. **`feed_transform`**  
   - **Type:** `Transform2D`  
   - **Default:** `Transform2D(1, 0, 0, -1, 0, 1)`  
   - **Description:** Transform applied to the camera's image.  

3. **`formats`**  
   - **Type:** `Array`  
   - **Default:** `[]`  
   - **Description:** Supported formats (array of `Dictionary` entries).  

---

### **Methods**  
1. **`_activate_feed()`** (virtual)  
   - **Description:** Called when the camera feed is activated.  

2. **`_deactivate_feed()`** (virtual)  
   - **Description:** Called when the camera feed is deactivated.  

3. **`get_datatype()`** (const)  
   - **Returns:** `FeedDataType`  
   - **Description:** Returns the feed image data type.  

4. **`get_id()`** (const)  
   - **Returns:** `int`  
   - **Description:** Returns the unique ID for this feed.  

5. **`get_name()`** (const)  
   - **Returns:** `String`  
   - **Description:** Returns the camera's name.  

6. **`get_position()`** (const)  
   - **Returns:** `FeedPosition`  
   - **Description:** Returns the position of the camera on the device.  

7. **`get_texture_tex_id()`**  
   - **Parameters:** `feed_image_type` (`FeedImage`)  
   - **Returns:** `int`  
   - **Description:** Returns the texture backend ID for external libraries.  

8. **`set_external(width, height)`**  
   - **Description:** Sets the feed as external (provided by another library).  

9. **`set_format(index, parameters)`**  
   - **Returns:** `bool`  
   - **Description:** Sets the feed format parameters. Output format can be:  
     - `separate` → `FeedDataType.YCBCR_SEP`  
     - `grayscale` → desaturated `FeedDataType.RGB`  
     - `copy` → `FeedDataType.YCBCR`  

10. **`set_name(name)`**  
    - **Description:** Sets the camera's name.  

11. **`set_position(position)`**  
    - **Description:** Sets the position of this camera.  

12. **`set_rgb_image(rgb_image)`**  
    - **Description:** Sets RGB image for this feed.  

13. **`set_ycbcr_image(ycbcr_image)`**  
    - **Description:** Sets YCbCr image for this feed.  

---

### **Signals**  
1. **`format_changed()`**  
   - **Description:** Emitted when the format changes.  

2. **`frame_changed()`**  
   - **Description:** Emitted when a new frame is available.  

---

### **Enumerations**  
#### **FeedDataType**  
- **FEED_NOIMAGE**  
  - No image data.  
- **FEED_RGB**  
  - Standard RGB format.  
- **FEED_YCBCR**  
  - YCbCr format (requires conversion).  
- **FEED_YCBCR_SEP**  
  - Separated YCbCr channels (requires shader).  

#### **FeedPosition**  
- **FEED_POSITION_UNKNOWN**  
  - Default position.  
- **FEED_POSITION_FRONT**  
  - Front-facing camera.  
- **FEED_POSITION_BACK**  
  - Back-facing camera.  

---

### **Key Notes**  
- **Platform Compatibility:** Works on most systems, but external libraries may be needed for texture handling.  
- **Texture Handling:** `get_texture_tex_id()` provides a backend ID for external libraries.  
- **Format Conversion:** YUYV streams default to `FEED_RGB`, but can be adjusted via `set_format()`.