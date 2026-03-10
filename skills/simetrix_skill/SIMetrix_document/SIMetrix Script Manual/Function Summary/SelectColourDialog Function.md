# SelectColourDialog Function

Opens a dialog box allowing the user to define a colour. The box is initialised with the colour specification supplied as an argument. The function returns the new colour specification.

If the user cancels the box, the function returns an empty vector.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | Specification for BLACK | Initial colour specification |

#### Argument 1

Initial colour specification. May be the name of a colour object, an integer value as returned by  [GetColourSpec](func_getcolourspec.htm)  or a colour in the form #rrggbb

### Returns

Return type: string

Colour in form #rrggbb

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_selectcolourdialog) | | |
| [◄ SelectAnalysis](func_selectanalysis.htm) |  | [SelectColumns ▶](func_selectcolumns.htm) |
