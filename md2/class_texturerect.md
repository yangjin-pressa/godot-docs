# TextureRect

**Inherits**: Control < CanvasItem < Node < Object

A control that displays a texture. The texture's placement can be controlled with the `stretch_mode` property. It can scale, tile, or stay centered inside its bounding rectangle.

## Tutorials
- 3D Voxel Demo [here](https://godotengine.org/asset-library/asset/2755)

## Properties
- **expand_mode**: ExpandMode (0)  
  Defines how minimum size is determined based on the texture's size. See ExpandMode for options.  
  **Experimental**: Certain modes may cause unstable behavior in containers.

- **flip_h**: bool (false)  
  If true, texture is flipped horizontally.

- **flip_v**: bool (false)  
  If true, texture is flipped vertically.

- **stretch_mode**: StretchMode (0)  
  Controls texture behavior when resizing the node's bounding rectangle. See StretchMode for options.

- **texture**: Texture2D  
  The node's Texture2D resource.

## Enumerations

### ExpandMode
- **EXPAND_KEEP_SIZE** (0): Minimum size equals texture size.
- **EXPAND_IGNORE_SIZE** (1): Size can be shrunk below texture size.
- **EXPAND_FIT_WIDTH** (2): Height ignored. Minimum width equals current height.
- **EXPAND_FIT_WIDTH_PROPORTIONAL** (3): Same as FIT_WIDTH but preserves aspect ratio.
- **EXPAND_FIT_HEIGHT** (4): Width ignored. Minimum height equals current width.
- **EXPAND_FIT_HEIGHT_PROPORTIONAL** (5): Same as FIT_HEIGHT but preserves aspect ratio.

### StretchMode
- **STRETCH_SCALE** (0): Scale to fit bounding rectangle.
- **STRETCH_TILE** (1): Tile inside bounding rectangle.
- **STRETCH_KEEP** (2): Texture stays in top-left corner.
- **STRETCH_KEEP_CENTERED** (3): Texture centered in bounding rectangle.
- **STRETCH_KEEP_ASPECT** (4): Scale to fit while preserving aspect ratio.
- **STRETCH_KEEP_ASPECT_CENTERED** (5): Scale to fit, center, and preserve aspect ratio.
- **STRETCH_KEEP_ASPECT_COVERED** (6): Scale to fit, clip excess.