# GetFirstSelectedElementOfType Function

Returns handle of first selected schematic element of the requested type or types.

If mulitple types are given, a search will be conducted on each type in turn, until a selected element of one of the requesting types is found. Only one handle is returned and this is the first element that the search comes across that is selected and is of the type requested.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Element type or types |

#### Argument 1

Either a single element type, or an array of different types. If several types are provided, it will search for a selected element of the different types in order, meaning that if there is a match for the first array index, any subsequent indexes will not be searched.

Available elements types are:

* ArrowAnnotation
* ImageAnnotation
* Instance
* LineAnnotation
* ShapeAnnotation
* TextAnnotation
* TitleBlock
* Wire

### Returns

Return type: string

Handle of the first selected element of the type requested, or an empty string if no matching elements were found.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getfirstselectedelementoftype) | | |
| [◄ GetFileViewerSelectedFiles](func_getfileviewerselectedfiles.htm) |  | [GetFonts ▶](func_getfonts.htm) |
