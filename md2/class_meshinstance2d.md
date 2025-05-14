**Class: MeshInstance2D**  
**Inherits:** Node2D → CanvasItem → Node → Object  

---

### Description  
A node for displaying a Mesh in 2D. Can be created from a Sprite2D via the editor: select the Sprite2D node and choose **Sprite2D > Convert to MeshInstance2D** in the 2D editor.  

---

### Tutorials  
- [2D meshes](../tutorials/2d/2d_meshes)  

---

### Properties  
- **mesh**: A Mesh object used for rendering.  
- **texture**: A Texture2D object for default materials. Accessible as `TEXTURE` in shaders.  

---

### Signals  
- **texture_changed()**: Emits when the `texture` property is modified.  

---

### Property Descriptions  
**mesh**  
- **set_mesh(value: Mesh)**: Sets the Mesh to use.  
- **get_mesh()**: Returns the current Mesh.  

**texture**  
- **set_texture(value: Texture2D)**: Sets the Texture2D for default materials.  
- **get_texture()**: Returns the current Texture2D.  

--- 

**Notes:**  
- The `texture` property can be referenced in shaders as `TEXTURE`.  
- The `mesh` property defines the geometry for rendering.