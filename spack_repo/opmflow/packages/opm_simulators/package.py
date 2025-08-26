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
#     spack install opm-simulators
#
# You can edit this file again by typing:
#
#     spack edit opm-simulators
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class OpmSimulators(CMakePackage):
    """OPM Flow and experimental simulators, including components such as well models etc."""

    homepage = "https://opm-project.org"
    url = "https://github.com/OPM/opm-simulators/archive/refs/tags/release/2025.04/final.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    license("GPL-3.0-or-later", checked_by="rubaldoch")

    version("2025.04", sha256="02aa85b82c843ecde2640b6e9bdbfa1a5026fd46ee1fb564284784e5c359d233")
    
    # Variants
    variant('mpi', default=True, description='Build with MPI.')
    variant('cuda', default=True, description='Build with CUDA support.')

    # Define dependencies
    depends_on("cmake", type="build")
    depends_on("cxx", type="build")

    depends_on("openblas")
    depends_on("boost+test+atomic+mpi+system+date_time")
    depends_on("suite-sparse")
    
    depends_on("dune-common")
    depends_on("dune-istl")
    depends_on("dune-grid")
    depends_on("dune-geometry")
    
    depends_on("opm-common")
    depends_on("opm-grid")

    # Optional dependencies
    depends_on('mpi', when='+mpi')
    depends_on('cuda@12.6.2', when='+cuda')

    def cmake_args(self):
        args = [
            f"-DUSE_OPENCL=OFF",
            f"-DUSE_GPU_BRIDGE=OFF",
            f"-DCMAKE_BUILD_TYPE=Release",
            f"-DWITH_NATIVE=OFF",
        ]
        return args
