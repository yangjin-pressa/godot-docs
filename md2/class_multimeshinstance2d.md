**Class Name**: MultiMeshInstance2D  
**Inherits**: Node2D → CanvasItem → Node → Object  

---

### Description  
A node to instance a MultiMesh resource in 2D. Usage mirrors MultiMeshInstance3D.  

---

### Properties  
- **multimesh**: Reference to a MultiMesh resource.  
  - Set: `set_multimesh(value: MultiMesh)`  
  - Get: `get_multimesh()`  
- **texture**: Reference to a Texture2D for default CanvasItemMaterial.  
  - Set: `set_texture(value: Texture2D)`  
  - Get: `get_texture()`  

---

### Signals  
- **texture_changed()**: Emitted when the texture property is modified.  

---

### Property Details  
- **multimesh**:  
  - The MultiMesh resource to be rendered by the node.  
- **texture**:  
  - Texture used if the default CanvasItemMaterial is applied. Accessible as `TEXTURE` in shaders.  

---

### Key Methods  
- `set_multimesh(value: MultiMesh)`: Updates the MultiMesh resource.  
- `get_multimesh()`: Retrieves the current MultiMesh.  
- `set_texture(value: Texture2D)`: Updates the texture.  
- `get_texture()`: Retrieves the current texture.  

---

### Notes  
- The class is designed for 2D rendering, similar to its 3D counterpart.  
- Texture and MultiMesh properties are essential for defining the visual output.