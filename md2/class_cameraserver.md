# CameraServer

**Inherits:** Object

## Description
Tracks external cameras (webcams, phone cameras) for use in AR modules. 
- Available on Linux, macOS, iOS
- Requires godot-ios-plugins for iOS camera support

## Properties
- **monitoring_feeds**: false (bool)  
  Whether the server is actively monitoring camera feeds

## Methods
- **add_feed(feed: CameraFeed)**: void  
  Adds a camera feed to the server
- **feeds()**: Array[CameraFeed]  
  Returns all registered camera feeds
- **get_feed(index: int)**: CameraFeed  
  Returns a feed by index
- **get_feed_count()**: int  
  Returns number of registered feeds
- **remove_feed(feed: CameraFeed)**: void  
  Removes a specified camera feed

## Signals
- **camera_feed_added(id: int)**  
  Emitted when a feed is added
- **camera_feed_removed(id: int)**  
  Emitted when a feed is removed

## Enumerations
### FeedImage
- **FEED_RGBA_IMAGE**: 0  
  RGBA camera image
- **FEED_YCBCR_IMAGE**: 0  
  YCbCr camera image
- **FEED_Y_IMAGE**: 0  
  Y component camera image
- **FEED_CBCR_IMAGE**: 1  
  CbCr component camera image

## Property Descriptions
**monitoring_feeds**: bool  
- Set/get whether the server is monitoring feeds
- Enable when actively accessing camera data

## Method Descriptions
- **add_feed()**: Adds a feed
- **feeds()**: Returns feed list
- **get_feed()**: Access by index
- **get_feed_count()**: Get total feeds
- **remove_feed()**: Remove specific feed

**Note:** iOS camera support requires godot-ios-plugins plugin.  
[Godot iOS Plugins](https://github.com/godotengine/godot-ios-plugins)