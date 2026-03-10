# Select Command

Select items on selected schematic. If the /prop switch is not specified the interactive select mode is entered.

```
Select [/wires] [/prop <prop-name>|/wire <wire-name>|/all]
```

### Parameters

|  |  |
| --- | --- |
| /all | If specified, all items on the current schematic sheet will be selected. |
| /prop | If  *value*  is specified, all components on the current schematic with property of name  *name*  and value  *value*  will be selected. If value is not specified then all components possessing the property  *name*  will be selected. |
| /wire | Select wire with handle defined by  *wirehandle* . |
| /wires | If specified, only wires will be selected. Otherwise both components and wires will be selected. |

### Notes

The `/prop` switch makes it possible to automate modification of component values using a script. For example, supposing you have a circuit with a resistor R2 and capacitors C4 and C5, you could modify the values of all of them with a script something like:

```
Unselect
Select /prop ref R2
Prop value 1.1K
Unselect
Select /prop ref C4
Prop value 120p
Unselect
Select /prop ref C5
Prop value 1.2n
```

The above script would change R2, C4 and C5 to 1.1k, 120p and 1.2n respectively.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_select) | | |
| [◄ ScriptStep](com_scriptstep.htm) |  | [SelectCurve ▶](com_selectcurve.htm) |
