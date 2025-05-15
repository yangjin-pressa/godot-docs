# TranslationServer Class Documentation

## Overview
The `TranslationServer` class manages translation domains and locales for a project, providing methods to retrieve, set, and manipulate translations. It supports multiple translation domains and standardizes locale strings for consistency.

---

## Key Methods

### 1. `set_locale(locale: String)`
**Description**: Sets the locale of the project. The locale string is standardized to match known locales (e.g., "en-US" becomes "en_US").

**Parameters**:
- `locale`: A string representing the desired locale (e.g., "en-US", "fr_FR").

**Notes**:
- If translations exist for the new locale, they are applied automatically.
- The locale is standardized using `standardize_locale()`.

---

### 2. `get_locale() -> String`
**Description**: Returns the current locale of the project.

**Returns**:
- The current locale string (e.g., "en_US").

**Note**:
- This is different from the editor's locale, which can be retrieved via `get_tool_locale()`.

---

### 3. `get_tool_locale() -> String`
**Description**: Returns the current locale of the editor.

**Note**:
- When called from an exported project, this returns the same value as `get_locale()`.

---

### 4. `get_locale_name(locale: String) -> String`
**Description**: Returns a human-readable name for the specified locale (e.g., "en_US" → "English (United States)").

---

### 5. `get_loaded_locales() -> PackedStringArray`
**Description**: Returns a list of all locales loaded for the project.

---

### 6. `get_translation_object(locale: String) -> Translation`
**Description**: Retrieves the `Translation` instance that best matches the specified locale in the main domain.

**Returns**:
- `null` if no matching translation is found.

---

### 7. `translate(message: StringName, context: StringName = "") -> StringName`
**Description**: Returns the translation for the given message and context using the current locale.

**Parameters**:
- `message`: The message key to translate.
- `context`: Optional context for the translation.

**Note**:
- Always uses the **main translation domain**.

---

### 8. `translate_plural(message: StringName, plural_message: StringName, n: Int, context: StringName = "") -> StringName`
**Description**: Translates a plural message based on the quantity `n`.

**Parameters**:
- `message`: The base message key.
- `plural_message`: The plural message key.
- `n`: The quantity to determine the plural form.
- `context`: Optional context for the translation.

**Note**:
- Always uses the **main translation domain**.

---

### 9. `pseudolocalize(message: StringName) -> StringName`
**Description**: Returns a pseudolocalized version of the given message.

**Parameters**:
- `message`: The message key to pseudolocalize.

**Note**:
- Always uses the **main translation domain**.
- Pseudolocalization is typically used for previewing translations in a non-locale-specific way.

---

### 10. `standardize_locale(locale: String, add_defaults: Bool = false) -> String`
**Description**: Converts the locale string to a standardized format (e.g., "en-US" → "en_US").

**Parameters**:
- `locale`: The input locale string.
- `add_defaults`: If `true`, adds default country or script if missing.

**Returns**:
- The standardized locale string.

---

### 11. `get_language_name(language: String) -> String`
**Description**: Returns a human-readable name for the specified language code (e.g., "en" → "English").

---

### 12. `get_country_name(country: String) -> String`
**Description**: Returns a human-readable name for the specified country code (e.g., "US" → "United States").

---

### 13. `get_script_name(script: String) -> String`
**Description**: Returns a human-readable name for the specified script code (e.g., "Latin" → "Latin script").

---

### 14. `get_or_add_domain(domain: StringName) -> TranslationDomain`
**Description**: Returns or creates a translation domain with the specified name.

**Returns**:
- The `TranslationDomain` instance.

**Note**:
- If the domain doesn't exist, an empty domain is created.

---

### 15. `has_domain(domain: StringName) -> Bool`
**Description**: Checks if a translation domain with the specified name exists.

---

### 16. `remove_domain(domain: StringName) -> void`
**Description**: Removes a translation domain by name.

**Note**:
- Cannot remove the **main translation domain**.

---

### 17. `remove_translation(translation: Translation) -> void`
**Description**: Removes a specific translation from the main domain.

---

### 18. `reload_pseudolocalization() -> void`
**Description**: Reparses pseudolocalization options and reloads translations for the main domain.

---

## Important Notes

- **Main Domain**: Most methods (e.g., `translate`, `pseudolocalize`) use the main translation domain by default. To use other domains, explicitly specify them.
- **Locale Standardization**: Always use `standardize_locale()` before setting or retrieving locales.
- **Pseudolocalization**: Use `pseudolocalize()` for previewing translations in a locale-agnostic way.
- **Domain Safety**: The main domain cannot be removed. Attempting to do so will result in an error.

---

## Example Usage

```gdscript
var locale = "en-US"
var standardized_locale = TranslationServer.standardize_locale(locale)
TranslationServer.set_locale(standardized_locale)

var translated_message = TranslationServer.translate("greeting")
var plural_translation = TranslationServer.translate_plural("greeting", "greetings", 3)
```

---

This documentation provides a comprehensive guide to using the `TranslationServer` class for managing translations in a project. Always ensure to standardize locales before using them, and use the main domain for default translations.