# Unif Function

Returns a random number with a uniform distribution. This function is intended to be used for SIMPLIS Monte Carlo analyses and would typically be used in device value expressions.

This function is only available in the Simulator process and cannot be called from scripts running in the context of the front end. The function is only active when used by the netlist pre-processor with Monte Carlo analysis enabled. When used in other contexts, the function returns 1.0.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Tolerance |

### Returns

Return type: real

Random number with a uniform distribution between 1.0-tolerance and 1.0+tolerance.

Returns 1.0 when used in non Monte Carlo contexts.

### Notes

### See Also

* [Gauss](func_gauss.htm)
* [GaussTrunc](func_gausstrunc.htm)
* [Distribution](func_distribution.htm)  - also alias  [UD](func_ud.htm)
* [WC](func_wc.htm)
* [WC2](func_wc2.htm)

### Example

1k\*Unif(0.1) will return 1000 +/- 10% with uniform probability distribution. Returns 1.0 in a non Monte Carlo run.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_unif) | | |
| [◄ UngroupCurve](func_ungroupcurve.htm) |  | [Units ▶](func_units.htm) |
