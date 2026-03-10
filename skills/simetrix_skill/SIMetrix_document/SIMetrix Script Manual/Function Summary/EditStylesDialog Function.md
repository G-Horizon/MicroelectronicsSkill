# EditStylesDialog Function

Opens the Edit Styles dialog. This is a system function and is unsupported.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Style names |
| 2 | string array | Yes |  | Style info |
| 3 | string array | Yes |  | Line types available |
| 4 | string array | No | empty string | Hidden default styles for viewer |
| 5 | string array | No | empty string | Flags for hiding buttons |
| 6 | string array | No | empty string | Global style info |
| 7 | string | No | empty string | Editor settings |

#### Argument 2

Style information for each style name specified in argument 1. Each element in the array is matched to the corresponding element in argument 1 and must be in the form:

```
Name|LineType|LineThickness|LineColour
```

#### Argument 3

Each array element is a different line type available to all styles. Options are: Solid, Dash, Dot, DashDot, DashDotDot.

#### Argument 4

Default styles to use in the preview window that are not shown or editable in the dialog. Only required to ensure the correct default wire, symbol and annotation styles are applied.

Each element in the array is a full style definition, in the form:

```
StyleName|lineColour:[lineColour] lineType:[lineType]
lineThickness:[lineThickness] fontFamily:[fontFamily]
fontItalics:[fontItalics] fontBold:[fontBold] fontColour:[fontColour]
fontSize:[fontSize] propertyStyle:[propertyStyle]
fontOverline:[fontOverline] fontUnderline:[fontUnderline]
```

StyleName values can be either: DefaultWire, DefaultInstance, DefaultAnnotation.

#### Argument 5

Optional flags for hiding buttons in the dialog. The flags are:

|  |  |
| --- | --- |
| **Flag** | **Behaviour** |
| noadd | Hides the  *New...*  button. |
| noduplicate | Hides the  *Duplicate*  button. |
| noedit | Hides the  *Edit Name...*  button. |

#### Argument 6

Global style information, used for reverting local styles back to their global settings. Each row is a separate style, defined in the same form as argument 4. Any style name is allowed.

#### Argument 7

If set to "  *FontOnly*  ", only font settings will be displayed within the editor.

### Returns

Return type: string array

String vector of updated styles if successful, or an empty string if cancel is selected.

Each element in the array is a different style. Styles are in the form:

```
StyleName|lineColour:[lineColour] lineType:[lineType]
lineThickness:[lineThickness] fontFamily:[fontFamily]
fontItalics:[fontItalics] fontBold:[fontBold] fontColour:[fontColour]
fontSize:[fontSize] propertyStyle:[propertyStyle]
fontOverline:[fontOverline] fontUnderline:[fontUnderline]
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editstylesdialog) | | |
| [◄ EditSimplisMosfetDriverDialog](func_editsimplismosfetdriverdialog.htm) |  | [EditSymbolBusDialog ▶](func_editsymbolbusdialog.htm) |
