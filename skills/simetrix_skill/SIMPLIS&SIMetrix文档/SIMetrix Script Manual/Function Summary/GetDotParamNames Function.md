# GetDotParamNames Function

Returns names of variables defined using .PARAM in the most recent simulation run.

### Arguments

No arguments

### Returns

Return type: string array

String array with names of variables. If no simulation has been run, an empty result will be returned. Note that real values in the front end's global group are passed to the simulator and entered as .PARAM values. So this function will always return those values. In addition the values 'PLANCK', 'BOLTZ' and 'ECHARGE' are always defined.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getdotparamnames) | | |
| [◄ GetDivisionLabels](func_getdivisionlabels.htm) |  | [GetDotParamValue ▶](func_getdotparamvalue.htm) |
