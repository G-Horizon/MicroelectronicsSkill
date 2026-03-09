# EncodeImageToBase64 Function

Returns the Base64 binary encoding of a png or bmp image file as a text string. The first argument can be a full file path name to the image, a directory path, or left blank. The latter two options will prompt a user with a dialog to choose the desired png or bmp file.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | No |  | File path name of png or bmp file |

#### Argument 1

Full file path name, file directory path, or empty.

### Returns

Return type: String

String with base64 encoding of png or bmp image if conversion is successful. In case of a failure to convert the file, returns a integer error code.

|  |  |
| --- | --- |
| **Integer Error Code** | **Description** |
| 0 | File doesn't exist |
| 1 | Incorrect file format - supported formats are PNG and BMP |
| 2 | Failed to convert file |

You can test the return value with the  [IsStr](func_isstr.htm)  function to catch and handle errors.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_encodeimagetobase64) | | |
| [◄ ElementProps](func_elementprops.htm) |  | [EnterTextDialog ▶](func_entertextdialog.htm) |
