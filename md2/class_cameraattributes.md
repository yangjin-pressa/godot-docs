**Class Name:** [Insert Class Name Here]  
**Inherits from:** WorldEnvironment, Camera3D  

**Description:**  
This class is designed to handle [specific functionality related to the class]. It provides methods for [list key features]. See also [Environment](class_Environment) for general 3D environment settings.  

**Properties:**  
- **auto_exposure_enabled** (bool): Determines whether auto-exposure is enabled.  
- **exposure_sensitivity** (float): Controls the sensitivity of exposure adjustments.  

**Property Descriptions:**  
- **auto_exposure_enabled**:  
  - **set_auto_exposure_enabled(value: bool):** Sets the auto-exposure enabled state.  
  - **is_auto_exposure_enabled():** Returns whether auto-exposure is enabled.  

- **exposure_sensitivity**:  
  - **set_exposure_sensitivity(value: float):** Sets the sensitivity of exposure adjustments.  
  - **get_exposure_sensitivity():** Returns the current sensitivity value.  

**Note:** The `exposure_sensitivity` property is dependent on the `ProjectSettings` class, which defines global parameters affecting exposure behavior. Adjustments here may require corresponding changes in the project configuration.  

**Related Classes:**  
- WorldEnvironment  
- Camera3D  
- Environment