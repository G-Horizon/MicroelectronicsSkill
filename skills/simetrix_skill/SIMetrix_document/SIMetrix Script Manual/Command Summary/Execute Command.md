# Execute Command

Run the script or command  *command* .

Scripts are usually run by simply entering their name in the same way as a command is entered. However, the script is executed slightly differently if run using the Execute command. If a script is called from another script in the normal way, the called script is read in and parsed before the main script is executed. If the Execute command is used, the called script is not read in until and unless the Execute command is actually executed. This has two main applications.

1. The name of the called script is not known initially, for example if its selected from a file dialog box.
2. The called script is very long and is not always called by the calling script. It may take some time to read in and parse the called script. This time would be wasted if the script is not actually called.

; Avoid using Execute if a script is called within a loop. The script would be read in and parsed each time around the loop which is very inefficient.

```
Execute [/echo] <command>
```

### Parameters

|  |  |
| --- | --- |
| /allowextbi |  |
| /echo | Command is copied to the command history drop down box in the commend shell. |
| /literal | Indicates the text in  *command*  should be read literally. This switch should be used if the complete command along with any arguments are stored in a variable, to be accessed by Execute through braced substituion. See the example for further explanation. |
| /startup | Used by initialisation scripts to indicate that a command is being executed on startup. The function  [CommandStatus](func_commandstatus.htm)  can be used to test this state. This switch must not be used in user scripts. |
| command | Command to be executed with arguments if required. See `/literal` above for more information. |

### Example

Use of the literal flag. If you have a script where a command to execute is contained within a variable, for example:

```
Let command = 'inst npn'
```

Then the literal flag should be used to enable the following braced substitution to work:

```
Execute /literal {command}
```

Here is another example of using the literal flag. Both of the following will do the same thing:

```
Execute /literal "inst npn"
Execute inst npn
```

But this will throw an error:

```
Execute "inst npn"
```

The problem with the last example is that the Execute command interprets the first token in  *command*  as the actual command or script name and the remainder of  *command*  as the arguments to it. Because "inst npn" is enclosed in quotation marks, it is treated as a single item specifying the command name "inst npn" which is incorrect.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_execute) | | |
| [◄ EndSym](com_endsym.htm) |  | [FileViewCleanUpFileWatchers ▶](com_fileviewcleanupfilewatchers.htm) |
