# Automating Simulations

In this topic:

## Overview

The script language allows you to automate simulations, that is automatically run a number of simulation runs with different component values, test conditions or analysis modes. This section describes the various commands needed to do this.

## Running the Simulator

Simulations are started using the [Run](com_run.htm) command. The Run command runs a netlist not a schematic, so you must first create the netlist using the [Netlist](com_netlist.htm) command. Some notes about the Run command:

1. The /an switch is very useful and allows you to run different analyses on the same circuit without having to modify it. /an specifies the analysis mode instead and overrides any analysis controls (e.g. .TRAN, .DC etc.) in the circuit itself.
2. If the run fails (e.g. due to non-convergence), the script will abort without performing any remaining runs. This behaviour can, however, be inhibited with the /noerr switch which must be placed immediately after the Run word:

   ```
   Run /noerr /file design.net
   ```

   `/noerr` is a general switch that can be applied to any command. See  [Command Switches](scriptlanguage_statementscommands.htm#scriptlanguage_statementscommands__commandswitches)  for details. If you want to test whether or a run was successful, use the [GetLastError](func_getlasterror.htm) function.

## Changing Component Values or Test Conditions

It is likely that in an automated run you will want to change component values or stimulus sources between runs. There are a number of ways of doing this, each with its own advantages and disadvantages.

### Edit Schematic

With this method, the changes are made to the schematic which is then re-netlisted. To do this you need to become familiar with the commands [Prop](com_prop.htm), [Select](com_select.htm) and [Unselect](com_unselect.htm). The procedure is first unselect everything, then select the component you wish to change and then use the Prop command to change the value. The following will change the value of R5 to 12k:

```
Unselect
Select /prop Ref R5
Prop value 12k
```

The second line says "select the component with a Ref property of R5". The third line says "change the value property of the selected component(s) to 12k".

You use the same basic method to edit a stimulus. The following sets V1 to be a pulse source with 0V start, 5V end, zero delay ???MATH???10nS???MATH??? rise and fall times, ???MATH???1\mu S???MATH??? pulse width and ???MATH???2.5\mu S???MATH??? period.

```
Unselect
Select /prop Ref V1
Prop value "Pulse 0 5 0 10n 10n 1u 2.5u"
```

Note the quotation marks.

You must ensure that you re-netlist the circuit before running the simulation.

### Circuit Parameters

Rather than edit the schematic and re-netlist, an alternative is to specify the component values as parameters then vary the parameter using the Let command. To do this, you must first edit the value of the components to be varied so that they are represented as a parameter expression enclosed by curly braces '{' and '}'. Again we will use the example of a resistor R5 whose value we wish to set to 12K. Proceed as follows:

1. Select R5 then press shift-F7. Enter {R5} as the new value.
2. Now in the script you can set the value of R5 with Let e.g.

   ```
   Let global:R5=12k
   ```

   The `global:` prefix is necessary to make the parameter global. Note we have named the parameter 'R5'. This is an obvious choice of parameter name but you could use anything as long as it starts with a letter and consists of letters numbers and the underscore character. (You *can* use other characters but we don't recommend it).You must use curly braces when defining parameters in this manner. Expressions enclosed in quotation marks will not evaluate if they access global parameters. You can however define another parameter using `.PARAM` which will be accessible in quoted expressions. E.g.

   ```
   .PARAM local_R5={R5}
   ```

   `local_R5` as defined above will be accessible in any type of expression in the netlist.

Expressions in curly braces that consist entirely of global parameters or/and constants and which have no local (.PARAM defined) parameters, may also be used to define simulator control values as well as component values. E.g.

```
.TRAN {stop_time}
```

is permissible as long as `stop_time` is defined using the [Let](com_let.htm) command in a script.

An alternative, and somewhat more sophisticated approach is to change the component value to parameter version (e.g. "{R5}") in the script itself. You could then call [Netlist](com_netlist.htm) to create the netlist with parameterised values after which the components can be restored to their original values. That way the schematic is preserved with its original values. To do this correctly you would need to save the original values so that they can be restored. This can be done using the [PropValue](func_propvalue.htm) function which returns the value of a property. The example shown below uses this technique.

### Mulitple Netlists

Conceptually this is probably the simplest approach but not very flexible. Simply create multiple versions of the netlist manually with different file names then run them one at a time.

### Include Files

A method of making complex changes to a netlist is to incorporate part of it in a separate file and include it in the main netlist using the `.INCLUDE` simulator control. A script can then generate the lines in the include file. This can be done using the command [Show](com_show.htm) with the switch `/plain` to write a string array to a file. The string array can be created using the function [MakeString](func_makestring.htm) and built using custom code.

## Organising Data Output from Automated Runs

A feature is available to organise data from multiple automated runs in the same way as for multi-step runs i.e. in the form of multi-division vectors. This is explained in the section describing the command [Run](com_run.htm).

## An Advanced Example - Reading Values from a File

In this section we supply an example of quite an advanced script that runs several simulations on a circuit. On each run a number of components are changed to values read in from a file. This script is general purpose and can be used for any circuit without modification. The script is quite complicated but is well commented throughout to explain in detail how it works. The basic sequence is as follows:

1. Get configuration file name from user
2. Read first line of file. This has the names of the components to be modified
3. Temporarily edit the modifiable components' values to reference a parameter
4. Create netlist
5. Restore original values
6. Read the rest of the file and write the values for each run to an array
7. Run the simulations
8. Clean up before exit

Here is the script. It is also supplied on the install CD under the script directory.

```
** Script to run multiple simulations using component values
** read from a file

** First ask the user for a file
Let filename = GetSIMetrixFile('Text', ['open', 'all'])

if Length(filename)=0 then
** User cancelled box
exit script
endif

** Read the file
Let lines = ReadFile(filename)
Let numLines = Length(lines)

** Test it has enough lines
if numLines<2 then
Echo "Definition file must have at least two lines"
exit script
endif


** We now parse the file and read in the component values
** to the array "compValues". We do the whole file at the
** beginning so that the user will know straight away if it
** has any errors.

** The first line is the list of components that will be changed
Let components=Parse(lines[0])
Let numComponents = Length(components)
if numComponents=0 then
Echo "No component names specified"
Echo "or first line of config file empty"
exit script
endif

** Before we read the rest of the file, we will attempt to
** replace the values of all listed components with parameters
** and netlist the circuit. If any of the components don't
** exist then we will find out here.

** array to store original values so that we can restore
** them later
Let origValues = MakeString(numComponents)
Unselect
Let error = 0
** Scan through list of components
for idx = 0 to numComponents-1
** Select it
Select /prop ref {components[idx]}
if SelectCount()=0 then
** Select count is zero so select failed.
** This means the circuit doesn't have this component
** Output a message and set error flag.
Echo "Cannot find component " {components[idx]}
Let error = 1
else
if HasProperty('value') then
** Save original value to be restored later
Let origValues[idx] = PropValue('value')

** Set value as a parameter of name which is the same
** as the ref
Let newVal = "'{' & PropValue('ref') & '}'"
Prop value {newVal}
else
** The component does not have a value
** property to alter.
Echo "Component " {components[idx]}
Echo "does not have a value"
Let error = 1
endif
endif
Unselect

next idx

** We have changed all the components so now we can netlist
** the circuit
if NOT error then
Netlist design.net
endif

** Once we have the netlist we can restore the original values
Unselect
for idx = 0 to numComponents-1
Select /prop ref {components[idx]}

if SelectCount()<>0 then
if HasProperty('value') then
Prop value {origValues[idx]}
endif
endif

Unselect
next idx

** If we had an error we must now abort
if error then
exit script
endif

** Now read the rest of the file.
** Create an array large enough to hold all the values.
** The values are actually stored as strings.
** That way we can vary
** model names as well as values.
Let compValues = MakeString(numComponents*(numLines-1))
Let error = 0
Let resIdx=0
for lineIdx=1 to numLines-1

** Parse the line into individual values
Let vals = Parse(lines[lineidx])
if Length(vals)<>numComponents then
** A line found with the wrong number of values.
** This is assumed
** to be a mistake unless the line is completely empty
if Length(vals)<>0 then
Echo "Wrong number of values at line " {lineIdx}
Let error = 1
endif
else
** line is OK so write the values to compValues
for idx=0 to numComponents-1
Let compValues[resIdx*numComponents+idx]=vals[idx]
next idx

** Because some lines may be empty we have to use
** a different index counter for the compValues entries
Let resIdx = resIdx+1
endif
next idx

if error then
exit script
endif

** resIdx finishes with the number of non-blank data lines
Let numRuns = resIdx

** Now, at last, we can run the circuit
for idx=0 to numRuns-1
for compIdx=0 to numComponents-1
Let paramName = 'global:' & components[compIdx]
Let {paramName}= compValues[idx*numComponents+compIdx]
next compIdx

Run /file design.net
next idx

** This isn't essential, but it is always best to delete
** global variables when we are finished with them
for compIdx=0 to numComponents-1
Let paramName = 'global:' & components[compIdx]
UnLet {paramName}
next compIdx
```

|  |  |  |
| --- | --- | --- |
| [◄ Custom Curve Analysis](applications_customcurveanalysis.htm) |  | [Optimiser ▶](applications_optimiser.htm) |
