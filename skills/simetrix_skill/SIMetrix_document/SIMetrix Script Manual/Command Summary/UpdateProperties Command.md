# UpdateProperties Command

Restores properties on specified schematic instances to symbol defaults.

Command has two modes of operation. If /all is specified then all properties will be restored to the state defined in the symbol. If /all is omitted, properties that exist on the symbol but are missing on the instance will be added. All existing instance properties will be unaffected.

```
UpdateProperties [/all] [<property-name> [<property-value>]]
```

### Parameters

|  |  |
| --- | --- |
| /all | Restore all properties to symbol state. If omitted only new properties added. See description for details |
| property-name | Property name used to identify instances to process. Use selected instances if omitted |
| property-value | Property value used to identify instances to process. If omitted but  *property-name*  is specified, all instances with  *property-name*  will be processed. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_updateproperties) | | |
| [◄ UpdateGraphColours](com_updategraphcolours.htm) |  | [UpdateRunningDialog ▶](com_updaterunningdialog.htm) |
