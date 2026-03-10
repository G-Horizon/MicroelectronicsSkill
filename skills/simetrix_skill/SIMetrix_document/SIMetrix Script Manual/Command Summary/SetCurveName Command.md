# SetCurveName Command

Changes curves label. This is the text displayed in the legend panel.

```
SetCurveName <curve-id> <curve-name>
```

### Parameters

|  |  |
| --- | --- |
| curve-id | Curve Id. Curve id is returned by the functions  [GetSelectedCurves](func_getselectedcurves.htm)  ,  [GetAxisCurves](func_getaxiscurves.htm)  and  [GetAllCurves](func_getallcurves.htm) . |
| curve-label | New label for curve. To restore a label to its default value set this to %DefaultLabel%. |

### Notes

Curve labels can also be edited using the command  [SetGraphAnnoProperty](com_setgraphannoproperty.htm)  to edit the curve's Label property.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_setcurvename) | | |
| [◄ SetAnnotationTextPosition](com_setannotationtextposition.htm) |  | [SetDefaultEncoding ▶](com_setdefaultencoding.htm) |
