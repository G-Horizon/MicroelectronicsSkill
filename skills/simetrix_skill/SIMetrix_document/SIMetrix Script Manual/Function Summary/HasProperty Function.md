# HasProperty Function

Determines whether a particular instance possesses a specified property.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name |
| 2 | string | No |  | Property name to identify |
| 3 | string | No |  | Property value to identify |
| 4 | real | No | -1 | Schematic ID |

#### Argument 1

Property name.

#### Argument 2

Property name to use to identify the instance to check. If present, this argument along with argument 3, identify the instance to be tested for property ownership. If only this argument is present and not argument 3, any instance possessing the property it specifies will be tested. If neither this or argument 3 are present, the currently selected instance will be tested.

If more than instance is identified one of them will be tested but there are no rules to determine which instance will be used.

An example of this property would be 'handle'.

#### Argument 3

Property value to use to identify the instance to check check. If present, this argument along with argument 2, identify the instance to be tested for property ownership. If neither this or argument 3 are present, the currently selected instance will be tested.

If more than instance is identified one of them will be tested but there are no rules to determine which instance will be used.

An example of this property would be a handle name, such as 'I2'.

#### Argument 4

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: real

Outcome of test: TRUE (1) or FALSE (0). If no instance matches argument 2 and 3, an empty value will be returned.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_hasproperty) | | |
| [◄ HasLogSpacing](func_haslogspacing.htm) |  | [HaveFeature ▶](func_havefeature.htm) |
