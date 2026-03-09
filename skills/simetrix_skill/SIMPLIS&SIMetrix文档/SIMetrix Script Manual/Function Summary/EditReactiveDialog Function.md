# EditReactiveDialog Function

Opens a dialog box designed to edit inductors and capacitors.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Initial values |
| 2 | string | Yes |  | Options |
| 3 | string | No |  | Parameter names |
| 4 | string | No |  | Parameter values |

#### Argument 1

First element is the initial value of device. Second element is the initial condition.

#### Argument 2

Three element string array. Each field has the meaning defined in the following table:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Caption for value group box |
| 1 | Initial range. Possible values: 'E6', 'E12', 'E24' |
| 2 | Type of device. Possible values: 'capacitor', 'inductor'. This controls the Initial condition group box design |
| 3 | Initial condition enabled for operating point check box. ('true' or 'false') |
| 4 | Initial condition enabled fro transient check box. ('true' or 'false') |
| 5 | Initial condition enabled for AC check box. ('true' or 'false') |
| 6 | Initial condition enabled for DC check box. ('true' or 'false') |

#### Argument 3

String array defining list of parameter names. See argument 4.

#### Argument 4

String array defining list of parameter values. If arguments 3 and 4 are supplied the Parameters... button will be visible. This button opens another dialog box that provides the facility to edit these parameters' values.

### Returns

Return type: string array

The function returns a string array in the following form:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Value in Result box |
| 1 | Value in Initial Voltage or Initial Current box. Empty if Open circuit or Short circuit is selected |
| 2 | Number of parameter values. |
| 3 | onwards The values of the parameters in the order they were passed. |
| number of parameters +3 | Initial condition enabled for operating point check box ('true' or 'false') |
| number of parameters +4 | Initial condition enabled fro transient check box ('true' or 'false') |
| number of parameters +5 | Initial condition enabled for AC check box. ('true' or 'false') |
| number of parameters +6 | Initial condition enabled for DC check box. ('true' or 'false') |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editreactivedialog) | | |
| [◄ EditPropertyDialog](func_editpropertydialog.htm) |  | [EditSelect ▶](func_editselect.htm) |
