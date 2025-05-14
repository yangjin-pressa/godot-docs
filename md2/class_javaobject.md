# JavaObject

**Inherits:** RefCounted < Object

Represents an object from the Java Native Interface.

## Description
Represents an object from the Java Native Interface. It can be returned from Java methods called on JavaClass or other JavaObject's. See JavaClassWrapper for an example.

**Note:** This class only works on Android. On any other platform, this class does nothing.

**Note:** This class is not to be confused with JavaScriptObject.

## Methods
- **get_java_class** (const): Returns the JavaClass that this object is an instance of.

## Key Information
- **Platform Compatibility:** Android only
- **Inheritance Chain:** RefCounted → Object
- **Key Method:** get_java_class (returns JavaClass, const)
- **Related Classes:** JavaClass, JavaClassWrapper, JavaScriptObject

## Reference Links
- JavaClass: https://godotengine.org/documentation/classes/class_javaclas.html
- JavaClassWrapper: https://godotengine.org/documentation/classes/class_javaclasswrapper.html