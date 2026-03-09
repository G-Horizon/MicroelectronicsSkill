# ListOptions Command

List all global options to file. Global options are set using the command  [Set](com_set.htm) .

Listing contains one line per option with each line being a semi-colon delimited list in the following form:

```
name;type;default-value
```

where:

|  |  |
| --- | --- |
| *name* | Name of option |
| *type* | Type of option. One of 'bool', 'string' or 'real' |
| *default\_value* | Default value if not set, or if unset using command  [UnSet](com_unset.htm) . |

```
ListOptions <filename>
```

### Parameters

|  |  |
| --- | --- |
| filename | File to receive options |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_listoptions) | | |
| [◄ ListModels](com_listmodels.htm) |  | [LoadModelIndex ▶](com_loadmodelindex.htm) |
