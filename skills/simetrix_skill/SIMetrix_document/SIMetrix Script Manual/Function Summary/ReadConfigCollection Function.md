# ReadConfigCollection Function

Returns the contents of an entire section in the configuration file. Note that only the values are returned, not the names of the keys. To get the names of the keys, use the function  [ReadConfigSetting](func_readconfigsetting.htm)  with an empty second argument.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Section |

#### Argument 1

Name of section to return.

### Returns

Return type: string array

An array of strings holding the values for every entry in the specified section. Note that the key names are not returned. This function is intended to be used for managing lists of values identified by their section name. Use the function  [AddConfigCollection](func_addconfigcollection.htm)  to write values to the list.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readconfigcollection) | | |
| [◄ ReadClipboard](func_readclipboard.htm) |  | [ReadConfigSetting ▶](func_readconfigsetting.htm) |
