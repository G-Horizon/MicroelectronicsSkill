# Errors

Loosely, there are two types of error, syntax errors and execution errors.

In this topic:

## Syntax Errors

Syntax errors occur when the script presented deviates from the language rules. An endif missing from an *if statement* for example. SIMetrix will attempt to find all syntax errors - it won't abort on the first one - but it will not execute the script unless the script is free of syntax errors. Sometimes one error can hide others so that fixing syntax errors can be an iterative process. On many occasions SIMetrix can identify the details of the error but on some occasions it is unable to determine anything other than the fact that it isn't right. In this instance a "Bad Statement" error will be displayed. These are usually caused by unterminated *if*, *while* or *for* statements. Although in many cases SIMetrix can correctly identify an unterminated statement, there are some situations where it can't.

Note that a syntax error in an expression will not be detected until execution.

## Execution Errors

These occur when the script executes and are mostly the result of a command execution failure or an expression evaluation failure.

|  |  |  |
| --- | --- | --- |
| [◄ User Interface to Scripts](scriptlanguage_userinterfacescripts.htm) |  | [Executing Scripts ▶](scriptlanguage_executingscripts.htm) |
