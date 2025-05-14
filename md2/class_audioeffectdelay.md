**AudioEffectDelay**  
- **Inherits**: AudioEffect → Resource → RefCounted → Object  

---

### **Description**  
A delay effect with two taps for stereo delay. Controls the mix between dry and wet signals, and adjusts the delay time, pan, and level for each tap.  

---

### **Tutorials**  
- [Audio buses](../tutorials/audio/audio_buses)  

---

### **Properties**  
1. **dry**  
   - **Type**: float  
   - **Default**: 1  
   - **Description**: Mix between dry and wet signal.  

2. **tap1_delay**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Delay time for the first tap.  

3. **tap1_level**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Level of the first tap.  

4. **tap1_pan**  
   - **Type**: float  
   - **Default**: 0  
   - **Description**: Pan position for the first tap (range: -1 to 1).  

5. **tap2_delay**  
   - **Type**: float  
   - **Default**: 1  
   - **Description**: Delay time for the second tap.  

6. **tap2_level**  
   - **Type**: float  
   - **Default**: 0.5  
   - **Description**: Level of the second tap.  

7. **tap2_pan**  
   - **Type**: float  
   - **Default**: 0  
   - **Description**: Pan position for the second tap (range: -1 to 1).  

---

### **Methods**  
- **set_dry(value: float)**: Sets the dry/wet mix.  
- **get_dry()**: Returns the dry/wet mix.  
- **set_tap1_delay(value: float)**: Sets the first tap delay.  
- **get_tap1_delay()**: Returns the first tap delay.  
- **set_tap1_level(value: float)**: Sets the first tap level.  
- **get_tap1_level()**: Returns the first tap level.  
- **set_tap1_pan(value: float)**: Sets the first tap pan.  
- **get_tap1_pan()**: Returns the first tap pan.  
- **set_tap2_delay(value: float)**: Sets the second tap delay.  
- **get_tap2_delay()**: Returns the second tap delay.  
- **set_tap2_level(value: float)**: Sets the second tap level.  
- **get_tap2_level()**: Returns the second tap level.  
- **set_tap2_pan(value: float)**: Sets the second tap pan.  
- **get_tap2_pan()**: Returns the second tap pan.  

--- 

This structure provides a concise overview of the AudioEffectDelay class, its properties, and methods.