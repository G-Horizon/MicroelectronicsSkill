# IsOptionMigrateable Function

Determines if an option variable may be migrated in a version upgrade.

This function is used in the script that is run when SIMetrix is started for the first time. Certain option variables (defined using the command  [Set](com_set.htm)  ) are marked internally as 'migrateable' meaning that their values are transferred to a new version installation if the user requests that configuration settings are to be migrated.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Option name |

### Returns

Return type: real

Return 1.0 if the option name is migrateable otherwise returns 0.0.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_isoptionmigrateable) | | |
| [◄ IsNum](func_isnum.htm) |  | [IsSameFile ▶](func_issamefile.htm) |
