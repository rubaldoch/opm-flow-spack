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
#     spack install opm-common
#
# You can edit this file again by typing:
#
#     spack edit opm-common
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.packages.boost.package import Boost
from spack.package import *


class OpmCommon(CMakePackage):
    """Tools for Eclipse reservoir simulation files."""

    homepage = "https://opm-project.org"
    url = "https://github.com/OPM/opm-common/archive/refs/tags/release/2025.04/final.tar.gz"

    maintainers("rubaldoch")

    license("GPL-3.0-or-later", checked_by="rubaldoch")

    version("2025.04", sha256="47dd88683babe0dd7cf7309d77a0499e4033cb0d2741d9a5ff9d3d7ac23b9f3d")
    
    # Configuration variants
    variant(
        "build_type",
        default="Release",
        description="The build type to build",
        values=("Debug", "Release", "DebugRelease"),
    )
    variant("dune", default=True, description="Build with Dune support")

    # Define dependencies
    depends_on('cmake@3.10:', type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("flexiblas")
    depends_on(Boost.with_default_variants)

    depends_on("dune-common", when="+dune")
    
    def cmake_args(self):
        args = []
        return args
