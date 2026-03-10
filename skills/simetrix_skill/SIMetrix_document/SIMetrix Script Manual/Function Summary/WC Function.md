# WC Function

Returns a random number with a worst case distribution. This function is intended to be used for SIMPLIS Monte Carlo analyses and would typically be used in device value expressions.

This function is only available in the Simulator process and cannot be called from scripts running in the context of the front end. The function is only active when used by the netlist pre-processor with Monte Carlo analysis enabled. When used in other contexts, the function returns 1.0.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Tolerance |

### Returns

Return type: real

Random number which is either 1.0+tolerance or 1.0-tolerance

### See Also

* [Gauss](func_gauss.htm)
* [GaussTrunc](func_gausstrunc.htm)
* [Distribution](func_distribution.htm)  - also alias  [UD](func_ud.htm)
* [Unif](func_unif.htm)
* [WC2](func_wc2.htm)

### Example

1k\*WC(0.1) will return 900 or 1100 chosen at random. Returns 1000 in a non Monte Carlo run.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_wc) | | |
| [◄ WAV\_WriteFile](func_wav_writefile.htm) |  | [WC2 ▶](func_wc2.htm) |
