# Schematic Template Scripts

In this topic:

## Overview

Schematic template scripts are a method of performing advanced netlist processing. The TEMPLATE property can be used to customise the netlist entry for a device and it has a number of features that allow quite complex devices to be created. However, the template syntax is not as powerful as a full featured programming language and this makes more complex devices very difficult to implement.

To overcome this the template script feature was developed. With this method a script is called during the netlist generation phase for every instance that possesses a TEMPLATESCRIPT property. A script can then generate the netlist entry for that instance. With this method there is no limit to the complexity of generated devices.

## Defining a Symbol for a Template Script

To use the template script feature, the schematic symbol must specify the script to be called. This can be done in one of two ways:

1. Using the TEMPLATESCRIPT\_TEXT property. Set the value of the property to the full text of the script. It is strongly recommended that the property is protected
2. Using the TEMPLATESCRIPT property. Set the value to the path of an external script. If a full path isn't given (and we recommend that you don't use a full path), SIMetrix will search the directory where the netlist resides followed by the SCRIPT directory for the specified file. If the file is not found, no error message will be output and the device netlist line will be created as if no template script was defined.

If both TEMPLATESCRIPT\_TEXT and TEMPLATESCRIPT are defined, TEMPLATESCRIPT\_TEXT takes precedence.

## When is the Template Script Called?

The template script is called for each instance just before its netlist entry is generated. The REF property of the instance is passed to the script as an argument along with the name of the property used for the template. The script controls the netlist output by calling the [TemplateSetValue](com_templatesetvalue.htm) command.

## The Template Script

The script is passed two string arguments. These are:

1. The value of the REF property of the instance being processed.
2. The name of the template property being used for that instance. This is usually 'TEMPLATE' but for SIMPLIS netlists it is usually 'SIMPLIS\_TEMPLATE'. There is also a netlist option to change the name of the template property.

There are two functions and two commands that are designed specifically for template scripts and indeed they cannot be used anywhere else. The commands and functions are listed below.

The most important command is [TemplateSetValue](com_templatesetvalue.htm). This is what you must use to define the netlist entry. The value supplied to this command defines the template that will be used to create the netlist entry. It can of course provide a completely literal netlist line, but more usually some template keywords would be used.

## Template Commands and Functions

This a brief summary. See the entries in the reference pages for more details.

### TemplateResolve(ref, template)

Performs the same process that is usually done on a template property except that is uses the template that you supply as an argument not the device's template. *ref* is the REF property of device being processed.

### TemplateGetPropValue(ref, prop)

Returns the value of the property *prop*. You should use this function not [PropValues](func_propvalues.htm) to get at property values. It is faster than PropValues() but won't work in regular scripts.

### TemplateEditProperty ref propname propvalue

Edits a property's value. Like TemplateGetPropValue it is much faster than the regular commands but only works in a template script. Note that this command records an instruction to edit a property's value but the instruction will not be actioned until the netlist operation has completed.

### TemplateSetValue ref templatevalue

Changes the value of the template used to create the netlist line currently being compiled. Does *not* change the template property itself.

|  |  |  |
| --- | --- | --- |
| [◄ Non-interactive and Customised Printing](applications_noninteractivecustomisedprinting.htm) |  | [Creating and Modifying Toolbars ▶](applications_creatingmodifyingtoolbars.htm) |
