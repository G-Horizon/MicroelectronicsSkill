# Creating and Modifying Toolbars

From version 5, SIMetrix allows the complete customisation of toolbars. You can modify the definitions of existing toolbars and buttons, as well as create new toolbars and new tool buttons. This section explains how.

In this topic:

## Modifying Existing Toolbars and Buttons

You can rearrange the button layout of existing toolbars by modifying the 'Set' option variables that define them. In the case of the schematic component buttons, this can be done via a simple GUI. See menu View|Configure Toolbar... .

For other toolbars use the command [Set](com_set.htm) to reassign the buttons. The following table shows the name of the 'Set' variable to use for each one.

|  |  |
| --- | --- |
| **'Set' Variable Name** | **Toolbar** |
| ComponentButtons | SimetrixSchemToolBar |
| SIMPLISComponentButtons | SimplisSchemToolBar |
| SchematicMainButtons | SimetrixSchemToolBar and SimplisSchemToolBar |
| SchematicFileButtons | SimetrixSchemToolBar |
| SchematicFileButtonsSIMPLIS | SimplisSchemToolBar |
| SchematicProbeButtons | SimetrixSchemToolBar and SimplisSchemToolBar |
| GraphMainButtons | GraphMain |
| SymbolFileButtons | SymbolMain |
| SymbolMainButtons | SymbolMain |

