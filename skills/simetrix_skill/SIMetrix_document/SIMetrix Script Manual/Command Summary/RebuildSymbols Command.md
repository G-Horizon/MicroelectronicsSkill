# RebuildSymbols Command

The installed symbol library is usually stored in RAM during normal operation. When a symbol is needed, the modified date of original source file is checked and if it has changed, that library file will be reloaded. This happens anyway whenever a symbol is required for any purpose.

RebuildSymbols forces the checking of all stored symbol libraries and any that are out of date will be reloaded from the source file.

There aren't many reasons for using this command. However, it is sometimes useful to call it in the startup script so that the symbols are automatically loaded when the program starts. Normally the symbols aren't loaded until they are first needed and this can introduce a slight delay.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_rebuildsymbols) | | |
| [◄ ReadLogicCompatibility](com_readlogiccompatibility.htm) |  | [Redirect ▶](com_redirect.htm) |
