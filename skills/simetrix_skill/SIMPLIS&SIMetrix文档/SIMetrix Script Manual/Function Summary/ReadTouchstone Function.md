# ReadTouchstone Function

Retrieves the data from a previously Touchstone file loaded using  [LoadTouchstone](func_loadtouchstone.htm) . Must provide data ID, row index and column index

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real | Yes |  | Data ID returned by |
| 2 | Real | Yes |  | Row index |
| 3 | Real | Yes |  | Column index |

#### Argument 1

Data ID returned by  [LoadTouchstone](func_loadtouchstone.htm)

#### Argument 2

Row index

#### Argument 3

Column index

### Returns

Return type: Real array

Y-parameter data in triplets. First value is frequency, second value is real part, third value is imaginary part. One triplet is returned for each frequency found in the file

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readtouchstone) | | |
| [◄ ReadTextEditorProp](func_readtexteditorprop.htm) |  | [real ▶](func_real.htm) |
