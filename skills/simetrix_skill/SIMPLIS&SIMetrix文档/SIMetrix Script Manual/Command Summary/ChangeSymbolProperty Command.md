# ChangeSymbolProperty Command

Modifies a named or selected symbol editor property. In the symbol editor, pin names are also represented as properties, so this command is also used to edit pin names.

```
ChangeSymbolProperty [/value <value>] [/flags <flags>] [/loc <x> <y>] [/overridestyle <override-style-name>] [/prefix <prefix>] [/suffix suffix] [/pin] [<prop-name>]
```

### Parameters

|  |  |
| --- | --- |
| /code |  |
| /flags | New property attribute flags. See  [Attribute Flags in the Prop command](com_prop.htm) |
| /loc | New absolute location. If the location was previously relative, this will be changed to absolute if this value is specified. |
| /overridestyle | Style name to use instead of the inferred style. |
| /pin | Property name specified is a pin |
| /prefix | Pin prefix for XSpice attributes |
| /suffix | Pin suffix for XSpice attributes |
| /value | New property value |

### See Also

* [Prop](com_prop.htm)
* [AddProp](com_addprop.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_changesymbolproperty) | | |
| [◄ ChangeStyle](com_changestyle.htm) |  | [ClearMessageWindow ▶](com_clearmessagewindow.htm) |
