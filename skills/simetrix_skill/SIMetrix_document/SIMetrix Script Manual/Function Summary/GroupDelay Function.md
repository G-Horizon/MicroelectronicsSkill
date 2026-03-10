# GroupDelay Function

Returns the group delay of the argument. Group delay is defined as:

\[ \frac{d}{dx}\left(\text{phase}\left(y\right)\right)\cdot \frac{1}{2\pi} \]

where ???MATH???y???MATH??? is the supplied vector and ???MATH???x???MATH??? is its reference. The GroupDelay function expects the result of an AC analysis where ???MATH???y???MATH??? is a voltage or current and its reference is frequency.

This function will yield an error if its argument is complex and has no reference.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real/complex array | Yes |  | Vector |

### Returns

Return type: real array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_groupdelay) | | |
| [◄ GraphLimits](func_graphlimits.htm) |  | [Groups ▶](func_groups.htm) |
