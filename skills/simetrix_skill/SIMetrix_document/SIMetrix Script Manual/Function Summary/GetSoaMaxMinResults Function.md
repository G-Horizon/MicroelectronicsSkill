# GetSoaMaxMinResults Function

Returns the maximum and minimum values reached for all SOA definitions.

### Arguments

No arguments

### Returns

Return type: string array

Returns an array of strings defining max and min values reached. Each element in the array corresponds to the elements returned by the GetSoaDefinitions function. Each string is of the form:

```
min_val;min_reached_at;max_val;max_reached_at;max_mean
```

Where:

|  |  |
| --- | --- |
| `min_val` | Minimum value reached |
| `min_reached_at` | Time at which the minimum value was reached |
| `max_val` | Maximum value reached |
| `max_reached_at` | Time at which the maximum value was reached |
| `max_mean` | Maximum mean value |

### Notes

This function returns the maximum and minimum values returned for all SOA definitions regardless of whether or not the limits were violated.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsoamaxminresults) | | |
| [◄ GetSoaDefinitions](func_getsoadefinitions.htm) |  | [GetSoaOverloadResults ▶](func_getsoaoverloadresults.htm) |
