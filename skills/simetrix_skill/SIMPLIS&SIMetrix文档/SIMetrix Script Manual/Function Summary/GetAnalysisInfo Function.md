# GetAnalysisInfo Function

Returns the parameters of the most recent analysis performed by the simulator. The parameters are returned in the form of a string array. If argument 1 is set to 'name' the function will return the names of each parameter.

The following sample shows how to obtain a the stop time of a transient analysis:

```
let stopIdx = Search(GetAnalysisInfo('name'), 'tstop')
Let stopTime = Val( (GetAnalysisInfo())[stopIdx])
```

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Options |

#### Argument 1

The following table shows the parameter names currently available for each analysis type:

|  |  |
| --- | --- |
| **Analysis Type** | **Parameter Names** |
| Transient | ANALYSISNAME, GROUPNAME, TSTART, TSTOP, TSTEP, TMAX, UIC, DELTA, RTNSTART, RTNSTOP, RTNSTEP, RTNENABLED, FAST |
| AC | ANALYSISNAME, GROUPNAME, PARAM, MODEL, TEMP, FREQ, MONTE, REPEAT, DEVICE, MODE, START, STOP, STEP, NUMSTEPS, GRAD, SINGLE, F |
| DC | ANALYSISNAME, GROUPNAME, PARAM, MODEL, TEMP, FREQ, MONTE, REPEAT, DEVICE, MODE, START, STOP, STEP, NUMSTEPS, GRAD, SINGLE |
| Noise | ANALYSISNAME, GROUPNAME, PARAM, MODEL, TEMP, FREQ, MONTE, REPEAT, DEVICE, MODE, START, STOP, STEP, NUMSTEPS, GRAD, SINGLE, V, VN, INSRC, PTSPERSUM, F |
| Transfer | Function ANALYSISNAME, GROUPNAME, PARAM, MODEL, TEMP, FREQ, MONTE, REPEAT, DEVICE, MODE, START, STOP, STEP, NUMSTEPS, GRAD, SINGLE, V, VN, I, INSRC, F, IMODE |
| Sensitivity | ANALYSISNAME, GROUPNAME, POSNAME, NEGNAME, I, GRAD, START, STOP, NUMSTEPS |
| Operating point | ANALYSISNAME, GROUPNAME |

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getanalysisinfo) | | |
| [◄ GetAllYAxes](func_getallyaxes.htm) |  | [GetAnalysisLines ▶](func_getanalysislines.htm) |
