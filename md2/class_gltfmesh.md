# GLTFMesh

**Inherits:** Resource < RefCounted < Object

A class representing a glTF mesh.

## Description
Handles 3D mesh data imported from glTF files. Includes properties for blend channels, blend weights, instance materials, and the mesh itself.

## Tutorials
- Runtime file loading and saving

## Properties
- **blend_weights**: PackedFloat32Array (default: PackedFloat32Array()) - Array of floats representing blend weights of the mesh.
- **instance_materials**: Array[Material] (default: []) - Array of Material objects for the mesh.
- **mesh**: ImporterMesh - Mesh representation.
- **original_name**: String (default: "") - Original name of the mesh.

## Methods
- **get_additional_data(extension_name: StringName)** → Variant - Retrieves arbitrary data for the mesh.
- **set_additional_data(extension_name: StringName, additional_data: Variant)** → void - Sets arbitrary data for the mesh.

## Property Descriptions
- **blend_weights**: Set and get methods for blend weights array.
- **instance_materials**: Set and get methods for material array.
- **mesh**: Set and get methods for the mesh object.
- **original_name**: Set and get methods for the original name.

## Method Descriptions
- **get_additional_data**: Used to retrieve custom data stored in the mesh.
- **set_additional_data**: Used to store custom data in the mesh.