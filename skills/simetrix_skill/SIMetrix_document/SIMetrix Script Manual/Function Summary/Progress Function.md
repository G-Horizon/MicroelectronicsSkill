# Progress Function

Opens a dialog box showing a progress bar.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Position of progress bar in % |
| 2 | string array | No | <<empty>> | options/control |

#### Argument 1

Value from 0 to 100 specifying the position of the bar.

#### Argument 2

String array of max length 2 used to specify options and control as follows:

|  |  |
| --- | --- |
| 'open' | Box is displayed (cannot be used with 'close') |
| 'close' | Box is hidden (cannot be used with 'open') |
| 'showabort' | If specified an abort button will be displayed |

### Returns

Return type: real

The function returns a two element array. The first element returns the value of argument 1, while the second returns 1 if the abort button has been pressed. If the abort button has not been pressed, the second element returns 0.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_progress) | | |
| [◄ ProcessingGuiAction](func_processingguiaction.htm) |  | [PropFlags ▶](func_propflags.htm) |
