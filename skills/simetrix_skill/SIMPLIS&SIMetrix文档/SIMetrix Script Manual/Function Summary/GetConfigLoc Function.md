# GetConfigLoc Function

Returns the location of the application's configuration settings. In versions prior to version 5, this would be in one of the following forms:

```
REG;registry_root_pathname
```

OR

```
PATH;inifile_pathname
```

If the first form is returned, the settings are stored in the registry. The path of the registry key is HKEY\_CURRENT\_USER  *registry\_root\_pathname* .

If the second form is returned the settings are stored in a file with full path equal to  *inifile\_pathname* .

From version 5, the registry is no longer used for storing settings, so only the second of the two forms will ever be returned.

The return value from GetConfigLoc can be used directly as the value of the `/config_location` switch at the simulator (SIM.EXE) command line. See the "Running the Simulator" chapter in the Simulator Reference Manual for more details.

### Arguments

No arguments

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getconfigloc) | | |
| [◄ GetComponentValue](func_getcomponentvalue.htm) |  | [GetConnectedPins ▶](func_getconnectedpins.htm) |
