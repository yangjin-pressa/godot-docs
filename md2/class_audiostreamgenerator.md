**AudioStreamGenerator**  
Inherits from: AudioStream → Resource → RefCounted → Object  

---

### **Overview**  
A class for procedural sound generation. Uses `mix_rate` and `mix_rate_mode` to control audio mixing rates.  

---

### **Key Features**  
- **Procedural Sound Generation**: Allows custom audio processing.  
- **Properties**:  
  - `buffer_length`: Controls buffer size (default: 0.5).  
  - `mix_rate`: Sets the audio sample rate (default: 44100 Hz).  
  - `mix_rate_mode`: Determines how mixing rate is handled (default: `MIX_RATE_CUSTOM`).  

---

### **Code Examples**  
#### **GDScript Example**  
```gdscript
# Basic usage
var audio = AudioStreamGenerator.new()
audio.buffer_length = 0.5
audio.mix_rate = 44100
```

#### **C# Example**  
```csharp
// Basic usage
AudioStreamGenerator audio = new AudioStreamGenerator();
audio.bufferLength = 0.5f;
audio.mixRate = 44100;
```

---

### **Properties Table**  
| Property            | Type              | Default Value | Description                             |  
|---------------------|-------------------|----------------|-----------------------------------------|  
| buffer_length       | float             | 0.5            | Buffer size for audio processing.       |  
| mix_rate            | float             | 44100          | Audio sample rate (Hz).                |  
| mix_rate_mode       | AudioStreamGeneratorMixRate | 2 | Determines how mixing rate is applied. |  

---

### **Enumerations**  
**AudioStreamGeneratorMixRate**  
- `MIX_RATE_OUTPUT`: Uses current `AudioServer` output rate.  
- `MIX_RATE_INPUT`: Matches `AudioServer` input rate.  
- `MIX_RATE_CUSTOM`: Uses `mix_rate` value directly.  

---

### **Property Descriptions**  
- **buffer_length**:  
  - **Purpose**: Controls the buffer size for audio processing.  
  - **Trade-off**: Larger values reduce latency but increase CPU usage.  

- **mix_rate**:  
  - **Purpose**: Sets the audio sample rate (Hz).  
  - **Note**: Must match the input data's rate for proper playback.  

- **mix_rate_mode**:  
  - **Purpose**: Determines how the mixing rate is calculated.  
  - **Usage**: Set to `MIX_RATE_CUSTOM` for custom rates.  

---

### **Notes**  
- **Optimal Use**: Prefer **C#** or **GDExtension** for performance-critical applications.  
- **Mixing Rate Matching**:  
  - If using `AudioEffectCapture`, set `mix_rate_mode` to `MIX_RATE_INPUT` or `MIX_RATE_OUTPUT` to match the current `AudioServer` rate.  
- **Nyquist-Shannon Theorem**:  
  - According to the [Nyquist-Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem), sampling rates must be at least twice the highest frequency in the signal.  

---

### **Tutorial**  
[Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)  

--- 

**Key Considerations**  
- Always ensure `mix_rate_mode` aligns with the source data's rate.  
- Adjust `buffer_length` based on latency requirements.