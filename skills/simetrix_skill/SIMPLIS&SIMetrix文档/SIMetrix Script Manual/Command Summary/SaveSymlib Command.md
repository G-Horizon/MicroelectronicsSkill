# SaveSymlib Command

Writes the entire global symbol library or a specified installed symbol library file to  *filename* . An append option allows a new symbol library file to be created that consists of multiple libraries combined in one file. This command can also be used to convert symbol libraries from ASCII to XML format and vice-versa.

Use /xml to save in XML format or /ascii to save in ASCII format. If neither is specified, the format used will be determined by the option setting SymbolLibrarySaveFormat. This usualy preserves the original format if appending otherwise uses ASCII format.

```
SaveSymlib [/v25] [/append] [/force] /lib <libname>|/all <filename>
```

### Parameters

|  |  |
| --- | --- |
| /all | Write out all installed symbols. |
| /append | Symbols are appended to  *filename* . Otherwise  *filename*  will be overwritten if it already exists. Note that any symbols written that are already present in  *filename*  will be overwritten. It is not possible to have duplicate symbols within the same library file. |
| /ascii | Force save to ascii file format. |
| /force | Allows symbols to be written to an existing library file. Otherwise if  *filename*  is an existing installed library, the command will abort with an error message. |
| /lib | Name of library file to write out. This must be an installed library. |
| /xml | Force to save in XML format |
| filename | File to receive symbols. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_savesymlib) | | |
| [◄ SaveSymbol](com_savesymbol.htm) |  | [SaveTextEditor ▶](com_savetexteditor.htm) |
