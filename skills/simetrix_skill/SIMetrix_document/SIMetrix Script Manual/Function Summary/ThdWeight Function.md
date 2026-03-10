# ThdWeight Function

Returns a real array of 34 elements containing the weighting coefficients from 10Hz to 20kHz. The weighting coefficient vector can be used to calculate the weighted THD of a time-domain vector using a FFT. Note that the

The weighting coefficients are defined in the IEC 61672-1 and IEC 60537 publications. For further information, see the \externalreference{IEC Website}{http://www.iec.ch}.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | The type of weighting to return |

#### Argument 1

Specifies the type of weighting, one of:

* "a" A-type weighting
* "b" B-type weighting
* "c" C-type weighting
* "d" D-type weighting

The weighting coefficient argument is not case sensitive.

### Returns

Return type: real array

Vector of weighting coefficients with reference values from 10Hz to 20kHz.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_thdweight) | | |
| [◄ TextEditorHasComments](func_texteditorhascomments.htm) |  | [TickCount ▶](func_tickcount.htm) |
