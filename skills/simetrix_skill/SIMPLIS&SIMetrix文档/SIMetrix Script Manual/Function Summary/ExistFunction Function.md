# ExistFunction Function

Returns TRUE or FALSE depending on whether specified function exists.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Function name |
| 2 | string | No | 'global' | Function type |

#### Argument 1

Function name.

#### Argument 2

Either 'global' or 'script'. If 'global', arg 1 is assumed to be the name of a built in function. If 'script' arg 1 is assumed to be a function defined as a script and installed using the command  [RegisterUserFunction](com_registeruserfunction.htm) .

User defined compiled functions linked in as a DLL are treated as 'global'.

### Returns

Return type: real

### Notes

There are two situations where a documented function may not be available:

* The function is not implemented in the currently executing version of the application.
* The function is not enabled with the current license. A few functions are 'licensed' and are not available with all products.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_existfunction) | | |
| [◄ ExistFile](func_existfile.htm) |  | [ExistSymbol ▶](func_existsymbol.htm) |
