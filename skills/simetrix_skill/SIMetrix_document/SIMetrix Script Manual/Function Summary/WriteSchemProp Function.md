# WriteSchemProp Function

Writes a schematic window property. If argument 3 is set to 'Create' the function will create the property if it doesn't already exist, otherwise the function can only change the value of an existing property. There are three writeable properties that are built-in, namely 'RootPath', 'Reference' and 'UserStatus'. See the function  [ReadSchemProp](func_readschemprop.htm)  for details.

Schematic window properties may be written to the schematic file so that they become persistent. Specify 'Save' for argument 3 to enable saving to the schematic file.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name |
| 2 | string | Yes |  | Propert value |
| 3 | string array | No |  | Options |
| 4 | number | No |  | Handle |

#### Argument 3

Legal values: 'Create', 'Save'. Note that 'Save' does not imply 'Create'. Both need to be specified to create a saveable property, i.e. ['create', 'save']

#### Argument 4

Handle to a schematic.

### Returns

Return type: real

The function returns an integer that indicates the success of the operation as follows:

|  |  |
| --- | --- |
| -1 | No schematic windows open |
| 0 | Success |
| 1 | Property does not exist and 'Create' not specified |
| 2 | Property is read only. (e.g. the 'Path' property) |
| 3 | Property successfully created |

### Example

To create a new persistent property: Let WriteSchemProp('myproperty', 'somevalue', ['Create', 'Save'])

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_writeschemprop) | | |
| [◄ WriteRegSetting](func_writeregsetting.htm) |  | [XCursor ▶](func_xcursor.htm) |
