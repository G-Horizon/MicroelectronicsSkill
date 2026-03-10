# User Interface to Scripts

In this topic:

## Dialog Boxes

A number of functions are available which provide means of obtaining user input through dialog boxes. These are:

|  |  |
| --- | --- |
| **Function name** | **Comment** |
| [AddRemoveDialog](func_addremovedialog.htm) | Add or remove items to or from a list |
| [BoolSelect](func_boolselect.htm) | Up to 6 check boxes |
| [ChooseDir](func_choosedir.htm) | Select a directory |
| [EditObjectPropertiesDialog](func_editobjectpropertiesdialog.htm) | Read/Edit a list of property names and values |
| [EditSelect](func_editselect.htm) | Up to 6 edit boxes |
| [EnterTextDialog](func_entertextdialog.htm) | Enter multi line text |
| [GetSimetrixFile](func_getsimetrixfile.htm) | Get file name of pre-defined type |
| [GetUserFile](func_getuserfile.htm) | Get file name (general purpose) |
| [InputGraph](func_inputgraph.htm) | Input text for graph |
| [InputSchem](func_inputschem.htm) | Input text for schematic |
| [NewValueDialog](func_newvaluedialog.htm) | General purpose dialog box |
| [RadioSelect](func_radioselect.htm) | Up to 6 radio buttons |
| [SelectDialog](func_selectdialog.htm) | Select item(s) from a list |
| [TableDialog](func_tabledialog.htm) | Present items in a table |
| [TableEditor](func_tableeditor.htm) | Present lists of items in a table |
| [TreeListDialog](func_treelistdialog.htm) | Select item from tree structured list |
| [UpDownDialog](func_updowndialog.htm) | Re order items |
| [UserParametersDialog](func_userparametersdialog.htm) | Read/Edit a list of parameter names and values |
| [ValueDialog](func_valuedialog.htm) | Up to 10 edit boxes for entering values |

The above are the general purpose user interface functions. In particular, the function [NewValueDialog](func_newvaluedialog.htm) is very universal in nature and has a wide range of applications. There are many more specialised functions. These are listed in [Functions by Application](functionsbyapplication.htm).

## User Control of Execution

Sometimes it is desirable to have a script free run with actions controlled by a key or menu item. For example you may require the user to select an arbitrary number of nodes on a schematic and then press a key to continue operation of the script to perform - say - some calculations with those nodes. You can use the [DefKey](com_defkey.htm) and [DefMenu](com_defmenu.htm) commands to do this. However, for a key or menu to function while a script is executing, you must specify "immediate" mode when defining it. Only a few commands may be used in "immediate" mode definitions. To control script execution, the [Let](com_let.htm) command may be used. The procedure is to have the key or menu assign a global variable a particular value which the script can test. The following example outputs messages if F2 or F3 is pressed, and aborts if F4 is pressed:

```
defkey F2 "scriptresume;let global:test=1" 5
defkey F3 "scriptresume;let global:test=2" 5
defkey F4 "scriptresume;let global:test=0" 5

let global:test = -1
while 1
scriptpause
if global:test=0 then
exit script
elseif global:test=1 then
echo F2 pressed
elseif global:test=2 then
echo F3 pressed
endif
let global:test = -1
endwhile

unlet global:test
```

|  |  |  |
| --- | --- | --- |
| [◄ Accessing Simulation Data](scriptlanguage_accessingsimulationdata.htm) |  | [Errors ▶](scriptlanguage_errors.htm) |
