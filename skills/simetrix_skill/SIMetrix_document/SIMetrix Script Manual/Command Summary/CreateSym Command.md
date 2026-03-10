# CreateSym Command

```
CreateSym [/local] [/file <libfile>] [/flags <flags>] <symbol-name> [<description> [<catalog>]]
```

### Parameters

|  |  |
| --- | --- |
| /file | If specified, the symbol will be saved to libfile. If neither /file nor /local are specified, the symbol will be saved to the file default.sxslb in the SymbolLibs directory. |
| /flags | If flags=1 then the symbol will be stored with tracking enabled. This means that any existing instances of the symbol with the specified name will be automatically be updated when the symbol is edited. |
| /local | If specified, the symbol will be created in the currently open schematic and will not be saved to the global library. |
| symbol-name | Text string. Name of symbol being defined. This can be anything not already used in a previous symbol definition and must not contain spaces. This is known as the "internal name" in the user interface. |
| symbol-description | Text string. Description of symbol. If specified this will appear in the choose symbol dialog box opened by the menu **Place** > **From Symbol Library...**. (This menu calls the function  [GetSymbols](func_getsymbols.htm)  ). This is known as the "user name" in the user interface. |
| catalogue | This permits the implementation of multiple catalogues for symbols. This is a method of categorising symbols so that they can be easily located. The menu **Place** > **From Symbol Library...** lists available symbols in a tree structure and the catalogue name is used to define its location in that tree. Branch names are separated by semi-colons. E.g. "Digital;Flip-flops" creates a top level called "Digital" and a sub-branch called "Flip-flops". |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_createsym) | | |
| [◄ CreateRunningDialog](com_createrunningdialog.htm) |  | [CreateToolBar ▶](com_createtoolbar.htm) |
