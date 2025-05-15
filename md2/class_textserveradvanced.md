# TextServerAdvanced

**Inherits:** TextServerExtension < TextServer < RefCounted < Object

An advanced text server with support for BiDi, complex text layout, and contextual OpenType features. Used by Godot as the default primary TextServer interface.

## Description
A TextServer implementation using HarfBuzz, ICU, and SIL Graphite to support:
- BiDi (bidirectional text)
- Complex text layout
- Contextual OpenType features

This is Godot's default TextServer implementation.

## Key Features
- **Virtual methods**: Methods that should typically be overridden by the user
- **Const methods**: Methods with no side effects
- **Vararg methods**: Methods accepting variable arguments
- **Static methods**: Methods callable directly via class name
- **Bitfield**: Integer values as bitmask flags

## Technical Dependencies
- HarfBuzz (for text shaping)
- ICU (International Components for Unicode)
- SIL Graphite (for complex text layout)

## Usage
- Default text server in Godot
- Provides advanced text rendering capabilities
- Supports complex text formatting features

## Related Classes
- TextServerExtension
- TextServer
- RefCounted
- Object