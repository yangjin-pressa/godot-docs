# RegExMatch

**Inherits:** RefCounted < Object

## Description
Contains the results of a single RegEx match returned by RegEx.search() and RegEx.search_all(). It can be used to find the position and range of the match and its capturing groups, and it can extract its substring for you.

## Properties
- **names**: Dictionary = {}  
- **strings**: PackedStringArray = PackedStringArray()  
- **subject**: String = ""

## Methods
- **get_end(name: Variant = 0)** → int  
- **get_group_count()** → int  
- **get_start(name: Variant = 0)** → int  
- **get_string(name: Variant = 0)** → String  

## Property Descriptions
**names**: Dictionary of named groups and their corresponding group numbers. Only groups that were matched are included. If multiple groups have the same name, that name refers to the first matching one.

**strings**: Array of the match and its capturing groups. The returned array is copied; changes to it do not affect the original property value.

**subject**: The source string used with the search pattern to find this matching result.

## Method Descriptions
**get_end(name: Variant = 0)** → int  
Returns the end position of the match within the source string. Returns -1 if the group did not match or doesn't exist.

**get_group_count()** → int  
Returns the number of capturing groups.

**get_start(name: Variant = 0)** → int  
Returns the starting position of the match within the source string. Returns -1 if the group did not match or doesn't exist.

**get_string(name: Variant = 0)** → String  
Returns the substring of the match from the source string. Returns an empty string if the group did not match or doesn't exist.