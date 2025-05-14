**Class: OpenXRActionSet**  
- **Inherits**: Resource < RefCounted < Object  

**Description**  
- Action sets define collections of actions for different game states.  
- Actions can be reinterpreted based on priority.  
- Example: menu, walking, vehicle control.  

**Properties**  
- **actions**: Array (default: [])  
- **localized_name**: String (default: "")  
- **priority**: int (default: 0)  

**Methods**  
- **add_action(action: OpenXRAction)**: Add an action to this action set.  
- **get_action_count()**: Retrieve the number of actions in the action set.  
- **remove_action(action: OpenXRAction)**: Remove an action from this action set.  

**Property Descriptions**  
- **actions**:  
  - Set: Set actions for the action set.  
  - Get: Get actions for the action set.  
- **localized_name**:  
  - Set: Set the localized name of the action set.  
  - Get: Get the localized name of the action set.  
- **priority**:  
  - Set: Set the priority for the action set.  
  - Get: Get the priority for the action set.  

**Method Descriptions**  
- **add_action**: Adds an action to the action set.  
- **get_action_count**: Returns the count of actions in the action set.  
- **remove_action**: Removes an action from the action set.