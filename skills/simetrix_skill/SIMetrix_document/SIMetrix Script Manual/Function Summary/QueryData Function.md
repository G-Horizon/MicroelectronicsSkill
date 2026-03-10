# QueryData Function

Filters a list of data items according to search criteria.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Data |
| 2 | string array | Yes |  | Filter |

#### Argument 1

The data to be filtered. This should consist of an array of strings comprising semicolon delimited fields. The filter supplied in argument 2 matches each field to certain criteria and returns the data in the output if those criteria are satisfied.

#### Argument 2

Filter to determine if data in arg 1 is passed to the output. The filter consists of one or more semi-colon delimited lists which can be combined in Boolean combinations. Each of the lists is compared with the input data for a match and if the resulting Boolean expression is true, the data item is accepted and passed to the return value. Wild cards '\*' and '?' may be used in any field. The system is best explained with examples.

Suppose a data item in arg 1 is as follows,

```
IRFI520N;nmos_sub;X;NMOS;;;;SIMetrix
```

and the filter supplied in arg 2 is:

```
*;*;X;*;*;*;*;SIMetrix
```

This will match successfully. The third and last fields are the same in both the data and the filter and the remaining filter fields are the '\*' wild card which means that anything will be accepted in the corresponding data field. With the following filter, however, the data will not be accepted:

```
*;*;X;*;*;*;*;SIMPLIS
```

Here the last field doesn't match.

In the above simple examples, only one filter list has been supplied. However, it is possible to use more sophisticated filters consisting of multiple lists combined using Boolean operators. Boolean operators are specified with the key words:

* \ OR
* \ AND
* \ XOR
* \ NOT

These can be used to make a Boolean expression using "reverse polish" notation. Here is an example:

```
['*;nmos;*;*;*;*;*;SIMetrix',
'*;nmos_sub;*;*;*;*;*;SIMetrix', '\OR']
```

This will accept any data where the last field is 'SIMetrix' and the second field is either 'nmos' or 'nmos\_sub'. Note that the keyword '\ OR' is applied after the filter lists. As well as the '\*' wild card, the '?' may also be used. '?' matches only a single character whereas '\*' matches any number of characters. For example:

```
?mos
```

Would match 'pmos' as well as 'nmos'. It would also match any other four letter word that ended with the three letters 'mos'.

### Returns

Return type: string array

String array of length up to but not exceeding the length of argument 1. Contains all arg 1 items that match the filter as explained above.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_querydata) | | |
| [◄ PWLDialog](func_pwldialog.htm) |  | [RadioSelect ▶](func_radioselect.htm) |
