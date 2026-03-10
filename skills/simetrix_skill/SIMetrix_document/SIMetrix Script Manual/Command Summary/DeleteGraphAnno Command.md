# DeleteGraphAnno Command

Deletes a graph annotation object such as a curve marker or legend box. See  [Graph Objects](applications_graphobjects.htm)  for details on graph annotation objects.

The command will fail if there are no graphs open. An attempt to delete a graph object which is not an annotation object (e.g. an Axis or Curve) will not raise an error condition, but no action will be taken.

[DeleteGraphObject](com_deletegraphobject.htm)  is a general purpose command that may be used to delete any graph object.

```
DeleteGraphAnno <object-id>
```

### Parameters

|  |  |
| --- | --- |
| object-id | Id of object to be deleted. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_deletegraphanno) | | |
| [◄ DeleteGlobalStyle](com_deleteglobalstyle.htm) |  | [DeleteGraphObject ▶](com_deletegraphobject.htm) |
