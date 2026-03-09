# ElementProps Function

Returns an array of strings holding the names of all properties of an instance. The functions  [PropValue](func_propvalue.htm)  or  [PropValues2](func_propvalues2.htm)  can be used to find values of these properties.

This is a generalisation of  [InstProps](func_instprops.htm)  , in that it will return the properties for any selected schematic element.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | -1 | Schematic ID |
| 2 | string | No |  | Property name |
| 3 | string | No |  | Property value |

#### Argument 1

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If equal to -1, the currently selected schematic will be used.

#### Argument 2

Property name to identify element. Along with parameter 2, if these arguments are not provided, the selected element, if any, will be used instead. If there are no selected elements or no elements that match the arguments, the function will return an empty vector. If the arguments identify more than one element, the function will return information for one of them but there are no rules to define which one.

Using the 'HANDLE' property and its value will guarantee uniqueness.

#### Argument 3

Property value to identify element. Along with parameter 1, if these arguments are not provided, the selected element, if any, will be used instead. If there are no selected elements or no elements that match the arguments, the function will return an empty vector. If the arguments identify more than one element, the function will return information for one of them but there are no rules to define which one.

Using the 'HANDLE' property and its value will guarantee uniqueness.

### Returns

Return type: string array

Array of strings with property values. Returns empty value if no match to property name and value is found. Also returns empty value if the schematic ID is invalid.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_elementprops) | | |
| [◄ EditWaveformStrDialog](func_editwaveformstrdialog.htm) |  | [EncodeImageToBase64 ▶](func_encodeimagetobase64.htm) |
