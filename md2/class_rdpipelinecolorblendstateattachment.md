**Class Name:** RDPipelineColorBlendStateAttachment  
**Description:** A class for setting blend parameters for a pipeline. It allows configuring blending behavior between source and destination fragments, including factors, modes, and color channel write controls.

---

### **Key Examples**  
```cpp
// Example: Setting up a "mix" blending mode with straight alpha
blendState.setAsMix();
```

---

### **Properties**  
1. **enable_blend**  
   - **Type:** bool  
   - **Default:** false  
   - **Description:** If `true`, performs blending between source and destination fragments using defined factors and modes.  

2. **src_color_blend_factor**  
   - **Type:** BlendFactor  
   - **Default:** 0  
   - **Description:** Determines how the source's color fragment is used in blending.  

3. **dst_color_blend_factor**  
   - **Type:** BlendFactor  
   - **Default:** 0  
   - **Description:** Determines how the destination's color fragment is used in blending.  

4. **src_alpha_blend_factor**  
   - **Type:** BlendFactor  
   - **Default:** 0  
   - **Description:** Determines how the source's alpha fragment is used in blending.  

5. **dst_alpha_blend_factor**  
   - **Type:** BlendFactor  
   - **Default:** 0  
   - **Description:** Determines how the destination's alpha fragment is used in blending.  

6. **write_r**  
   - **Type:** bool  
   - **Default:** true  
   - **Description:** If `true`, writes the new red channel to the final result.  

7. **write_g**  
   - **Type:** bool  
   - **Default:** true  
   - **Description:** If `true`, writes the new green channel to the final result.  

8. **write_b**  
   - **Type:** bool  
   - **Default:** true  
   - **Description:** If `true`, writes the new blue channel to the final result.  

9. **write_a**  
   - **Type:** bool  
   - **Default:** true  
   - **Description:** If `true`, writes the new alpha channel to the final result.  

---

### **Methods**  
1. **setAsMix()**  
   - **Return Type:** void  
   - **Description:** Sets properties to enable standard "mix" blending (e.g., for alpha blending).  
   - **Note:** This method is **virtual** and should typically be overridden by the user to customize behavior.  

---

### **Notes**  
- Properties like `src_color_blend_factor` and `dst_color_blend_factor` can be set to values like `BlendFactor::SRC_COLOR` or `BlendFactor::ONE_MINUS_SRC_ALPHA` for specific blending behavior.  
- The `setAsMix()` method simplifies configuring blending for scenarios where source and destination colors are combined linearly.