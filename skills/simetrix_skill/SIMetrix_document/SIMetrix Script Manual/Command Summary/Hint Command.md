# Hint Command

Displays a message box intended to be used to provide hints to the user. The box contains a check box allowing the user to choose not to receive such hints again.

```
Hint [/help help-context] [/id id] [/icon info|warn|error|question] message
```

### Parameters

|  |  |
| --- | --- |
| /help | If specified, the box will show a help button which will display the help topic specified by  *help-context* . This is used in some internal scripts but has limited user application. |
| /icon | Controls the icon displayed in the hint box. This may be one of:  |  |  | | --- | --- | | info | An icon showing the letter 'i' indicating that this message is for information only. This is the default. | | warn | An icon showing an exclamation mark in a yellow triangle indicating that the message is a warning | | error | An icon showing a cross in a red background indicating an error condition. This is usually inappropriate for a hint, but is included for completeness. | | question | An icon showing a question mark indicating a question. Currently the hint box is not interactive so the usefulness of this is limited. | |
| /id | Identifier used to identify hint for the purposes of saving the redisplay status controlled by the "Don't show this message again" check box . If not supplied, a default will be used derived from the message text. This is satisfactory in most cases and there is rarely ever a need to use this switch. |
| message | Message to be displayed. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_hint) | | |
| [◄ HighlightWidget](com_highlightwidget.htm) |  | [HourGlass ▶](com_hourglass.htm) |
