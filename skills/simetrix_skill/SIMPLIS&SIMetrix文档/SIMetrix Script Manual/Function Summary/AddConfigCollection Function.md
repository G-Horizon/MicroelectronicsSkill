# AddConfigCollection Function

Adds a list of entries to a named section in the configuration file.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Section name |
| 2 | string array | Yes |  | List of entries |
| 3 | string | No |  | Options |

#### Argument 1

Section name in configuration file where entries are to be added. The configuration file is where SIMetrix stores its settings. See the User's Manual chapter 13 for more information.

#### Argument 2

List of entries to be added. Note that duplicates are not permitted and any entered will be ignored.

#### Argument 3

Set to 'nonpath' if the values being stored are not path names. Set to 'uselogicalpaths' if the values being stored are pathnames and they should be stored using logical symbols if possible.

### Returns

Return type: real

The number of new entries successfully added is returned. This will may be less than the number of entries supplied to argument 2 if any are already entered or if their are duplicates in the list supplied.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_addconfigcollection) | | |
| [◄ ACSourceDialogStr](func_acsourcedialogstr.htm) |  | [AddGraphCrossHair ▶](func_addgraphcrosshair.htm) |
