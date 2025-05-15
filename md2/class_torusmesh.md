# TorusMesh

**Inherits:** `PrimitiveMesh` → `Mesh` → `Resource` → `RefCounted` → `Object`

## Description
Class representing a torus primitive mesh.

## Properties

- **inner_radius** (float) = 0.5  
  The inner radius of the torus.  
  Set/Get methods: `set_inner_radius(float)`, `get_inner_radius()`

- **outer_radius** (float) = 1.0  
  The outer radius of the torus.  
  Set/Get methods: `set_outer_radius(float)`, `get_outer_radius()`

- **ring_segments** (int) = 32  
  The number of edges each ring of the torus is constructed of.  
  Set/Get methods: `set_ring_segments(int)`, `get_ring_segments()`

- **rings** (int) = 64  
  The number of slices the torus is constructed of.  
  Set/Get methods: `set_rings(int)`, `get_rings()`

## Notes
- These properties define the geometry of a torus mesh.  
- Values can be modified via the provided set/get methods.