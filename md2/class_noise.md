**Class: Noise**  
Inherits from: `Resource`  
Inherited By: `Noise` (no subclasses listed)  

---

**Description**  
The `Noise` class provides methods for generating 2D and 3D noise data. It includes a default `get_seamless_image` method to create seamless noise patterns.  

---

**Methods**  
- **`get_image(width: int, height: int, invert: bool = false, in_3d_space: bool = false, skirt: float = 0.1, normalize: bool = true) -> Image`**  
  Returns a 2D image of noise. Notes: The `normalize` parameter affects the output range if set to `false`.  

- **`get_seamless_image(width: int, height: int, invert: bool = false, in_3d_space: bool = false, skirt: float = 0.1, normalize: bool = true) -> Image`**  
  Returns a seamless 2D noise image. Notes: The `normalize` parameter affects the output range if set to `false`.  

- **`get_image_3d(width: int, height: int, depth: int, invert: bool = false, skirt: float = 0.1, normalize: bool = true) -> Array[Image]`**  
  Returns a 3D noise array for use with `ImageTexture3D`. Notes: The `normalize` parameter affects the output range if set to `false`.  

- **`get_seamless_image_3d(width: int, height: int, depth: int, invert: bool = false, skirt: float = 0.1, normalize: bool = true) -> Array[Image]`**  
  Returns seamless 3D noise for use with `ImageTexture3D`. Notes: The `normalize` parameter affects the output range if set to `false`.  

- **`get_noise_value(x: float, y: float, z: float = 0.0) -> float`**  
  Returns a single noise value at coordinates (x, y, z).  

- **`get_noise_value_2d(x: float, y: float) -> float`**  
  Returns a 2D noise value at (x, y).  

- **`get_noise_value_3d(x: float, y: float, z: float) -> float`**  
  Returns a 3D noise value at (x, y, z).  

- **`get_noise_value_3d_vararg(*args: float) -> float`**  
  Accepts variable arguments for 3D noise values.  

--- 

**Notes**  
- The `normalize` parameter in methods like `get_image` and `get_seamless_image` determines whether the output values are clamped to the range [-1.0, 1.0] or scaled to [0.0, 1.0].  
- The `skirt` parameter in seamless methods controls the blending area between noise tiles.  
- The `invert` parameter flips the noise values.  
- The `in_3d_space` flag is used in 2D methods to generate 3D noise patterns.