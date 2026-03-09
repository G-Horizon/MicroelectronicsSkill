# PutEnvVar Function

Write a system environment variable. Note that this only modifies environment variables in the current process and any child processes initiated using the commands  [Shell](com_shell.htm)  or  [ShellOld](com_shellold.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Definition |

#### Argument 1

Definition. Must be of form `name=value`.

### Returns

Return type: real

The function returns 1 on success or 0 on failure. Failure can occur if the argument is of the wrong format.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_putenvvar) | | |
| [◄ PropValuesWires](func_propvalueswires.htm) |  | [PWLCurveFit ▶](func_pwlcurvefit.htm) |
