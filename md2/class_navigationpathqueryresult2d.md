# NavigationPathQueryResult2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** RefCounted < Object

Represents the result of a 2D pathfinding query.

## Description
Stores the result of a 2D navigation path query from NavigationServer2D.

## Tutorials
- [Using NavigationPathQueryObjects](../tutorials/navigation/navigation_using_navigationpathqueryobjects)

## Properties
- **path**: PackedVector2Array (default: PackedVector2Array())
- **path_owner_ids**: PackedInt64Array (default: PackedInt64Array())
- **path_rids**: Array<RID> (default: [])
- **path_types**: PackedInt32Array (default: PackedInt32Array())

## Enumerations
**PathSegmentType**
- PATH_SEGMENT_TYPE_REGION = 0
- PATH_SEGMENT_TYPE_LINK = 1

## Method
- **reset()**: Reset the result object to its initial state.

## Property Descriptions
- **path**: The resulting path array from the navigation query. All positions are in global coordinates. Changes to the array do not affect the original property value.
- **path_owner_ids**: ObjectID of the objects managing regions and links in the path.
- **path_rids**: RIDs of regions and links in the path.
- **path_types**: Type of navigation primitive (region or link) for each path point.

## Method Descriptions
- **reset()**: Reset the result object to its initial state. Use this to reuse the object across multiple queries.