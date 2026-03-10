# OpenSchem Command

Reads a schematic file a draws it in a new schematic window. If the schematic is already open, it will be brought into view.

```
OpenSchem [/cd] [/readonly] [/backup] filename
```

### Parameters

|  |  |
| --- | --- |
| /backup | Restore temporary backup file. Same as normal restore except:   * The 'modified' flag is restored to its state when the file was saved. Normally the 'modified' flag is cleared. * The pathname is restored to the path of the original file (if any) not the path of the backup file. * This command assumes that the original file was saved as a backup. * This switch is used for the save/restore session feature and for recovering auto-saved schematics after an unexpected program exit. |
| /cd | If specified, the directory holding  *filename*  is made current. |
| /readonly | Opens schematic in read-only mode. When opened in this mode, the file is not locked so that other users may open the file and write to it. If the file is already opened in non-readonly mode by another user, this switch must be specified in order to be able to open the file. |
| filename | The name of the file to load the schematic from. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_openschem) | | |
| [◄ OpenRawFile](com_openrawfile.htm) |  | [OpenScript ▶](com_openscript.htm) |
