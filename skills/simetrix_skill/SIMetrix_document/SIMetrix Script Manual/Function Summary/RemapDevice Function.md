# RemapDevice Function

Map SIMetrix simulator device to model name and level number.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Mapping spec |

#### Argument 1

Comma delimited list of name=value pairs providing spec to map a device type to its model and level number. Name=value pairs are defined as follows:

### Returns

### Notes

All device models (that is the binary code that implements the device equations) have an internal name that is used to uniquely identify it, but this name is not used externally. Instead.MODEL statements use their own name (e.g. nmos, pnp) coupled with an optional LEVEL parameter to define the actual device referred to. For example, the MOS level 3 device is referred internally as "MOS3" but the .MODEL statements use the names NMOS or PMOS and set the LEVEL parameter to 3. The mapping between NMOS and LEVEL 3 to "MOS3" is defined in an internal table which can be modified by this function. A call to this function can add new entries to the table so providing additional methods of accessing a device. It can also modify existing entries to point to a new device. To modify an existing mapping, you only need to provide ModelName, Device and Level values. The modelname and level must point to an existing combination that is already in use, e.g. ModelName=D and Level=1, and device would then be set to the new device that this combination is to point to, e.g. Diode3. So this is what the spec would be:

```
RemapDevice('ModelName=D,Level=1,Device=Diode3')
```

The above would make level 1 diodes use the same model as level=3. Here is another example:

```
RemapDevice('ModelName=R,Level=0,Device=HspiceRes')
```

Level=0 is the level value when the LEVEL parameter is not specified. In the case of resistors, no .MODEL statement is required at all, so the above line will change the default model used for all resistors to the Hspice model instead of the native SIMetrix model. It is also possible to add a new mapping in which case the level and modelname parameters must be currently unused. Also when creating a new mapping the 'Letter' parameter must be specified. 'Letter' is the first letter of the component reference traditionally used to identify the type of device in SPICE netlists. For example 'Q' refers to BJTs and 'D' refers to diodes. For example, the following entries define LEVEL=69 as a valid level for accessing the PSP 1.03 model:

```
RemapDevice('ModelName=nmos,Level=69,Device=psp103_n,report=on')
```

Note that two entries are required in order to support both n-channel and p-channel devices. The above doesn't change the existing level it adds an additional level. Both the original level number and 69 will be accepted and be equivalent. When defining a new mapping the letter must be specified and usually this should be the letter conventionally used for the class of device. If defining a new mapping for a MOSFET, the letter 'M' should be used, for a diode the letter 'D' should be used and so on. However, the letters, 'N', 'P', 'W', 'U' and 'Y' maybe used as well for any type of device.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_remapdevice) | | |
| [◄ RelativePath](func_relativepath.htm) |  | [RemoveConfigCollection ▶](func_removeconfigcollection.htm) |
