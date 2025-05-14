# AudioStreamPlaybackPlaylist

**Inherits:** AudioStreamPlayback < RefCounted < Object  

Playback class used for AudioStreamPlaylist.  

---

**Citations**  
Generated automatically from Godot engine sources.  
Generator: https://github.com/godotengine/godot/tree/master/doc/tools/make_rst.py.  
XML source: https://github.com/godotengine/godot/tree/master/modules/interactive_music/doc_classes/AudioStreamPlaybackPlaylist.xml  

---

**Constructor**  
`AudioStreamPlaybackPlaylist()`: Creates an instance of the class.  

---

**Methods**  
- `_validate()`:  
  - **Purpose**: Validates the playlist.  
  - **Type**: Virtual (overrides default behavior).  
- `set_playlist(playlist: AudioStreamPlaylist)`:  
  - **Purpose**: Sets the playlist to play.  
  - **Type**: Public.  

---

**Properties**  
- `playlist: AudioStreamPlaylist`:  
  - **Description**: Reference to the playlist being played.  
  - **Type**: Public.  

---

**Key Notes**  
- This class is designed for playing audio streams from a playlist.  
- Inherits behavior from AudioStreamPlayback and RefCounted.  
- Requires a valid AudioStreamPlaylist instance to function.