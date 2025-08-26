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
#     spack install opm-upscaling
#
# You can edit this file again by typing:
#
#     spack edit opm-upscaling
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class OpmUpscaling(CMakePackage):
    """Single-phase and steady-state upscaling methods."""

    homepage = "https://opm-project.org"
    url = "https://github.com/OPM/opm-upscaling/archive/refs/tags/release/2025.04/final.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")
    
    license("GPL-3.0-or-later", checked_by="rubaldoch")

    version("2025.04", sha256="8ba85d00606feb793ce23c77fde798f907ab72dc31d309c22cc0f0e135e162e2")

    # Define dependencies
    depends_on("cmake", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("openblas")
    depends_on("boost+test+atomic+mpi+system+date_time")
    depends_on("suite-sparse")
    depends_on("zoltan")
    
    depends_on("dune-common")
    depends_on("dune-geometry")
    depends_on("dune-grid")
    depends_on("dune-istl")
    
    depends_on("opm-common")
    depends_on("opm-grid")

    def cmake_args(self):
        args = []
        return args
