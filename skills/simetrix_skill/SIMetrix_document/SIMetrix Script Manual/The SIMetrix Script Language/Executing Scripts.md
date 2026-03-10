# Executing Scripts

Scripts are executed by typing their file name at the command line, running them from the script editor, or dragging and dropping the file to the Command shell. Additionally, scripts can be assigned to a key or menu. See [User Defined Key and Menu Definitions](applications_userinterface.htm#applications_userinterface__userdefinedkeymenu).

If a full pathname is not given, SIMetrix first searches a number of locations. The rules are a little complicated and are as follows:

1. Search the BiScript directory followed by all its descendants. On Windows the BiScript directory is usually at *\textlangle simetrix\_root\textrangle/support/biscript*.
2. Search for a built in script of that name. Built in scripts are bound into the executable binary of SIMetrix. See [Built-in Scripts](scriptlanguage_executingscripts.htm#scriptlanguage_executingscripts__builtinscripts).
3. Search the SCRIPT directory. This is defined by the ScriptDir option setting (see [Set](com_set.htm)) which can also be accesses in the File Locations tab of the options dialog box. (see **File** > **Options** > **General...**).
4. Search the User Script list of directories. This is defined by the UserScriptDir option variable (see [Set](com_set.htm)). This may be set to a semi-colon delimited list of search paths.
5. Search the current working directory if the script was executed from a menu or the command line. If the script was called from another script, the directory where the calling script was located is searched instead

Scripts can also be executed using the [Execute command](com_execute.htm).

In this topic:

## Script Arguments

You can pass data to and from scripts using arguments.

### Passing by Value

To pass a value *to* a script, simply place it after the script name. E.g.

```
my_script 10
```

The value `10` will be passed to the script. There are two methods of retrieving this value within the script. The easiest is to use the [Arguments](com_arguments.htm) command. In the script you would place a line like:

```
Arguments num
```

In the above the variable `num` would be assigned the value `10`. If the `Arguments` command is used, it becomes compulsory to pass the argument. If you wish to provide a script with optional arguments you must use the `$arg` variables. When an argument is passed to a script a variable with name `$argn` is assigned with the value where ???MATH???n???MATH??? is the position of the argument on the command line starting at 1. To find out if the argument has been passed, use the [ExistVec](func_existvec.htm) function. E.g.

```
if ExistVec('$arg1') then
.. action if arg 1 passed
else
.. action if arg 1 not passed
endif
```

### Passing by Reference

When an argument is passed by value, the script in effect obtains a local copy of that data. If it subsequently modifies it, the original data in the calling script remains unchanged even if a variable name was used as the argument. The alternative is to pass *by reference* which provides a means of passing data back to the calling script. To pass by reference you must pass a variable prefixed with the @ character. E.g.

```
Let var = 10
my_script @var
```

To retrieve the value in the called script we use the [Arguments](com_arguments.htm) command as we did for passing by value but also prefix with @. E.g.

```
Arguments @var
Let var = 20
```

The above modifies `var` to 20 and this change will be passed back to the `var` in the calling script. In the above example we have used the same variable name `var` in both the called and calling scripts. This is not necessary, we have just done it for clarity. You can use any name you like in either script.

Optional arguments passed by reference work the same way as arguments passed by value except that instead of using the variable `$argn` you must use `$varn`. You do not need to use @ when accessing arguments in this way. See the internal script *define\_curve* for an example.

### Important

There is currently a limitation that means you can't use an argument passed by reference directly in a braced substitution. E.g.

```
{var}
```

where var is an argument passed by reference will not work. Instead you can assign the value to a local variable first.

### Passing Large Arrays

In many computer languages it is usually recommended that you pass large data items such as arrays by reference as passing by value involves making a fresh copy which is both time consuming and memory hungry. Passing by reference only passes the location of the data so is much more efficient. In the SIMetrix script language, however, you can efficiently pass large arrays by value as it uses a technique known as *copy on write* that does not make a copy of the data unless it is actually modified.

## Built-in Scripts

All the scripts needed for the standard user interface are actually built in to the executable file. The source of all of these can be found on the installation CD.

## Debugging Scripts

### Displaying Commands Executed

You can watch the script being executed line by line by typing at the command line before starting the script:

```
Set EchoOn
```

This will cause the text of each command executed to be displayed in the message window. When you have finished you cancel this mode with:

```
Unset EchoOn
```

### Single Step a Script

Run the script by typing at the command line:

```
ScriptPause ; scriptname
```

where `scriptname` is the name of the script you wish to debug. To be useful it is suggested that you enable echo mode as described above. To single step through the script, press F2.

Note that [ScriptPause](com_scriptpause.htm) only remains in effect for the first script. Subsequent scripts will execute normally.

### Abort Currently Executing Script

Press escape key.

To pause a currently executing script.

Press shift-F2. Note that it is not possible to run other commands while a script is paused but you can single step through it using F2.

### Resume a Paused Script

Press ctrl-F2

## Startup Script

The startup script is executed automatically each time SIMetrix is launched. By default it is called startup.sxscr but this name can be changed with in the options dialog box. (**File** > **Options** > **General...**). The startup file may reside in the script directory (defined by ScriptDir option variable) or in a user script directory (defined by UserScriptDir option variable).

The most common use for the startup script is to define custom menus and keys but any commands can be placed there.

To edit the startup script, select the **File** > **Options** > **Edit Startup Script** menu item.

|  |  |  |
| --- | --- | --- |
| [◄ Errors](scriptlanguage_errors.htm) |  | [Unsupported Functions and Commands ▶](scriptlanguage_unsupportedfunctionscommands.htm) |
