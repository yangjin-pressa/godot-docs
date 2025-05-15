# ResourceImporterCSVTranslation

Inherits: ResourceImporter → RefCounted → Object

Imports comma-separated values

## Description
Comma-separated values are a plain text table storage format. The format's simplicity makes it easy to edit in any text editor or spreadsheet software. This makes it a common choice for game localization.

**Example CSV file:**
```
keys,en,es,ja
GREET,"Hello, friend!","Hola, amigo!",こんにちは
ASK,How are you?,Cómo está?,元気ですか
BYE,Goodbye,Adiós,さようなら
QUOTE,"""Hello"" said the man.","""Hola"" dijo el hombre.",「こんにちは」男は言いました
```

## Tutorials
- Importing translations: https://godotengine.org/tutorials/assets_pipeline/importing_translations

## Properties
- compress: bool = true
- delimiter: int = 0

## Property Descriptions
compress: If true, creates an OptimizedTranslation instead of a Translation. This makes the resulting file smaller at the cost of a small CPU overhead.

delimiter: The delimiter to use in the CSV file. The default value matches the common CSV convention. Tab-separated values are sometimes called TSV files.