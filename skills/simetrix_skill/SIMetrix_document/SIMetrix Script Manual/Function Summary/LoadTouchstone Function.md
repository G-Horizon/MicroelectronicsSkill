# LoadTouchstone Function

Loads a Touchstone network parameter file and converts it to Y-parameter values.

LoadTouchstone returns an ID for subsequent access to the data in the file or error messages if the load failed.

If the load was successful, use the function  [ReadTouchstone](func_readtouchstone.htm)  to read its data. If unsuccessful, error messages may be read using  [GetTouchstoneErrors](func_gettouchstoneerrors.htm) .

Use  [DeleteTouchstone](func_deletetouchstone.htm)  to delete the data loaded by LoadTouchstone.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Filename |
| 2 | Real | Yes |  | Order of network |

#### Argument 1

Path to Touchstone file

#### Argument 2

Order of network, that is the number of ports

### Returns

Return type: Real array

Two field real array. First field is an integer ID than can be used for functions  [ReadTouchstone](func_readtouchstone.htm)  ,. Second field is 1 if the file was successfully read, otherwise 0.

### Notes

Currently only 1 and 2 port s-parameter data and y-parameter data of any size is accepted. The data is returned as y-parameter values.

### See Also

* [ReadTouchstone](func_readtouchstone.htm)
* [GetTouchstoneErrors](func_gettouchstoneerrors.htm)
* [DeleteTouchstone](func_deletetouchstone.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_loadtouchstone) | | |
| [◄ LoadSensitivityReport](func_loadsensitivityreport.htm) |  | [Locate ▶](func_locate.htm) |
