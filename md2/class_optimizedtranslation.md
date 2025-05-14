**Class Name**: OptimizedTranslation  
**Inherits**: Translation < Resource < RefCounted < Object  

---

### **Description**  
An optimized translation used by default for CSV Translations. Utilizes real-time compressed translations, resulting in very small dictionaries.  

---

### **Methods**  
- **generate**  
  - **Parameters**: `from: Translation`  
  - **Returns**: `void`  
  - **Purpose**: Generates and sets an optimized translation from the given Translation resource.  
  - **Note**: This method is intended for use in the editor. It does nothing when called from an exported project.  

---

### **Key Attributes**  
- **Optimized**: Compressed data for efficient memory usage.  
- **Default**: Used as the default translation format for CSV.  
- **Editor-Only**: Functionality restricted to the editor environment.