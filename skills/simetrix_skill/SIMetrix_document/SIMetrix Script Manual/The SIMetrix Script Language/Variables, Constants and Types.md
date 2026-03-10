# Variables, Constants and Types

SIMetrix scripts, like all computer programs, process data stored in variables. Variables may hold real, complex or string data and may be scalar - possessing only a single value - or single dimension arrays called vectors.

In this topic:

## Variable names

Variables names must be a sequence of characters but the first must be non-numeric. Any character may be used except:

```
\ " & + - * / ^ < > ' @ { } ( ) [ ] ! % ; : |=
```

and spaces.

Although it is legal the following names should be avoided as they are statement keywords:

* all
* do
* else
* elseif
* end
* endif
* endwhile
* exit
* for
* foreach
* foreachdiv
* if
* loop
* next
* script
* step
* then
* to
* while

## Types

Variables may have real, complex or string type. Real and complex are self-explanatory. Strings are a sequence of ASCII characters of any length.

SIMetrix does not have an integer type. Although all numbers are represented internally as floating point values, the format used permits integers to be represented exactly up to values of about ???MATH???2^{52}???MATH???.

## Constants

These can be real complex or string. Real numbers are represented in the usual way but may also contain the engineering suffixes:

|  |  |
| --- | --- |
| a | ???MATH???10^{-18}???MATH??? |
| f | ???MATH???10^{-15}???MATH??? |
| p | ???MATH???10^{-12}???MATH??? |
| n | ???MATH???10^{-9}???MATH??? |
| u | ???MATH???10^{-6}???MATH??? |
| m | ???MATH???10^{-3}???MATH??? |
| k | ???MATH???10^{+3}???MATH??? |
| Meg | ???MATH???10^{+6}???MATH??? |
| G | ???MATH???10^{+9}???MATH??? |
| T | ???MATH???10^{+12}???MATH??? |

Note that engineering suffixes *are not case sensitive*. A common mistake is to use 'M' when what was meant was 'Meg'. 'M' is the same as 'm'.

Complex numbers are represented in the form:

(*real*, *imaginary*)

Strings are a sequence of text characters enclosed in single quotation marks. Single quotation marks themselves are represented by two in succession.

### Example 1: Real

```
2.3
4.6899
45
1e-3
1.2u
```

### Example 2: Complex

```
(1,1)      means 1+i
(2.34,10)  means 2.34+10i
```

### Example 3: String

```
'this is a string'
'This is a "string"'
```

## Creating and Assigning Variables

Variables are created and assigned using the `Let` command. For example:

```
Let x=3
```

assigns the value 3 to the variable x. Note that `Let` is not optional as it is in most forms of Basic.

You can also assign complex numbers and strings e.g.

```
Let x=(5,1)
Let s='This is a string'
```

All of the above are *scalar* that is they contain only one value. Variables may also be single dimension arrays called *vectors*. Vectors are described below.

## Special Characters

Some characters have a special meaning and if entered into a string literal will not work correctly. Characters affected are newline, tab, semi-colon, single and double quotation and open and close brace characters.

