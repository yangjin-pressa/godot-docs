# RDAttachmentFormat

**Inherits:** RefCounted < Object

## Description
This object is used by RenderingDevice.

## Properties

- **format**: DataFormat = 36
- **samples**: TextureSamples = 0
- **usage_flags**: int = 0

## Property Descriptions

### format
The attachment's data format.

**Methods:**
- set_format(value: DataFormat)
- get_format()

### samples
The number of samples used when sampling the attachment.

**Methods:**
- set_samples(value: TextureSamples)
- get_samples()

### usage_flags
The attachment's usage flags, which determine what can be done with it.

**Methods:**
- set_usage_flags(value: int)
- get_usage_flags()