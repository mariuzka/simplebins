import math
import numbers

def _validate_input(
    x,
    step,
    output,
    origin,
    ):
    if not isinstance(x, numbers.Number):
        raise ValueError(f"The argument x has to be a number. {x} is not.")
    
    if not isinstance(step, numbers.Number) or step <= 0:
        raise ValueError(f"The argument step has to be a number > 0. {step} is not valid.")
    
    if output not in {"index", "floor", "ceiling", "mid", "label"}:
        raise ValueError(f"The argument output must be one of 'index', 'floor', 'ceiling', 'mid', or 'label'. {output} is not valid.")
    
    if not isinstance(origin, numbers.Number):
        raise ValueError(f"The argument origin has to be a number. {origin} is not.")
    

def _transform(
    x: float, 
    step: float,
    output: str = "floor",
    origin: float = 0, 
    validate_input: bool = True,
    ):

    if validate_input:
        _validate_input(x=x, step=step, output=output, origin=origin)
    
    group_index = math.floor((x - origin) / step)
    
    if output == "index":
        return group_index
    
    floor = group_index * step

    if output == "floor":
        return floor

    ceiling = floor + step

    if output == "ceiling":
        return ceiling
    
    if output == "mid":
        return (floor + ceiling) / 2
    
    if output == "label":
        return f"{floor} <= x < {ceiling}"


def to_group(
    x: float | list, 
    step: float,
    output: str = "floor",
    origin: float = 0,
    validate_input: bool = True,
    ):
    
    """
    Assigns a number or a list of numbers to defined numerical groups (bins).

    Parameters
    ----------
    x : float or list of float
        A single number or list of numbers to be grouped.
    step : float
        Width of each group (must be > 0).
    output : str, default="floor"
        Defines the output format:
        - "floor" : lower bound of the group
        - "ceiling" : upper bound of the group
        - "mid" : midpoint of the group
        - "index" : zero-based index of the group
        - "label" : human-readable label (e.g. "10 <= x < 15")
    origin : float, default=0
        Starting point for the first group. Groups expand from here in steps.
    validate_input : bool, default=True
        If True, performs type and range checks on inputs.

    Returns
    -------
    float, str or list
        A single grouped value or a list of grouped values depending on input and `output`.

    Raises
    ------
    ValueError
        If inputs are invalid or of unsupported type.

    Examples
    --------
    >>> to_group(12, step=5)
    10

    >>> to_group(12, step=5, output="label")
    '10 <= x < 15'

    >>> to_group([3, 7, 12], step=5)
    [0, 5, 10]
    """
    
    if isinstance(x, numbers.Number):
        return _transform(x=x, origin=origin, step=step, output=output, validate_input=validate_input)
    
    elif isinstance(x, list):
        return [
            _transform(x=number, step=step, output=output, origin=origin, validate_input=validate_input)
            for number in x
        ]
    raise ValueError(f"The argument x has to be a number or list. {x} is not.")