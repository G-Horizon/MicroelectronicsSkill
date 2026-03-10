# DeleteAxis Command

Deletes the specified axis. If the grid that owns the axis is empty and it is not the only grid in the graph sheet, the grid itself will also be deleted.

The axis will not be deleted if there are curves attached to it.

```
DeleteAxis <axis-id>
```

### Parameters

|  |  |
| --- | --- |
| axis-id | Axis id as returned by functions  [GetAllYAxes](func_getallyaxes.htm)  ,  [GetSelectedYAxis](func_getselectedyaxis.htm)  or  [GetCurveAxis](func_getcurveaxis.htm) . |

### Notes

An axis may only be deleted if it is empty i.e. has no attached curves. Also the main axis may not be deleted.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_deleteaxis) | | |
| [◄ Delete](com_delete.htm) |  | [DeleteGlobalStyle ▶](com_deleteglobalstyle.htm) |
