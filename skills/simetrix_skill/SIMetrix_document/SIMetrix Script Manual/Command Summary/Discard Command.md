# Discard Command

Frees up memory used for vectors. This does not destroy the vectors, just removes any copies that reside in RAM. The data is always stored on disc and can be recovered to RAM when needed.

```
Discard [/vec <vecname>] | [<groupname>]
```

### Parameters

|  |  |
| --- | --- |
| /vec | If specified  *vecname*  specifies a single vector. |
| groupname | Name of group data is to be discarded. Use current group if omitted. |

### Notes

It is rare that this command is needed but may be useful if you are running long simulations and the data generated is so large that a great deal of disk swapping is taking place. The vectors created by the simulator are initially stored in a file. If they are needed - usually for plotting a graph - the data is copied to memory. Once the data has been copied to memory, it will stay there until the group to which the vector belongs is destroyed. Simply closing the graph that used the data will not free up the memory as it is assumed that the data may be needed again and the process of reading from the disk can be time consuming. If the data is very large it will consume a lot of memory which can have adverse consequences. The discard command deletes the data stored in memory for all vectors in the specified group or a single vector if `/vec` is specified. It does  *not*  delete the vectors altogether as they are still stored on disc in the temporary file. After discarding a group, it is still possible to plot all vectors that it contains.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_discard) | | |
| [◄ Detach](com_detach.htm) |  | [Display ▶](com_display.htm) |
