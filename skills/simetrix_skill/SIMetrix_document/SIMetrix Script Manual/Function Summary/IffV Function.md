# IffV Function

If the first argument evaluates to TRUE (i.e. non-zero) the function will return the value of argument 2. Otherwise it will return the value of argument 3. Note that the type of arguments 2 and 3 must both be the same. No implicit type conversion will be performed on these arguments.

This function performs the same operation as  [Iff](func_iff.htm)  but also works with vectors whereas Iff only works with scalar values.

All three arguments may be vectors but the lengths must satisfy the following conditions:

Argument 2 (true value) must be the same length as argument 3 (false value) Argument 1 (test) must either be the same length as arguments 2 and 3 or must have a length of 1

If the test has a length greater than 1 then each element of the test is tested to select the corresponding element in the true and false vectors. If the length of the test is 1 then this value is used to select the entire vector - either the true value or false value.

The return value includes the reference value copied from argument 2. To be useful this assumes that the references of arguments 2 and 3 are the same. This would usually be the case in most applications but the function does not test this.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Test |
| 2 | real, complex, string | Yes |  | true value |
| 3 | real, complex, string | Yes |  | false value |

### Returns

Return type: Matches arguments 2 and 3 (must be the same)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_iffv) | | |
| [◄ Iff](func_iff.htm) |  | [IIR ▶](func_iir.htm) |
