# AudioEffect

## Inheritance
- **Inherits:** Resource < RefCounted < Object  
- **Inherited By:**  
  AudioEffectAmplify, AudioEffectCapture, AudioEffectChorus, AudioEffectCompressor, AudioEffectDelay, AudioEffectDistortion, AudioEffectEQ, AudioEffectFilter, AudioEffectHardLimiter, AudioEffectLimiter, AudioEffectPanner, AudioEffectPhaser, AudioEffectPitchShift, AudioEffectRecord, AudioEffectReverb, AudioEffectSpectrumAnalyzer, AudioEffectStereoEnhance

## Description
Base class for audio effect resources. In the editor, audio effects can be added to buses via the Audio panel. At runtime, use AudioServer methods to manipulate effects. When applied to a bus, an AudioEffectInstance is created to handle sound manipulation based on the effect's properties.

## Tutorials
- Audio buses: [Audio buses](../tutorials/audio/audio_buses)
- Audio Microphone Record Demo: [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)

## Methods
- **_instantiate()**:  
  Override this method to customize the AudioEffectInstance created when the effect is applied to a bus.  
  **Example:**  
  ```  
  extends AudioEffect  

  @export var strength = 4.0  

  func _instantiate():  
      var effect = CustomAudioEffectInstance.new()  
      effect.base = self  
      return effect  
  ```  
  **Note:** Maintain a reference to the original AudioEffect in the instance to enable run-time modifications.

## Key Details
- **Purpose:** Base class for all audio effects, enabling runtime manipulation via AudioServer.  
- **Instance Management:** Each bus application creates an AudioEffectInstance for sound processing.  
- **Customization:** Override _instantiate() to define custom effect instances.  
- **Reference Handling:** Ensure the original AudioEffect is accessible in the instance for dynamic updates.