# PinName Function

Returns information about the schematic instance pin nearest the mouse cursor. The format of the result depends on the values of the arguments.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | <<empty>> | Options |
| 2 | string | No | <<empty>> | Property name |

#### Argument 1

May be one of five possible values:

|  |  |
| --- | --- |
| <<empty>> | Return value is full hierarchical name of pin. (e.g. U1.U6.Q1#c) |
| 'flat' | Return value is local name without hierarchical prefix (e.g. Q1#c) |
| 'property' | Return value is string array with a pair of elements for each pin at the location. First value in each pair is the value of the property specified in argument 2 and the second is the pin number. |
| 'distance' | Return value has two elements. The second element is the distance of the cursor to the pin in "sheet units". There are 120 "sheet units" per grid at X 1 magnification. |
| ~['flat', 'distance'] | As 'distance' but returns local net name without hierarchical prefix. |

#### Argument 2

Property name whose value is returned if argument 1 is 'property'. See above.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_pinname) | | |
| [◄ PhysType](func_phystype.htm) |  | [PrepareSetComponentValue ▶](func_preparesetcomponentvalue.htm) |
