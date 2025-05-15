# VisualShaderNodeColorFunc

## Inheritance
- `VisualShaderNode`
- `Resource`
- `RefCounted`
- `Object`

## Description
Accepts a `Color` to the input port and applies a color function based on the `function` property.

## Properties
- `function`: `Function` = `0` (see enum for options)

## Enumerations
### Function
- **FUNC_GRAYSCALE** = `0`
  - Converts to grayscale using:
    ```glsl
    vec3 c = input;
    float max1 = max(c.r, c.g);
    float max2 = max(max1, c.b);
    float max3 = max(max1, max2);
    return vec3(max3, max3, max3);
    ```

- **FUNC_HSV2RGB** = `1`
  - Converts HSV to RGB.

- **FUNC_RGB2HSV** = `2`
  - Converts RGB to HSV.

- **FUNC_SEPIA** = `3`
  - Applies sepia tone:
    ```glsl
    vec3 c = input;
    float r = (c.r * 0.393) + (c.g * 0.769) + (c.b * 0.189);
    float g = (c.r * 0.349) + (c.g * 0.686) + (c.b * 0.168);
    float b = (c.r * 0.272) + (c.g * 0.534) + (c.b * 0.131);
    return vec3(r, g, b);
    ```

- **FUNC_LINEAR_TO_SRGB** = `4`
  - Converts linear to sRGB:
    ```glsl
    vec3 c = clamp(c, vec3(0.0), vec3(1.0));
    const vec3 a = vec3(0.055f);
    return mix((vec3(1.0f) + a) * pow(c.rgb, vec3(1.0f / 2.4f)) - a, 12.92f * c.rgb, lessThan(c.rgb, vec3(0.0031308f)));
    ```
  - Compatibility renderer uses:
    ```glsl
    vec3 c = input;
    return max(vec3(1.055) * pow(c, vec3(0.416666667)) - vec3(0.055), vec3(0.0));
    ```

- **FUNC_SRGB_TO_LINEAR** = `5`
  - Converts sRGB to linear:
    ```glsl
    vec3 c = input;
    return mix(pow((c.rgb + vec3(0.055)) * (1.0 / (1.0 + 0.055)), vec3(2.4)), c.rgb * (1.0 / 12.92), lessThan(c.rgb, vec3(0.04045)));
    ```
  - Compatibility renderer uses:
    ```glsl
    vec3 c = input;
    return c * (c * (c * 0.305306011 + 0.682171111) + 0.012522878);
    ```

- **FUNC_MAX** = `6`
  - Represents enum size.

## Property Descriptions
- **function**: Sets/gets the color function to apply. Options are defined in the `Function` enum.