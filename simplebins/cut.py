import math
import numbers
import pandas as pd
import numpy as np

VALID_OUTPUTS = [
        "index",
        "floor",
        "ceiling",
        "center",
        "label",
    ]

def _cut(
    x: float | None, 
    binwidth: float,
    output: str,
    origin: float, 
    ) -> float:
    
    # ignore NAs
    if pd.isna(x):
        return x
    
    # transform numbers
    if isinstance(x, numbers.Number):
        bin_index = math.floor((x - origin) / binwidth)
        
        if output == "index":
            return bin_index
        
        floor = bin_index * binwidth + origin

        if output == "floor":
            return floor

        ceiling = floor + binwidth

        if output == "ceiling":
            return ceiling
        
        if output == "center":
            return (floor + ceiling) / 2
        
        if output == "label":
            return f"{floor} <= x < {ceiling}"

    # Raise error if x is not a number or a NA
    raise ValueError(f"Wrong input for x. It must be a number or a missing value. {x} is not.")


def cut(
    x: float | list | pd.Series | pd.DataFrame | None, 
    binwidth: float,
    origin: float = 0,
    output: str = "floor",
    ) -> float | list | pd.Series | pd.DataFrame | None:
    """
    Assigns numeric values to equal-width bins.

    Parameters
    ----------
    x : float, int, list of numbers, pandas.Series or pandas.DataFrame
        The input data to be binned. Missing values (e.g. NaN) are preserved.
    binwidth : float
        The width of each bin. Must be a positive number.
    origin : float, default=0
        The reference point from which bins start.
    output : {'index', 'floor', 'ceiling', 'center', 'label'}, default='floor'
        Determines the bin representation:
        - 'index'   : Zero-based bin index
        - 'floor'   : Lower edge of the bin
        - 'ceiling' : Upper edge of the bin
        - 'center'  : Center point of the bin
        - 'label'   : Human-readable label, e.g. "10 <= x < 15"

    Returns
    -------
    Union[float, str, list, pandas.Series, pandas.DataFrame]
        Transformed input with values replaced by their corresponding bin representation.

    """
    
    if not isinstance(binwidth, (int, float)):
        raise ValueError("The argument binwidth must be int or float.")
    
    if binwidth <= 0:
        raise ValueError("Binwidth must be > 0.")
    
    if not isinstance(origin, (int, float)):
        raise ValueError("The argument origin must be int or float.")
    
    if output not in VALID_OUTPUTS:
        raise ValueError(f"The argument output must be one of {VALID_OUTPUTS}")
    
    # number
    if isinstance(x, numbers.Number):
        return _cut(x=x, origin=origin, binwidth=binwidth, output=output)
    
    # list
    elif isinstance(x, list):
        return [_cut(x=number, binwidth=binwidth, origin=origin, output=output) for number in x]
    
    # pandas series
    elif isinstance(x, pd.Series):
        return x.apply(lambda number: _cut(
            x=number, 
            binwidth=binwidth,
            origin=origin,
            output=output, 
            ))
    
    # pandas dataframe
    elif isinstance(x, pd.DataFrame):
        return x.map(lambda number: _cut(
            x=number, 
            binwidth=binwidth,
            origin=origin,
            output=output, 
        ))
    
    # NAs
    elif pd.isna(x):
        return x
    
    else:
        raise ValueError(
            f"The argument x has to be one of: number, list, pandas.Series, pandas.DataFrame. {x} is not."
        )