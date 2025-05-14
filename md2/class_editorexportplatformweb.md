**Class: EditorExportPlatformWeb**  
**Description:** Configures settings for a web build of the Godot engine.  

---

### **Properties**  

1. **customization**  
   - **Type:** `bool`  
   - **Description:** Enables the web build to be customized (e.g., for PWA features).  

2. **html/head_include**  
   - **Type:** `String`  
   - **Description:** Additional HTML tags to include in the `<head>` section (e.g., `<meta>` tags).  

3. **html/focus_canvas_on_start**  
   - **Type:** `bool`  
   - **Description:** Focuses the canvas when the application loads if the browser window is already in focus.  

4. **html/export_path**  
   - **Type:** `String`  
   - **Description:** Specifies the directory for exporting the web build.  

5. **progressive_web_app/background_color**  
   - **Type:** `Color`  
   - **Description:** Background color for the web application.  

6. **progressive_web_app/display**  
   - **Type:** `int`  
   - **Description:** Display mode for the progressive web app (e.g., fullscreen, standalone).  
     - `0`: Fullscreen  
     - `1`: Standalone  
     - `2`: Minimal UI  
     - `3`: Browser  

7. **progressive_web_app/enabled**  
   - **Type:** `bool`  
   - **Description:** Enables the web build as a progressive web application (PWA).  

8. **progressive_web_app/ensure_cross_origin_isolation_headers**  
   - **Type:** `bool`  
   - **Description:** Ensures cross-origin isolation headers (COEP/COOP) for requests.  

9. **progressive_web_app/icon_144x144**  
   - **Type:** `String`  
   - **Description:** Path to the 144×144 icon for the web app. Defaults to the project icon if not defined.  

10. **progressive_web_app/icon_180x180**  
    - **Type:** `String`  
    - **Description:** Path to the 180×180 icon for the web app. Defaults to the project icon if not defined.  

11. **progressive_web_app/icon_512x512**  
    - **Type:** `String`  
    - **Description:** Path to the 512×512 icon for the web app. Defaults to the project icon if not defined.  

12. **progressive_web_app/offline_page**  
    - **Type:** `String`  
    - **Description:** Page to display if the server is unreachable. Saved locally on the client.  

13. **progressive_web_app/orientation**  
    - **Type:** `int`  
    - **Description:** Orientation for mobile devices.  
      - `0`: Any  
      - `1`: Landscape  
      - `2`: Portrait  

14. **variant/extensions_support**  
    - **Type:** `bool`  
    - **Description:** Enables GDExtension support for the web build.  

15. **variant/thread_support**  
    - **Type:** `bool`  
    - **Description:** Enables multithreading. Requires cross-origin isolation (COOP/COEP).  
      - **Note:** Enabled by default for HTTPS sites; disabled for non-HTTPS.  

16. **vram_texture_compression/for_desktop**  
    - **Type:** `bool`  
    - **Description:** Optimizes textures for desktop using S3TC/BPTC.  

17. **vram_texture_compression/for_mobile**  
    - **Type:** `bool`  
    - **Description:** Optimizes textures for mobile using ETC2/ASTC.  

---

**Notes:**  
- Icons (144×144, 180×180, 512×512) are automatically resized if not the specified dimensions.  
- Progressive Web App (PWA) settings require proper hosting and may need CORS/CDN configurations.  
- Thread support is experimental and may not work in all environments.