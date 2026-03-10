# EditDeviceDialog Function

Opens a dialog box used to select a device and optionally specify its parameters.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | options/initial settings |
| 2 | string array | Yes |  | devices |
| 3 | string array | No | <<empty>> | parameter names |
| 4 | string array | No | <<empty>> | parameter values |

#### Argument 1

Defines options and initial settings as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Text entered in edit control above list box. If the text item is also present in the device list (argument 2), then that item will be selected. |
| 1 | Ignored unless element 1 is empty. Integer (entered in string form) which defines selected device. |
| 2 | Dialog box caption. Default if omitted: "Select Device" |
| 3 | Message at the top of the dialog box. . Default if omitted: "Select Device" |

#### Argument 2

String array defining the list of devices.

#### Argument 3

String array defining list of parameter names. See argument 4.

#### Argument 4

String array defining list of parameter values. If arguments 3 and 4 are supplied the "Parameters..." button will be visible. This button opens another dialog box that provides the facility to edit these parameters' values.

### Returns

Return type: string array

If the user selects Cancel the function returns an empty vector, otherwise returns a string array.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Entry in the text edit box. |
| 1 | Index into device list (argument 2) of device in text edit box. If this device is not in the list, -1 will be returned. |
| 2 | Number of parameter values. |
| 3 | (Onwards) The values of the parameters in the order they were passed. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editdevicedialog) | | |
| [◄ EditCurveMarkerDialog](func_editcurvemarkerdialog.htm) |  | [EditDigInitDialog ▶](func_editdiginitdialog.htm) |
