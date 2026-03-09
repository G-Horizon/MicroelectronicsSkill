# Custom Curve Analysis

The menus Probe|More Probe Functions... and the graph menu Measure|More Functions... each open a tree list dialog box that displays the function available. In this section we describe how this system works and how it can be extended.

We have only skimmed over the basics. For more information, please refer to the scripts themselves.

In this topic:

## Adding New Functions

The operations listed for the menus described above are obtained from one of two built-in text files. These files are:

|  |  |
| --- | --- |
| analysis\_tree.sxscr | For curve analysis functions |
| probe\_tree.sxscr | For probe functions |

Like built in scripts, these are embedded in the binary executable but can also be overridden by placing files of the same name in the biscript directory.

Both files use the same format. Each entry in the tree list is defined by a single line in the file. Each line contains a number of fields separated by semi-colons. The first field is that command that is called to perform the action while the remaining fields describe the hierarchy for the entry in the tree list control. The command is usually a script often with a number of arguments. To add a new function, simply add a new line to the relevant file. The order is not important.

## 'measure', 'measure\_span' Scripts

These are the "driver" scripts that perform the curve analysis and curve analysis over cursor span analysis respectively. These don't perform the actual calculations but carry out a number of housekeeping tasks. The calculations themselves are performed by a script whose name is passed as an argument. To add a new function you need to create one of these scripts. For simple functions the script is not complicated. In the example below we show how the "Mean" function is implemented and you will see that it is very simple.

## An Example: The 'Mean' Function

The entry for the full version of this in analysis\_tree.txt is:

```
measure_mean;Measure;Transient;Mean;Full
```

This means that the script 'measure\_mean' will be called when this function is selected. 'measure\_mean' is quite simple, it is just a single line

```
measure /ne 'calculate_mean' 'Mean'
```

`/ne` is not that important, it just tells the script system not to enter the command in the history list.

'calculate\_mean' specifies the script to call to perform the calculation.

'Mean' specifies the y-axis label.

The 'calculate\_mean' script is as follows:

```
Arguments data xLower xUpper @result @error

if xUpper>xLower then
Let result = Mean1(data, xLower, xUpper)
else
Let result = Mean1(data)
endif
```

The argument `data` is the data that is to be processed. In this case we simply need to find its Mean. `xUpper` and `xLower` specify the range over which the mean should be calculated. These would be specified if the "cursor span" version of the mean function was selected by the user. The result of the calculation is assigned to the argument `result` which has been "passed by reference". The error argument is not used here but it can be used to signal an error condition which will abort the operation. This is done by setting it to 1.

|  |  |  |
| --- | --- | --- |
| [◄ User Interface](applications_userinterface.htm) |  | [Automating Simulations ▶](applications_automatingsimulations.htm) |
