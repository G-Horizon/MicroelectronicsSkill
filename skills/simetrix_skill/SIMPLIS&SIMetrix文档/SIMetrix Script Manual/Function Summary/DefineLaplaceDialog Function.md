# DefineLaplaceDialog Function

Opens a dialog box to define a Laplace transfer function. This is used to interface to the simulator devices s\_xfer and Laplace. The former implements a Laplace transfer function using a network of integrators while the latter uses frequency-time domain conversion by convolution. This dialog box provides a unified user interface to both devices.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Initial settings |
| 2 | string array | No |  | Layout options |

#### Argument 1

The argument is a string array of length 14 that defines the initial settings. The meaning of each element is as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Laplace expression. (contents of "Define output using s variable" box) |
| 1 | Device type: |  |  | | --- | --- | | 0 | Transfer function | | 1 | Impedance - V/I | | 2 | Admittance - I/V | |
| 2 | Input type: |  |  | | --- | --- | | 0 | Single ended voltage | | 1 | Single ended current | | 2 | Differential voltage | | 3 | Differential current | |
| 3 | Output type: |  |  | | --- | --- | | 0 | Single ended voltage | | 1 | Single ended current | | 2 | Differential voltage | | 3 | Differential current | |
| 4 | Frequency scale factor |
| 5 | Method: 0 Lumped network, 1 Convolution |
| 6 | Convolution size: Size of convolution as power of 2. Value from 9 to 30. Dialog will limit maximum value according to available memory |
| 7 | Enable error control: 0 Error control disabled, 1 Error control enabled |
| 8 | Relative tolerance |
| 9 | Absolute tolerance |
| 10 | Impulse extraction method: |  |  | | --- | --- | | 0 | Try all methods | | 1 | Analytic | | 2 | Inverse FFT | | 3 | Stehfest | |
| 11 | Inverse FFT size as power of 2. . Value from 9 to 32. Dialog will limit maximum value according to available memory |
| 12 | Additional Delay |
| 13 | Enable diagnostics |

#### Argument 2

Options for setting layout. Set to 'allowconvolution' to enable the advanced features relating to convolution method. If this option is not provided, a simplified version of the dialog will be displayed that allows only lumped network definitions to be entered

### Returns

Return type: string array

The function returns a string array of length 14 with the same format as the argument described above. If the user selects "Cancel" the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definelaplacedialog) | | |
| [◄ DefineIdealTxDialog](func_defineidealtxdialog.htm) |  | [DefineLogicGateDialog ▶](func_definelogicgatedialog.htm) |
