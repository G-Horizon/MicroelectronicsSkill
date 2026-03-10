# Inst Command

Places an instance of  *symbolname*  onto the current schematic. User must press left mouse key to fix the symbol to the schematic.

```
Inst [/centre] [/select] [/repeat] [/norepeat] [/repeatalways] [/loc <x> <y> <orient>] [/orient] [/comp] [/nolocal] [/useph] <symbolname> [propname] [propvalue]
```

### Parameters

|  |  |
| --- | --- |
| /centre | If specified the cursor will be positioned in the centre of the selected schematic window. Otherwise the cursor will remain at whatever position it happens to occupy when the command is executed. |
| /comp | Places a component symbol whose path is specified by  *symbolname* . |
| /fast | (Unsupported) Disables operations that are time consuming. Intended to be used when large numbers of instances are placed using a script. After completion, must call Anno followed by a refresh operation such as "Zoom full" |
| /loc | If specified, instance is placed directly on sheet without user interaction at the location specified by  *x*  and  *y*  and orientation specified by  *orient* . These values are relative. The origin of the schematic is not fixed. Usually the values used would have been returned from a call to the function  [InstPoints](func_instpoints.htm) . |
| /nolocal | Only effective if `/comp` also specified. Forces reloading of the component symbol from the original file instead of using a local cached copy. This may be different if the source file has changed. |
| /norepeat | If specified a single instance will be placed regardless of the value of the 'RepeatPlace' global option. |
| /orient | Specifies orientation of symbol. Value from 0 - 7 as illustrated below. |
| /repeat | If specified the instantiation is repetitive. This means that once one instance has been placed, another will be presented. This continues until the user presses the right mouse key. This switch will be ignored if the RepeatPlace option is set to 'Never' (Placement options set to 'Never' in schematic sheet of options dialog). If RepeatPlace is set to 'Always', the repeat action will be enabled even if this switch is not present as long as `/norepeat` isn't present. If the `/loc` switch is present repeat action is disabled in all circumstances. |
| /repeatalways | If specified, instance is placed directly on sheet without user interaction at the location specified by  *x*  and  *y*  and orientation specified by  *orient* . These values are relative. The origin of the schematic is not fixed. Usually the values used would have been returned from a call to the function  [InstPoints](func_instpoints.htm) . |
| /select | If specified, the instance is selected after being placed on the schematic. |
| /useph | Only effective if `/comp` also specified. Will place a place holder symbol if the component symbol specified is not found. Without this switch an error message will be displayed if a component symbol is missing. |
| symbolname | Name of symbol. Symbol names "caption" and "free\_text" are treated specially. See notes. |
| propname | If specified, property of this name is changed to  *propvalue* . |
| propvalue | See above. |

### Notes

The symbol name 'caption' will instantiate the built-in caption annotation object and not a symbol called 'caption'. Similarly the symbol name 'free\_text' will instantiate the built-in free text annotation object. In both cases the text displayed will be the property value given. The property name will be ignored. If no property value is provided, the default values "Caption" and "Text" will be used respectively.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_inst) | | |
| [◄ ImportSymbol](com_importsymbol.htm) |  | [KeepGroup ▶](com_keepgroup.htm) |
