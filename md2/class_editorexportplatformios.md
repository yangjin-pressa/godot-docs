Here's a structured documentation of the iOS platform settings, organized by category and property:

---

### **Privacy & Permissions**

#### **Microphone Access**
- **`microphone_usage_description`**  
  A localized message displayed when requesting microphone permission.  
  - Type: `String`  
  - Example: `"Use your microphone to record audio."`  

- **`microphone_usage_description_localized`**  
  A dictionary of localized messages for different languages.  
  - Type: `Dictionary<String, String>`  
  - Example: `{"en": "Use your microphone...", "es": "Usar el micrófono..."}`  

#### **Photo Library Access**
- **`photolibrary_usage_description`**  
  A message for requesting photo library access.  
  - Type: `String`  

- **`photolibrary_usage_description_localized`**  
  Localized version of the above message.  
  - Type: `Dictionary<String, String>`  

#### **API Access Reasons**
- **`disk_space_access_reasons`**  
  Reasons for using disk space APIs (e.g., `kDiskSpaceUsageReason`).  
  - Type: `Int`  

- **`file_timestamp_access_reasons`**  
  Reasons for accessing file timestamps/metadata.  
  - Type: `Int`  

- **`system_boot_time_access_reasons`**  
  Reasons for using system boot time APIs.  
  - Type: `Int`  

- **`user_defaults_access_reasons`**  
  Reasons for using user defaults.  
  - Type: `Int`  

#### **Tracking Settings**
- **`tracking_domains`**  
  List of domains used for tracking (e.g., `example.com`).  
  - Type: `PackedStringArray`  
  - Note: The array is copied; changes do not affect the original.  

- **`tracking_enabled`**  
  Whether the app uses data for tracking.  
  - Type: `Bool`  

---

### **Storyboards & Launch Screen**

#### **Custom Launch Screen**
- **`storyboard/custom_bg_color`**  
  Custom background color for the launch screen.  
  - Type: `Color`  

- **`storyboard/custom_image@2x`**  
  Launch screen image for 2x DPI.  
  - Type: `String`  
  - Fallback: Project setting `boot_splash/image` if empty.  

- **`storyboard/custom_image@3x`**  
  Launch screen image for 3x DPI.  
  - Type: `String`  

- **`storyboard/image_scale_mode`**  
  Scaling mode for the launch screen image.  
  - Type: `Int` (e.g., 0 = aspect fit, 1 = aspect fill).  

- **`storyboard/use_custom_bg_color`**  
  Whether to use the custom background color.  
  - Type: `Bool`  

---

### **User Data Access**

#### **Document Folder Access**
- **`user_data/accessible_from_files_app`**  
  Whether the app's "Documents" folder is accessible via the Files app.  
  - Type: `Bool`  
  - Relates to Apple's `LSSupportsOpeningDocumentsInPlace`.  

- **`user_data/accessible_from_itunes_sharing`**  
  Whether the app's folder is accessible via iTunes file sharing.  
  - Type: `Bool`  
  - Relates to Apple's `UIFileSharingEnabled`.  

---

### **Key Notes**
- **Localization**: Strings like `microphone_usage_description` must be in English, while localized versions are for multi-language support.  
- **Copy Behavior**: Properties like `tracking_domains` return a copied array; modifications do not affect the original.  
- **Fallbacks**: Image paths for launch screens default to project settings if empty.  
- **Apple APIs**: Reason codes for API access must align with Apple's documented values (e.g., `kDiskSpaceUsageReason`).  

This documentation ensures clarity for developers configuring iOS app settings, covering permissions, launch screen customization, and data access controls.