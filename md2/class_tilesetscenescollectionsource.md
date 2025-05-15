# TileSetScenesCollectionSource

**Inherits:** TileSetSource ← Resource ← RefCounted ← Object

Exposes a set of scenes as tiles for a TileSet resource.

## Description
When placed on a TileMapLayer, tiles from TileSetScenesCollectionSource will automatically instantiate an associated scene at the cell's position in the TileMapLayer.

Scenes are instantiated as children of the TileMapLayer when it enters the tree. If you add/remove a scene tile in the TileMapLayer that is already inside the tree, the TileMapLayer will automatically instantiate/free the scene accordingly.

**Note:** Scene tiles all occupy one tile slot and instead use alternate tile ID to identify scene index. TileSetSource.get_tiles_count() will always return 1. Use get_scene_tiles_count() to get a number of scenes in a TileSetScenesCollectionSource.

Example code to find the scene path at a given tile in TileMapLayer:

```gdscript
var source_id = tile_map_layer.get_cell_source_id(Vector2i(x, y))
if source_id > -1:
    var scene_source = tile_map_layer.tile_set.get_source(source_id)
    if scene_source is TileSetScenesCollectionSource:
        var alt_id = tile_map_layer.get_cell_alternative_tile(Vector2i(x, y))
        # The assigned PackedScene.
        var scene = scene_source.get_scene_tile_scene(alt_id)
```

```csharp
int sourceId = tileMapLayer.GetCellSourceId(new Vector2I(x, y));
if (sourceId > -1)
{
    TileSetSource source = tileMapLayer.TileSet.GetSource(sourceId);
    if (source is TileSetScenesCollectionSource sceneSource)
    {
        int altId = tileMapLayer.GetCellAlternativeTile(new Vector2I(x, y));
        // The assigned PackedScene.
        PackedScene scene = sceneSource.GetSceneTileScene(altId);
    }
}
```

## Methods

- **create_scene_tile**: Creates a new scene tile with the specified scene and optional ID.
- **get_next_scene_tile_id**: Returns the next available ID for a new scene tile.
- **get_scene_tiles_count**: Returns the number of scene tiles this TileSet source has.
- **has_scene_tile_id**: Returns whether this TileSet source has a scene tile with the specified ID.
- **remove_scene_tile**: Removes the scene tile with the specified ID.
- **set_scene_tile_display_placeholder**: Sets whether the scene tile should display a placeholder in the editor.
- **set_scene_tile_id**: Changes a scene tile's ID from the old value to the new value.
- **set_scene_tile_scene**: Assigns a PackedScene resource to the scene tile. The scene must extend CanvasItem for positioning.

Each method has specific parameters and functionality as described in their individual explanations.