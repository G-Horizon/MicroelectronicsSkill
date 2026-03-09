# DefineSaturableTxDialog Function

Opens a dialog box to define a saturable transformer.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Core material info |
| 2 | string array | Yes |  | Part number info |
| 3 | real array | Yes |  | Winding ratios |
| 4 | real array | Yes |  | Initial values |

#### Argument 1

Array of core material specifications. Each element is a string has the format:

```
name;model_name;saturation_flux_density
```

#### Argument 2

Array of core part specifications. Each element is a string which has the format:

```
name;Ae;Le;Ue;material_name
```

#### Argument 3

Array of turns ratios.

#### Argument 4

Real array with up to 9 elements that defines the initial values for the controls in the dialog box, as defined in the following table:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Primary number of turns |
| 1 | Selected material index (into arg 1) |
| 2 | Selected part index (into arg 2). -1 for manual entry. |
| 3 | Number of primaries |
| 4 | Number of secondaries |
| 5 | Effective area |
| 6 | Effective length |
| 7 | Ue |
| 8 | Coupling factor |

### Returns

Return type: real array

The return value is a real array containing the user's selection. The definition of the values is identical to that for argument 4 as described above.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definesaturabletxdialog) | | |
| [◄ DefineRipperDialog](func_defineripperdialog.htm) |  | [DefineShiftRegDialog ▶](func_defineshiftregdialog.htm) |
