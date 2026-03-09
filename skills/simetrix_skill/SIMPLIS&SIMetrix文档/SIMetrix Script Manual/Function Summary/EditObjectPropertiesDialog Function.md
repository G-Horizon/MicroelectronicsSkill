# EditObjectPropertiesDialog Function

Displays a dialog box allowing the editing of property values. This is used for a number of functions. See the schematic right-click popup menu Edit Properties... for an example.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Property names |
| 2 | string array | Yes |  | Property values |
| 3 | string array | No |  | Property types |
| 4 | string array | No |  | Options |
| 5 | string | No | <<empty>> | Override Style |
| 6 | string | No | <<empty>> | Available override styles |

#### Argument 1

Function will list in a dialog box the property names and values given in the first two arguments. The function returns the values of the properties. Unless declared read-only (see below) the value of each property may be edited by the user by double clicking on its entry in the list.

#### Argument 2

Function will list in a dialog box the property names and values given in the first two arguments. The function returns the values of the properties. Unless declared read-only (see below) the value of each property may be edited by the user by double clicking on its entry in the list.

#### Argument 3

The third argument of the function declares the type for each property. Possible values are:

|  |  |
| --- | --- |
| 'String' | Property value is a simple text string |
| 'Font' | Property value is a font definition. When the user double clicks the item to edit, a font dialog box will be opened. Font definitions consist of a series of numeric a text values separated by semi-colons. E.g. '-11;0;0;0;0;0;Arial' |
| 'Colour' | Property value is a colour definition. When the user double clicks the item to edit, a "choose colour" dialog box will be opened. Colours are defined by a single integer that specifies the colour's RGB value. |
| item1|item2|item3|... | Up to six items separated by the '|' symbol. When the user double clicks a property so defined, a dialog showing a number of radio buttons is displayed labelled item1, item2 etc. The value of the property will be the item selected. |
| '\*' | Declares the property read-only. If the user attempts to edit its value a warning message box will be displayed. |

#### Argument 4

Array of up to 4 values as described in the following table:

|  |  |  |
| --- | --- | --- |
| **Index** | **Description** | **Default** |
| 0 | Box caption | 'Edit Properties' |
| 1 | Properties tabbed sheet tab title | 'Properties' |
| 2 | Name column title | 'Name' |
| 3 | Value column title | 'Value' |

Note that fields 2 and 3 should be provided as a pair. If 2 is supplied but not 3, 2 will be ignored and the default value will be used.

#### Argument 5

If set, this specifies the style the property should use when being displayed on the schematic.

#### Argument 6

A set of styles that can be chosen between if setting an override style for a property. These styles are chosen from those styles in the Style Library that have the override style flag checked.

### Returns

Return type: string array

String array containing values for all properties. An empty result is returned if the user cancels the dialog box.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editobjectpropertiesdialog) | | |
| [◄ EditLegendBoxDialog](func_editlegendboxdialog.htm) |  | [EditPinDialog ▶](func_editpindialog.htm) |
