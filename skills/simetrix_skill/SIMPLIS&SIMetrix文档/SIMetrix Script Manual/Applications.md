# User Interface

A full description of the user interface is outside the scope of this manual. Instead, in this section, we provide a few pointers on how to go about finding how a particular feature works so that it can be altered or adapted.

In this topic:

## User Defined Key and Menu Definitions

Virtually the entire user interface is accessed through menus, keyboard keys or tool bar buttons all of which may be redefined, deleted or replaced. The only parts of the UI which are not accessible are the mouse keys. These have fixed definitions and may not be modified by the user.

In principle it is possible to define completely new menus or/and toolbars which bear no similarity with the built-in definitions. A more normal use of menu, button and key redefinition would probably be to add a special function or perhaps to delete some unused items.

Menus are defined using the command [DefMenu](com_defmenu.htm) and keys can be defined with the [DefKey](com_defkey.htm). To define toolbars and buttons, see  [Creating and Modifying Toolbars](applications_creatingmodifyingtoolbars.htm) . Commands to define new user interface elements such as menus are usually placed in the [Startup Script](scriptlanguage_executingscripts.htm#scriptlanguage_executingscripts__startupscript).

Key definitions may be *context sensitive*. That is, the definition is dependent on which type of window is currently active.

## Rearranging or Renaming the Standard Menus

The standard menu definitions are loaded from the built in script 'menu' when the program first starts. The source for all built in (or internal) scripts can be found on the install CD the latest version of which may be downloaded from our web site (http://www.simetrix.co.uk). To modify any of the standard menus, you need to modify the 'menu' script. For details on how to modify internal scripts, see  [Modifying Internal Scripts](applications_userinterface.htm#applications_userinterface__modifyinginternalscripts) .

When editing menu.sxscr, please note the following:

* Each menu definition must occupy a single line.
* Menus are created in the order they appear in the script. To change the order, simply rearrange the lines.
* You can disable a menu definition by putting a '\*' as the first character of the line. This makes it easy to later undelete it.

## Menu Shortcuts

These are keys which activate defined menus. The key name is displayed to the right of the menu text. All menu definitions may have shortcuts specified using the `/shortcut` switch for the [DefMenu](com_defmenu.htm) command. A potential problem arises if the same key is used for a shortcut and a key definition using [DefKey](com_defkey.htm). If this happens, the DefKey definition takes precedence.

## Editing Schematic Component Values

When you press F7 or select the schematic popup menu Edit Value/Model the internal script 'value' is called. 'value' is a complicated script that identifies the type of component that is selected and performs an action appropriate for it. However the first thing this script does is find out if the component (or components) selected have a *valuescript* property. If it does then that script is called. This feature is used by all types of component developed since release 3 but some older devices are handled differently.

If you wish to modify the behaviour for a particular component type when F7 is pressed, first check to see if it has a *valuescript* property. If it has you can edit the script that it calls or change the property's value to call a different one. If it hasn't you can add such a property and provide a script for it.

There are two other properties associated with component values. These are *incscript* and *decscript*. These increment and decrement a components value when the shift-up and shift-down keys are pressed. Currently only the resistors, capacitor, inductor and potentiometer symbols use this property but you can add your own to any other symbol.

## Modifying Internal Scripts

The SIMetrix user interface is implemented with about 550 internal (or built-in) scripts. These are built in to the executable file but can be bypassed so that their function can be changed. The code for all of these scripts can be found on the installation CD in directory script/builtin. The procedure for replacing an internal script is very straightforward. Simply place a script with the same name but with the extension .sxscr in the built-in script directory. The location of this directory is set in the file locations sheet of the options dialog box (menu File|Options|General...). On Windows this is usually *<SIMetrix root>/support/biscript*. SIMetrix always searches this directory first when executing an internal script.

|  |  |  |
| --- | --- | --- |
| [◄ Zoom](com_zoom.htm) |  | [Custom Curve Analysis ▶](applications_customcurveanalysis.htm) |
