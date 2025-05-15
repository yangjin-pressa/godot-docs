# SphereMesh

**Inherits:** PrimitiveMesh < Mesh < Resource < RefCounted < Object

Class representing a spherical PrimitiveMesh.

## Description
Class representing a spherical PrimitiveMesh.

## Properties
- **height**: float = 1.0
- **is_hemisphere**: bool = false
- **radial_segments**: int = 64
- **radius**: float = 0.5
- **rings**: int = 32

## Property Descriptions

### height
**Type:** float  
**Default:** 1.0  
**Description:** Full height of the sphere.

**Methods:**
- set_height(value: float)
- get_height()

### is_hemisphere
**Type:** bool  
**Default:** false  
**Description:** If true, a hemisphere is created rather than a full sphere.

**Note:** To get a regular hemisphere, the height and radius of the sphere must be equal.

**Methods:**
- set_is_hemisphere(value: bool)
- get_is_hemisphere()

### radial_segments
**Type:** int  
**Default:** 64  
**Description:** Number of radial segments on the sphere.

**Methods:**
- set_radial_segments(value: int)
- get_radial_segments()

### radius
**Type:** float  
**Default:** 0.5  
**Description:** Radius of sphere.

**Methods:**
- set_radius(value: float)
- get_radius()

### rings
**Type:** int  
**Default:** 32  
**Description:** Number of segments along the height of the sphere.

**Methods:**
- set_rings(value: int)
- get_rings()