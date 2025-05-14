# NavigationMeshGenerator

**Deprecated**: This class may be changed or removed in future versions.  
**Inherits**: [Object](class_Object)  

## Description  
Helper class for creating and clearing 3D navigation meshes used as [NavigationMesh](class_NavigationMesh) resources inside [NavigationRegion3D](class_NavigationRegion3D).  
- **Key Functionality**:  
  - Collects 3D source geometry from the SceneTree  
  - Creates navigation meshes for [NavigationMesh](class_NavigationMesh) resources  
  - Requires 3D geometry for baking; not suitable for 2D  
  - Baking is performance-intensive and best done in a separate thread  

## Tutorials  
- [Using NavigationMeshes](../tutorials/navigation/navigation_using_navigationmeshes)  

## Methods  

### bake() (deprecated)  
- **Parameters**:  
  - navigation_mesh: [NavigationMesh](class_NavigationMesh)  
  - root_node: Node to start geometry collection  
- **Replacement**: Use [parse_source_geometry_data](#parse_source_geometry_data) with explicit geometry data  

### bake_from_source_geometry_data()  
- **Parameters**:  
  - source_geometry_data: Geometry data (e.g., collision shapes)  
  - callback: Function to process geometry data  
- **Purpose**: Creates navigation meshes from custom geometry data  

### clear()  
- **Parameters**:  
  - navigation_mesh: [NavigationMesh](class_NavigationMesh)  

### parse_source_geometry_data()  
- **Parameters**:  
  - source_geometry_data: Geometry data (e.g., collision shapes)  
  - root_node: Node to start geometry collection  
  - callback: Function to process geometry data  
- **Important Notes**:  
  - Must be called on the main thread  
  - Avoid using GPU data for performance; prefer collision shapes  

## Key Notes  
1. **Deprecation**: `bake()` is obsolete; use `bake_from_source_geometry_data()` instead.  
2. **Threading**: Parse operations must run on the main thread.  
3. **Performance**: Using GPU data (e.g., Mesh) is discouraged; use collision shapes for faster processing.  
4. **Geometry Considerations**: The algorithm does not distinguish between "inside" and "outside" of geometry.  

## References  
- [NavigationMesh](class_NavigationMesh)  
- [NavigationRegion3D](class_NavigationRegion3D)  
- [Object](class_Object)