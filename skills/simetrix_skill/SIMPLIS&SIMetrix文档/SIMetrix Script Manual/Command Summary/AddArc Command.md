# AddArc Command

AddArc is a Symbol Definition Command. It is used to create whole circles and ellipses as well as arcs of circles and ellipses.

The command line arguments are integers describing symbol co-ordinates and all are compulsory. Their meaning is described by the following diagram: ![](../../assets/addarc.png) The arc drawn by this command is a segment of an ellipse specified by a bounding rectangle described by the first four arguments. The last four arguments describe two lines drawn from the centre of the ellipse which specify the start and end of the arc. The arc is drawn anti clockwise.

Note that it is better to define a complete 360 degree circle (or ellipse) as two 180 degree arcs. 360 degree circles, where the start and end are coincident or near coincident do not always work reliably with some printer drivers.

```
AddArc <left> <top> <right> <bottom> <start-x> <start-y> <end-x> <end-y>
```

### See Also

* [Schematic Symbol Script Definition](applications_schematicsymbolscriptdefinition.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addarc) | | |
| [◄ AddAnnotationText](com_addannotationtext.htm) |  | [AddCirc ▶](com_addcirc.htm) |
