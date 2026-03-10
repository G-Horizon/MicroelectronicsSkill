# OptimiserWidgetPreFlightChecks Function

Check optimiser widget (GUI) data prior to starting an optimiser run. Checks that the configuration is valid. The following checks are made:

|  |
| --- |
| Checks parameter initial values are inside any minimum or maximum values |
| Checks that minimum and maximum values are defined for algorithms that require them |
| Checks that the specified algorithms supports constraints if any are specified |
| Checks that SIMPLIS runs do not specify more than one of each analysis type |
| Checks that a SIMPLIS POP analysis is defined if an AC analysis is also defined |
| Checks that SIMPLIS runs do not define measurement data for POP analyses if tranalso specified |
| Checks that there is one and one only objective function |

### Arguments

No arguments

### Returns

Return type: String error

Two element string array.

|  |  |
| --- | --- |
| 0 | 1: ok to run 0: not Ok to run |
| 1 | Error message |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserwidgetpreflightchecks) | | |
| [◄ OptimiserWidgetGetInfo](func_optimiserwidgetgetinfo.htm) |  | [OptimiserWidgetWriteCommandFile ▶](func_optimiserwidgetwritecommandfile.htm) |
