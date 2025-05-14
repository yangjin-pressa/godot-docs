# Engine Class Documentation

The `Engine` class provides a set of methods for interacting with the Godot engine, including checking the editor context, managing singletons, and retrieving version information. Below is a detailed breakdown of each method:

---

## `get_write_movie_path()`

**Description**:  
Returns the path to the `MovieWriter`'s output file, or an empty string if the engine wasn't started in Movie Maker mode. The default path can be changed in `ProjectSettings`.

**Return Value**:  
A `String` representing the path. Use `ProjectSettings.editor/movie_writer/movie_file` to change the default path.

**Example**:
```gdscript
# GDScript
print(Engine.get_write_movie_path())

# C#
print(Engine.GetWriteMoviePath());
```

---

## `is_editor_hint()`

**Description**:  
Returns `true` if the script is currently running inside the editor, otherwise returns `false`. Useful for `@tool` scripts to conditionally draw editor helpers.

**Return Value**:  
A `bool` indicating whether the script is in the editor.

**Example**:
```gdscript
# GDScript
if Engine.is_editor_hint():
    draw_gizmos()
else:
    simulate_physics()

# C#
if (Engine.IsEditorHint())
    DrawGizmos();
else
    SimulatePhysics();
```

**Note**:  
Use `OS.has_feature("editor")` to detect if the script is running in an editor build (e.g., when pressing `F5`).

---

## `is_embedded_in_editor()`

**Description**:  
Returns `true` if the engine is running embedded in the editor. Useful to prevent modifying window flags that are not supported in embedded mode.

**Return Value**:  
A `bool` indicating whether the engine is embedded in the editor.

---

## `is_in_physics_frame()`

**Description**:  
Returns `true` if the engine is inside the fixed physics process step of the main loop. This is useful for physics-related logic.

**Return Value**:  
A `bool` indicating whether the engine is in the physics step.

**Example**:
```gdscript
# GDScript
func _enter_tree():
    print(Engine.is_in_physics_frame())

func _process(delta):
    print(Engine.is_in_physics_frame()) # Prints false

func _physics_process(delta):
    print(Engine.is_in_physics_frame()) # Prints true

# C#
public void _EnterTree()
{
    Console.WriteLine(Engine.IsInPhysicsFrame());
}

public void _Process(float delta)
{
    Console.WriteLine(Engine.IsInPhysicsFrame()); // Prints false
}

public void _PhysicsProcess(float delta)
{
    Console.WriteLine(Engine.IsInPhysicsFrame()); // Prints true
}
```

---

## `register_script_language(language: ScriptLanguage)`

**Description**:  
Registers a `ScriptLanguage` instance to be available with `ScriptServer`. This allows custom scripting languages to be used in the engine.

**Return Value**:  
- `@GlobalScope.OK` on success  
- `@GlobalScope.ERR_UNAVAILABLE` if `ScriptServer` is full  
- `@GlobalScope.ERR_ALREADY_EXISTS` if the language already exists

**Example**:
```gdscript
# GDScript
var lang = ScriptLanguage.new("mylang", "My Language")
var result = Engine.register_script_language(lang)
if result == @GlobalScope.OK:
    print("Language registered successfully.")
else:
    print("Failed to register language.")

# C#
ScriptLanguage lang = new ScriptLanguage("mylang", "My Language");
Engine.RegisterScriptLanguage(lang);
```

---

## `register_singleton(name: StringName, instance: Object)`

**Description**:  
Registers the given `Object` as a singleton, available globally under `name`. Useful for plugins.

**Example**:
```gdscript
# GDScript
Engine.register_singleton("MySingleton", MySingletonInstance)

# C#
Engine.RegisterSingleton("MySingleton", MySingletonInstance);
```

**Note**: The singleton object is not freed. Only user-defined singletons can be removed.

---

## `unregister_script_language(language: ScriptLanguage)`

**Description**:  
Unregisters a `ScriptLanguage` instance from `ScriptServer`.

**Return Value**:  
- `@GlobalScope.OK` on success  
- `@GlobalScope.ERR_DOES_NOT_EXIST` if the language is not registered

**Example**:
```gdscript
# GDScript
var lang = ScriptLanguage.get_by_name("mylang")
var result = Engine.unregister_script_language(lang)
if result == @GlobalScope.OK:
    print("Language unregistered successfully.")
else:
    print("Failed to unregister language.")

# C#
ScriptLanguage lang = ScriptLanguage.GetByName("mylang");
Engine.UnregisterScriptLanguage(lang);
```

---

## `unregister_singleton(name: StringName)`

**Description**:  
Removes the singleton registered under `name`. The singleton object is not freed.

**Example**:
```gdscript
# GDScript
Engine.unregister_singleton("MySingleton")

# C#
Engine.UnregisterSingleton("MySingleton");
```

---

## `get_version_info()`

**Description**:  
Retrieves version information for the engine, including the Git commit hash, build name, and version string.

**Return Value**:  
A `Dictionary` containing version details, including:
- `version`: The version string (e.g., "4.3.1").
- `commit_hash`: The Git commit hash.
- `build`: The build number.
- `date`: The date the version was built.

**Example**:
```gdscript
# GDScript
var version_info = Engine.get_version_info()
print("Version:", version_info["version"])
print("Commit Hash:", version_info["commit_hash"])

# C#
var version_info = Engine.GetVersionInfo();
Console.WriteLine("Version: " + version_info["version"]);
Console.WriteLine("Commit Hash: " + version_info["commit_hash"]);
```

**Note**: The `hex` value in the version dictionary is an `int`, and hexadecimal literals are preferred for comparisons (e.g., `0x123456`).