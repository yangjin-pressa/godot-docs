# XRTracker

**Inherits:** RefCounted < Object  
**Inherited By:** XRFaceTracker, XRPositionalTracker  

## Description  
This object serves as the base class for all XR trackers.  

## Tutorials  
- [XR documentation index](../tutorials/xr/index)  

## Properties  
- **description**: String (default: "")  
- **name**: StringName (default: "&Unknown")  
- **type**: TrackerType (default: 128)  

## Property Descriptions  

### description  
- **set_tracker_desc**(value: String): void  
- **get_tracker_desc**(): String  
  - The description of this tracker.  

### name  
- **set_tracker_name**(value: StringName): void  
- **get_tracker_name**(): StringName  
  - Unique identifier for the tracker. Reserved names:  
    - `head`: XRPositionalTracker for player's head  
    - `left_hand`: XRControllerTracker for left hand  
    - `right_hand`: XRControllerTracker for right hand  
    - `/user/hand_tracker/left`: XRHandTracker for left hand  
    - `/user/hand_tracker/right`: XRHandTracker for right hand  
    - `/user/body_tracker`: XRBodyTracker for player's body  
    - `/user/face_tracker`: XRFaceTracker for player's face  

### type  
- **set_tracker_type**(value: TrackerType): void  
- **get_tracker_type**(): TrackerType  
  - The type of tracker (e.g., positional, face, etc.).