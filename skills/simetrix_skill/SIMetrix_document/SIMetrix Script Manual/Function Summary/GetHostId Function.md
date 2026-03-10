# GetHostId Function

Get MAC address or dongle serial numbers used for licensing

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | -1 | Host id type |

#### Argument 1

Can be the following value

|  |  |
| --- | --- |
| **Value** | **Description** |
| '-1' | Default host id - this is the MAC address on Windows systems |
| '2' | MAC address |
| '15' | Serial number of FLEXid-9 type dongle |
| '51' | Serial number of FLEXid-10 type dongle |

### Returns

Return type: string

String as used in a license file

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_gethostid) | | |
| [◄ GetHighlightedWidgetId](func_gethighlightedwidgetid.htm) |  | [GetHttpContentSize ▶](func_gethttpcontentsize.htm) |
