# SetDefaultEncoding Command

When text files such as scripts, netlists and Verilog-A files are open in text editors and when processed, the encoding is expected to be in UTF-8 (8 bit UNICODE). The encoding affects how characters are encoded in the file. UTF-8 is a universal format that is able to render all characters world-wide but retains compatibility with 7 bit ASCII. If at least one character in an input sequence is detected that is not a valid UTF-8 sequence, an assumption has to be made as to what the encoding is. The default is to use the setting defined by the system locale which can be set in the control panel. This function can be used to set an alternative encoding.

The setting made by this command will also affect the display of text in schematics created in older versions of SIMetrix. For example, if you have a schematic created with version 7.1 on a Japanese system setup with the Japanese code-page, any Japanese characters in that schematic will not show correctly unless your system is also setup with the Japanese code page. If you execute command `SetDefaultEncoding shift-jis` this schematic will show correctly - once it is reopened. You can resave the schematic, in which case it will be saved using UTF-8 and will show correctly on any system.

The argument to the command is the encoding. Some possible values are:

* default - resets to system locale
* windows-1252 - the default on English language windows systems
* shift-jis - Japanese characters
* UTF-8 - Input unconditionally assumed to be UTF-8

A complete list of valid values is returned by the function  [GetCodecNames](func_getcodecnames.htm) . Note that the default encoding only affects behaviour when an input sequence does not comply with UTF-8. Some character encoding schemes (e.g. UTF-16) cannot be easily differentiated from UTF-8 and so are not easily detected. It is usually not appropriate to use this command to set such a default encoding.

This command sets the default encoding for the current session but willbe restored to the previous encoding in future sessions. To set a persistent encoding that doesn't change, set the DefaultEncoding option variable as shown below:

```
Set DefaultEncoding=value
```

where value is one of the values described above. To reset to the default, use:

```
Unset DefaultEncoding
```

```
SetDefaultEncoding <encoding>
```

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_setdefaultencoding) | | |
| [◄ SetCurveName](com_setcurvename.htm) |  | [SetDisable ▶](com_setdisable.htm) |
