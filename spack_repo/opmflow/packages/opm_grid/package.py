# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install opm-grid
#
# You can edit this file again by typing:
#
#     spack edit opm-grid
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.packages.boost.package import Boost
from spack.package import *


class OpmGrid(CMakePackage):
    """DUNE module supporting grids in a corner-point format."""

    homepage = "https://opm-project.org"
    url = "https://github.com/OPM/opm-grid/archive/refs/tags/release/2025.10/final.tar.gz"

    maintainers("rubaldoch")

    license("GPL-3.0-or-later", checked_by="rubaldoch")

    version("2025.10", sha256="2c45180351df688d27326d1532cab391e2c61054a877d9c9de1ea8eff61ea526")
    version("2025.04", sha256="fbb3ab60efc9f7df59246528b6b700a86207a94a3b08a236604ff1d60b32db58")

    # Variants
    variant('mpi', default=True, description='Build with MPI.')
   
    # Define dependencies
    depends_on('cmake@3.10:', type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("flexiblas")
    depends_on(Boost.with_default_variants)
    depends_on("suite-sparse")
    depends_on("zoltan")
    
    depends_on("dune-common")
    depends_on("dune-geometry")
    depends_on("dune-grid") 
    depends_on("dune-istl") 

    depends_on("opm-common")

    def cmake_args(self):
        args = []
        return args
