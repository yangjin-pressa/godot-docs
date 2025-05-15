# TileMapPattern

**Inherits:** Resource → RefCounted → Object

## Description

A resource that holds a pattern for bulk manipulation of TileMap objects. Patterns always start at (0,0) and cannot have negative coordinates.

## Methods

- **get_cell_alternative_tile(coords: Vector2i) → int**  
  Returns the tile alternative ID at specified coordinates.

- **get_cell_atlas_coords(coords: Vector2i) → Vector2i**  
  Returns the tile atlas coordinates for the cell at specified coordinates.

- **get_cell_source_id(coords: Vector2i) → int**  
  Returns the tile source ID at specified coordinates.

- **get_size() → Vector2i**  
  Returns the pattern size in cells.

- **get_used_cells() → Array<Vector2i>**  
  Returns list of used cell coordinates in the pattern.

- **has_cell(coords: Vector2i) → bool**  
  Checks if the pattern has a tile at specified coordinates.

- **is_empty() → bool**  
  Returns whether the pattern is empty.

- **remove_cell(coords: Vector2i, update_size: bool)**  
  Removes the cell at specified coordinates. Updates pattern size if requested.

- **set_cell(coords: Vector2i, source_id: int = -1, atlas_coords: Vector2i = Vector2i(-1, -1), alternative_tile: int = -1)**  
  Sets tile identifiers for the cell at coordinates. See TileMap.set_cell() for details.

- **set_size(size: Vector2i)**  
  Sets the pattern size.