# CreateToolBar Command

Creates a new empty toolbar. To add buttons to the toolbar use command  [DefineToolBar](com_definetoolbar.htm) .

```
CreateToolBar <context-name> <toolbar-name>
```

### Parameters

|  |  |
| --- | --- |
| /vert | Toolbar will be positioned on a new row below the standard toolbar. Otherwise it will be placed to right of the standard toolbar |
| context-name | Name of window where toolbar is to reside. Must be one of:  |  |  | | --- | --- | | CommandShell | Command shell window | | Schematic | Schematic windows | | SimetrixSchemToolBar | Schematic windows (SIMetrix mode only) | | SimplisSchemToolBar | Schematic windows (SIMPLIS mode only) | | Symbol | Symbol editor windows | | Graph | Graph windows | | AsciiFileEditor | ASCII Schematic file editor windows | | LogicDefinitionEditor | Logic definition editors | | NetlistEditor | Netlist and model text editors | | ScriptEditor | Script text editors | | TextEditor | Plain text editors | | VerilogAEditor | Verilog-A editors | | VerilogHDLEditor | Verilog-HDL editors | | WebView | Web view windows | |
| toolbar-name | User assigned name for toolbar. You can use any name that doesn't clash with a pre-defined toolbar name as defined in the table below. The name must not contain spaces. Pre-defined toolbars are:  |  |  | | --- | --- | | AsciiFileEditor | ASCII Schematic file editor windows | | Shell | Command Shell toolbar | | LogicDefinitionEditor | Logic definition editors | | NetlistEditor | Netlist and model text editors | | SimetrixSchemToolBar | Schematic windows (SIMetrix mode only) | | SimplisSchemToolBar | Schematic windows (SIMPLIS mode only) | | ScriptEditor | Script text editors | | SymbolMain | Symbol editor toolbar | | TextEditor | Plain text editors | | VerilogAEditor | Verilog-A editors | | VerilogHDLEditor | Verilog-HDL editors | | GraphMain | Graph window toolbar | | WebView | Web view windows |  This name is used to reference the tool bar in the  [DefineToolBar](com_definetoolbar.htm)  command. |

### Notes

It is legal to define multiple toolbars with the same name but a different context name. This allows the same toolbar to be placed in multiple contexts. For example, the following is allowed:

```
CreateToolBar VerilogAEditor verilogtoolbar
CreateToolBar VerilogHDLEditor verilogtoolbar
```

The toolbar will show in both Verilog-A and Verilog-HDL editors Changes to the toolbar configuration of a window type (i.e. context), do not take effect until all windows of that type have been closed.

### See Also

* [CreateToolButton](com_createtoolbutton.htm)
* [DefButton](com_defbutton.htm)
* [GetToolButtons](func_gettoolbuttons.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_createtoolbar) | | |
| [◄ CreateSym](com_createsym.htm) |  | [CreateToolButton ▶](com_createtoolbutton.htm) |
