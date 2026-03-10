# CreateNewTitleBlockDialog Function

Displays the title block creation dialog.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string vector | No |  | Initial display values |

#### Argument 1

Initial display values for the dialog. Each value is in a separate vector element and will start with one of the following prefixes (including the colon ':'):

|  |  |
| --- | --- |
| **Prefix** | **Description** |
| CompanyName: | Company name to appear |
| Title: | Title of the schematic |
| Author: | Author of the schematic |
| Notes: | Notes about the schematic |
| LayoutStyle: | Either 'Horizontal' or 'Vertical'. Vertical mode will not display an image. |
| Logo: | Full path to an image to use. |
| Version: | Schematic version number. Use "<<auto>>" for an automatically assigned version number. |
| Date: | Schematic version date. Use "<<auto>>" for an automatically assigned version number. |

Not all of these values have to be defined. If no values are defined, then the company, author and logo image will attempt to be chosen from option settings.

### Returns

Return type: string array

Title block definition. Values are specified one per vector element and have one of the following prefixes (including the colon ':'):

|  |  |
| --- | --- |
| **Prefix** | **Description** |
| CompanyName: | Company name to appear |
| Title: | Title of the schematic |
| Author: | Author of the schematic |
| Notes: | Notes about the schematic |
| LayoutStyle: | Either 'Horizontal' or 'Vertical'. Vertical mode will not display an image. |
| Logo: | Full path to an image to use. |
| Version: | Schematic version number. Use "<<auto>>" for an automatically assigned version number. |
| Date: | Schematic version date. Use "<<auto>>" for an automatically assigned version number. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_createnewtitleblockdialog) | | |
| [◄ CreateMutex](func_createmutex.htm) |  | [CreateSharedAxisConnector ▶](func_createsharedaxisconnector.htm) |