Open and close brace characters ('{' and '}') and semi-colon (';') may be included in a string literal by enclosing the whole string with *double* quotation marks. (There is more information here [Quotes: Single or Double](scriptlanguage_variablesconstantstypes.htm#scriptlanguage_variablesconstantstypes__quotessingledouble)).

Single and double quotation marks can be included by doubling them up. However, this can be inconvenient and an alternative method is to assign a variable with the special character using the [Chr](func_chr.htm) function. This method is also the only way to enter a tab character into a literal string. For example:

```
Let tab = chr(9)
Let string = 'This is a tab ' & tab & ' character'
```

This method can be used to enter new line characters (chr(10)) and also single quotes (chr(39)), double quotes (chr(34)) and semi-colons (chr(59))

## Vectors

Vectors can be created using a *bracketed list*, with a function that returns a vector or by the simulator which creates a number of vectors to represent node voltages and device currents. A bracketed list is of the form:

```
[ expression1, expression2, ...]
```

E.g.

```
let v = [1, 3, 9]
```

These are described in more detail in the section on [Bracketed Lists](scriptlanguage_expressions.htm#scriptlanguage_expressions__bracketedlists). Functions and simulator vectors are described in following sections.

Vectors, like other variables may also contain strings or complex numbers but all the elements must be the same *type*.

Individual elements of vectors may be accessed using square brackets: '[' and ']'. E.g.

```
let v = [1, 3, 9]
let a = v[2]
```

`a` is assigned 9 in the above example. Index values start at 0 so the first element (1) is `v[0]`.

It is also possible to assign values to individual elements e.g.

```
let v[2] = 5
```

In which case the value assigned must have the same type (i.e. real, complex or string) as the other elements in the vector.

Vectors, like other variables may also contain strings or complex numbers but all the elements must be the same type.

## Scope of Variables, Global Variables

Variables created using the [Let](com_let.htm) command are only available within the script where the `Let` command was executed. The variable is destroyed when the script is completed and it is not accessible to scripts that the script calls. If, however, the `Let` command was called from the command line, the variable is then *global* and is available to all scripts until it is explicitly deleted with the [UnLet](com_unlet.htm) command. If a global variable needs to be created within a script, the variable name must be preceded by `global`: For example:

```
Let global:result = 10
```

`global:result` will be accessible by all scripts and from the command line. Further it will be permanently available until explicitly deleted with `UnLet`. After the variable has been created with the `global:` prefix, it can subsequently be omitted. For example in:

```
Let global:result = 10
Show result
Let result = 11
Show result
```

will display

```
result=10
result=11
```

in the message window. The variable `result` will be available to other scripts whereas if the `global:` prefix had been left off, it would not. Although it is not necessary to include the `global:` prefix except when first creating the variable, it is nevertheless good practice to do so to aid readability of the script.

## Empty Values

Many functions return *empty* values (also known as empty vectors or zero-length vectors) when they are unable to produce a return value. An empty value contains no data. An empty value can be tested with the [length](func_length.htm) function which will return 0. Most other functions and operators will yield an error if presented with an empty value. The exceptions are

* [JoinStringArray](func_joinstringarray.htm)
* [JoinVectors](func_joinvectors.htm)
* [NumElems](func_numelems.htm)
* [SetDifference](func_setdifference.htm)
* [SetIntersect](func_setintersect.htm)
* [SetSymmetricDifference](func_setsymmetricdifference.htm)
* [SetUnion](func_setunion.htm)

Empty values should not be confused with empty strings. The latter is explained in the next section.

## Empty Strings

An empty string is one that has no characters. An empty string can be entered on a command line with the character sequence:

```
{"}
```

Empty strings are not the same as empty values. An empty value has no data at all and will result in an error if supplied to any function other than the Length function.

## Quotes: Single and Double

Single quotation marks ( \textquotesingle\ ) and double quotation marks ( " ) both have a special, but different, meaning in SIMetrix and in the past this has been the source of much confusion. Here we explain what each means and when they should be used. Single quotes are used to signify a text string in an expression. Expressions are used as arguments to the [Plot](com_plot.htm), [Curve](com_curve.htm), [Let](com_let.htm) and [Show](com_show.htm) commands, they are used in braced substitutions and also as the tests for `if`, `for` and `while` statements. These are the only places where you will find or need single quotes. Double quotes are used in commands to bind together words separated by spaces or semi-colons so that they are treated as one. Normally spaces and semi-colons have a special meaning in a command. Spaces are used to separate arguments of the command while semi-colons terminate the command and start a new one. If enclosed within double quotes, these special meanings are disabled and the text within the quotes is treated as a single argument to the command. Double quotes are often used to enclose strings that contain spaces (see example) but this doesn't necessarily have to be the case.

### Examples

```
Let PULSE_SPEC = 'Pulse 0 5 0 10n 10n 1u 2.5u'
```

In the above line we are assigning the variable `PULSE_SPEC` with a string. This is an expression so the string is in single quotes. `Let` is a command but it is one of the four commands that take an expression as its argument.

```
Prop value "Pulse 0 5 0 10n 10n 1u 2.5u"
```

`Prop` is a command that takes a number of arguments. The second argument is the value of a property that is to be modified. In the above line, the new property value, `Pulse 0 5 0 10n 10n 1u 2.5u` has spaces in it so we must enclose it double quotation marks so that the command treats it as a single string. If there were no quotes, the second argument would be just `Pulse` and the remainder of the line would be ignored. If an argument contains no spaces or semi-colons then no quotes are necessary although they will do no harm if present.

### Where you need both single and double quotes

There are situations where both single and double quotes are needed together. In some of the internal scripts you will find the [Scan](func_scan.htm) function used to split a number of text strings separated by semi-colons. The second argument to Scan is a string and must be enclosed in single quotation marks. But this argument is also a semi-colon which, despite being enclosed in single quotes, will still be recognised by the command line interpreter as an end-of-command character. So this must be enclosed in double quotes. The whole expression can be enclosed in double quotes in this case.

### If you need a literal quote

If you need a string that contains a double or single quote character, use two of them together.

|  |  |  |
| --- | --- | --- |
| [◄ A Tutorial](scriptlanguage_atutorial.htm) |  | [Expressions ▶](scriptlanguage_expressions.htm) |
