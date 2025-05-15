### VideoStreamPlayback Class

**Inheritance:**
- `Resource`
- `RefCounted`
- `Object`

---

### Description
This class is designed for video playback and is typically overridden by video decoder implementations to handle specific playback logic.

---

### Methods

1. **_get_channels()**
   - **Return Type:** `int`
   - **Description:** Returns the number of audio channels.

2. **_get_channels()**
   - **Return Type:** `int`
   - **Description:** Returns the number of audio channels.

3. **_play()**
   - **Description:** Called when autoplay or play is triggered. This method is virtual and should be overridden by the user.

4. **_seek(time: float)**
   - **Parameters:** `time` (float)
   - **Description:** Selects the audio track `idx`. Called when playback starts, and in response to the `VideoStreamPlayer.audio_track` setter.

5. **_set_audio_track(idx: int)**
   - **Parameters:** `idx` (int)
   - **Description:** Sets the paused status of video playback. The `_is_paused()` method must return `paused`. Called in response to the `VideoStreamPlayer.paused` setter.

6. **_stop()**
   - **Description:** Stops playback. May be called multiple times before `_play()`, or in response to `VideoStreamPlayer.stop()`. The `_is_playing()` method should return `false` once stopped.

7. **_update(delta: float)**
   - **Parameters:** `delta` (float)
   - **Description:** Ticks video playback for `delta` seconds. Called every frame as long as both `_is_paused()` and `_is_playing()` return `true`.

8. **mix_audio(num_frames: int, buffer: PackedFloat32Array = PackedFloat32Array(), offset: int = 0)**
   - **Parameters:** `num_frames` (int), `buffer` (PackedFloat32Array), `offset` (int)
   - **Return Type:** `int`
   - **Description:** Renders `num_frames` audio frames from `buffer`, starting from index `offset`. Returns the number of audio frames rendered or -1 on error.

---

### Key Notes
- **Virtual Methods:** Methods marked as `virtual` should be overridden by the user to have any effect.
- **Const Methods:** Methods marked as `const` have no side effects and do not modify instance variables.
- **Constructor/Static:** These terms are used for method types (not part of the class definition).