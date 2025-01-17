# Functions to become Probe methods

import numpy as np
from ..emd import Metadata




# Kernel generation

def get_kernel(
    self,
    mode = 'flat',
    returncalc = True,
    **kwargs
    ):
    """
    Creates a kernel from the probe for cross-correlative template matching.

    Precise behavior and valid keyword arguments depend on the `mode`
    selected.  In each case, the center of the probe is shifted to the
    origin and the kernel normalized such that it sums to 1. In 'flat'
    mode, this is the only processing performed. In the remaining modes,
    some additional processing is performed which adds a ring of
    negative intensity around the central probe, which results in
    edge-filetering-like behavior during cross correlation. Valid modes
    are:

        - 'flat': creates a flat probe kernel. For bullseye or other
            structured probes, this mode is recommended.
        - 'gaussian': subtracts a gaussian with a width of standard
            deviation 'sigma'
        - 'sigmoid': subtracts an annulus with inner and outer radii
            of (ri,ro) and a sine-squared sigmoid radial profile from
            the probe template.
        - 'sigmoid_log': subtracts an annulus with inner and outer radii
            of (ri,ro) and a logistic sigmoid radial profile from
            the probe template.

    Each mode accepts 'center' (2-tuple) as a kwarg to manually specify
    the center of the probe, which is otherwise autodetected. Modes which
    accept additional kwargs and those arguments are:

        - 'gaussian':
            sigma (number)
        - 'sigmoid':
            radii (2-tuple)
        - 'sigmoid_log':
            radii (2-tuple)

    Accepts:
        probe (2D array):
        mode (str): must be in 'flat','gaussian','sigmoid','sigmoid_log'
        **kwargs: depend on `mode`, see above

    Returns:
        (2D array)
    """

    # perform computation
    from ....process.probe import get_kernel
    kern = get_kernel(
        self.probe,
        mode = mode,
        **kwargs
    )

    # add to the Probe
    self.kernel = kern

    # Set metadata
    md = Metadata(name='kernel')
    md['mode'] = mode
    for k,v in kwargs.items():
        md[k] = v
    self.metadata = md

    # return
    if returncalc:
        return kern







