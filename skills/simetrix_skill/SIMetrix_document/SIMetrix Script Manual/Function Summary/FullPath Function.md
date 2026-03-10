# FullPath Function

Returns the full path name of the specified relative path and reference directory.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | relative path name |
| 2 | string | No | Current working directory | reference directory |

### Returns

Return type: real

### See Also

* [RelativePath](func_relativepath.htm)
* [SplitPath](func_splitpath.htm)

### Example

```
FullPath('amplifier.sch', 'c:\simulation\circuits') =
c:\simulation\circuits\amplifier.sch

FullPath('..\amplifier.sch', 'c:\simulation\circuits') =
c:\simulation\amplifier.sch
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_fullpath) | | |
| [◄ FourierWindow](func_fourierwindow.htm) |  | [gamma ▶](func_gamma.htm) |
