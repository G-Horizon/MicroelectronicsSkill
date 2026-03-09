# WriteConfigSetting Function

Writes a configuration setting. Configuration settings are stored in the configuration file. See  [User's Manual/Sundry Topics/Configuration Settings](../../user_manual/topics/sundrytopics_configurationsettings.htm)  for more information. Settings are defined by a key-value pair and are arranged into sections. The function writes the value in argument three to the specified key and section. If the value is missing, the setting will be deleted.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Section |
| 2 | string | Yes |  | Key |
| 3 | string | No |  | Value |

#### Argument 1

Section name

#### Argument 2

Key name

#### Argument 3

Value to set. Setting will be deleted if this is omitted.

### Returns

Return type: real

### See Also

* [ReadConfigSetting](func_readconfigsetting.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_writeconfigsetting) | | |
| [◄ WM\_NumberSystemWidgets](func_wm_numbersystemwidgets.htm) |  | [WriteF11Lines ▶](func_writef11lines.htm) |
