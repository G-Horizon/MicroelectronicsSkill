# DeleteGraphObject Command

Deletes a graph object such as an axis, curve or annotation object such as a curve marker or legend box. See  [Graph Objects](applications_graphobjects.htm)  for details on graph objects.

If the object being deleted is a graph, all contained objects will also be deleted. The graph is not required to be empty.

If the object being deleted is a grid, all contained axes and curves will be deleted.

If the object being deleted is an axis, the delete operation will fail unless the axis has no attached curves and is not the last axis of its type (X or Y) in its associated grid.

The  [DeleteAxis](com_deleteaxis.htm)  command may be used to delete an axis along with its associated grid.

The command will fail if there are no graphs open.

```
DeleteGraphObject <object-id>
```

### Parameters

|  |  |
| --- | --- |
| object-id | Id of object to be deleted. This can be obtained from a number of functions. See  [Graph Objects](applications_graphobjects.htm)  for a complete list. |

### See Also

* [DeleteGraphAnno](com_deletegraphanno.htm)
* [DeleteAxis](com_deleteaxis.htm)
* [DelCrv](com_delcrv.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_deletegraphobject) | | |
| [◄ DeleteGraphAnno](com_deletegraphanno.htm) |  | [DeleteShortWires ▶](com_deleteshortwires.htm) |
