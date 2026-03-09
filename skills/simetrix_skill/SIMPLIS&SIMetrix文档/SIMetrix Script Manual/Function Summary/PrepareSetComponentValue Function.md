# PrepareSetComponentValue Function

Configures  [SetComponentValue](func_setcomponentvalue.htm)  function to define how parameters are stored on schematic instances. The definition is in the form of two tables, 'parameter definitions' and 'implicit defaults'. The 'parameter definitions' defines how parameters are stored. The 'implicit defaults' defines parts that have an implicit value. For example, a resistor value can be set by simply defining the reference of the device without a parameter name. This is known as an implicit value.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Table data |
| 2 | string | Yes |  | Table type |

#### Argument 1

This is either the 'parameter definitions' or the 'implicit defaults' depending on the setting of argument 2. Usually PrepareSetComponentValue is called twice, once for the 'parameter definitions' and again for the 'implicit defaults'.

The 'parameter definitions' table is a List of semi-colon delimited definitions to describe how to handle parameters stored in K=V pairs - as opposed to individual properties. The system looks at the VALUESCRIPT property and its arguments. It scans down the table until it finds an entry that matches the script called by VALUESCRIPT. VALUESCRIPT is the property used by nearly all parts that defines the script that is used to edit the part.

The following table describes the 'parameter definitions' table:

|  |  |
| --- | --- |
| **Field number** | **Description** |
| 1 | 'writeprop' OR 'defaultnames'. If 'writeprop' definition defines the name of the property that will hold the modified K=V values. If 'defaultnames', definition defines how you obtain the names of the parameters and their default values. |
| 2 | VALUESCRIPT script name |
| 3 | VALUESCRIPT argument to examine. 0 means the VALUESCRIPT arguments are ignored |
| 4 | 'Direct' OR 'Model'. Only relevant of Field 1 is 'defaultnames'. 'Direct' means the default names data is read from the property specified as the argument in Field 3 or its default in Field 6 (see below). 'Model' means it is read from the params: or vars: list in the device's model file. |
| 5 | Boolean can be true/false, off/on or yes/no. Specifies whether the F11 window can be searched for the model. Only relevant if Field 4 is set to 'Model' |
| 6 | Default value for argument. If the argument to VALUESCRIPT is not present (or if Field 3 is zero) use this value instead |
| 7 | Boolean. Means that a property of the same name will also be written as well as the K=V parameter |

The following table describes the 'implicit defaults' table:

|  |  |
| --- | --- |
| **Field number** | **Description** |
| 1 | Property,Value pair. The value can use wildcards \* and ? |
| 2 | The property or parameter that is read or set by an implicit action on this device. What happens is that the address is appended with this value when a match is found. So if the user entered U1.R1 where R1 is a resistor, the action will be the same as entering U1.R1.<contents-of-field2>. (And that is how this is implemented internally) |
| 3 | Boolean: If true read or write the first unlabelled value only and leave the rest alone |

#### Argument 2

Specifies what the contents of argument 1 defines. Either 'parameter\_definitions' or 'implicit\_defaults'

### Returns

Return type: real

Number of table entries entered

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_preparesetcomponentvalue) | | |
| [◄ PinName](func_pinname.htm) |  | [PreProcessNetlist ▶](func_preprocessnetlist.htm) |
