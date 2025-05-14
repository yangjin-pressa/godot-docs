# CameraTexture

**Inherits:** Texture2D < Texture < Resource < RefCounted < Object

Texture provided by a CameraFeed.

## Description
This texture gives access to the camera texture provided by a CameraFeed.

**Note:** Many cameras supply YCbCr images which need to be converted in a shader.

## Properties
- **camera_feed_id**: int = 0  
  The ID of the CameraFeed for which we want to display the image.

- **camera_is_active**: bool = false  
  Convenience property that gives access to the active property of the CameraFeed.

- **which_feed**: FeedImage = 0  
  Which image within the CameraFeed we want access to, important if the camera image is split in a Y and CbCr component.

## Property Descriptions
### camera_feed_id
- set_camera_feed_id(value: int)
- get_camera_feed_id()

### camera_is_active
- set_camera_active(value: bool)
- get_camera_active()

### which_feed
- set_which_feed(value: FeedImage)
- get_which_feed()