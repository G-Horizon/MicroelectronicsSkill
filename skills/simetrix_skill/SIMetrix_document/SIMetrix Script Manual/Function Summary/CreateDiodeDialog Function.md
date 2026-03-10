# CreateDiodeDialog Function

Opens a specialised dialog used by the diode model in circuit parameter extractor. See internal script  *make\_srdiode\_model*  for an application example of this function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | No |  | Initial values |

#### Argument 1

String array providing initial values for the various controls. The order is 'IF', 'IRM', 'dIf/dt', 'Tr', 'Vd1', 'Id1', 'Vd2', 'Id2', 'Cj0', 'Save option', 'Device name'. The 'Save option' will be '0' if 'Save to schematic symbol' is specified and '1' if 'Save to model library' is specified.

### Returns

Return type: string array

String array corresponding exactly to argument 1 and holding the user's selected values. Return value will be empty if the user cancels the box.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_creatediodedialog) | | |
| [◄ CountChars](func_countchars.htm) |  | [CreateGraphMeasurement ▶](func_creategraphmeasurement.htm) |
