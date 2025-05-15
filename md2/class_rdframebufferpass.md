# RDFramebufferPass

**Inherits:** RefCounted < Object

## Description
Contains attachment descriptions for a framebuffer pass. Used by RenderingDevice.

## Properties
- **color_attachments**: PackedInt32Array() - Color attachments in order. Use ATTACHMENT_UNUSED to skip unused attachments.
- **depth_attachment**: -1 - Depth attachment. Use ATTACHMENT_UNUSED for no depth buffer.
- **input_attachments**: PackedInt32Array() - For multipass framebuffers. Must be provided in RDUniform for uniform set.
- **preserve_attachments**: PackedInt32Array() - Attachments to preserve in this pass.
- **resolve_attachments**: PackedInt32Array() - Resolve attachments for multisampled color attachments.

## Constants
- **ATTACHMENT_UNUSED** = -1 - Attachment is unused.

## Property Details
### color_attachments
- **set**: set_color_attachments(value: PackedInt32Array)
- **get**: get_color_attachments()

### depth_attachment
- **set**: set_depth_attachment(value: int)
- **get**: get_depth_attachment()

### input_attachments
- **set**: set_input_attachments(value: PackedInt32Array)
- **get**: get_input_attachments()

### preserve_attachments
- **set**: set_preserve_attachments(value: PackedInt32Array)
- **get**: get_preserve_attachments()

### resolve_attachments
- **set**: set_resolve_attachments(value: PackedInt32Array)
- **get**: get_resolve_attachments()

**Note**: All array properties return copies. Changes to the returned arrays do not update the original property values. See PackedInt32Array for details.