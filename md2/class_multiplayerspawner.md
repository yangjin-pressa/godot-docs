# MultiplayerSpawner

**Inherits:** Node → Object

## Description
- Spawns and replicates nodes across multiplayer peers.
- Supports:
  - Editor-defined spawnable scenes via `add_spawnable_scene()`
  - Custom spawns via `spawn()` using `spawn_function`
- Uses `MultiplayerAPI` to notify spawn/despawn events

## Properties
- **spawn_function** (Callable): Called on all peers when a custom spawn is requested. Receives `data` and returns a Node not in the scene tree.
- **spawn_limit** (int): Maximum number of nodes to spawn. Default: 0.
- **spawn_path** (NodePath): Path to the spawn root. Spawnable scenes added as children are replicated.

## Methods
- **add_spawnable_scene(path)**: Adds a scene path to be replicated.
- **clear_spawnable_scenes()**: Removes all registered spawnable scenes.
- **get_spawnable_scene(index)**: Returns a spawnable scene by index.
- **get_spawnable_scene_count()**: Returns the number of registered spawnable scenes.
- **spawn(data)**: Requests a custom spawn using `spawn_function`. Returns the locally spawned node added to the scene tree.

## Signals
- **despawned(node)**: Emitted when a node is despawned. Only called on remote peers.
- **spawned(node)**: Emitted when a node is spawned. Only called on remote peers.

## Property Details
- **spawn_function**: 
  - Called on all peers when a custom spawn is requested.
  - Receives `data` and returns a Node not in the scene tree.
- **spawn_limit**: 
  - Maximum number of nodes to spawn. Default: 0.
- **spawn_path**: 
  - Path to the spawn root. Spawnable scenes added as children are replicated.

## Method Details
- **add_spawnable_scene(path)**: 
  - Adds a scene path to be replicated. 
  - Spawnable scenes are automatically spawned.
- **clear_spawnable_scenes()**: 
  - Removes all registered spawnable scenes.
- **get_spawnable_scene(index)**: 
  - Returns a spawnable scene by index.
- **get_spawnable_scene_count()**: 
  - Returns the number of registered spawnable scenes.
- **spawn(data)**: 
  - Requests a custom spawn using `spawn_function`. 
  - Returns the locally spawned node added to the scene tree. 
  - Spawnable scenes are spawned automatically.