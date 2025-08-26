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
from spack.package import *


class OpmGrid(CMakePackage):
    """DUNE module supporting grids in a corner-point format."""

    homepage = "https://opm-project.org"
    url = "https://github.com/OPM/opm-grid/archive/refs/tags/release/2025.04/final.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    license("GPL-3.0-or-later", checked_by="rubaldoch")

    version("2025.04", sha256="fbb3ab60efc9f7df59246528b6b700a86207a94a3b08a236604ff1d60b32db58")

    # Variants
    variant('mpi', default=True, description='Build with MPI.')
   
    # Define dependencies
    depends_on("cmake", type="build")
    depends_on("cxx", type="build")

    depends_on("openblas")
    depends_on("boost+test+atomic+mpi+system+date_time")
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
