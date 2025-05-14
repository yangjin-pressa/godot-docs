# EditorResourcePreview

**Inherits:** Node < Object

## Description
A node used to generate previews for resources or files.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using `EditorInterface.get_resource_previewer()`.

---

## Methods

- **add_preview_generator** (generator: EditorResourcePreviewGenerator)
  - Create an own, custom preview generator.

- **check_for_invalidation** (path: String)
  - Check if the resource changed, if so, it will be invalidated and the corresponding signal emitted.

- **queue_edited_resource_preview** (resource: Resource, receiver: Object, receiver_func: StringName, userdata: Variant)
  - Queue the `resource` being edited for preview. Once ready, the `receiver`'s `receiver_func` is called with: path, preview, thumbnail_preview, userdata.

- **queue_resource_preview** (path: String, receiver: Object, receiver_func: StringName, userdata: Variant)
  - Queue a resource file at `path` for preview. Once ready, the `receiver`'s `receiver_func` is called with: path, preview, thumbnail_preview, userdata.

- **remove_preview_generator** (generator: EditorResourcePreviewGenerator)
  - Removes a custom preview generator.

---

## Signals

- **preview_invalidated** (path: String)
  - Emitted if a preview was invalidated (changed). `path` corresponds to the preview path.

---

## Key Notes

1. Methods require explicit parameters:
   - `receiver_func` must accept: String, Texture2D, Texture2D, Variant
   - If preview creation fails, `receiver_func` is still called but preview is `null`.

2. The class is a singleton; direct instantiation is not allowed.