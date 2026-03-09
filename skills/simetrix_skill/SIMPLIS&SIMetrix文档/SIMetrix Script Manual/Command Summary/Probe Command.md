# Probe Command

Moves mouse cursor to currently selected schematic, changes cursor shape to a symbol depicting an oscilloscope probe then suspends command execution. When any mouse key is clicked, the cursor shape reverts to normal and command execution is resumed. Probe does not suspend commands executed directly on assignment to keystrokes or menu items. This allows the Cancel command, when assigned to a key or menu, to terminate a probe command. Note that the Probe command completes on both up and down strokes of a mouse key.

```
Probe [/type 1|2|P|N] [<probe-message>]
```

### Parameters

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /type | Alters slightly the cursor shape by adding a single character as follows:  |  |  | | --- | --- | | 1 | adds '1' | | 2 | adds '2' | | P | adds a '+' character | | N | adds a '-' character | |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_probe) | | |
| [◄ PrintSchematic](com_printschematic.htm) |  | [Prop ▶](com_prop.htm) |
