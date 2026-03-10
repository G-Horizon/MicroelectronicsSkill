# ReadF11Analyses Function

Reads SIMetrix simulator analysis specifications in the schematic F11 window and returns a string array describing parameters for a specified analysis type

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Analysis type |

#### Argument 1

Define the type of analysis to be returned. Maybe one of the following string values

|  |  |
| --- | --- |
| AC | AC analysis |
| DC | DC analysis |
| NOISE | Noise analysis |
| TF | Transfer function analysis |
| TRAN | Transient analysis |
| ACMULTISTEP | AC multistep analysis |
| DCMULTISTEP | DC multistep analysis |
| NOISEMULTISTEP | Noise multistep analysis |
| TFMULTISTEP | Transfer function multistep analysis |
| TRANMULTISTEP | Transient multistep analysis |

### Returns

Return type: string array

Three element string array.

|  |  |
| --- | --- |
| 0 | Indicates whether analysis type is defined |
|  | '0': not defined, '1': defined |
| 1 | Indicates whether analysis type is enabled |
|  | '0': not enabled, '1': enabled |
|  | Disabled analysis definitions are prefixed with a single '\*' |
| 2 | List of name=value pairs describing various analysis parameters |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readf11analyses) | | |
| [◄ ReadConfigSetting](func_readconfigsetting.htm) |  | [ReadF11Options ▶](func_readf11options.htm) |
