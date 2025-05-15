# PlaceholderMesh

**Inherits:** Mesh < Resource < RefCounted < Object

Placeholder class for a mesh.

## Description

Used when loading a project that uses a Mesh subclass in:
- Dedicated server mode: only texture dimensions are kept.
- When the subclass is missing due to engine version differences.

## Properties

- **aabb**: AABB(0, 0, 0, 0, 0, 0)

## Property Descriptions

**aabb**: Smallest AABB enclosing this mesh in local space.

## Method Definitions

- void set_aabb(value: AABB)
- AABB get_aabb()