#   Copyright 2020 The PyMC Developers
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import aesara.tensor as at
import numpy as np

from aesara.tensor.math import gammaln, psi

__all__ = ["gammaln", "multigammaln", "psi", "log_i0"]


def multigammaln(a, p):
    """Multivariate Log Gamma

    Parameters
    ----------
    a: tensor like
    p: int
       degrees of freedom. p > 0
    """
    i = at.arange(1, p + 1)
    return p * (p - 1) * at.log(np.pi) / 4.0 + at.sum(gammaln(a + (1.0 - i) / 2.0), axis=0)


def log_i0(x):
    """
    Calculates the logarithm of the 0 order modified Bessel function of the first kind""
    """
    return at.switch(
        at.lt(x, 5),
        at.log1p(
            x ** 2.0 / 4.0
            + x ** 4.0 / 64.0
            + x ** 6.0 / 2304.0
            + x ** 8.0 / 147456.0
            + x ** 10.0 / 14745600.0
            + x ** 12.0 / 2123366400.0
        ),
        x
        - 0.5 * at.log(2.0 * np.pi * x)
        + at.log1p(
            1.0 / (8.0 * x)
            + 9.0 / (128.0 * x ** 2.0)
            + 225.0 / (3072.0 * x ** 3.0)
            + 11025.0 / (98304.0 * x ** 4.0)
        ),
    )
