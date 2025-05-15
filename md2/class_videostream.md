# VideoStream

## Inheritance
- **VideoStream** inherits from:  
  `Resource` → `RefCounted` → `Object`

## Inherited By
- `VideoStreamTheora`

---

## Description
Base resource type for all video streams. Classes that derive from **VideoStream** can be used as resource types to play back videos in `VideoStreamPlayer`.

---

## Tutorials
- Playing videos  
- Runtime file loading and saving

---

## Properties
- **file**: `String` = `""`  
  The video file path or URI that this **VideoStream** resource handles.  
  For `VideoStreamTheora`, this filename should be an Ogg Theora video file with the `.ogv` extension.

---

## Methods
- **_instantiate_playback**(): `VideoStreamPlayback` (virtual)  
  Called when the video starts playing, to initialize and return a subclass of `VideoStreamPlayback`.

---

## Notes
- **Tutorials**: Reference documentation pages for video playback and file handling.  
- **Properties**: The `file` property defines the video source path.  
- **Methods**: The virtual method `_instantiate_playback` is used to create playback functionality.