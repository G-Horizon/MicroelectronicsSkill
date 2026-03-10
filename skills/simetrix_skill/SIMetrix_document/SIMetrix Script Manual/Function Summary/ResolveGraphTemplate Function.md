# ResolveGraphTemplate Function

Evaluate template string used by graph object.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Graph object ID |
| 2 | string | Yes |  | Template |
| 3 | string | No |  | Options |

#### Argument 1

ID of graph object whose properties are to be used in the template. See  [Graph Object Identifiers - the 'ID'](applications_graphobjects.htm#applications_graphobjects__graphobjectidentifiers) .

#### Argument 2

Template string. This can consist of literal text, properties enclosed with '%' and expressions enclosed with '{' and '}'. The property values are those belong to the object supplied in argument 1. Properties available for the various types of graph object are described in  [Objects and Their Properties](applications_graphobjects.htm#applications_graphobjects__objectsandtheirproperties) . Some properties return the id of another graph object. These can be used to create nested property definitions. For example `%curve:label%` } when applied to a curve marker object returns the label of the attached curve.

The template string may also contain the special keywords `<if>` }, `<ifd>` }, `<t>` } and `<repeat>` }. These behave the same and have identical syntax as the keywords of the same name used for schematic TEMPLATE properties described in the  *User's Manual* .

#### Argument 3

Options. Currently there is only 1 and that is the action to take when an expression fails to evaluate. Possible values are:

|  |  |
| --- | --- |
| 'msg' | Requires a second arg 3 to have two elements. Returns error message specified in second element of string. |
| 'empty' | Returns an empty value on error |
| 'literal' | (default) Returns the literal text of the expression |

### Returns

Return type: string

Returns the result of evaluating the template.

### Notes

This function along with  [ResolveTemplate](func_resolvetemplate.htm)  are implemented using the same internal program code that implements the schematic TEMPLATE property in a netlist generation and behaves in the same way.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_resolvegraphtemplate) | | |
| [◄ RemoveSymbolFiles](func_removesymbolfiles.htm) |  | [ResolveTemplate ▶](func_resolvetemplate.htm) |
