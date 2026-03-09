# Optimiser

The SIMetrix optimiser can be accessed using the script language and can also be used to control an optimisation process. The latter feature is used to drive SIMPLIS optimiser analyses.

The following diagram shows the structure of the optimiser framework and its interaction with the script language:

|  |
| --- |
|  |
| Accessing Optimiser Definitions |

**Optimiser definition**. This is an internal object which stores the analysis definitions, parameter definitions, measurements and other settings needed to define an optimisation session. It also stores the results of any completed optimisation.

In this topic:

## Accessing Optimiser Definitions

The script language accesses the optimiser definition by obtaining an ID reference to it. The ID is an integer value which a wide range of script functions take as an argument in order to retrieve information about the optimiser or to control an optimisation session. The following functions may be used to obtain an optimiser ID:

|  |  |
| --- | --- |
| **Function Name** | **Description** |
| [OptimiserCreateFromXML](func_optimisercreatefromxml.htm) | Reads an optimiser definition from a file, creates an optimiser definition, then returns the ID to access it |
| [OptimiserCreateFromXMLString](func_optimisercreatefromxmlstring.htm) | Creates an optimiser definition from an XML string then returns the ID to access it |
| [OptimiserWidgetCreateOptDef](func_optimiserwidgetcreateoptdef.htm) | Creates an optimiser definition from the current optimiser GUI then returns an ID to it |
| [OptimiserSimulatorGetDef](func_optimisersimulatorgetdef.htm) | Creates an optimiser definition from the current state of the SIMetrix simulator then returns an ID to it |

## Running an Optimiser Session

It is possible to run an optimiser session from the script language and this is how optimisation for SIMPLIS is achieved. The SIMetrix simulator is able to run optimisation sessions internally defined by netlist commands and does not usually require to be driven by the script language. But this is nevertheless possible if required. In this section the functions needed to drive an optimiser session are described.

|  |  |
| --- | --- |
| **Function Name** | **Description** |
| [OptimiserStart](func_optimiserstart.htm) | Starts an optimiser session |
| [OptimiserFinish](func_optimiserfinish.htm) | Terminates and optimiser session. [OptimiserCloseDef](func_optimiserclosedef.htm) will also implicitly terminate a currently running session |
| [OptimiserGetParameterValues](func_optimisergetparametervalues.htm) | Returns the current values for the parameters |
| [OptimiserParameterLine](func_optimiserparameterline.htm) | Returns a line of text providing the names and current values of the parameters |
| [OptimiserApplySpecification](func_optimiserapplyspecification.htm) | To be called after running all the analyses for an optimiser session. This calculates all the measurements and applies them to the optimiser session. The optimiser algorithm will then calculate new values for the parameters which can be retrieved from [OptimiserGetParameterValues](func_optimisergetparametervalues.htm) |

A typical sequence to run an optimiser session could be:

1. Create optimiser definition and obtain its ID
2. Start optimiser using [OptimiserStart](func_optimiserstart.htm)
3. Get parameter values using [OptimiserGetParameterValues](func_optimisergetparametervalues.htm)
4. Run all simulation analyses using parameter values obtained in step 3. If running a SIMPLIS simulation, pass the optimiser ID to the [PreProcessNetlist](com_preprocessnetlist.htm) command. This will setup the analyses and parameters for the SIMPLIS run. For SIMetrix simulations, the [OptimiserAnalysisLine](func_optimiseranalysisline.htm) function returns all the analysis lines
5. Call [OptimiserApplySpecification](func_optimiserapplyspecification.htm)
6. Test [OptimiserRunning](func_optimiserrunning.htm) to see if optimisation can finish. If so continue to next step. If not go back to step 3
7. Call [OptimiserCloseDef](func_optimiserclosedef.htm) to delete optimiser definition

## Postprocessing Optimiser Results

The following functions can be used to examine the results of an optimiser session:

|  |  |
| --- | --- |
| [OptimiserResults](func_optimiserresults.htm) | Returns optimiser parameter and measurement values for best iteration of specified optimiser definition |
| [OptimiserSimulatorResults](func_optimisersimulatorresults.htm) | Returns optimiser parameter and measurement values for best iteration of most recent SIMetrix simulation optimiser analysis |
| [OptimiserGetIteration](func_optimisergetiteration.htm) | Returns optimiser parameter and measurement values for a specified iteration of specified optimiser definition |
| [OptimiserStatus](func_optimiserstatus.htm) | Returns the currents status of an optimiser session as a string |
| [OptimiserSimulatorStatus](func_optimisersimulatorstatus.htm) | Returns the currents status of the SIMetrix simulation optimiser analysis as a string |
| [OptimiserUserMessage](func_optimiserusermessage.htm) | Returns a message about the current state of the specified optimiser |
| [OptimiserSimulatorUserMessage](func_optimisersimulatorusermessage.htm) | Returns a message about the current state of the SIMetrix simulation optimiser |

|  |  |  |
| --- | --- | --- |
| [◄ Automating Simulations](applications_automatingsimulations.htm) |  | [Schematic Symbol Script Definition ▶](applications_schematicsymbolscriptdefinition.htm) |
