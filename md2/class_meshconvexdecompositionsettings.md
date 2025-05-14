### MeshConvexDecompositionSettings

**Inherits from**: `RefCounted`  

**Description**  
Parameters for approximate convex decomposition of a `Mesh`. This class provides control over various aspects of the decomposition process, including normalization of the mesh, projection of vertices, and bias for clipping plane searches.

---

### Properties

| Type         | Name                              | Default Value       | Description |
|--------------|-----------------------------------|---------------------|-------------|
| `bool`       | `normalize_mesh`                   | `false`             | Whether the mesh is normalized before decomposition. |
| `bool`       | `project_hull_vertices`            | `true`              | Whether vertices are projected onto the original mesh. |
| `int`        | `resolution`                       | `10000`             | Maximum number of voxels (resolution) for the decomposition. |
| `int`        | `plane_downsampling`               | `4`                 | Granularity of clipping plane search during decomposition. |
| `float`      | `revolution_axes_clipping_bias`    | `0.05`              | Bias for revolution axes during clipping plane computation. |
| `float`      | `symmetry_planes_clipping_bias`    | `0.05`              | Bias for symmetry planes during clipping plane computation. |
| `float`      | `min_volume_per_convex_hull`       | `0.0001`            | Minimum volume per convex hull to ensure valid decomposition. |
| `int`        | `max_triangles_per_convex_hull`    | **4–1024**         | Maximum number of triangles per convex hull during decomposition. |

---

### Enumerations

**Mode**: `Mode`  
This enumeration defines the behavior of the decomposition process, including options for handling different types of geometries or constraints.  

- **`Mode::DECOMPOSE`**: Default mode for standard convex decomposition.  
- **`Mode::PRUNE`**: Prune unnecessary geometry during decomposition.  
- **`Mode::SKELETON`**: Decompose into skeletal structures for performance.  

---

### Notes

- This class is designed for fine-grained control over the decomposition algorithm, allowing users to tailor the process to specific geometric constraints or performance requirements.  
- The `Mode` enum allows users to override the default decomposition strategy for advanced use cases.