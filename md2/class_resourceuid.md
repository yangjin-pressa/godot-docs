**ResourceUID Class**  
- **Inherits from**: Object  
- **Purpose**: Manages unique identifiers for resources. Allows references to persist even if files are renamed. UIDs can be accessed via `uid://`.  

---

### **Constants**  
- **INVALID_ID**  
  - **Value**: -1  
  - **Text representation**: `uid://<invalid>`  

---

### **Methods**  
1. **add_id(int, String)**  
   - **Description**: Adds a new UID mapped to a path. Fails if the UID already exists.  

2. **create_id()**  
   - **Description**: Generates a random UID. Must be registered (e.g., via `add_id`) to be valid.  

3. **create_id_for_path(String)**  
   - **Description**: Seeds the UID with the given path. Same UID is generated for the same path.  

4. **get_id_path(int)**  
   - **Description**: Returns the path associated with the given UID.  

5. **has_id(int)**  
   - **Description**: Checks if a UID exists.  

6. **id_to_text(int)**  
   - **Description**: Converts a UID to its string representation (`uid://<value>`).  

7. **remove_id(int)**  
   - **Description**: Removes a UID. Checks if it exists before removal.  

8. **set_id(int, String)**  
   - **Description**: Updates the path for an existing UID.  

9. **text_to_id(String)**  
   - **Description**: Extracts a UID from a `uid://` string (e.g., `uid://123`).  

---

### **Key Notes**  
- **Citations**:  
  - **INVALID_ID**: `class_ResourceUID_constant_INVALID_ID`  
  - **Method references**: See `has_id()`, `add_id()`, etc., for detailed behavior.  

- **Usage**: Ensure UIDs are registered (e.g., via `add_id`) before relying on them.