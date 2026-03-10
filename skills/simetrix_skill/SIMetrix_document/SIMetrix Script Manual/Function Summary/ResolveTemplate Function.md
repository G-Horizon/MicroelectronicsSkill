# ResolveTemplate Function

Evaluate template string.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Template string |
| 2 | string | Yes |  | Property names |
| 3 | string | Yes |  | Property values |
| 4 | string | No | Input template unmodified | Return value for evaluation error |

#### Argument 1

Template string. This can consist of literal text, expressions enclosed in '{' and '}' and special property names enclosed in '%'. The property names and their respective values may be defined in arguments 2 and 3. Properties names are substituted with their values by this function.

The template string may also contain the special keywords `<if>` }, `<ifd>` }, `<t>` } and `<repeat>` }. These behave the same and have identical syntax as the keywords of the same name used for schematic TEMPLATE properties described in the  *User's Manual* .

#### Argument 2

Property names.

#### Argument 3

Property values corresponding to property names given in argument 2.

#### Argument 4

If the template contains an expression encloded in braces and the evaluation of the expression fails, the value defined in this argument is returned by the function

### Returns

Return type: string

Returns the result of evaluating the template.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_resolvetemplate) | | |
| [◄ ResolveGraphTemplate](func_resolvegraphtemplate.htm) |  | [RestartTranDialog ▶](func_restarttrandialog.htm) |
