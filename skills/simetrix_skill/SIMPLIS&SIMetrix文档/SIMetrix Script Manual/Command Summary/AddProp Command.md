# AddProp Command

AddProp is a Symbol Definition Command. A Property is a text string that can be attached to a symbol which is normally used to describe a special characteristic such as a component reference or value. A comprehensive explanation on properties can be found in  [User's manual/Schematic Editor/Properties](../../user_manual/topics/schematiceditor_properties.htm) .

```
AddProp [/font <font>] [/sel] <name> [<init-value>] [<flags>] [<x-pos> <y-pos>]
```

### Parameters

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /font | Integer from 1 - 8 that specifies one of 8 fonts as follows:  |  |  | | --- | --- | | 1 | Default | | 2 | Caption | | 3 | Free text | | 4 | Annotation | | 5 | User 1 | | 6 | User 2 | | 7 | User 3 | | 8 | User 4 |  The value specified by /font  *fontIndex*  overrides bits 11-13 of the  *flags*  value (see above). |
| /sel | If specified the property is marked "selectable". This means that the selection boundary of the instance which owns the property will be extended to include the property text. This is usually used for symbols that consist only of properties and have no body. |
| /styleOverride | Optional override style for the property. This property will then use this style instead of the infered default style. |
| name | Text string. This can be anything but usually would be one of the special properties which convey a special meaning. A full listing of these is given in the "Schematic Editor" chapter of the User's manual. The important ones are listed below:  |  |  | | --- | --- | | ref | Component reference. | | value | Component value or model name (E.g. BC547) | | model | Single letter to signify type of device. | | netname | If present forces netlister to assign value of value property to all nets connected to component. This property is used by the 'Terminal' component in the Symbols menu. | | schematic\_path | File system pathname for a hierarchical block. | | valuescript | Script that is called when F7 is pressed or the menu Edit Value/Model is selected. |  Some other property names are used in scripts such as biasv which is used by the bias point annotation scripts and is attached to the bias point annotation markers. |
| initvalue | Text string, integer or real. The initial value of the property when the component is first placed. It may be changed subsequently with the Prop command. Examples: the value of a ref property would be something like 'R23' or 'Q4'. The value of a value property maybe '33k' or 'IRF640'. |
| flags | This is the property's attribute flags. It is a single integer that describes a number of attributes for the property. For full information see  [Attribute Flags in the Prop command](com_prop.htm) . |
| x-pos, y-pos | If specified, the property will be placed at an absolute location specified by X\_pos and Y\_pos relative to the reference point of the symbol. The flags value specifies the justification of the text as described in  [Attribute Flags in the Prop command](com_prop.htm) .  If X\_pos and Y\_pos are specified, the text will be displayed vertically in 90 and 270 degree rotated orientations. |

### See Also

* [Schematic Symbol Script Definition](applications_schematicsymbolscriptdefinition.htm)

### Example

```
AddProp ref Q? 26
```

A symbol containing this line in its definition will possess the property of name ref and when first placed on a schematic will have the initial value of Q?. The text Q? will be displayed on the schematic to the right of the symbol when in normal orientation and underneath the symbol when in a ???MATH???90°???MATH??? rotated orientation.

```
AddProp ref Q? 8 100 200
```

The same property as the above example but instead it will be placed 100 units horizontally and 200 unit vertically from the symbol origin. The text of the property will be left justified and positioned vertically referenced to its base line.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addprop) | | |
| [◄ AddPin](com_addpin.htm) |  | [AddProperty ▶](com_addproperty.htm) |
