# AddCurveMarker Command

Adds a curve marker to the currently selected graph sheet. A curve marker is a graph annotation object and its purpose is to label a curve for the purposes of identification or to highlight a feature. See  [Graph Objects](applications_graphobjects.htm)  for more information.

```
AddCurveMarker <curve-id> <division> <x-position> <y-position> <label> [length [angle]]
```

### Parameters

|  |  |
| --- | --- |
| curve-id | Id for curve to which marker will be attached. |
| division | Division of curve if curve-id refers to a curve group created by a multi-step run. Divisions are numbered from 0 up to 1 minus the number of curves in the group. For single curves set this to zero. |
| x-position | X-axis location of marker. |
| y-position | Y-axis location of marker. This is only used if the curve is non monotonic and has more than one point at  *x-position* . The marker will be placed at the point on the curve with the  *y-axis*  value that is nearest to y-position. |
| label | Label for marker. This may use symbolic values enclosed by '%'. See  [SymbolicValues](applications_graphobjects.htm#applications_graphobjects__symbolicvalues)  for details. |
| length | Length of marker line in view units. See  [GraphCoordinateSystems](applications_graphobjects.htm#applications_graphobjects__graphcoordinatesystems)  for an explanation of view units and the view co-ordinate space. If omitted length defaults to 0.1. |
| angle | Angle of the marker line in the view co-ordinate space (See  [GraphCoordinateSystems](applications_graphobjects.htm#applications_graphobjects__graphcoordinatesystems)  ). Default is 45°. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addcurvemarker) | | |
| [◄ AddCurveData](com_addcurvedata.htm) |  | [AddDoubleClickAction ▶](com_adddoubleclickaction.htm) |
