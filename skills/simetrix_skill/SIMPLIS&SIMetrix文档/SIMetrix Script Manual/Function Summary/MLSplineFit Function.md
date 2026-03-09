# MLSplineFit Function

Performs a spline based line fit to a set of data.

Given a set of training parameters and observations (x and y values) along with a parameter controlling the smoothness of the required output, the function returns a set of values that make up a curve that fits to the parameters and observations.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | Training parameters (x values) |
| 2 | real array | Yes |  | Training observations (y values) |
| 3 | real array | Yes |  | Smoothness parameter |
| 4 | real array | Yes |  | Result parameters (x values) |

#### Argument 1

The parameters for the training data. This would normally be the values on the x-axis of a graph. The values must be ordered from lowest to highest value.

#### Argument 2

The observations for the training data. This would normally be the values on the y-axis of a graph.

#### Argument 3

Parameter that controls how smooth the fit to the data will be. Value must be 0-positive, where the smoothness of the fit increases as the parameter increases.

At the extremes, a value of 0 produces a result made up of straight lines between each training point in order, whilst a value tending towards infinity produces a single straight line through the whole of the data.

#### Argument 4

The parameters to fit the resulting curve to.

### Returns

Return type: real array

Vector the same length as parameter 4  *(Result parameters (x values))*  , with fitted values for each parameter in order.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_mlsplinefit) | | |
| [◄ MLRidgeRegressionFit](func_mlridgeregressionfit.htm) |  | [MLVector ▶](func_mlvector.htm) |
