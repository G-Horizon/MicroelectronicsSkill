# Branch Function

Returns the  *branch current formula*  for the wire nearest the cursor on the selected schematic. This function will only return a result after the circuit has been netlisted.

The branch current formula is an expression that when evaluated yields the current flowing in the wire. The polarity of the result assumes current flows from right to left and top to bottom. An empty string will be returned if there is more than one path for current to flow or if the wire is dangling.

### Arguments

No arguments

### Returns

Return type: string

### See Also

* [NearestInst](func_nearestinst.htm)
* [NetName](func_netname.htm)
* [PinName](func_pinname.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_branch) | | |
| [◄ BoolSelect](func_boolselect.htm) |  | [BuildMclogHTML ▶](func_buildmcloghtml.htm) |
