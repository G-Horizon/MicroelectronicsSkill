# MLRidgeRegressionFit Function

Performs a ridge regression based line fit to a set of data, producing a polynomial curve that fits the data.

Given a set of training parameters and observations (x and y values) along with a parameter controlling the smoothness of the required output, the function returns a set of values that make up a curve that fits to the parameters and observations.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | Training parameters (x values) |
| 2 | real array | Yes |  | Training observations (y values) |
| 3 | real array | Yes |  | Polynomial |
| 4 | real array | Yes |  | Regularisation parameter |
| 5 | real array | Yes |  | Result parameters (x values) |

#### Argument 1

The parameters for the training data. This would normally be the values on the x-axis of a graph. The values must be ordered from lowest to highest value.

#### Argument 2

The observations for the training data. This would normally be the values on the y-axis of a graph.

#### Argument 3

The degree of polynomial to fit the data to.

#### Argument 4

Parameter that controls how smooth the fit to the data will be. Value must be 0-positive, where the smoothness of the fit increases as the parameter increases.

At the extremes, a value of 0 produces a resulting that will try to pass through all given data points, subject to the flexibility within the polynomial chosen, whilst a value tending towards infinity produces a single straight line through the whole of the data.

#### Argument 5

The parameters to fit the resulting curve to.

### Returns

Return type: real array

Vector the same length as parameter 5  *(Result parameters (x values))*  , with fitted values for each parameter in order.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_mlridgeregressionfit) | | |
| [◄ MkVec](func_mkvec.htm) |  | [MLSplineFit ▶](func_mlsplinefit.htm) |
