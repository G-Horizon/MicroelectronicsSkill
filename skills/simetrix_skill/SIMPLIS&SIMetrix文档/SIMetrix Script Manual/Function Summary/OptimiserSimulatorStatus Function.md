# OptimiserSimulatorStatus Function

Returns current status of the simulator's optimiser as a string

### Arguments

No arguments

### Returns

Return type: String array

Two element array. First element:

|  |  |
| --- | --- |
| success | Optimiser has completed successfully |
| notstarted | Optimiser has not been started |
| running | Optimiser is running |
| failed | Optimiser failed |
| unknown | Unknown status |

Second element returns one of the following codes which provides more detail:

|  |  |
| --- | --- |
| not\_started | Optimiser not started |
| running | Optimiser running |
| success | Optimiser completed successfully. This is not usually returned, instead one of the reasons for the optimiser completing will be returned instead |
| stopvalreached | Optimiser objective function reached its stop value |
| ftolreached | Optimiser objective function converged |
| xtolreached | [Future use] Optimiser parameter values converged |
| maxitersreached | Optimiser iteration count reached upper limit |
| maxtimereached | [Future use] Optimiser execution time reached upper limit |
| failed | Optimiser failed |
| invalidargs | [Internal error] Arguments to optimiser invalid |
| outofmemory | Optimiser out of memory |
| roundofflimited | Optimiser reached accuracy limit |
| forcedstop | Optimiser forced stop |
| convergencefail | Simulator convergence failed |
| simulationfailed | Other simulator failure |
| measurementfailed | Measurement evaluation failed |
| userrequest | User requested optimiser analysis abort |
| unknown | Uknown error |
| invalid | No simulator optimiser available |

### See Also

* [OptimiserStatus](func_optimiserstatus.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisersimulatorstatus) | | |
| [◄ OptimiserSimulatorResults](func_optimisersimulatorresults.htm) |  | [OptimiserSimulatorUserMessage ▶](func_optimisersimulatorusermessage.htm) |
