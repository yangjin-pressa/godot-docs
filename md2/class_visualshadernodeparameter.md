# VisualShaderNodeParameter

## Description
A base type for parameters within the visual shader graph. Parameters represent variables set externally from the ShaderMaterial. Exposed as properties in ShaderMaterial and can be assigned via the Inspector or script.

## Properties
- **parameter_name**: String (default: "")
  - Name of the parameter used in ShaderMaterial properties.
- **qualifier**: Qualifier (default: 0)
  - Defines the scope of the parameter.

## Enumerations
### Qualifier
- **QUAL_NONE** = 0
  - Parameter tied to ShaderMaterial.
- **QUAL_GLOBAL** = 1
  - Uses a global value from Project Settings.
- **QUAL_INSTANCE** = 2
  - Tied to the node's ShaderMaterial.
- **QUAL_MAX** = 3
  - Enum size.

## Property Descriptions
### parameter_name
- **set_parameter_name**(value: String): void
- **get_parameter_name**(): String
  - Name used to access the parameter in ShaderMaterial.

### qualifier
- **set_qualifier**(value: Qualifier): void
- **get_qualifier**(): Qualifier
  - Scope definition for the parameter.

## Method Notes
- **virtual**: Override for custom behavior.
- **const**: No side effects; does not modify instance variables.
- **vararg**: Accepts variable arguments.
- **static**: Called directly via class name.
- **operator**: Valid operator for this type.
- **bitfield**: Integer bitmask of flags.