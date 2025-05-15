# RDPipelineColorBlendState

## Inheritance
- RefCounted < Object

## Description
Used by RenderingDevice for pipeline color blending.

## Properties
- **attachments**: Array of RDPipelineColorBlendStateAttachment. Default: []
- **blend_constant**: Color. Default: Color(0, 0, 0, 1)
- **enable_logic_op**: bool. Default: false
- **logic_op**: LogicOperation. Default: 0

## Property Details

### attachments
- **set_attachments**(value: Array of RDPipelineColorBlendStateAttachment)
- **get_attachments**()

**Description**: Attachments blended together.

### blend_constant
- **set_blend_constant**(value: Color)
- **get_blend_constant**()

**Description**: Constant color for blending. See also RenderingDevice.draw_list_set_blend_constants().

### enable_logic_op
- **set_enable_logic_op**(value: bool)
- **get_enable_logic_op**()

**Description**: If true, applies logic operation from logic_op.

### logic_op
- **set_logic_op**(value: LogicOperation)
- **get_logic_op**()

**Description**: Logic operation to apply if enable_logic_op is true.