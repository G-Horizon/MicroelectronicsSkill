# Introduction

SIMetrix features a simple interpreted script language, loosely based on BASIC, in which most of the user interface is written.

This manual provides the means for users sympathetic to the concept of computer programming to develop their own scripts or to adapt the user interface by modifying the internal scripts.

We have identified three main applications for script development although there may be others we haven't thought of. These are:

1. User interface modification perhaps to suit individual taste or for specialised applications.
2. Automated simulations. For example, you may have a large circuit which for which you need to run a number of tests. The simulations take along time so you would like to run them overnight or over a weekend. A simple script can perform this task.
3. Specialised analysis. The curve analysis functions supplied with SIMetrix are all implemented using scripts. You can write your own to implement specialised functionality. Also the goal functions used for performance and histogram analysis are "user defined functions" and are actually implemented as scripts. More goal functions may be added for special applications.

The scripting language is supported by about 776 functions and 322 commands that provide the interface to the SIMetrix core as well as some general purpose functionality.

As well as the built-in functions, a tool kit is available that allows you to develop your own functions in 'C' or 'C++'.

|  |  |  |
| --- | --- | --- |
|  |  | [A Tutorial ▶](scriptlanguage_atutorial.htm) |
