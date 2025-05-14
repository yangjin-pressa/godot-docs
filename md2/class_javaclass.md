# JavaClass

**Inherits**: RefCounted < Object  

Represents a class from the Java Native Interface.  

## Description  
- This class only works on Android. On any other platform, it does nothing.  
- Not to be confused with JavaScriptObject.  

## Methods  
- **get_java_class_name**  
  Returns the Java class name.  

- **get_java_method_list**  
  Returns the object's Java methods and their signatures as an Array of dictionaries.  

- **get_java_parent_class**  
  Returns a JavaClass representing the Java parent class of this class.  

## Method Descriptions  
- **get_java_class_name**  
  Retrieves the name of the Java class associated with this object.  

- **get_java_method_list**  
  Provides a list of Java methods in the same format as Object.get_method_list().  

- **get_java_parent_class**  
  Identifies the parent Java class of the current class.  

## Notes  
- This class is designed for Android platforms only.  
- Distinguishes from JavaScriptObject, which is a different type.