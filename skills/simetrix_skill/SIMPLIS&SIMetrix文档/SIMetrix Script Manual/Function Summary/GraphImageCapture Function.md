# GraphImageCapture Function

Opens the Graph Image Capture dialog for extracting data from a graph image. Is used in the  **Digitise Data Sheet Curve**  feature. The command handles initial image selection and opening.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | Current working directory | Starting directory for location of graphic files |

### Returns

Return type: real array

Returns the data points extracted. First element is the number of data points extracted,  *n* . The next  *n*  elements are the x-values, the following  *n*  elements are the y-values of those data points.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_graphimagecapture) | | |
| [◄ GetXAxis](func_getxaxis.htm) |  | [GraphImageParameter ▶](func_graphimageparameter.htm) |
