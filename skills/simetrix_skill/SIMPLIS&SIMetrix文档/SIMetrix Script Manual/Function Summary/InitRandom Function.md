# InitRandom Function

Initialises the random number generator used for SIMPLIS Monte Carlo distribution functions.

A seed value can be specified allowing the generator to be reset to a known state. This will allow a Monte Carlo run to be repeated to give identical results.

This function resets the random number generator used for functions  [Unif](func_unif.htm)  ,  [Gauss](func_gauss.htm)  ,  [GaussTrunc](func_gausstrunc.htm)  ,  [GaussLim](func_gausslim.htm)  ,  [Distribution](func_distribution.htm)  ,  [UD](func_ud.htm)  and  [WC](func_wc.htm) . These functions can only be used for evaluating expressions in a netlist processed by the pre-processor. This applies to value expressions used for components in SIMPLIS simulations.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | seed randomly generated | seed value |

### Returns

Return type: real

seed used to initialise generator

### Example

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_initrandom) | | |
| [◄ imag](func_imag.htm) |  | [InputGraph ▶](func_inputgraph.htm) |
