# SetOrigin Command

Sets the origin of the current symbol.

```
SetOrigin <x> <y>
```

### Parameters

|  |  |
| --- | --- |
| x, y | The co-ordinates of the origin in units of 100 per grid square. The origin is placed relative to a location defined by the top left of a rectangle that encloses all the pins of the symbol. |

### Notes

The symbol's origin is a reference point used to define the location of all the elements of the symbol. In the majority of applications the position of the origin is immaterial as long as it does not change once an instance of the symbol has been placed on a schematic. If a new symbol is created from scratch to replace an old one, its origin would have to be maintained and this command would be needed for this. In practice, however, the user would usually modify an existing symbol in which case the origin would be maintained automatically.

### See Also

* [GetSymbolOrigin](func_getsymbolorigin.htm)
* [SetSymbolOriginVisibility](com_setsymboloriginvisibility.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_setorigin) | | |
| [◄ SetHighlight](com_sethighlight.htm) |  | [SetPinPrefix ▶](com_setpinprefix.htm) |
