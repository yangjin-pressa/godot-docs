# PackedScene

**Inherits:** Resource < RefCounted < Object

An abstraction of a serialized scene.

## Description
A simplified interface to a scene file. Provides access to operations and checks that can be performed on the scene resource itself.

Can be used to save a node to a file. When saving, the node as well as all the nodes it owns get saved (see Node.owner property).

**Note:** The node doesn't need to own itself.

**Example:** Load a saved scene:
```gdscript
var scene = preload("res://scene.tscn").instantiate()
add_child(scene)
```

```csharp
var scene = ResourceLoader.Load<PackedScene>("res://scene.tscn").Instantiate();
AddChild(scene);
```

**Example:** Save a node with different owners:
```gdscript
var node = Node2D.new()
var body = RigidBody2D.new()
var collision = CollisionShape2D.new()

body.add_child(collision)
node.add_child(body)

body.owner = node
var scene = PackedScene.new()

var result = scene.pack(node)
if result == OK:
    var error = ResourceSaver.save(scene, "res://path/name.tscn")
    if error != OK:
        push_error("An error occurred while saving the scene to disk.")
```

```csharp
var node = new Node2D();
var body = new RigidBody2D();
var collision = new CollisionShape2D();

body.AddChild(collision);
node.AddChild(body);

body.Owner = node;
var scene = new PackedScene();

Error result = scene.Pack(node);
if (result == Error.Ok)
{
    Error error = ResourceSaver.Save(scene, "res://path/name.tscn");
    if (error != Error.Ok)
    {
        GD.PushError("An error occurred while saving the scene to disk.");
    }
}
```

## Tutorials
- [2D Role Playing Game (RPG) Demo](https://godotengine.org/asset-library/asset/2729)

## Methods
- `can_instantiate()`: Returns true if the scene file has nodes.
- `get_state()`: Returns the SceneState representing the scene file contents.
- `instantiate(edit_state=0)`: Instantiates the scene's node hierarchy. Triggers child scene instantiation(s). Triggers a Node.NOTIFICATION_SCENE_INSTANTIATED notification on the root node.
- `pack(path)`: Packs the path node, and all owned sub-nodes, into this PackedScene. Any existing data will be cleared. See Node.owner.

## Enumerations
**GenEditState**
- `GEN_EDIT_STATE_DISABLED`: Blocks edits to the scene state.
- `GEN_EDIT_STATE_INSTANCE`: Provides local scene resources to the local scene. Only available in editor builds.
- `GEN_EDIT_STATE_MAIN`: Provides local scene resources to the local scene. Only the main scene should receive the main edit state.
- `GEN_EDIT_STATE_MAIN_INHERITED`: Similar to GEN_EDIT_STATE_MAIN, but for the case where the scene is being instantiated to be the base of another one.

## Method Descriptions
- `can_instantiate()`: Returns true if the scene file has nodes.
- `get_state()`: Returns the SceneState representing the scene file contents.
- `instantiate(edit_state=0)`: Instantiates the scene's node hierarchy. Triggers child scene instantiation(s). Triggers a Node.NOTIFICATION_SCENE_INSTANTIATED notification on the root node.
- `pack(path)`: Packs the path node, and all owned sub-nodes, into this PackedScene. Any existing data will be cleared. See Node.owner.