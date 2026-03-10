# Wire Command

Enter schematic wiring mode.

```
Wire [/start] [/loc <x1> <y1> <x2> <y2>] [/mode] [/startloc <x1> <y1>]
```

### Parameters

|  |  |
| --- | --- |
| /loc | If specified, command in non-interactive and wire is placed at location specified by x1 y1 x2 y2. Co-ordinates are relative and would usually be derived from a call to  [WirePoints](func_wirepoints.htm) . |
| /mode | If specified, the schematic editor is placed in a temporary wiring mode. The next left click will start a wire and wiring may proceed in the usual manner. After pressing the right mouse button, wiring mode will be cancelled. |
| /start | If specified, a new wire is started. |
| /startloc |  |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_wire) | | |
| [◄ WebOpen](com_webopen.htm) |  | [WireMode ▶](com_wiremode.htm) |
