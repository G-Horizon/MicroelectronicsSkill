# XMLOpenElement Command

Opens the XML element and sets it as the current focus level.

```
XMLOpenElement /index [idx] /tag [tag-name] <reference>
```

### Parameters

|  |  |
| --- | --- |
| /index | Chooses the element based on the index number, as defined by  [XMLGetElements](func_xmlgetelements.htm) . |
| /tag | Chooses the element based on the tag name. If there are multiple tags with the same name, it opens the first one, unless index is defined, then it uses that index position in the elements of the type requested. |
| reference | Reference for the XML document. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_xmlopenelement) | | |
| [◄ XMLNew](com_xmlnew.htm) |  | [XMLOpenFile ▶](com_xmlopenfile.htm) |
