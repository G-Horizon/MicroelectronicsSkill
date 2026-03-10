# ComposeDigital Function

ComposeDigital builds a new vector from a binary weighted combination of digital vectors. It is intended to be used to plot or analyse digital bus signals. The simulator outputs bus signals as individual vectors. To plot a bus signal as a single value - either in numeric or analog form - these individual vectors must be combined as one to create a single value.

Note that ComposeDigital can only process purely digital signals. These are expected to have one of three values namely 0, 1 and 0.5 to represent an invalid or unknown state.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Bus name |
| 2 | real array | No | See notes | Index range |
| 3 | string array | No |  | Options |
| 4 | string | No |  | Wire template |
| 5 | real | No | [0.8,0.9] | Analog thresholds |

#### Argument 1

Signal root name. The function expects a range of vectors to be available in a form defined by the  *wire template*  argument. By default this is in the form  *busname#n*  where  *busname*  is specified in argument 1 while the range of values for  *n*  is specified in argument 2.

#### Argument 2

Index range. The function processes vectors from  *busname#idx\_start*  to  *busname#idx\_end* .  *idx\_start*  and  *idx\_end*  are specified by this argument as a two dimensional array. For example if arg 1 is 'BUS' and arg 2 is [0,3], the function will process vectors:

```
BUS1#0
BUS1#1
BUS1#2
BUS1#3
```

as long all 4 vectors exist. If one or more vectors do not exist the first contiguous set of vectors will be used within the indexes specified. So if BUS1#0 didn't exist, the function would use BUS1#1 to BUS1#3. If BUS1#2 didn't exist, it would use just BUS1#0 and BUS1#1.

Note that the index may not be larger than 31.

#### Argument 3

1 or 2 element string array. Values may be any combination of 'holdInvalid' and 'scale'.

'holdInvalid' determines how invalid states in the input are handled. If the 'holdInvalid' option is specified, they are treated as if they are not present and the previous valid value is used instead. If omitted, invalid states force an output that alternates between -1 or -2. This is to allow consecutive invalid states to be distinguished. For example, suppose there are 4 bits with one bit invalid. If one of the valid bits changes, the end result will still be invalid, but it sometimes desirable to know that the overall state has changed. So, in this case the first invalid state will show as a -1 and the second invalid state will be -2. In any following invalid state, the result will be -1 and so on.

'scale' forces the output to be scaled by the value ???MATH???2^{(-\text{idxend}-\text{idxstart}+1)}???MATH???.

#### Argument 4

Optional wire template used to describe how bus vectors are named. The default value is %BUSNAME%#%WIRENUM% which means that bus vectors are of the form  *busname#n*  where  *busname*  is the name of the bus (argument 1) and  *n*  is the index value. For more details about wire templates, see  [Netlist](com_netlist.htm) .

#### Argument 5

Threshold used to define logic levels for analog signals. Two element array. The first element is the lower threshold and the second element is the upper threshold. If either or both is omitted these values default to 0.8 and 0.9 respectively.

The lower threshold is the value below which an analog signal is considered to be a logic zero. The upper threshold is the value above which an analog signal is considered to be a logic one.

### Returns

Return type: real vector

The return value is a real vector that is the binary weighted sum of the vectors defined by arg 1 and arg 2 but treating invalid values (=0.5) as described above. So, in the example above, the result will be:

BUS1#0 + BUS1#1 \* 2 + BUS1#2 \* 4 + BUS1#3 \* 8.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_composedigital) | | |
| [◄ CompareSymbols](func_comparesymbols.htm) |  | [ConvertFromBase64 ▶](func_convertfrombase64.htm) |
