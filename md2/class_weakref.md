# WeakRef

**Inherits:** RefCounted < Object

## Description
A weakref can hold an Object without contributing to the reference counter. Created via @GlobalScope.weakref(). Useful for preventing memory leaks in cyclic dependencies between classes.

## Methods
- **get_ref** (const): Returns the Object this weakref is referring to. Returns null if the object no longer exists.

## Notes
- This method is const (no side effects).
- Works with RefCounted objects, but does not affect their reference count.
- Prevents cyclic reference issues in class relationships.