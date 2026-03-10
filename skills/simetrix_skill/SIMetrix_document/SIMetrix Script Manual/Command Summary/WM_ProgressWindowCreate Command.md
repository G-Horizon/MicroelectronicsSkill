# WM\_ProgressWindowCreate Command

Creates a progress window, with given number of steps and identifier.

The window contains a progress bar that increments each time  [WM\_ProgressWindowReport](com_wm_progresswindowreport.htm)  is called.

```
WM_ProgressWindowCreate <number steps> <identifier> [/title <window title>] [/caption <caption message>] [/message <progress message>]
```

### Parameters

|  |  |
| --- | --- |
| /caption | The caption of the window. This appears above the progress bar and cannot be changed after the window is created. |
| /message | The status message of the progress window. This appears below the window and can be changed after the window is created. |
| /title | The title of the window. |
| number steps | The number of times  [WM\_ProgressWindowReport](com_wm_progresswindowreport.htm)  has to be called to make the progress bar be completely full. |
| identifier | The identifier that will be used to reference the progress window on update and close calls. |

### See Also

* [WM\_ProgressWindowClose](com_wm_progresswindowclose.htm)
* [WM\_ProgressWindowCloseAll](com_wm_progresswindowcloseall.htm)
* [WM\_ProgressWindowReport](com_wm_progresswindowreport.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_wm_progresswindowcreate) | | |
| [◄ WM\_ProgressWindowCloseAll](com_wm_progresswindowcloseall.htm) |  | [WM\_ProgressWindowReport ▶](com_wm_progresswindowreport.htm) |
