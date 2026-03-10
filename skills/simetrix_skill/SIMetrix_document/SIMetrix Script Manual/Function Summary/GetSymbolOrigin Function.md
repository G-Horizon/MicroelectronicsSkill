# GetSymbolOrigin Function

Returns the location of the origin point of the symbol currently open in the symbol editor. The origin is the location of the point 0,0 on the symbol. It is in turn located at a position relative to the  *reference point* . The reference point is an absolute location defined by the symbol's geometry. If the symbol has pins, it is the top left of a rectangle that encloses all the pins. Otherwise it is the top left of a rectangle that encloses all the segments.

### Arguments

No arguments

### Returns

Return type: real array

Two element real array. Index 0 is the x-coordinate while index 1 is the y-coordinate. The units are 100 per grid square.

### See Also

* [SetOrigin](com_setorigin.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsymbolorigin) | | |
| [◄ GetSymbolInfo](func_getsymbolinfo.htm) |  | [GetSymbolPropertyInfo ▶](func_getsymbolpropertyinfo.htm) |
