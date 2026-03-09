# ReadLogicCompatibility Command

Reads a file to define the compatibility relationship between logic families. For an example of a compatibility table, see the file COMPAT.TXT which you will find in the CD in directory Docs/Manuals/Supporting Files. This file is actually identical to the built-in definitions except for the "UNIV" family which cannot be redefined.

Please refer to the "Digital Simulation" chapter of the Simulator Reference Manual for full details on logic compatibility tables.

**File format**

The file format consists of the following sections:

* Header
* In-Out resolution table
* In-In resolution table
* Out-Out resolution table

*Header:*  The names of all the logic families listed in one line. The names must not use the underscore ('\_') character.

*In-Out resolution table:*  A table with the number of rows and columns equal to the number of logic families listed in the header. The columns represent outputs and the rows inputs. The entry in the table specifies the compatibility between the output and the input when connected to each other. The entry may be one of three values:

|  |  |
| --- | --- |
| OK | Fully compatible |
| WARN | Not compatible but would usually function. Warn user but allow simulation to continue. |
| ERR | Not compatible and would never function. Abort simulation. |

*In-In resolution table*  A table with the number of rows and columns equal to the number of logic families listed in the header. Both column and rows represent inputs. The table defines how inputs from different families are treated when they are connected. The entry may be one of four values:

|  |  |
| --- | --- |
| ROW | Row take precedence |
| COL | Column takes precedence |
| OK | Doesn't matter. (Currently identical to ROW) |
| ERR | Incompatible, inputs cannot be connected. |

*Out-out resolution table*  A table with the number of rows and columns equal to the number of logic families listed in the header. Both column and rows represent outputs. The table defines how outputs from different families are treated when they are connected. The entry may be one of four values:

|  |  |
| --- | --- |
| ROW | Row take precedence |
| COL | Column takes precedence |
| OK | Doesn't matter. (Currently identical to ROW) |
| ERR | Incompatible, outputs cannot be connected. |

```
ReadLogicCompatibility <filename>
```

### Parameters

|  |  |
| --- | --- |
| filename | Logic compatbility file |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_readlogiccompatibility) | | |
| [◄ RD](com_rd.htm) |  | [RebuildSymbols ▶](com_rebuildsymbols.htm) |
