# ResourceImporterBitMap

**Inherits:** ResourceImporter < RefCounted < Object

Imports a BitMap resource (2D array of boolean values).

## Description
BitMap resources are typically used as click masks in TextureButton and TouchScreenButton.

## Tutorials
- Importing images: ../tutorials/assets_pipeline/importing_images

## Properties
- create_from (int): 0  
  The data source to use for generating the bitmap.  
  - Black & White: Pixels whose HSV value is greater than the threshold will be considered "enabled" (bit is true). If the pixel is lower than or equal to the threshold, it will be "disabled" (bit is false).  
  - Alpha: Pixels whose alpha value is greater than the threshold will be considered "enabled" (bit is true). If the pixel is lower than or equal to the threshold, it will be "disabled" (bit is false).  

- threshold (float): 0.5  
  The threshold to use for determining enabled/disabled bits. See also create_from.

## References
- [Importing images](../tutorials/assets_pipeline/importing_images)