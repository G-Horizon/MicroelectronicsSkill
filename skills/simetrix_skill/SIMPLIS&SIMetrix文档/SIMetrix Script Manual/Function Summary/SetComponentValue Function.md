# SetComponentValue Function

SetComponentValue is a specialised function that is used by some internal scripts. It provides a way of setting or getting a value or parameter on a schematic using a single string to identify it. This is in contrast to the usual methods to retrieve values or set values that require a sequence of commands or functions.

For example, to set a resistor R2 to 2200 ohms using conventional methods requires this sequence:

```
Unselect
Select /Prop REF R2
Prop VALUE 2200
```

With SetComponentValue, this can be done simply with:

```
Let SetComponentValue('R2', 2200)
```

However, SetComponentValue can also descend into hierarchies and set values at lower levels. For example:

```
Let SetComponentValue('U1.R2', 2200)
```

Will set the resistor R2 in hierarchical block U1.

SetComponentValue can also set named parameters. For example, if X1 is a parameterised opamp:

```
Let SetComponentValue('X1.GBW', 16.5E6)
```

will set the GBW parameter to 16.5E6.

Because the methods use to store component values and parameters is dependent on the part being edited or viewed, this function requires pre-configuring. This is done using  [PrepareSetComponentValue](func_preparesetcomponentvalue.htm) . A built-in script is available that will configure SetComponentValue for the most commonly used cases. The script is called prepare\_set\_component\_default. See  [PrepareSetComponentValue](func_preparesetcomponentvalue.htm)  for further details.

Be aware that SetComponentValue will not work for all types of device - only those whose method of storing values it has been configured to accept.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Address |
| 2 | string | No | If omitted, value will not be changed but the current value will be returned | Value |
| 3 | real | No | -1 | Schematic ID |
| 4 | real | No | 0 | Flags for new properties |
| 5 | string | No | none | Options |

#### Argument 3

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

#### Argument 4

Flags used for any new properties added to an instance

#### Argument 5

If set to 'noopen' the schematic will not be opened to view by a call to this function

### Returns

Return type: string array

String array of lenght 6 with elements defined by the following table

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Current value (before being edited) |
| 1 | Status code. May be one of 'Noerr', 'BadAddress', 'AmbiguousAddress', 'IncompleteAddress', 'MissingChild', 'WriteProtected' or 'NewProp'. See table below for details |
| 2 | Full path of hierarchical schematic that contained the part that was processed |
| 3 | Handle property of instance that was processed |
| 4 | Parameter or property name that was processed |
| 5 | Debug error message. This has more detailed information than the error code |

|  |  |
| --- | --- |
| **Status code** | **Description** |
| 'Noerr' | No error, function completed successfully |
| 'BadAddress' | The address given was not recognised |
| 'AmbiguousAddress' | The address given could refer to more than one item |
| 'IncompleteAddress' | The address was incomplete. For example, it might refer to a valid part without specifying which parameter is to be written or read |
| 'MissingChild' | Address refers to a hierarchical block which is missing, that is the schematic file could not be found |
| 'WriteProtected' | The operation required an instance property to be edited but that property was protected and could not be edited |
| 'NewProp' | A new property was added to the part to complete the required edit. This is not necessarily an error. Some parameters will assume default values if not present. If set to an explicit value a property may be added to the schematic instance |

### Notes

If the address requires a hierarchical schematic to be written, that schematic will be automatically opened.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_setcomponentvalue) | | |
| [◄ SelSchem](func_selschem.htm) |  | [SetDifference ▶](func_setdifference.htm) |
