# StyleInfo Function

Returns the style information for the requested styles. If a requested style does not exist, the default style information is returned (unless the global flag has been set, when no data would be returned).

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Style names |
| 2 | string | No |  | Options flag |

#### Argument 1

A list of style names to return the style information for. Each array element is a different style name.

#### Argument 2

If set to  *"global"*  , only global styles are returned.

### Returns

Return type: string array

The style information for the requested styles. If a style does not exist and the global flag has not been set, the default style will be returned. If a style does not exist and the global flag has been set, no style information is returned for that style.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_styleinfo) | | |
| [◄ StrStr](func_strstr.htm) |  | [StyleLineTypes ▶](func_stylelinetypes.htm) |
