**AudioEffectReverb**  
**Description**  
Simulates acoustic environments, such as rooms or spaces, by adjusting parameters like reverb and echo.  

**Tutorials**  
- [Tutorial Link](https://godotengine.org/tutorials/): Learn how to use this effect.  
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710): Example project showcasing its application.  

**Properties**  
1. **damping**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Controls how quickly sound decays in the environment. Range: 0.0–1.0.  
   - **Methods**: `set_damping(float value)`, `get_damping()`.  

2. **dry**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Determines the balance between dry (unprocessed) and wet (processed) audio. Range: 0.0–1.0.  
   - **Methods**: `set_dry(float value)`, `get_dry()`.  

3. **room**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Adjusts the size of the virtual room. Range: 0.0–1.0.  
   - **Methods**: `set_room(float value)`, `get_room()`.  

4. **room_low**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Controls low-frequency room reflections. Range: 0.0–1.0.  
   - **Methods**: `set_room_low(float value)`, `get_room_low()`.  

5. **room_high**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Adjusts high-frequency room reflections. Range: 0.0–1.0.  
   - **Methods**: `set_room_high(float value)`, `get_room_high()`.  

6. **early_reflections**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Modulates the strength of early reflections (direct echoes). Range: 0.0–1.0.  
   - **Methods**: `set_early_reflections(float value)`, `get_early_reflections()`.  

7. **reverse**  
   - **Type**: bool  
   - **Default**: false  
   - **Description**: Enables reversed audio processing (e.g., for echo effects).  
   - **Methods**: `set_reverse(bool value)`, `get_reverse()`.  

8. **mix**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Balances the mix of processed and unprocessed audio. Range: 0.0–1.0.  
   - **Methods**: `set_mix(float value)`, `get_mix()`.  

9. **width**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Adjusts the stereo width of the effect. Range: 0.0–1.0.  
   - **Methods**: `set_width(float value)`, `get_width()`.  

10. **feedback**  
    - **Type**: float  
    - **Default**: 0.5  
    - **Description**: Controls the amount of feedback (repetition) in the effect. Range: 0.0–1.0.  
    - **Methods**: `set_feedback(float value)`, `get_feedback()`.  

This structure organizes the properties with their types, default values, descriptions, and associated methods, preserving the original technical details while removing markdown formatting.