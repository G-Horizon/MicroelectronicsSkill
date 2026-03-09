# GetHttpContentSize Function

Get the size of an HTTP object specified by its URL. This function can be used to determine the size of a file on a web server. Note that for the function to work the HTTP server must send the required header information containing the file size. Some servers may not send the information.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | URL |

#### Argument 1

URL of object whose size is requested

### Returns

Return type: Real

Size of object in bytes. On failure (such as a an invalid URL) the function returns -1.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_gethttpcontentsize) | | |
| [◄ GetHostId](func_gethostid.htm) |  | [GetInstanceBounds ▶](func_getinstancebounds.htm) |
