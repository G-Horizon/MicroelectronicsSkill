# CompareSymbolLibs Command

Compares two symbol libraries by comparing each symbol in turn. A message will be output for each symbol that is different or is not found in one of the libraries. Symbols are classed as identical if:

1. All graphical elements are identical. Graphical elements are segments and arc segments. (Circles are classed as arc segments)

2. All pins have the same name, location and order

3. All protected properties are identical.

Unprotected properties are not compared. If no differences are found the command will output the message "The symbol files are identical".

```
CompareSymbolLibs [/detail] <file1> <file2>
```

### Parameters

|  |  |
| --- | --- |
| /detail | If specified, a detailed report is given when two symbols do not match. Detail about what doesn't match will be provided. This could be mismatched segments, properties or pins. |
| /difflib | If specified the second library is expected to be a difference library. Symbols not found will not be reported. |
| lib1 | Path of first symbol library file |
| lib2 | Path of second symbol library file |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_comparesymbollibs) | | |
| [◄ CombineMenu](com_combinemenu.htm) |  | [ConvertBinaryGraph ▶](com_convertbinarygraph.htm) |
