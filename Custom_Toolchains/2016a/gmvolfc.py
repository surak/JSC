# This file is part of JSC's public easybuild repository (https://github.com/easybuilders/jsc)
##
# Copyright 2016-2016 Ghent University
# Copyright 2016-2016 Forschungszentrum Juelich
#
# This file is triple-licensed under GPLv2 (see below), MIT, and
# BSD three-clause licenses.
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for gmvolfc compiler toolchain (includes GCC, MVAPICH2, OpenBLAS, LAPACK, ScaLAPACK 
and FFTW, and CUDA as dependency).

@author: Damian Alvarez (Forschungszentrum Juelich)
"""

from easybuild.toolchains.gmvapich2c import Gmvapich2c
from easybuild.toolchains.fft.fftw import Fftw
from easybuild.toolchains.linalg.openblas import OpenBLAS
from easybuild.toolchains.linalg.scalapack import ScaLAPACK


class Gmvolfc(Gmvapich2c, OpenBLAS, ScaLAPACK, Fftw):
    """Compiler toolchain with GCC, MVAPICH2, OpenBLAS, ScaLAPACK and FFTW, and CUDA as dependency."""
    NAME = 'gmvolfc'
    SUBTOOLCHAIN = Gmvapich2c.NAME
