# Gauss Function

Returns a random number with a Gaussian distribution. This function is intended to be used for SIMPLIS Monte Carlo analyses and would typically be used in device value expressions.

This function is only available in the Simulator process and cannot be called from scripts running in the context of the front end. The function is only active when used by the netlist pre-processor with Monte Carlo analysis enabled. When used in other contexts, the function returns 1.0.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Tolerance - 3-sigma spread |

### Returns

Return type: real

Random number with a Gaussian distribution of mean 1.0 and standard deviation of tolerance/3 where tolerance is the value supplied to argument 1.

Returns 1.0 when used in non Monte Carlo contexts.

### Notes

The function can return values outside the tolerance range. For example Gauss(0.1) can return values greater than 1.1 and less than 0.9 which would violate the tolerance specification for many components. Use the  [GaussTrunc](func_gausstrunc.htm)  function to get a distribution that does not extend beyond the tolerance range.

### See Also

* [Unif](func_unif.htm)
* [GaussTrunc](func_gausstrunc.htm)
* [Distribution](func_distribution.htm)  - also alias  [UD](func_ud.htm)
* [WC](func_wc.htm)
* [WC2](func_wc2.htm)

### Example

1k\*Gauss(0.1) will return 1000 +/- 10% with a 3-sigma spread. Returns 1.0 in a non Monte Carlo run.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_gauss) | | |
| [◄ gamma](func_gamma.htm) |  | [GaussLim ▶](func_gausslim.htm) |
