# Event Scripts

There are three special scripts that are automatically called by the SIMetrix system in response to user events. These scripts are detailed in the following table:

|  |  |
| --- | --- |
| on\_graph\_anno\_doubleclick | Called when the user double clicks on certain graph objects |
| on\_accept\_file\_drop | Called when a file of directory is dropped on a SIMetrix window. |
| on\_schem\_double\_click | Called when the left mouse button is double clicked in the schematic window. |

All three scripts are defined internally but can be customised if desired. (See [Modifying Internal Scripts](applications_userinterface.htm#applications_userinterface__modifyinginternalscripts)). Details on these event scripts follow.

In this topic:

## on\_graph\_anno\_doubleclick

The script is called when some graph objects are double clicked.

The script is passed two arguments when it is called. The first is the object's ID and the second is specific to the object that is double clicked. Currently the second argument is only used by curves and is set to its division index.

## on\_accept\_file\_drop

This is called when an a file, folder or group or files and/or folders is dropped on the command shell or a schematic or graph window.

Two arguments are passed. The first identifies the window type. This may be one of:

|  |  |
| --- | --- |
| Schematic | Schematic window |
| Graph | Graph window |
| Shell | Command shell |

The second argument contains a list of full path names of the objects dropped. The items are separated by semi-colons.

## on\_schem\_double\_click

Script is called when the left mouse button is double clicked in the schematic window. Two arguments are supplied providing the x and y coordinates of the mouse at the time the double click event occurred.

IMPORTANT: This script is only called if the schematic double click mode is set to 'Edit Selected Component'. See options dialog box (menu File|Options|General...). In 'Classic' mode it is not called at all.

|  |  |  |
| --- | --- | --- |
| [◄ Graph Objects](applications_graphobjects.htm) |  | [User Defined Script Based Functions ▶](applications_userdefinedscriptbasedfunctions.htm) |
