# PreProcessNetlist Command

Pre-processes the specified netlist. The netlist pre-processor was developed for use with the SIMPLIS simulator but is general purpose in nature and may also be used with SIMetrix. Currently this command is automatically called when a SIMPLIS simulation is run from the GUI.

Some SIMetrix models do make use of the pre-processor. For example the multi-level capacitor and inductor models employ the pre-processor. Placing 'vars:' followed by any parameters at the end of a SIMetrix subcircuit call will result in the subcircuit model being pre-processed.

Documentation for the pre-processor language syntax may be found in  [SIMPLIS Reference Manual/Running SIMPLIS/Netlist Preprocessor](../../simplis_reference/topics/runningsimplis_netlistpreprocessor.htm) .

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_preprocessnetlist) | | |
| [◄ Plot](com_plot.htm) |  | [PrintGraph ▶](com_printgraph.htm) |
