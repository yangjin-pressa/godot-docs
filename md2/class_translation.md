# Translation

**Inherits:** Resource → RefCounted → Object  
**Inherited By:** OptimizedTranslation  

## Overview  
A resource for mapping strings to translations, supporting pluralization.  

## Tutorials  
- [Internationalizing games](../tutorials/i18n/internationalizing_games)  
- [Locales](../tutorials/i18n/locales)  

## Properties  
- **locale** (String): Language code (default: "en")  

## Methods  
### Property Methods  
- `set_locale(value: String)`: Sets the locale.  
- `get_locale()`: Retrieves the current locale.  

### Message Management  
- `add_message(src: String, translated: String, context: String)`: Adds a message if it doesn’t exist.  
- `remove_message(key: String)`: Removes a message.  
- `has_message(key: String)`: Checks if a message exists.  

### Data Retrieval  
- `get_message_count()`: Returns number of messages.  
- `get_message_list()`: Returns all message keys.  
- `get_translated_message_list()`: Returns all translated text.  

### Translation Functions  
- `get_message(key: String)`: Retrieves a translated message.  
- `get_plural_message(key: String, count: Int)`: Returns pluralized translation.  

### Virtual Methods  
- `get_message(key: String)`: Virtual (override for custom behavior).  
- `get_plural_message(key: String, count: Int)`: Virtual (override for custom behavior).  

## Notes  
- **Virtual methods** should be overridden for custom translation logic.  
- **Const methods** (e.g., `get_message_count()`) do not modify instance data.  
- Context can be used to differentiate between message variations.