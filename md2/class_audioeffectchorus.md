The `AudioEffectChorus` class is designed to implement a **chorus audio effect**, which uses multiple voices (or oscillators) to create a rich, stereo modulation effect. Below is a structured summary of its key properties, methods, and their purposes:

---

### **Core Properties**
1. **Voice Parameters (Per Voice):**
   - **`cutoff_hz`**: Cutoff frequency of a high-pass filter for the voice. Controls the range of frequencies affected by the effect.
   - **`delay_ms`**: Delay time in milliseconds for the voice. Determines the time between the original and modulated signal.
   - **`depth_ms`**: Modulation depth (in milliseconds) that affects how much the signal is altered.
   - **`level_db`**: Volume level (in decibels) of the effect. Controls the intensity of the chorus.
   - **`pan`**: Stereo position (left-right placement) of the voice. Influences the spatial balance of the effect.
   - **`rate_hz`**: Modulation rate (in Hz) of the voice. Affects the speed of the modulation.

2. **Wet/Dry Mix:**
   - **`wet`**: Blend between the original (dry) and processed (wet) signal. A value of 0.5 means equal mixing.

3. **Voice Count:**
   - **`voice_count`**: Number of voices (e.g., 2 for a standard chorus effect). More voices create more complex modulation.

---

### **Method Descriptions**
#### **Getter/Setter Methods:**
- **`get_voice_cutoff_hz(voice_idx)`**: Returns the cutoff frequency for the specified voice. Used to adjust the filter cutoff.
- **`set_voice_cutoff_hz(voice_idx, cutoff_hz)`**: Sets the cutoff frequency for the voice. Adjusts the frequency range affected by the effect.
- **`get_voice_delay_ms(voice_idx)`**: Returns the delay time for the voice. Controls the time between the original and modulated signal.
- **`set_voice_delay_ms(voice_idx, delay_ms)`**: Sets the delay time for the voice. Influences the stereo effect depth.
- **`get_voice_depth_ms(voice_idx)`**: Returns the modulation depth. Determines how much the signal is altered.
- **`set_voice_depth_ms(voice_idx, depth_ms)`**: Sets the modulation depth. Adjusts the intensity of the chorus effect.
- **`get_voice_level_db(voice_idx)`**: Returns the volume level of the voice. Controls the loudness of the effect.
- **`set_voice_level_db(voice_idx, level_db)`**: Sets the volume level of the voice. Adjusts the output strength.
- **`get_voice_pan(voice_idx)`**: Returns the stereo position of the voice. Determines the left-right balance.
- **`set_voice_pan(voice_idx, pan)`**: Sets the stereo position. Adjusts the spatial placement of the effect.
- **`get_voice_rate_hz(voice_idx)`**: Returns the modulation rate (Hz) for the voice. Influences the speed of the effect.
- **`set_voice_rate_hz(`**: Sets the modulation rate. Controls how fast the modulation occurs.

#### **Wet Mix:**
- **`get_wet()`**: Returns the wet/dry mix value.
- **`set_wet(value)`**: Sets the wet/dry mix. Adjusts the balance between the original and processed signal.

---

### **How It Works**
- **Chorus Effect Mechanism**: 
  - Each voice uses an LFO (low-frequency oscillator) to modulate the pitch and timing of the signal.
  - The delay time and depth parameters create a stereo, swirling effect.
  - The `wet` parameter blends the original and processed signals, allowing control over the effect's intensity.
- **Voice Count**: 
  - Multiple voices (e.g., 2) create layered modulation, enhancing the richness of the effect.

---

### **Usage Example**
```cpp
// Set delay time for voice 1
audioEffectChorus.set_voice_delay_ms(0, 10.0); // 10ms delay

// Set modulation depth for voice 2
audioEffectChorus.set_voice_depth_ms(1, 5.0); // 5ms depth

// Set wet mix to 0.8 (80% processed signal)
audioEffectChorus.set_wet(0.8);
```

---

### **Key Tuning Tips**
- **Delay Time**: Higher values create a more pronounced, "wah-wah" effect.
- **Modulation Depth**: Slightly higher values add more depth to the chorus.
- **Modulation Rate**: Slow rates (e.g., 2–5 Hz) produce smooth, subtle effects; faster rates create more erratic modulation.
- **Voice Count**: 2 is standard; 4+ can create complex, lush effects.

---

### **Summary**
The `AudioEffectChorus` class provides fine-grained control over a chorus effect, allowing users to customize the sound through parameters like delay, depth, and modulation rate. It's ideal for creating dynamic, rich audio textures in music production or sound design.