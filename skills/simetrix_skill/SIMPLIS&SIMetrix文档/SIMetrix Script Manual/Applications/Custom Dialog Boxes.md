# Custom Dialog Boxes

In this topic:

## Overview

SIMetrix has a feature that permits the creation of custom dialog boxes without the need to write program code. This can be done using a special graphical tool called the "Designer" supplied with SIMetrix. "Designer" is redistributable tool provided with the Qt toolkit used for SIMetrix UI development.

## Starting "Designer"

The tool is installed with the rest of the SIMetrix binaries and is called "designer.exe". Use windows explorer to locate designer.exe in the "bin64" folder under the SIMetrix root. The SIMetrix installer does not create a short cut to this but you may create one yourself if required.

## Developing Dialogs

The basic procedure is:

1. Start Designer
2. Select **New...** then choose either **Dialog with Buttons Bottom** or **Dialog with Buttons Right**. Click on **Create**
3. Set the top level object's objectName property to the required name of the SIMetrix script function. To begin with this is 'Dialog' and has the QDialog class name. Change 'Dialog' to a name of your choice. The name must not clash with a name already used by another dialog or a standard SIMetrix script function
4. Edit windowTitle property as required. This is the text that will appear in the caption bar of the dialog
5. Add widgets as required. See next section for further details. See also [Using Geometry Management](applications_customdialogboxes.htm#applications_customdialogboxes__usinggeometrymanagement).
6. Save result as a .ui file to the directory support/dialogs under SIMetrix root (Windows). This is the default location for user dialogs. There is an option setting that allows them to be located elsewhere. See below for details.

The dialog is now designed. If SIMetrix is currently running, shut it down and restart it to register the new dialog function.

Note that you do not need to restart after editing the dialog - only when creating it for the first time or when changing the function name. SIMetrix registers the filename and function name on startup, but will reread it when the function is called. This means that you can make changes to your dialog without having to shut down and restart SIMetrix each time.

You can select a different location for user dialogs with the option setting UserDialogsDir. Type this at the command line:

```
Set UserDialogsDir=path
```

where path is the full path of the new dialogs location. You may use logical path symbols in the definition. For example "%SXAPPDATAPATH%/userdialogs" resolves to a directory under the application data path. Note that you must restart SIMetrix after changing the path.

## The Widgets

"Widgets" are the dialog elements such as edit boxes and push buttons that you use to enter data and choices. In Windows "Widgets" are sometimes called "Controls".

A range of special widgets is supplied that have some extra properties to define how they will be initialised when the dialog is opened and what they will return through the SIMetrix script function call mechanism. These widgets can be found under the "SIMetrix" group. Always use these for anything used for data entry. Other widgets that do not require initialisation nor output data may also be used. E.g. the items under "Containers". Note that the "Radio Button" widget in the "Buttons" group can only be used inside a "RadioGroup" which you will find in the SIMetrix group.

In general data is transferred to the dialog widgets by the arguments of the SIMetrix script function. Each argument is an array of strings and each widget may specify through its properties the argument index and the array element index where the data is located. In every case the data is a single string. If multiple values are required for a widget, it will either have multiple properties to define them, or, in the case of lists of values, the items will be delimited by a pipe ('|') symbol.

Data is returned in a similar manner. But as there is only one return value, just a single array element is specified.

### General Properties

There are five user settable properties in use by the various widgets, but not all widgets use all of the properties. Some widgets may have aditional special purpose properties. These five general properties are:

|  |  |
| --- | --- |
| **Property Name** | **Description** |
| argIndex | Index of script function argument used for initialisation of widget. First argument has index=0. You may use a maximum of 32 arguments so this property may not be larger than 31 |
| inElementIndex | Index into array supplied to argIndex for value used to initialise widget. First element has index=0 |
| outElementIndex | Index into array returned by script function for user entered value |
| itemsArgIndex | Index of script function argument used to supply items to initialise list. Items separated by pipe ('|') symbol. Currently used by list boxes and combo boxes. |
| itemsElementIndex | Index into array supplied to itemsArgIndex for items to initialise list. Items separated by pipe ('|') symbol. Currently used by list boxes and combo boxes |

Full details and examples for each widget type follow.

### EditBox

The properties argIndex, inElementIndex and outElementIndex initialise and return the text value stored in a single line edit box.

The EditBox widget may be configured to accept signal data pasted from a schematic or graph window. This is the same function as provided with the Define Curve Dialog box opened with the schematic menu **Probe** > **Define Curve...** and others. When you click on a node in the schematic, its node name is pasted directly in the edit box. To enable this functionality with the EditBox widget, set the `enablePasteText` property to `true`.

When `enablePasteText` for at least one EditBox widget is set, the whole dialog box will be opened in a 'Modeless' fashion. This means that it is possible to switch to other windows while the dialog is open.

### TextEdit

As EditBox but multi-line and does not support the `enablePasteText` property.

### Spinner

Used for entering numeric values. argIndex, inElementIndex and outElementIndex used to initialise and return. Note that box stores a numeric value, but the script arguments must still be strings. This widget has the following properties that govern its behaviour:

|  |  |
| --- | --- |
| **Property Name** | **Description** |
| engMode | Boolean. If true, value is always displayed in engineering notaion using suffixes such as m, u, k etc |
| step125 | Boolean. If true, spinner buttons step in 1-2-5 sequence. Otherwise they step in a linear sequence controlled by the 'increment' property |
| increment | Increment for spinner buttons. Only effective if 'step125' property is false |
| max | Maximum value allowed for widget |
| min | Minimum value allowed for widget |
| precision | Value displayed and returned to precision specified. |
| allowExpressions | If true, the user may enter expressions enclosed with curly braces: '{' and '}'. If false, only numeric values will be allowed. |

### CheckBox

A check box providing a simple on-off selection. argIndex, inElementIndex and outElementIndex used to define initial setting and return value in normal way. '1' indicates checked and '0' indicates unchecked. Label Static label. Can be set with static value in which case argIndex and inElementIndex should be -1. Alternatively can be initialised via function call using argIndex an inElementIndex. Does not return a value.

### RadioGroup

A container that should be filled with one or more Radio Buttons (these may be found under the "Buttons" group). Only one of the radio buttons in the group maybe checked at any time. The usual properties are used to initialise and the return values. '0' means check the top most button, '1' the second button, '2' the third etc.

### PushButton

A push button with two alternative modes of operation. If the property 'toggleButton' is false, then this may be used to close the dialog box. In this case the property 'action' must be set to either 'reject' or 'accept'. If 'reject' is set then the dialog box function will return an 'empty vector'. That is the array returned will have a length of zero. (You must test this with the script langauge's length() function). If set to 'accept' the normal data will be returned. The 'outElementIndex' property may be set in this case in which case the value returned will be 'clicked' if the button was clicked to close the box or 'notclicked'.

If 'toggleButton' is set to true then 'action' must be set to 'none' to be meaningful. In this case the button will toggle on or off. The return value controlled by outElementIndex will be either 'on' or 'off'. Currently there is no method to initialise the toggle state. This will be corrected in a later release.

### CancelButton and OkButton

These are identical to PushButton except for changes to default values of some properties. "Cancel Button" behaves as a button to cancel a dialog and will cause the calling function to return an empty vector. "Ok Button" closes a dialog and accepts the user's input.

### ListBox

A list box containing a list of values. The values themselves are defined using itemsArgIndex and itemsElementIndex properties and must be in the form of a single string containing a list of values separated by a pipe symbol.

The initial value selected is defined by argIndex and inElementIndex. This is the actual value not the index into the list. The item selected in the list is returned in outElementIndex.

### ComboBox

A drop down "combo box" otherwise the same as the ListBox.

### ParameterView

This is experimental and currently unsupported.

## Using Geometry Management

SIMetrix Dialog Designer features an advanced system, known as geometry management, that automatically arranges widgets in the dialog. Geometry management controls the position and size of the widgets in a manner that maintains the layout in an aethestically pleasing form even if the dialog is resized.

These features are available via the toolbar and also with the context popup menu in the form and the object inspector. The features available are:

1. Layout horizontally. Lays out selected widgets in a horizontal line
2. Layout vertically. Lays out selected widgets in a vertical line
3. Layout in a grid. Lays out widgets in a grid arrangement using their initial position as a guide
4. Layout vertically/horizontally in a splitter. Lays out two widgets with a splitter bar in between allowing the user to control their relative sizes

The geometry management actions work on either selected widgets or all the widgets in a selected container. If no widget or container is selected, the action will be applied to all the widgets in the form. A container is a widget that is designed to hold other widgets. The containers are the widgets in the containers group and also the RadioGroup widget in the SIMetrix group.

The best way to learn about geometry management is to experiment with various widgets and containers. You may need to use the "spacer" widget to provide empty spaces. Some widgets (e.g. buttons) resize to fill the space available and this is not always desirable. Further documentation on the Designer tool can be found at the developer's web site:

http://doc.qt.io.

See menu **Help** > **About...** for the current version.

## Examples

A number of trivial examples are supplied that demonstrate each of the widgets. These are supplied in the examples directory under scripts/dialogs. To use them you must copy them to the support/dialogs folder. Here is a list:

### EditDialog

Simple dialog with an edit box and an Ok button. Type:

```
Show EditDialog('Initial message')
```

to see what it does.

### TestCombo

Demo of combo box, try this:

```
Show TestCombo('bill', 'fred|bill|john')
```

### TestFunction

A spinner and a check box. Try:

```
Show TestFunction(['2.345', '1'])
```

### ListBoxFunction

A list box and a check box, Try this:

```
Show listboxfunction(['john','1'], 'fred|bill|john')
```

### TextEditTest

TextEdit and two push buttons, one of them with toggle action. Try this:

```
Show textedittest('A message')
```

### JohnsModelDialog

Bits and pieces. Try this:

```
Show johnsmodeldialog(['bill', '2.345', '4.567', '1'],
'fred|bill|john')
```

### RadioTest

A couple of radio buttons and a toggle button

```
Show radiotest('1')
```

## ExecuteDialog Function

The ExecuteDialog function executes a .ui file directly using the dialog definition's full path name. The first argument to this function is the full path to the dialog .ui file and subsequent arguments are the dialog's arguments shifted one place. So argument 0 of the dialog function is argument 1 of ExecuteDialog. Note that the first argument must be a full path, but you may use logical path symbols.

ExecuteDialog does not require the .ui file to present when SIMetrix starts up unlike the usual method of calling the dialog functions.

All script functions are limited to a maximum of 32 arguments. Because the first argument is reserved for the path name, this means that the maximum number of arguments that can be passed to the dialog is 31. If calling the dialog directly, the limit is 32.

## Performance

Complex dialog designs can take a noticeable time to open. This is because the definition file is read and parsed every time the dialog function is called.

|  |  |  |
| --- | --- | --- |
| [◄ Creating and Modifying Toolbars](applications_creatingmodifyingtoolbars.htm) |  | [Pre-defined Buttons ▶](applications_buttons.htm) |
