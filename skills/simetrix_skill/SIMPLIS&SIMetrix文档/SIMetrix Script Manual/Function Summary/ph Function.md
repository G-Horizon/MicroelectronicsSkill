# ph Function

Returns the phase of the argument in degrees.

Each of the functions ph,  [phase](func_phase.htm)  and  [phase\_rad](func_phase_rad.htm)  produce a continuous output i.e. it does not wrap from 180 degrees to -180 degrees. The  [arg](func_arg.htm)  function may be used to obtain a phase value that is always between +/- 180 degrees.

This function always returns a result in degrees. This has changed from versions 3.1 and earlier which returned in degrees or radians depending on the setting of the 'Degrees' option. For phase in radians, use  [phase\_rad](func_phase_rad.htm)  ().

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real/complex array | Yes |  | vector |

### Returns

Return type: real array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_ph) | | |
| [◄ PerCycleValue](func_percyclevalue.htm) |  | [phase ▶](func_phase.htm) |
