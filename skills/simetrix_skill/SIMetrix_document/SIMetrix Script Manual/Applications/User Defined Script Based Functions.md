# User Defined Script Based Functions

In this topic:

## Overview

The SIMetrix script language provides a method of creating user defined functions that can be used in any front end expression. These expressions may be used in scripts, on the command line and even within a schematic template property.

User defined functions are used to define some of the goal functions designed for performance and histogram analysis. The scripts for these all begin "uf\_" and are registered using the script "reg\_user\_funcs". The source for these can be found on the installation CD.

## Defining the Function

User defined functions are defined as a script. The arguments to the function and the return value from the function are passed as the script's arguments. The script's first argument is passed by reference and is the return value while the remaining arguments are the arguments passed in the call to the function. The function may have up to seven arguments and they may be of any type. See example below.

## Registering the Script

For the expression evaluator to recognise the function name, the script and function name must be registered. This is done with the [RegisterUserFunction](com_registeruserfunction.htm) command. The definition of this is:

```
RegisterUserFunction Function-Name Script-Name [min-num-args] [max-num-args]
```

For details see [RegisterUserFunction](com_registeruserfunction.htm).

Note that function registration is not persistent. That is the registration only lasts for the current session. If you wish to make a permanent function definition, place the RegisterUserFunction command in the startup script.

## Example

Here is a trivial example. The following shows the steps to create a function that multiplies a number by 2. First the script

```
Arguments @rv arg1
Let rv = 2*arg1
```

Save this to a file called - say - times\_two.sxscr and place it in the script directory. Now, register the script as a function called "Times2". To do this, execute the command:

```
RegisterUserFunction Times2 times_two 1 1
```

The definition is now complete. To test it type at the command line:

```
Show Times2(2)
```

You should see the result:

```
Times2(2) = 4
```

|  |  |  |
| --- | --- | --- |
| [◄ Event Scripts](applications_eventscripts.htm) |  | [User Defined Binary Functions ▶](applications_userdefinedbinaryfunctions.htm) |
