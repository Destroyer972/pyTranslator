# pyTranslator library
pyTranslator is a simple library that helps you to translate your applications and games more easily with a simple file system in xml.

## Installation
To install the library you need to copy the translator.py file into your project and create a folder where you can put the language files.

## How to use
The strength of pyTranslator is his ease of use. 
- Create all language file in the same folder with the prefix `lang_` and in each lang file write all your sentances and words between <application> tag as in the exemple.
- In your code, import the library and create a translator object. Then, each time you need to display a word or a sentence, call him into the lang file with the function `get_element`

## exemple
`langs/lang_en.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<application>
	<global>
		<title>My game</title>
		<description>This is my first game</description>
	</global>
</application>
```
`main.py`
```python3
import pyTranslator as pT

ts = pT.translator("en","en","langs/")
title = ts.get_element("global/title")
description = ts.get_elemnt("global/description")
print("title","description")
```

