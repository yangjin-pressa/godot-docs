# TileSetSource

**Inherits:** Resource < RefCounted < Object  
**Inherited By:** TileSetAtlasSource, TileSetScenesCollectionSource  

**Description**  
Exposes a set of tiles for a TileSet resource.  
Tiles are indexed with coordinates ID (Vector2i) and alternative ID (int).  
This class provides methods to access tile data, but does not implement specific logic for tile storage.  

**Warning**  
TileSetSource can only be added to one TileSet at a time. Calling `TileSet.add_source()` on a second TileSet will remove the source from the first.  

**Methods**  
- **get_alternative_tile_id(atlas_coords: Vector2i, index: int)** → int  
  Returns the alternative ID for the tile at specified coordinates and index.  

- **get_alternative_tiles_count(atlas_coords: Vector2i)** → int  
  Returns the number of alternative tiles for a given coordinates ID. Returns -1 if no tile exists at the coordinates.  

- **get_tile_id(index: int)** → Vector2i  
  Returns the coordinates ID of the tile at the specified index.  

- **get_tiles_count()** → int  
  Returns the total number of tiles (excluding alternative tiles).  

- **has_alternative_tile(atlas_coords: Vector2i, alternative_tile: int)** → bool  
  Checks if a specific alternative tile exists for the given coordinates.  

- **has_tile(atlas_coords: Vector2i)** → bool  
  Verifies if a tile exists at the specified coordinates.  

**Key Notes**  
- Methods retrieve tile data via coordinates and indices but do not manage tile storage.  
- Use `TileSetAtlasSource` for disk-based tile storage, `TileSetScenesCollectionSource` for scene-based tile management.