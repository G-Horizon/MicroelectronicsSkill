# SelectCurve Command

Selects/unselects the identified curve or all curves.

If the `/all` flag is used, then all curves on the currently selected graph are selected or unselected, depending on the `/unselect` flag. Otherwise, a single curve must be specified with  *curveId* .

```
SelectCurve [/unselect] /all|<curveId>
```

### Parameters

|  |  |
| --- | --- |
| /all | All curves will be selected or unselected. |
| /unselect | Curve or curves will be unselected. |
| curveId | Only used if `/all` flag is not used. Specifies a particular curve by it's ID, which can be obtained from the functions  [GetSelectedCurves](func_getselectedcurves.htm)  ,  [GetAxisCurves](func_getaxiscurves.htm)  and  [GetAllCurves](func_getallcurves.htm) . |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_selectcurve) | | |
| [◄ Select](com_select.htm) |  | [SelectGraph ▶](com_selectgraph.htm) |
