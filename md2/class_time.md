# Time Class Documentation

## Overview
The `Time` class provides a comprehensive set of methods for handling time, date, and time zone conversions. It includes functionality for retrieving current time, converting between various time representations, and working with Unix timestamps, time zones, and system time.

---

## Time Conversion Methods

### `get_offset_string_from_offset_minutes(offset_minutes)`
**Description**: Converts a timezone offset in minutes to a formatted timezone string.
**Parameters**:  
- `offset_minutes` (int): Timezone offset in minutes (e.g., -480, 345, 0).
**Return**:  
- String in format `"+HH:MM"` or `"-HH:MM"` (e.g., "-08:00", "+05:45", "+00:00").
**Note**: Handles sub-hour offsets (e.g., +05:45).

---

## Time Ticks and Duration

### `get_ticks_msec()`
**Description**: Returns the number of milliseconds since the engine started.
**Return**:  
- 64-bit integer (positive or zero). Will wrap after ~500 million years.

### `get_ticks_usec()`
**Description**: Returns the number of microseconds since the engine started.
**Return**:  
- 64-bit integer (positive or zero). Will wrap after ~half a million years.

---

## Date and Time Handling

### `get_datetime_string_from_system(utc=False, use_space=False)`
**Description**: Returns the current date and time as an ISO 8601 string (e.g., "YYYY-MM-DDTHH:MM:SS").
**Parameters**:  
- `utc` (bool): If `True`, returns UTC time; otherwise, local time.
- `use_space` (bool): If `True`, separates date and time with a space (e.g., "YYYY-MM-DD HH:MM:SS").
**Return**:  
- String in ISO 8601 format.

### `get_datetime_string_from_unix_time(unix_time_val, use_space=False)`
**Description**: Converts a Unix timestamp to an ISO 8601 date and time string.
**Parameters**:  
- `unix_time_val` (int): Unix timestamp (seconds since 1970-01-01 UTC).
- `use_space` (bool): If `True`, separates date and time with a space.
**Return**:  
- String in ISO 8601 format.

---

## Time Zone Information

### `get_time_zone_from_system()`
**Description**: Returns the current system time zone as a dictionary.
**Return**:  
- Dictionary with:
  - `bias` (int): Offset from UTC in minutes (e.g., -300 for UTC-5).
  - `name` (str): Localized time zone name (e.g., "America/New_York").

---

## Unix Timestamp Handling

### `get_unix_time_from_system()`
**Description**: Returns the current Unix timestamp in seconds (UTC) as a float.
**Return**:  
- Float with sub-second precision (e.g., 1699272000.123).
**Note**: Unlike other methods, this returns a float for sub-second accuracy.

### `get_unix_time_from_datetime_string(datetime_str)`
**Description**: Converts an ISO 8601 string to a Unix timestamp.
**Parameters**:  
- `datetime_str` (str): ISO 8601 string (e.g., "2023-10-01T12:34:56").
**Return**:  
- Integer Unix timestamp (seconds since 1970-01-01 UTC).

---

## Date and Time Dictionaries

### `get_time_dict_from_system(utc=False)`
**Description**: Returns the current time as a dictionary of hour, minute, and second.
**Parameters**:  
- `utc` (bool): If `True`, returns UTC time; otherwise, local time.
**Return**:  
- Dictionary with `hour`, `minute`, and `second` (integers).

### `get_time_dict_from_unix_time(unix_time_val)`
**Description**: Converts a Unix timestamp to a time dictionary.
**Parameters**:  
- `unix_time_val` (int): Unix timestamp (seconds since 1970-01-01 UTC).
**Return**:  
- Dictionary with `hour`, `minute`, and `second` (integers).

---

## Date and Time Conversion

### `get_date_string_from_system(utc=False)`
**Description**: Returns the current date as an ISO 8601 string (e.g., "YYYY-MM-DD").
**Parameters**:  
- `utc` (bool): If `True`, returns UTC date; otherwise, local date.

### `get_date_string_from_unix_time(unix_time_val)`
**Description**: Converts a Unix timestamp to an ISO 8601 date string.
**Parameters**:  
- `unix_time_val` (int): Unix timestamp (seconds since 1970-01-01 UTC).
**Return**:  
- String in "YYYY-MM-DD" format.

---

## Time Calculations

### `get_unix_time_from_datetime_dict(datetime_dict)`
**Description**: Converts a time dictionary (year, month, day, hour, minute, second) to a Unix timestamp.
**Parameters**:  
- `datetime_dict` (dict): Contains `year`, `month`, `day`, `hour`, `minute`, and `second`.
**Return**:  
- Integer Unix timestamp.

---

## Notes
- All methods that return times use the system's local time unless explicitly specified to use UTC.
- Timezone handling is based on the system's local settings, but `get_time_zone_from_system()` provides explicit timezone information.
- Methods involving Unix timestamps treat time as a 32-bit integer (seconds since 1970-01-01 UTC), which wraps in 2038.