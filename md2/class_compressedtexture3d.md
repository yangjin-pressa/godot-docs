# CompressedTexture3D

## Class Hierarchy
- Inherits from: Texture3D < Texture < Resource < RefCounted < Object

## Description
A 3D texture format using VRAM compression. Files have extension `.ctex3d`. This format is internal to Godot and is created via the import system. VRAM compression reduces GPU memory usage and improves loading times but may cause visible artifacts, ideal for 3D rendering.

See Texture3D for general 3D texture descriptions.

## Properties
- **load_path**: String = ""  
  The file path to a `.ctex3d` file.

## Methods
- **load(path: String)** → Error  
  Loads the texture from the specified `path`.

## Property Descriptions
**load_path**:  
The file path to a `.ctex3d` file used by the texture.

## Method Descriptions
**load**:  
Loads the texture from the specified `path`. Returns an Error value.