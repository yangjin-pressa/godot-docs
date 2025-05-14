# GLTFTexture

**Inherits:** Resource → RefCounted → Object

## Tutorials
- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving)

## Properties
- **sampler**: int = -1  
  ID of the texture sampler. Default uses linear filtering and repeat wrapping.
- **src_image**: int = -1  
  Index of associated image. -1 means no image is assigned.

## Property Descriptions
### sampler
- **set_sampler(value: int)**: Assigns sampler ID.
- **get_sampler()**: Retrieves current sampler ID.

### src_image
- **set_src_image(value: int)**: Assigns image index.
- **get_src_image()**: Retrieves current image index.