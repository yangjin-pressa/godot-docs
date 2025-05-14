**Class Name:** AnimationNodeStateMachineTransition

**Description:**  
This class is used to define transitions between states in an animation state machine. It manages properties such as the type of transition, cross-fade timing, priority, and conditions for automatic traversal.

---

**Tutorials:**  
- **Using AnimationTree**: A guide to integrating this class into an animation state machine for advanced transition control.

---

**Properties:**  
- **advance_condition** (StringName, default: "")  
  - Used as a condition for automatic transitions. Example: `node.set("advance_condition", "some_condition")`.

- **advance_mode** (AdvanceMode, default: 0)  
  - Determines when transitions are enabled or auto-traversed. Value 0 is normal, 1 is reset, 2 is loop.

- **break_loop_at_end** (bool, default: false)  
  - If true, the state machine will break the loop at the end of the transition.

- **priority** (int, default: 1)  
  - Defines the priority of the transition within the state machine. Higher values take precedence.

- **reset** (bool, default: true)  
  - If true, the state machine resets to the initial state after the transition.

- **switch_mode** (SwitchMode, default: 0)  
  - The type of transition. Value 0 is normal, 1 is reset, 2 is loop.

- **xfade_curve** (Curve, default: "")  
  - Defines the curve used for cross-fading transitions. Example: `node.set("xfade_curve", "linear")`.

- **xfade_time** (float, default: 0.0)  
  - The duration of the cross-fade transition. Note: This behavior may vary based on other state machine settings.

---

**Signals:**  
- **advance_condition_changed**  
  - Emitted when the `advance_condition` property changes.

---

**Enumerations:**  
- **SwitchMode**  
  - 0: Normal transition  
  - 1: Reset  
  - 2: Loop  

- **AdvanceMode**  
  - 0: Normal  
  - 1: Auto-traverse  
  - 2: Loop  

---

**Additional Notes:**  
- The `xfade_time` property's behavior may depend on other state machine configurations, such as the use of `break_loop_at_end`.  
- For advanced transitions, the `advance_condition` and `switch_mode` properties work together to control how states are handled.  
- Use the `AnimationTree` tutorial to learn how these properties integrate with state machine logic.