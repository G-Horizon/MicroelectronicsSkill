# Prop Command

Modifies a property value of a schematic component if it exists. If it doesn't exist the property is added.

```
Prop [/hide|/show|/toggle] [/flags <attrib. flags>] [/noAdd] [/showName] [/hideName] [/code 0|1|2|3] [/overridestyle styleName] <name> [<value>]
```

### Parameters

|  |  |
| --- | --- |
| /all | Update properties on all element types (instances, wires and annotation), without this flag only instances will be updated. |
| /code |  |
| /flags | Argument is either a value or a property.  If a value is specified, it changes/assigns the  *flags*  value of the property. The flags value defines the properties attributes. How this number is composed is detailed below.  If a property is specified, it copies the flags value from the specified property so the new/changed property defined by  *property-name*  will have the same flags as the already existing  *property* . The flags define the property's attributes. |
| /handle |  |
| /hide | Make property invisible. |
| /hideName | If specified, the name of the property will be hidden. |
| /hideNew | Hide property value if a new property is being added. If the property already exists, its visibility will remain unchanged. |
| /noAdd | If specified, property will not be added if the instance does not already possess it. |
| /order | Override of order for auto positioned properties. Set this value to be 0 or above to manually adjust property order. Set to -1 to revert back to default ordering. |
| /overridestyle | Style name to use, overriding any styles inheritted from the parent instance. If unset or the value is "", the style of the instance it is associated with will be used. |
| /pinloc | If specified, the property will be positioned at a fixed location next to the pin specified by pinnumber. |
| /prop |  |
| /propval |  |
| /show | Make property visible. |
| /showName | If specified, the name of the property will be made visible along with its value in the form "name=value". |
| /toggle |  |

### Notes

**Attribute flags**  The attributes flag value is a 16 bit number with each bit having a defined function. These bits are defined in the following table:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bit 0,1 | Auto text location for normal orientation: |  |  | | --- | --- | | 00 | Left | | 01 | Top | | 10 | Right | | 11 | Bottom | |
|  | If fixed position, value controls left-right justification: |  |  | | --- | --- | | 00 | left | | 01 | centre | | 10 | right |  Unused set to 0 |
| Bit 3,4 | Auto text location for 90 degree rotated orientation: |  |  | | --- | --- | | 00 | Left | | 01 | Top | | 10 | Right | | 11 | Bottom | |
|  | If fixed position, value controls top-bottom justification, where baseline means the base for upper case characters, the tails of some lower case characters go below the baseline: |  |  | | --- | --- | | 00 | top | | 01 | baseline | |
| Bit 5 | Unused set to 0 |
| Bit 6 | Visibility |  |  | | --- | --- | | 0 | Visible | | 1 | Hidden | |
| Bit 7 | Protected status |  |  | | --- | --- | | 0 | Not protected | | 1 | Protected | |
| Bit 8 | Location method |  |  | | --- | --- | | 0 | Auto (use bits 0,1,3,4 to define) | | 1 | Fixed pos (actual location can only be defined in symbol) | |
| Bit 9 | Text scale method |  |  | | --- | --- | | 0 | Optimum readability | | 1 | Linear | |
| Bit 10 | Does property text define select border |  |  | | --- | --- | | 0 | No | | 1 | Yes | |
| Bits 11-13 | Font index |  |  | | --- | --- | | 0 | Default | | 1 | Caption | | 2 | Free text | | 3 | Annotation | | 4 | User 1 | | 5 | User 2 | | 6 | User 3 | | 7 | User 4 | |
| Bit 14 | Rotated. Property at 90 degrees to symbol orientation. Ignored if location method = auto. |
| Bit 15 | Display property name with value. |
| Bit 16 | Resolve symbolic value if specified. Currently only three are permitted namely, <version>, <date> and <time>. If this flag is set any of the above strings are found in the property, they will be replaced by their value. <version> will be replaced by an integer that is incremented each time the schematic is saved. <date> and <time> will be replaced by the date and time of the schematic file respectively. |

The final value has to be entered as a decimal value. Note that attributes are usually edited using the popup menu Edit Properties... dialog.

### Example

To change a R3's component reference to R4 (i.e. change its  *ref*  property from R3 to R4) select R3 then enter:

```
Prop ref R4
```

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_prop) | | |
| [◄ Probe](com_probe.htm) |  | [Protect ▶](com_protect.htm) |
