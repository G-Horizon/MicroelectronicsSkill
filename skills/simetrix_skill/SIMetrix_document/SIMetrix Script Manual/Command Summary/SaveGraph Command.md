# SaveGraph Command

Saves the currently selected graph to an XML file. This can subsequently be restored using  [OpenGraph](com_opengraph.htm) .

```
SaveGraph <filename>
```

### Parameters

|  |  |
| --- | --- |
| /id | Graph object id. If more than one graph is displayed,  *graph-id*  can be used to identify which graph is saved. If omitted the currently selected graph is used. All currently open graphs can be obtained from the function  [GetGraphObjects](func_getgraphobjects.htm)  , using `GetGraphObjects('graph')` , while  [GetGraphTabs](func_getgraphtabs.htm)  can be used to obtain the graph objects within a single window. |
| /wid |  |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_savegraph) | | |
| [◄ SaveAs](com_saveas.htm) |  | [SaveGroup ▶](com_savegroup.htm) |
