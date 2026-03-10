# GetNextDefaultStyleName Function

Returns next fully available default style name. This is used when creating new styles with a default name, where an index increments for additional styles created.

Names are in the form: MyStyleNormal[index] and MyStyleSelected[index], eg MyStyleNormal10. Returns a name that will be valid for both the normal style and the selected style.

### Arguments

No arguments

### Returns

Return type: string

Next available style name that is not being used elsewhere, which can be used to create Normal and Selected variants of it.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getnextdefaultstylename) | | |
| [◄ GetNearestNet](func_getnearestnet.htm) |  | [GetNodeConvergenceInfo ▶](func_getnodeconvergenceinfo.htm) |
