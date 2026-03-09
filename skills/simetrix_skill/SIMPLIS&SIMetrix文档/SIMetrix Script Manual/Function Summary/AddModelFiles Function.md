# AddModelFiles Function

Installs a list of new models to the model library. Models may be either single files or wildcard specifications. Duplicates will be ignored

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Model path names |

#### Argument 1

String array containing library specifications to be added. A library specification can either be a single file or a wildcard definition, e.g. path???MATH???\backslash???MATH???\*.lb

### Returns

Return type: real

Number of models actually installed. This may be less than the number supplied if any are already installed

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_addmodelfiles) | | |
| [◄ AddGraphCrossHair](func_addgraphcrosshair.htm) |  | [AddPropertyDialog ▶](func_addpropertydialog.htm) |
