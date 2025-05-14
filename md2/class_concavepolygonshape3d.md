**Class:** ConcavePolygonShape3D  
**Inherits:** Shape3D → Resource → RefCounted → Object  

---

### **Description**  
A 3D trimesh shape for physics collision. Used to define complex geometry for CollisionShape3D.  
- **Key Characteristics:**  
  - Made of interconnected triangles.  
  - Hollow by design, unsuitable for physics detection.  
  - Slow for collision checks; reserved for level geometry.  

**Notes:**  
- Best for static bodies (e.g., StaticBody3D).  
- Not recommended for dynamic bodies (e.g., CharacterBody3D).  
- Risk of clipping for fast-moving objects.  

**Performance Warning:**  
- Avoid for dynamic physics. Use convex decomposition for concave shapes.  

---

### **Tutorials**  
- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)  

---

### **Properties**  
- **backface_collision**: `bool` (default: `false`)  
  - If `true`, collisions occur on both sides of faces.  

---

### **Methods**  
- **get_faces()** → `PackedVector3Array` (const)  
  - Returns triangle vertices as an array (triples per triangle).  

- **set_faces(faces: `PackedVector3Array`)**  
  - Sets triangle vertices. Input must be triples defining triangles.  

---

### **Key Usage Notes**  
- **Hollow Shape:** Collisions are detected on the outside of faces.  
- **Convex Alternative:** Use ConvexPolygonShape3D for performance.  
- **Static Use Cases:** Ideal for static environments, not dynamic physics.  

--- 

**Citations**  
- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)