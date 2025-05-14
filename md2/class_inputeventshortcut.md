# InputEventShortcut

**Inherits:** [InputEvent](class_InputEvent) < [Resource](class_Resource) < [RefCounted](class_RefCounted) < [Object](class_Object)

## Description
- Represents a triggered keyboard [Shortcut](class_Shortcut)
- Received in: `Node._input()`, `Node._shortcut_input()`, `Node._unhandled_input()`
- Typically sent by the editor's Command Palette
- Can be manually sent using `Viewport.push_input()`

## Properties
- Property: `shortcut` (Shortcut)

## Method Descriptions
- **set_shortcut**(value: Shortcut): void
- **get_shortcut**(): Shortcut

The `Shortcut` represented by this event. Its `Shortcut.matches_event()` method always returns `true` for this event.

## Notes
- **virtual** (This method should typically be overridden by the user to have any effect.)
- **const** (This method has no side effects. It doesn't modify any of the instance's member variables.)
- **vararg** (This method accepts any number of arguments after the ones described here.)
- **constructor** (This method is used to construct a type.)
- **static** (This method doesn't need an instance to be called, so it can be called directly using the class name.)
- **operator** (This method describes a valid operator to use with this type as left-hand operand.)
- **bitfield** (This value is an integer composed as a bitmask of the following flags.)
- **void** (No return value.)