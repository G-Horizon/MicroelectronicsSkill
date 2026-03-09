# GaussTrunc Function

Returns a random number with a Gaussian distribution but truncated so that it won't return values outside the specified tolerance range. This function is intended to be used for SIMPLIS Monte Carlo analyses and would typically be used in device value expressions.

This function is only available in the Simulator process and cannot be called from scripts running in the context of the front end. The function is only active when used by the netlist pre-processor with Monte Carlo analysis enabled. When used in other contexts, the function returns 1.0.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Tolerance |
| 2 | real | No | 3 | sigma multiplier |

### Returns

Return type: real

Random number with a Gaussian distribution of mean 1.0 and standard deviation of (tolerance/sigma\_multiplier) where tolerance is the value supplied to argument 1 and sigma\_multiplier is the argument provided to argument 2. Values outside the range 1.0 +/-tolerance are rejected so the function will never return values outside this range

### See Also

* [Gauss](func_gauss.htm)
* [Unif](func_unif.htm)
* [Distribution](func_distribution.htm)  - also alias  [UD](func_ud.htm)
* [WC](func_wc.htm)

### Example

1k\*GaussTrunc(0.1) will return 1000 +/- 10% with a 3-sigma spread. Will not return values outside the range 0.9-1.1. Returns 1.0 in a non Monte Carlo run.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_gausstrunc) | | |
| [◄ GaussLim](func_gausslim.htm) |  | [GenPrintDialog ▶](func_genprintdialog.htm) |
