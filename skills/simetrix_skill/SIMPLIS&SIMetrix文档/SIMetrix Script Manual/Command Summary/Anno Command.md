# Anno Command

Automatically allocates unique component references to all components on currently selected schematic.

Typically Anno is used prior to running the Netlist command. The latter requires unique references to function.

Note that Anno will not allocate a new reference to a component unless it is necessary to do so to avoid a duplication. When there is a duplication, the component which was most recently added to the schematic will be modified.

```
Anno [/prop property_name] [/nopaint ] [/bypos] [/minSuffix min_suffix]
```

### Parameters

|  |  |
| --- | --- |
| /bypos | If specified, all references will be reassigned according to their position on the schematic working left to right. Unlike /minSuffix this switch does reassign all references. It can be used with /minSuffix to reassign all references in a schematic according to a desired specification. |
| /minSuffix | Minimum suffix value that will be used for new references. The anno command works by locating duplicate references then searching for the first suffix value that resolves the duplicate. The minSuffix switch specifies the lowest value that will be used. So if set to 100 for example, the lowest resistor reference would be R100. Note that this will not force existing references to be updated to values greater than  *min-suffix* . Only values that need changing will be affected. |
| /nopaint | The anno command always forces the schematic window to refresh if any changes to properties were made. This action is inhibited if this switch is specified. This is usually used if the property being annotated is hidden and therefore will cause no visual change. |
| /prop | If specified, annotates properties of name  *property-name* . Otherwise properties of name "ref" are annotated. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_anno) | | |
| [◄ AlignText](com_aligntext.htm) |  | [AppendGroup ▶](com_appendgroup.htm) |
