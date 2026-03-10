# LocalDeclAll Command

Declare all variables in a script to be local.

Variables can be defined as global by assigning the variable in the form: global:name. Subsequently the variable may be accesed with the name alone without the global: prefix. The LocalDeclAll command disables this behaviour and thus requires all global variables to be accessed using their fully qualified name. The name used alone will access a local variable of that name.

For example, in the following fragment, the variable var1 will be displayed as having the value 20 as the global variable is reassigned in the second Let command

```
Let global:var1 = 10
Let var1=20
Show global:var1
```

In the following, var1 will be displayed as having the value 10 which is the original assignment. The second Let command in this case will assign a new local variable var1 distinct from the global variable

```
LocalDeclAll
Let global:var1 = 10
Let var1=20
Show global:var1
```

LocalDeclAll remains in force for the current script. It is not inherited by scripts that it calls nor does it continue in force in the calling script after exit.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_localdeclall) | | |
| [◄ LoadStyleSheet](com_loadstylesheet.htm) |  | [MakeAlias ▶](com_makealias.htm) |
