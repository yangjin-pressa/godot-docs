Here's a structured guide on using the `Image` class in Godot, focusing on pixel manipulation and image saving:

---

### **1. Creating an Image**
To create an image, use the `Image.create()` method. The parameters are:
- `width`: Width of the image.
- `height`: Height of the image.
- `use_mipmaps`: Whether to use mipmaps (use `false` for most cases).
- `format`: The image format (e.g., `Image.FORMAT_RGBA8`).

**GDScript Example:**
```gdscript
var img_width = 10
var img_height = 5
var img = Image.create(img_width, img_height, false, Image.FORMAT_RGBA8)
```

**C# Example:**
```csharp
int imgWidth = 10;
int imgHeight = 5;
var img = Image.Create(imgWidth, imgHeight, false, Image.Format.Rgba8);
```

---

### **2. Setting Pixels**
Use `set_pixel()` or `set_pixelv()` to set the color of a specific pixel.

- **`set_pixel(x, y, color)`:** Directly set the color at coordinates `(x, y)`.
- **`set_pixelv(point, color)`:** Use a `Vector2i` for the point.

**GDScript Example:**
```gdscript
img.set_pixel(1, 2, Color.RED)
img.set_pixelv(Vector2i(1, 2), Color.RED)
```

**C# Example:**
```csharp
img.SetPixel(1, 2, Colors.Red);
img.SetPixelv(new Vector2I(1, 2), Colors.Red);
```

**Note:** Ensure coordinates are within bounds (`0 ≤ x < width`, `0 ≤ y < height`).

---

### **3. Saving Images**
Use the `save_` methods to export the image in various formats. For example:

- **PNG:**
  ```gdscript
  var png_data = img.save_png_to_buffer()
  ```

- **JPEG (no alpha):**
  ```gdscript
  var jpg_data = img.save_jpg_to_buffer(quality=0.8)
  ```

- **WebP (lossy):**
  ```gdscript
  var webp_data = img.save_webp_to_buffer(lossy=true, quality=0.9)
  ```

**Important Notes:**
- **Alpha Channels:** JPEG and PNG formats support alpha, but JPEG is lossy. WebP (lossy) and PNG (lossless) are better for preserving alpha.
- **Resolution Limits:** WebP is limited to 16383×16383 pixels.

---

### **4. Modifying Image Data**
Use `set_data()` to overwrite existing image data. This is useful for creating images from raw pixel data.

**Parameters:**
- `width`: New width.
- `height`: New height.
- `use_mipmaps`: Whether to use mipmaps.
- `format`: Format of the new data.
- `data`: Raw pixel data as a `PackedByteArray`.

**GDScript Example:**
```gdscript
var new_data = PackedByteArray([0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0x00])  # Example RGBA data
img.set_data(10, 5, false, Image.FORMAT_RGBA8, new_data)
```

---

### **5. Shrinking the Image**
Use `shrink_x2()` to reduce the image size by a factor of 2 in both dimensions. This is useful for optimizing memory or preparing for texture atlases.

**GDScript Example:**
```gdscript
img.shrink_x2()
```

---

### **6. Color Space Conversion**
Use `srgb_to_linear()` to convert the image from sRGB to linear color space, which is important for accurate lighting calculations.

**GDScript Example:**
```gdscript
img.srgb_to_linear()
```

**Note:** This works only on `Image.FORMAT_RGBA8` or `Image.FORMAT_RGB8` images.

---

### **Key Considerations**
- **Alpha Channel Handling:** When saving to formats that do not support alpha (like JPEG), the alpha channel is ignored.
- **Format Compatibility:** Ensure the image format matches the output format when saving.
- **Performance:** `shrink_x2()` is fast but may lose detail in complex images.

---

### **Summary of Methods**
| Method                  | Purpose                              |
|-------------------------|--------------------------------------|
| `set_pixel()`           | Set a single pixel color              |
| `set_pixelv()`          | Set a pixel using a Vector2i          |
| `save_png_to_buffer()` | Save as PNG in a byte array           |
| `save_jpg_to_buffer()` | Save as JPEG (no alpha)               |
| `save_webp_to_buffer()`| Save as WebP (supports alpha)         |
| `set_data()`            | Replace image data with raw pixels    |
| `shrink_x2()`           | Reduce image size by half             |
| `srgb_to_linear()`      | Convert color space to linear         |

This guide covers the essentials for working with the `Image` class, ensuring you can create, modify, and save images effectively.