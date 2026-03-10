# EditSimplisMosfetDriverDialog Function

Opens a specialized dialog used to edit the parameters for a SIMPLIS multi-Level MOSFET Driver. See internal script  *simplis\_edit\_mosfet\_driver*  for an application example of this function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | No |  | Initial values |
| 2 | string array | No |  | Caption, combo options, Help context id |

#### Argument 1

String array providing initial values for the various controls. The order is:

|  |  |  |  |
| --- | --- | --- | --- |
| **Index** | **Purpose** | **Notes** | **Default** |
| 0 | LEVEL | The model level | 1 |
| 1 | INVERTING | Inverting flag | 0 |
| 2 | USE\_DELAY | Delay flag | 1 |
| 3 | THRESHOLD | The input threshold | 2.5 |
| 4 | HYSTWD | The input hysteresis | 1.0 |
| 5 | RISE\_DELAY | The rising edge delay | 15n |
| 6 | FALL\_DELAY | The falling edge delay | 10n |
| 7 | HS\_RDSON | The upper switch RDS(on) for Level 0 and 1 models | 1 |
| 8 | HS\_RSAT | The upper switch saturation resistance for Level 0 and 1 models | 10Meg |
| 9 | HS\_ISAT | The upper switch saturation current for Level 0 and 1 models | 2 |
| 10 | LS\_RDSON | The lower switch RDS(on) for Level 0 and 1 models | 1 |
| 11 | LS\_RSAT | The lower switch saturation resistance for Level 0 and 1 models | 10Meg |
| 12 | LS\_ISAT | The lower switch saturation current for Level 0 and 1 models | 3 |
| 13 | IC | The initial condition of the upper switch. | <<empty>> |
| 14 | HS\_ROFF | The upper switch off resistance for Level 0 and 1 models | 10Meg |
| 15 | LS\_ROFF | The lower switch off resistance for Level 0 and 1 models | 10Meg |
| 16 | HS\_VON | The upper switch on-state voltage | 0 |
| 17 | LS\_VON | The lower switch on-state voltage | 0 |
| 18 | HS\_RDSON\_L2 | The upper switch RDS(on) for Level 2 models | 10 |
| 19 | HS\_R2\_L2 | The upper switch resistance for the second PWL segment | 500m |
| 20 | HS\_RSAT\_L2 | The upper switch saturation current for Level 2 models | 10Meg |
| 21 | HS\_V1\_L2 | The voltage where the upper switch transitions from the 1st to 2nd PWL segments | 500m |
| 22 | HS\_ISAT\_L2 | The upper switch saturation current for Level 2 models | 1 |
| 23 | LS\_RDSON\_L2 | The lower switch RDS(on) for Level 2 models | 10 |
| 24 | LS\_R2\_L2 | The lower switch resistance for the second PWL segment | 500m |
| 25 | LS\_RSAT\_L2 | The lower switch saturation current for Level 2 models | 10Meg |
| 26 | LS\_V1\_L2 | The voltage where the lower switch transitions from the 1st to 2nd PWL segments | 100m |
| 27 | LS\_ISAT\_L2 | The lower switch saturation current for Level 2 models | 3 |

#### Argument 2

|  |  |  |  |
| --- | --- | --- | --- |
| **Index** | **Purpose** | **Notes** | **Default** |
| 0 | Caption | The dialog box caption | "Edit Multi-Level MOSFET Driver" |
| 1 | Combo options | Combo items for the initial conditions box. | <<empty>> |
| 2 | Help context id | The help context id, used for the built-in Multi-Level MOSFET Driver. | <<empty>> |

### Returns

Return type: string array

String array corresponding exactly to argument 1 and holding the user's selected values. Return value will be empty if the user cancels the box.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editsimplismosfetdriverdialog) | | |
| [◄ EditSimplisLaplaceFilterDialog](func_editsimplislaplacefilterdialog.htm) |  | [EditStylesDialog ▶](func_editstylesdialog.htm) |
