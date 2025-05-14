# NavigationPathQueryResult3D

**Experimental:** This class may be changed or removed in future versions.  
**Inherits:** RefCounted < Object  

Represents the result of a 3D pathfinding query from NavigationServer3D.

## Description
Stores the result of a 3D navigation path query.

## Tutorials
- [Using NavigationPathQueryObjects](../tutorials/navigation/navigation_using_navigationpathqueryobjects)

## Properties
- **path**: PackedVector3Array()  
  The resulting path array from the navigation query. All positions are in global coordinates.  

- **path_owner_ids**: PackedInt64Array()  
  ObjectID's of the Object instances managing regions/links in the path.  

- **path_rids**: []  
  RIDs of regions and links each path point goes through.  

- **path_types**: PackedInt32Array()  
  Type of navigation primitive (region or link) for each path point.  

## Methods
- **reset()**:  
  Resets the result object to its initial state for reuse across queries.

## Enumerations
### PathSegmentType
- **PATH_SEGMENT_TYPE_REGION** = 0  
  Path goes through a region.  

- **PATH_SEGMENT_TYPE_LINK** = 1  
  Path goes through a link.  

## Notes
- All property arrays are copied; modifications do not affect the original data.  
- Path array positions are in global coordinates unless customized query parameters are used.