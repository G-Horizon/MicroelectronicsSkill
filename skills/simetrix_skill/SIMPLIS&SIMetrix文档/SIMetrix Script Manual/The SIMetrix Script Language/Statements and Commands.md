# Statements and Commands

Scripts are composed of a sequence of *statements*. Statements usually comprise at least one command and optionally control words such as `if` and `then`. A *command* is a single line of text starting with one of the command names listed in the [Command Reference](commandsummary.htm).

There are six types of statement. These are:

* command statement
* if statement
* while statement
* for statement
* foreach statement
* foreachdiv statement
* exit statement
* script statement

In this topic:

## Commands

Commands begin with one of the names of commands listed in the [Command Summary](commandsummary.htm). A command performs an action such as running a simulation or plotting a result. E.g.:

```
Plot v1_p
```

is a command that will create a graph of the vector `v1_p`. The syntax varies for each command. Full details are given in the [Command Reference](commandsummary.htm).

All commands must start on a new line or after a semi-colon. They must also end with a new line or semi-colon.

A command statement is a sequence of one or more commands.

## Command Switches

Many commands have *switches*. These are always preceded by a '/' and their meaning is specific to the command. There are however four global switches which can be applied to any command. These *must* always be placed immediately after the command. Global switches are as follows:

* /e Forces command text to copied to command history. Use this when calling a command from a script that you wish to be placed in the command history.
* /ne Inhibits command text copying to command history. Use this for commands executed from a menu or key definition that you do *not* wish to be included in the command history.
* /quiet Inhibits error messages for that command. This only stops error message being displayed. A script will still be aborted if an error occurs but no message will be output.
* /noerr Stops scripts being aborted if there is an error. The error message will still be displayed.

## If Statement

An *if statement* is of the form:

```
if expression then
statement
endif
```

OR

```
if expression then
statement
else
statement
endif
```

OR

```
if expression then
statement
[[elseif expression then
statement ]...]
else
statement
endif
```

### Examples

```
if NOT SelSchem() then
echo There are no schematics open
exit all
endif

if length(val)==1 then
echo {refs[idx]} {val}
else
echo Duplicate reference {refs[idx]}. Ignoring
endif
if opts[0] && opts[1] then
let sel = 1
elseif opts[0] then
let sel = 2
else
let sel = 3
endif
```

In form1, if the expression resolves to a TRUE value the statement will be executed. (TRUE means not zero, FALSE means zero). In the second form the same happens but if the expression is FALSE the statement after the `else` is executed. In the third form, if the first expression is FALSE, the expression after the `elseif` is tested. If that expression is TRUE the next statement is executed if not control continues to the next `elseif` or `else`.

## While Statement

While statements are of the form:

```
do while expression
statement
loop
```

OR (alternative form)

```
while expression
statement
endwhile
```

### Example

```
do while GetOption(opt)<>'FALSE'
let n = n+1
let opt = 'LibFile' & (n+99)
loop
```

Both forms are equivalent.

In while loops the expression is evaluated and if it is TRUE the statement is executed. The expression is then tested again and the process repeated. When the expression is FALSE the loop is terminated and control passes to the statement following the `endwhile`.

## For Statement

These are of the form:

```
for variable=expression1 to expression2 [ step expression3]
statement
next [variable]
```

A for loop executes statement for values of `variable` starting at `expression1` and ending with `expression2`. Each time around the loop variable is incremented by `expression3` or if there is no step expression, by 1. If `expression2` starts off with a value less than `expression1`, `statement` will not be executed at all.

### Example

This finds the sum of all the values in `array`

```
for idx=0 to length(array)-1
let sum = sum + array[idx]
next idx
```

## Foreach Statement

These are of the form:

```
foreach variable array_expression
statement
next
```

The foreach statement executes `statement` for every item in the array `array_expression`. The item in the array is assigned to the variable `variable`

### Notes

`array_expression` is evaluated before the loop is executed and assigned to a hidden variable. So changes to `array_expression` will not affect the execution of the loop.

If `array_expression` is actually a scalar, the loop will execute once with the scalar value assigned to `variable`.

If `array_expression` is a multi-division vector with 2 or more divisions, the loop will execute for each division and the division will be assigned to `variable`.

A [foreachdiv statement](scriptlanguage_statementscommands.htm#scriptlanguage_statementscommands__foreachdivstatement) can alternatively be used. This will execute only once for a single division vector.

## Foreachdiv Statement

These are of the form:

```
foreachdiv variable array_expression
statement
next
```

The foreachdiv statement works with [Multi-division vectors](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__multidivisionvectors).

The foreach statement executes `statement` for every division in the array `array_expression`. The division in the array is assigned to the variable `variable`.

## Script Statement

A script statement is a call to execute another script. Scripts are executed initially by typing their name at the command line (or if the script has .sxscr extension, the .sxscr can be omitted) or selecting a key or menu which is defined to do the same. Scripts can also be called from within scripts in which case the call is referred to as *script statement*. Note that a script may not call itself.

## Exit Statement

There are four types:

```
exit while
exit for
exit script
exit all
```

`exit while` forces the innermost while loop to terminate immediately. Control will pass to the first statement after the terminating `endwhile` or `loop`.

`exit for` does the same for for-loops.

`exit script` will force the current script to terminate. Control will pass to the statement following the call to the current script.

`exit all` will abort all script execution and control will return to the command line.

|  |  |  |
| --- | --- | --- |
| [◄ Expressions](scriptlanguage_expressions.htm) |  | [Accessing Simulation Data ▶](scriptlanguage_accessingsimulationdata.htm) |
