# FastNoiseLite Documentation

A class for generating noise in 3D environments, supporting various noise algorithms, fractal effects, and domain warping.

---

## Enums

### NoiseType
Specifies the noise algorithm used.

```cpp
enum class NoiseType {
    Perlin = 0,
    Simplex = 1,
    Voronoi = 2,
    Cellular = 3,
    Hash = 4
};
```

### FractalType
Specifies the method for combining octaves into a fractal.

```cpp
enum class FractalType {
    Fractal = 0,
    PingPong = 1,
    Weighted = 2
};
```

### DomainWarpType
Specifies the algorithm for domain warping.

```cpp
enum class DomainWarpType {
    None = 0,
    Simplex = 1,
    Perlin = 2
};
```

---

## Properties

### seed
**Type:** `int`  
**Default:** `0`  
**Description:** The random number seed for all noise types. A higher seed value results in different noise patterns.

### frequency
**Type:** `float`  
**Default:** `0.01`  
**Description:** The frequency for all noise types. Lower values produce smoother noise, higher values produce rougher, more granular noise.

### noise_type
**Type:** `NoiseType`  
**Default:** `Simplex`  
**Description:** The noise algorithm to use. Options include Perlin, Simplex, Voronoi, Cellular, and Hash.

### offset
**Type:** `Vector3`  
**Default:** `(0, 0, 0)`  
**Description:** Translates the noise input coordinates by the given `Vector3`. Useful for offsetting noise patterns.

### fractal_type
**Type:** `FractalType`  
**Default:** `Fractal`  
**Description:** The method for combining octaves into a fractal. Options include Fractal, PingPong, and Weighted.

### fractal_octaves
**Type:** `int`  
**Default:** `5`  
**Description:** The number of noise layers to sample for fractal noise. More octaves create more complex patterns.

### fractal_lacunarity
**Type:** `float`  
**Default:** `2.0`  
**Description:** Frequency multiplier between subsequent octaves. Higher values create rougher noise.

### fractal_gain
**Type:** `float`  
**Default:** `0.5`  
**Description:** Strength of each subsequent octave in fractal noise. Lower values emphasize lower frequency layers.

### fractal_ping_pong_strength
**Type:** `float`  
**Default:** `2.0`  
**Description:** Strength of the fractal ping pong type. Controls how the noise is reflected between octaves.

### fractal_weighted_strength
**Type:** `float`  
**Default:** `0.0`  
**Description:** Weighting for higher octaves in weighted fractal type. Higher values reduce the impact of higher octaves.

### domain_warp_type
**Type:** `DomainWarpType`  
**Default:** `None`  
**Description:** The algorithm for domain warping. Options include Simplex and Perlin.

### domain_warp_frequency
**Type:** `float`  
**Default:** `0.05`  
**Description:** Frequency of the noise used for domain warping. Controls the scale of the warp effect.

### domain_warp_type
**Type:** `DomainWarpType`  
**Default:** `None`  
**Description:** The algorithm for domain warping. Options include Simplex and Perlin.

---

## Methods

### getNoise(x, y, z)
**Returns:** `float`  
**Description:** Generates a noise value at the specified 3D coordinates. The coordinates are transformed using the offset and domain warp parameters before being passed to the noise algorithm.

### getNoise2D(x, y)
**Returns:** `float`  
**Description:** Generates a 2D noise value. Equivalent to calling `getNoise(x, y, 0)`.

### getNoise1D(x)
**Returns:** `float`  
**Description:** Generates a 1D noise value. Equivalent to calling `getNoise(x, 0, 0)`.

---

## Usage Notes

- **Seed:** Change the seed value to generate different noise patterns.
- **Frequency:** Adjust frequency to control the smoothness of the noise.
- **Domain Warping:** Use domain warp to create more complex, natural-looking patterns.
- **Fractal Types:** Use fractal settings to create layered noise effects with multiple octaves.

This class provides a flexible way to generate procedural noise for simulations, terrain generation, and other applications requiring random but structured patterns.