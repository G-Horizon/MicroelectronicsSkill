# SetUnits Command

Changes physical type of  *vector-name*  to  *physical-type* . Physical type may be any of the following:

|  |  |
| --- | --- |
| 'unknown' | '?' |
| 'Voltage' | 'V' |
| 'Current' | 'A' |
| 'Time' | 'Secs' |
| 'Frequency' | 'Hertz' |
| 'Resistance' | 'Ohm' |
| 'Conductance' | 'Sie' |
| 'Capacitance' | 'F' |
| 'Inductance' | 'H' |
| 'Energy' | 'J' |
| 'Power' | 'W' |
| 'Charge' | 'C' |
| 'Flux' | 'Vs' |
| 'Volt???MATH???^2???MATH???' | 'V???MATH???^2???MATH???' |
| 'Volt???MATH???^2???MATH???/Hz' | 'V???MATH???^2???MATH???/Hz' |
| 'Volt/rtHz' | 'V/rtHz' |
| 'Amp???MATH???^2???MATH???' | 'A???MATH???^2???MATH???' |
| 'Amp???MATH???^2???MATH???/Hz' | 'A???MATH???^2???MATH???/Hz' |
| 'Amp/rtHz' | 'A/rtHz' |
| " (means dimensionless - see notes) |  |

Note that this command uses non-standard abbreviations for seconds (Secs), Hertz (Hertz) and Siemens (Sie). These are compatible with the  [Units](func_units.htm)  function. The  [UnitsNew](func_unitsnew.htm)  function returns the standard abbreviations 's', 'Hz' and 'S' respectively.

The physical type of a vector is the name of the physical quantity it represents e.g. Voltage, Current, Time etc. This is used by graph plotting routines to set appropriate units for axes. To set a vector as dimensionless, use the following syntax:

```
SetUnits vector {"}
```

```
SetUnits <vector-name> <units>
```

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_setunits) | | |
| [◄ SetSymbolOriginVisibility](com_setsymboloriginvisibility.htm) |  | [Shell ▶](com_shell.htm) |
