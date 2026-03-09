# AddSymbolProperty Command

Adds a property to the symbol currently open in the symbol editor. See the User's Manual for detailed information on properties.

```
AddSymbolProperty <name> <flags> <value> [<x> <y>] [/styleoverride <style-name>]
```

### Parameters

|  |  |
| --- | --- |
| /styleoverride | Style name to use instead of the inferred style. |
| name | Property name |
| flags | Property attribute flags. See  [Attribute Flags in the Prop command](com_prop.htm) . |
| value | Property value |
| x,y | If both specified the property will automatically be given a fixed position attribute and will be located at the position given. The position is relative to the symbol's origin |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addsymbolproperty) | | |
| [◄ AddSeg](com_addseg.htm) |  | [AddTextBox ▶](com_addtextbox.htm) |
