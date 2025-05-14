**EditorFeatureProfile**  
**Inherits from:** RefCounted  

---

### **Description**  
The `EditorFeatureProfile` class allows you to control which features are visible in the Godot editor. It supports disabling classes, properties, and entire editor features. This is useful for customizing the editor interface based on project needs.  

**Use Cases:**  
- Hide specific classes from the "Create New Node" dialog.  
- Disable property editing for certain classes.  
- Remove entire editor features (e.g., the scene tree editor).  

---

### **Methods**  
- **`get_feature_name()`**  
  Returns the name of a feature.  

- **`is_class_disabled(class_name)`**  
  Checks if a class is disabled.  
  **Returns:** `true` if the class is disabled (not visible in the "Create New Node" dialog).  

- **`is_class_editor_disabled(class_name)`**  
  Checks if editing for a class is disabled.  
  **Returns:** `true` if the class appears in the "Create New Node" dialog but the Inspector is read-only.  

- **`is_class_property_disabled(class_name, property)`**  
  Checks if a property is disabled for a class.  
  **Returns:** `true` if the property does not appear in the Inspector for nodes of the specified class.  

- **`is_feature_disabled(feature)`**  
  Checks if a feature is disabled.  
  **Returns:** `true` if the feature is completely removed from the editor.  

- **`load_from_file(path)`**  
  Loads a feature profile from a JSON file.  
  **Note:** Files are typically saved with `.profile` extension in the `feature_profiles` directory.  

- **`save_to_file(path)`**  
  Saves the current feature profile in JSON format.  
  **Note:** Files are saved with `.profile` extension in the `feature_profiles` directory.  

- **`set_disable_class(class_name, disable)`**  
  Disables or enables a class.  
  **If `disable` is true:** The class is not visible in the "Create New Node" dialog.  

- **`set_disable_class_editor(class_name, disable)`**  
  Disables or enables editing for a class.  
  **If `disable` is true:** The class appears in the "Create New Node" dialog, but the Inspector is read-only.  

- **`set_disable_class_property(class_name, property, disable)`**  
  Disables or enables a property for a class.  
  **If `disable` is true:** The property is not visible in the Inspector for nodes of the specified class.  

- **`set_disable_feature(feature, disable)`**  
  Disables or enables an editor feature.  
  **If `disable` is true:** The feature is removed from the editor entirely.  

---

### **Enumerations**  
**`Feature`**  
- **`FEATURE_1`**  
  Represents a specific editor feature (e.g., scene tree, resource editor).  
- **`FEATURE_2`**  
  Another editor feature.  
- ...  
- **`FEATURE_N`**  
  Additional features.  

**Note:** Each feature is uniquely identified by an integer value.  

---

### **Notes**  
- Feature profiles are typically saved in the `feature_profiles` directory.  
- Use `EditorPaths.get_config_dir()` to locate the editor configuration folder.  
- Profiles can be imported/exported via the feature profile manager.