The 'Set' variable should be set to a value consisting of a semi-colon delimited list of valid button names. For a list of pre-defined buttons, see [Pre-defined Buttons](applications_creatingmodifyingtoolbars.htm#applications_creatingmodifyingtoolbars__predefinedbuttons).

To determine the current definition, use the [GetOption](func_getoption.htm) function with the 'Set' variable name as described in the table above. For example:

```
Show GetOption('SchematicFileButtons')
```

will display in the message window the current definition for the SchematicFile tool bar.

You can then use the [Set](com_set.htm) command to add a new button.

You can also use [UnSet](com_unset.htm) command to restore a toolbar to its default setting. E.g.

```
Unset SchematicFileButtons
```

will restore the schematic file toolbar to just three buttons without the new schematic button.

Any changes made using the [Set](com_set.htm) command will not take place until you restart SIMetrix/SIMPLIS. If desired you can force a rebuild of the toolbar for each window type by executing the following built-in scripts:

|  |  |
| --- | --- |
| Schematic | update\_schematic\_toolbar |
| Symbol editor | update\_symbol\_toolbar |
| Graph | update\_waveform\_toolbar |

## Redefining Button Commands

You can change the command executed when a button is pressed using the command [DefButton](com_defbutton.htm). This is useful if you want to change the symbol placed for one of the component buttons. For example if you wanted to change one of the NMOS buttons, you could do something like:

```
DefButton NMOS4 "inst /ne my_nmos"
```

redefines the four-terminal NMOS button to place a symbol with name my\_nmos.

You can redefine any of the pre-defined buttons. See [Pre-defined Buttons](applications_creatingmodifyingtoolbars.htm#applications_creatingmodifyingtoolbars__predefinedbuttons) for a complete list.

## Defining New Buttons and Editing Buttons

You can define completely new buttons with your own graphic design and add them to an existing toolbar. The same method can also be used to redefine the graphics for existing buttons.

This is done using the command [CreateToolButton](com_createtoolbutton.htm). These are the steps to take:

1. Create a graphical image for the button. This should be in a windows bitmap (.bmp), portable network graphic (.png) or JPEG (.jpg) format. You can use almost any paint application to do this. But, if you want to define a mask - that is you wish to define transparent areas - then you must use an editor capable of creating 'portable network graphics' (PNG) images.You can make your graphic any size, but we recommend using 64x64.When you have created your image, you should save or copy it to the images directory. This is located at `simetrix-root/support/images`, where `simetrix-root` is the top level directory in the SIMetrix tree.
2. Execute the command [CreateToolButton](com_createtoolbutton.htm). As with menu and key definitions, the definitions created by this command are not *persistent* that is they will be lost when SIMetrix exits. To make permanent definitions, you should place the commands in the start up script. See [Startup Script](scriptlanguage_executingscripts.htm#scriptlanguage_executingscripts__startupscript) for more details.CreateToolButton will not add the button to any toolbar nor does it assign a command to be executed when it is pressed. These operations are described in the following steps.
3. Define a command to be executed when this button is pressed. This is done using the command [DefButton](com_defbutton.htm). Again, this should be place in your startup script.
4. Add the button to a toolbar. See [Modifying Existing Toolbars and Buttons](applications_creatingmodifyingtoolbars.htm#applications_creatingmodifyingtoolbars__modifyingexistingtoolbarsbuttons) to find out how to add this to an existing toolbar. If you wish to create a new toolbar for the new button, see [Creating New Toolbars](applications_creatingmodifyingtoolbars.htm#applications_creatingmodifyingtoolbars__creatingnewtoolbars).

For example, suppose you created a symbol for a diffused resistor and wanted to assign this to a toolbar button that is distinct from the regular resistor button. These are the steps:

1. First you would create a graphical image called, for example, diffres.png. Copy this to the images directory as described above.
2. Execute (or place in startup script):

   ```
   CreateToolButton /class component diffres diffres.png
   "Place Diffused Resistor"
   ```

   (This must all be on one line)This will create a button called 'diffres' that we will refer to in the following steps. The switch `/class component` identifies the button as one that places a component and so will be listed in the GUI based system to edit component toolbars. (See schematic menu View|Configure Toolbar...) . This will make adding the button to a component toolbar a simple operation.
3. Execute (or place in startup script):

   ```
   DefButton diffres "inst /ne diffressym"
   ```

   where diffressym is the name of the schematic symbol created for the diffused resistor.
4. To add to the button to a component toolbar, simply select schematic menu View|Configure Toolbar... You should see 'Place Diffused Resistor' on the left hand side. Select and press *Add* to add to the toolbar, then use the up down buttons to choose a suitable position.

Its a little harder to edit non-component toolbars as there is currently no GUI to perform the operation in step 4 above. For pre-defined toolbars you can obtain the current specification using the [GetOption](func_getoption.htm) function and then add your new button to the resulting value at an appropriate location. Then use the Set command to redefine the toolbar. See [Modifying Existing Toolbars and Buttons](applications_creatingmodifyingtoolbars.htm#applications_creatingmodifyingtoolbars__modifyingexistingtoolbarsbuttons) for more details.

## Creating New Toolbars

To create a completely new toolbar, use the command [CreateToolBar](com_createtoolbar.htm). This will create an empty toolbar.

To add buttons to a new toolbar, you must use the command [DefineToolBar](com_definetoolbar.htm). You can add both pre-defined and user-defined buttons to a custom toolbar.

## Pre-defined Buttons

The following table lists all the buttons that are pre-defined. All of these buttons may be redefined if required.

The bitmaps are embedded in the SIMetrix binary, but can also be found on the install CD in the directory script/images.

|  |  |  |
| --- | --- | --- |
| **Button name** | **Description** | **Bitmap** |
| AsciiFileEditorClose | Close Ascii File | close.png |
| AsciiFileEditorNew | New SIMetrix Schematic | filenew.png |
| AsciiFileEditorOpen | Open Ascii File | open.png |
| AsciiFileEditorSave | Save Ascii File | save.png |
| BiasV | Place Bias Marker | biasv.png |
| CalcAveragePower | Display Average Power/Cycle | avg.png |
| CalcFall | Display Fall Time | falltime.png |
| CalcHighPass3db | Display -3dB Point (High Pass) | 3dbhighpass.png |
| CalcLowPass3db | Display -3dB Point (Low Pass) | 3dblowpass.png |
| CalcRise | Display Rise Time | risetime.png |
| CalcRMS | Display RMS/Cycle | rms.png |
| Capacitor | Place Capacitor | capacitor.png |
| Copy | Duplicate | copy.png |
| Delete | Cut | cut.png |
| DeleteAllCurves | Delete All Curves | deleteall.png |
| DeleteAxis | Delete Axis/Grid | delgrid.png |
| DeleteCurve | Delete Curve | delete.png |
| Detach | Detach | detach.png |
| Diode | Place Diode | diode.png |
| Flip | Flip | flip.png |
| GraphClose | Close Graph | fileclose.bmp |
| GraphNew | New Graph | filenew.png |
| GraphNewCurve | Add Curve | newcurve.png |
| GraphNewFourier | Add Fourier Spectrum Plot | newfourier.png |
| GraphOpen | Open Graph | fileopen.bmp |
| GraphSave | Save Graph | filesave.bmp |
| Ground | Place Ground | ground.png |
| HideCurves | Hide Selected Curves | hide.png |
| IGBT | Place IGBT | igbt.png |
| Inductor | Place Inductor | inductor.png |
| IProbe | Place Current Probe | iprobeplaced.png |
| IProbeInteractive | Probe Pin Current (interactive) | iprobe.png |
| ISource | Place Current Source | isource.png |
| LogicDefinitionEditorClose | Close Logic Definition | close.png |
| LogicDefinitionEditorNew | New SIMetrix Schematic | filenew.png |
| LogicDefinitionEditorOpen | Open Logic Definition | open.png |
| LogicDefinitionEditorSave | Save Logic Definition | save.png |
| Mirror | Mirror | mirror.png |
| MoveCurve | Move Curve to Selected Axis/Grid | movecurve.png |
| NetlistEditorClose | Close Netlist | close.png |
| NetlistEditorNew | New SIMetrix Schematic | filenew.png |
| NetlistEditorOpen | Open Netlist | open.png |
| NetlistEditorSave | Save Netlist | save.png |
| NetlistRun | Run SIMetrix Netlist | run.png |
| NewAxis | New Axis | newaxis.png |
| NewCurve | Add Curve | newcurve.png |
| NewFourier | Add Fourier Spectrum Plot | newfourier.png |
| NewGrid | New Grid | newgrid.png |
| NJFET | Place N-channel JFET | njfet.png |
| NMOS3IC | Place 3 term N-channel MOSFET | nmos\_ic3.png |
| NMOS4 | Place 4 term N-channel MOSFET | nmos\_ic.png |
| NMOS | Place N-channel MOSFET | nmos.png |
| NPN | Place NPN Transistor | npn.png |
| Opamp | Place Opamp | opamp.png |
| PJFET | Place P-channel JFET | pjfet.png |
| PMOS3IC | Place 3 term P-channel MOSFET | pmos\_ic3.png |
| PMOS4 | Place 4 term P-channel MOSFET | pmos\_ic.png |
| PMOS | Place P-channel MOSFET | pmos.png |
| PNP | Place PNP Transistor | pnp.png |
| Print | Print | print.png |
| PSU | Place PSU | psu.png |
| Redo | Redo | redo.png |
| Resistor | Place Resistor (Box shape) | resistor.png |
| ResistorZ | Place Resistor (Z shape) | resz.png |
| Rotate | Rotate | rotate.png |
| SatInd | Place Saturable Inductor | sat\_ind.png |
| SatTx | Place Saturable Transformer | tx\_sat.png |
| SchemClose | Close Schematic | close.png |
| SchemFind | Search | find.png |
| SchemNew | New SIMetrix Schematic | filenew.png |
| SchemOpen | Open Schematic | open.png |
| SchemSave | Save Schematic | save.png |
| SchemSaveAll | Save All Schematics | saveall.png |
| SCR | Place Thyristor | scr.png |
| ScriptEditorClose | Close Script | close.png |
| ScriptEditorNew | New SIMetrix Schematic | filenew.png |
| ScriptEditorOpen | Open Script | open.png |
| ScriptEditorSave | Save Script | save.png |
| ScriptRun | Run Script | run.png |
| ShellNewSchem | New Schematic | filenew.png |
| ShowCurves | Show Selected Curves | show.png |
| SIMextrixOptions | Options | options.png |
| SimPause | Pause Simulation | pause.png |
| SIMPLISOptions | SIMPLIS Options | simplis\_options2.png |
| SimRunSchem | Run Schematic | run.png |
| SymbolClose | Close Symbol | close.png |
| SymbolCut | Cut Selected | cut.png |
| SymbolDetach | Detach Selected | detach.png |
| SymbolDuplicate | Duplicate Selected | copy.png |
| SymbolFlip | Flip Selected | flip.png |
| SymbolMirror | Mirror Selected | mirror.png |
| SymbolNew | New Symbol | filenew.png |
| SymbolOpen | Open Symbol | open.png |
| SymbolRedo | Redo | redo.png |
| SymbolRotate | Rotate Selected | rotate.png |
| SymbolSave | Save Symbol | save.png |
| SymbolUndo | Undo | undo.png |
| SymbolWireMode | Segment Mode | pencil.png |
| SymbolZoomBox | Zoom to Rectangle | zoomrect.png |
| SymbolZoomIn | Zoom In | zoomin2.png |
| SymbolZoomOut | Zoom Out | zoomout2.png |
| TextEditorClose | Close Text | close.png |
| TextEditorNew | New SIMetrix Schematic | filenew.png |
| TextEditorOpen | Open Text | open.png |
| TextEditorSave | Save Text | save.png |
| TitleCurve | Change Curve Name | curvetitle.png |
| TL | Place Transmission Line | tl.png |
| Tx | Place Transformer | tx.png |
| Undo | Undo | undo.png |
| UndoZoom | Undo Zoom | undo.png |
| VerilogAEditorClose | Close Verilog-A | close.png |
| VerilogAEditorNew | New SIMetrix Schematic | filenew.png |
| VerilogAEditorOpen | Open Verilog-A | open.png |
| VerilogAEditorSave | Save Verilog-A | save.png |
| VerilogHDLEditorClose | Close Verilog HDL | close.png |
| VerilogHDLEditorNew | New SIMetrix Schematic | filenew.png |
| VerilogHDLEditorOpen | Open Verilog HDL | open.png |
| VerilogHDLEditorSave | Save Verilog HDL | save.png |
| VProbe | Place Voltage Probe | vprobeplaced.png |
| VProbeInteractive | Probe Voltage (interactive) | vprobe.png |
| VSource | Place Voltage Source | vsource.png |
| Waveform | Place Waveform Generator | vsig.png |
| WebBack | Back | back.png |
| WebForward | Forward | forward.png |
| WebNew | New SIMetrix Schematic | filenew.png |
| WebReload | Reload | reload.png |
| WebSIMextrixOptions |  | options.png |
| WebSIMPLISOptions |  | simplis\_options2.png |
| WebStop | Stop | stop.png |
| Wire | Wire Mode | pencil.png |
| Zener | Place Zener Diode | zener.png |
| ZoomFull | Zoom to Fit | zoomfull.png |
| ZoomFullGraph | Fit Window | zoomfull.png |
| ZoomIn | Zoom In | zoomin2.png |
| ZoomOut | Zoom Out | zoomout2.png |
| ZoomRect | Zoom Box | zoomrect.png |
| ZoomXAuto | Fit Width | zoomwidth.png |
| ZoomYAuto | Fit Height | zoomheight.png |

|  |  |  |
| --- | --- | --- |
| [◄ Schematic Template Scripts](applications_schematictemplatescripts.htm) |  | [Custom Dialog Boxes ▶](applications_customdialogboxes.htm) |
