# ReadConfigSetting Function

Reads a configuration setting. Configuration settings are stored in the configuration file. See  [User's Manual/Sundry Topics/Configuration Settings](../../user_manual/topics/sundrytopics_configurationsettings.htm)  for more information. Settings are defined by a key-value pair and are arranged into sections. The function takes the name of the key and section and returns the value. Note that option settings (as defined by the Set command) are placed in the 'Options' section. Although these values can be read by this function this is not recommended and instead you should always use the function  [GetOption](func_getoption.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Section |
| 2 | string | No |  | Key |

#### Argument 1

Section name. See description above for explanation.

#### Argument 2

Key name. See description above for explanation.

If this argument is omitted, the function will return a list of all keynames found in the specified section.

### Returns

Return type: string or string array

Value read from configuration file.

### See Also

* [WriteConfigSetting](func_writeconfigsetting.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readconfigsetting) | | |
| [◄ ReadConfigCollection](func_readconfigcollection.htm) |  | [ReadF11Analyses ▶](func_readf11analyses.htm) |
