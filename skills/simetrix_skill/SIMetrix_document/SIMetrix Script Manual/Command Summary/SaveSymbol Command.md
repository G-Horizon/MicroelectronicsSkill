# SaveSymbol Command

Save a symbol to a library or as a component. Source may be the current symbol editor symbol or a specified symbol in the global library.

```
SaveSymbol [/comp] [/file <filename>] [/lib <lib-symbol-name>] [/flags <flags>] <symbol-name> [<symbol-description> [<catalog>]]
```

### Parameters

|  |  |
| --- | --- |
| /comp | Saves symbol as a component to path  *symbol-name* . |
| /file | Symbol saved to specified library file. This is ignored if `/comp` is specified. If a full path is not supplied, the path will be relative to the SymbolLibs directory. |
| /flags | If flags=1, symbol is saved with tracking enabled. This forces all instances of the symbol to always be loaded from the global symbol library rather than from the local schematic. This is the action of the  *"All references to symbol automatically updated"*  check box in the symbol editor's **File** > **Save...** dialog box. |
| /lib | Use specified library symbol as source instead of the symbol editor.  *lib-symbol-name*  must be the internal name for a symbol in an installed library. |
| symbol-name | Name of symbol. This is known as the 'internal name' in the user interface. This is the name that the software uses to identify the symbol. It is stored in schematic files and it is used for a number of script functions and commands, for example the command  [Inst](com_inst.htm)  to place a symbol uses this name. This name may not contain spaces or special characters and cannot be changed once the symbol is created. |
| symbol-description | Symbol description. This is the name that is displayed in the dialog opened with **Place** > **From Symbol Library...**. Unlike the  *symbol-name*  (above) it has no naming restrictions and can be changed at any time without affecting any existing instances of the symbol. |
| catalog | Symbol catalog. This determines how the symbol is categorised in **Place** > **From Symbol Library...**. This may be a list of strings separated by semi-colons, each identifying a node in the tree list display shown in the place symbol dialog box. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_savesymbol) | | |
| [◄ SaveSnapShot](com_savesnapshot.htm) |  | [SaveSymlib ▶](com_savesymlib.htm) |
