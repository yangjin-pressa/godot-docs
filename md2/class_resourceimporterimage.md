# ResourceImporterImage

## Inheritance
- Inherits from: ResourceImporter
  - Inherits from: RefCounted
    - Inherits from: Object

## Description
- Imports `Image` resources, not `CompressedTexture2D`.
- For rendering in 2D/3D, use `ResourceImporterTexture`.

## Tutorials
- Importing images

## Method Definitions
- virtual void set_extension(const StringView &p_extension)
- const StringView get_extension() const
- virtual bool has_extension(const StringView &p_extension) const
- virtual bool supports_extension(const StringView &p_extension) const
- virtual bool supports_format(const StringView &p_extension) const
- virtual bool is_format_supported(const StringView &p_extension) const
- virtual bool is_format_supported(const StringView &p_extension) const
- virtual void set_format(const StringView &p_format)
- const StringView get_format() const
- virtual bool has_format(const StringView &p_format) const
- virtual bool supports_format(const StringView &p_format) const
- virtual bool is_format_supported(const StringView &p_format) const
- virtual bool is_format_supported(const StringView &p_format) const
- virtual void set_metadata(const StringView &p_key, const Variant &p_value)
- const Map<StringName, Variant> get_metadata() const
- virtual void set_metadata(Map<StringName, Variant> p_metadata)
- virtual Map<StringName, Variant> get_metadata() const
- virtual void set_metadata(const StringName &p_key, const Variant &p_value)
- virtual void set_metadata(const Map<StringName, Variant> &p_metadata)
- virtual void set_metadata(const StringName &p_key, const Variant &p_value)
- virtual void set_metadata(const Map<StringName, Variant> &p_metadata)