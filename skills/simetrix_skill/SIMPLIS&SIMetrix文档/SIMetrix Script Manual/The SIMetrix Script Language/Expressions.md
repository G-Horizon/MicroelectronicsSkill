# Expressions

An expression is a sequence of variable *names*, *constants*, *operators* and *functions* that can be evaluated to yield a result. Expressions are required by four commands: [Let](com_let.htm), [Curve](com_curve.htm), [Plot](com_plot.htm) and [Show](com_show.htm) and they are also used in  [*braced substitutions*](scriptlanguage_expressions.htm#scriptlanguage_expressions__bracedsubstitutions) ) and *if statements*, *while statements* and *for statements*. This section describes expression syntax and how they are evaluated.

In this topic:

## Operators

operators. Available operators are:

### Arithmetic

```
+ - * / ^ %
```

'%' performs a remainder function

### Relational

```
< > == <= >=
```

Important: a single '=' can be used as equality operator if used in an *if* or *while* statement. In other places it is an assignment operator and '==' must be used for equality.

### Logical

```
AND, OR, NOT,
&& || !
```

Note: `AND`, `OR`, `NOT` are equivalent to `&& || !` respectively.

### String

```
&
```

'&' concatenates two strings.

### Operator Precedence

When calculating an expression like `3+4*5`, the 4 is multiplied by 5 first then added to 3. The multiplication operator - '\*' - is said to have higher precedence then the addition operator - '+'. The following lists all the operators in order of precedence:

```
( ) [ ]
Unary - + NOT !
^
* / %
+ -
< > <= >= ==
AND &&
OR ||
&
=
,
```

### Notes

1. A single '=' is interpreted as '==' meaning equality when used in if statements and while statements and has the same precedence.
2. Parentheses have the highest precedence and are used in their traditional role to change order of evaluation. So `(3+4)*5` is 35 whereas `3+4*5` is 23.
3. The comma ',' is used as a separator and so has the lowest precedence.

## Functions

Functions are central to SIMetrix scripts. All functions return a value and take zero or more arguments. The [sqrt](func_sqrt.htm) function for example takes a single argument and returns its square root. So:

```
Let x = sqrt(16)
```

will assign 4 to x.

Functions are of the form:

```
function_name( [ argument, ...] )
```

### Examples

Function taking no arguments:

```
NetName()
```

function taking two arguments:

```
FFT( vout, 'Hanning')
```

Functions don't just perform mathematical operations like square root. There are functions for string processing, functions which return information about some element of the program such as a schematic or graph, and there are user interface functions. Complete documentation on all available functions is given in  [Function Reference](functionsummary.htm) .

## Braced Substitutions

A braced substitution is an expression enclosed in curly braces '{' and '}'. When the script interpreter encounters a braced substitution, it evaluates the expression and substitutes the expression and the braces with the result of the evaluation - as if it had been typed in by the user. Braced substitutions are important because, with the exception of [Let](com_let.htm), [Show](com_show.htm), [Plot](com_plot.htm) and [Curve](com_curve.htm), commands cannot accept expressions as arguments. For example, the [Echo](com_echo.htm) command displays in the message window the text following the `Echo`. If the command `Echo x+2` was executed, the message `x+2` would be displayed not the result of evaluating x+2. If instead the command was `Echo { x+2 }` the result of evaluating `x+2` would be displayed.

If the expression inside the braces evaluates to a vector each element of the vector will be substituted. Note that the line length for commands is limited (although the limit is large - in excess of 2000 characters) so substituting vectors should be avoided unless it is known that the vector does not have many elements.

Braced substitutions may not be used in the control expression for conditional statements, while loops and for loops. For example, the following is not permitted

```
if {netname()} < 4.56 then
```

To achieve the same result the result of the braced expression must be assigned to a variable e.g.:

```
let v = {netname()}
if v < 4.56 then
```

## Bracketed Lists

These are of the form

```
[ expression1, expression2, ...]
```

The result of a bracketed list is a vector of length equal to the number of expressions separated by commas. There must be at least one expression in a bracketed list - an empty list is not permitted. For example:

```
Let v = [3, 5, 7]
```

assigns a vector of length `3` to `v`. So `v[0]=3`, `v[1]=5` and `v[2]=7`. The expressions in a bracketed list may be any type, as long they are all the same. The following for example, is illegal:

```
Let v = [3, 'Hello', 'World']
```

The second element is of type string whereas the first is real. The following example is however legal:

```
Let v = ['3', 'Hello', 'World']
```

3 which is real has been replaced by '3' which is a string.

## Type Conversion

Most functions and operators expect their arguments to be of a particular type. For example the `+` operator expects each side to be a numeric (real or complex) type and not a string. Conversely, the `&` operator which concatenates strings naturally expects a string on each side. The majority of functions also expect a particular type as arguments, although there are some that can accept any type.

In the event that the type presented is wrong, SIMetrix will attempt to convert the value presented to the correct type. To convert a numeric value to a string is straightforward, the value is simply represented in ASCII form to a reasonable precision. When a string is presented but a numeric value is required, the string is treated as if it were an expression and is evaluated. If the evaluation is successful and resolves to the correct type the result is used as the argument to the operator or function. If the evaluation fails for any reason an error message will be displayed.

## Aliases

An *alias* is a special type of string. Alias strings hold an expression which is always evaluated when used. The simulator outputs some of its data in alias form to save memory and simulation time. For example, the currents into subcircuit pins are calculated by adding the currents of all devices within the subcircuit connected to that pin. If its efficient to do so, this current is not calculated during simulation. Instead the expression to perform that calculation is stored as an alias so that it can be calculated if needed. Aliases may also be created using the [MakeAlias](com_makealias.htm) command.

|  |  |  |
| --- | --- | --- |
| [◄ Variables, Constants and Types](scriptlanguage_variablesconstantstypes.htm) |  | [Statements and Commands ▶](scriptlanguage_statementscommands.htm) |
