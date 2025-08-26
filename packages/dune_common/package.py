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
#     spack install dune-common
#
# You can edit this file again by typing:
#
#     spack edit dune-common
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class DuneCommon(CMakePackage):
    """Basic infrastructure classes for all Dune modules."""

    homepage = "https://www.dune-project.org"
    url = "https://www.dune-project.org/download/2.10.0/dune-common-2.10.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    license("GPL-2.0-or-later", checked_by="rubaldoch")

    version("2.10.0", sha256="94c0dc8ccbb870a17b308368f0cc939f071cc74afb8759f5a90e9cb23aedafdd")

    depends_on("cxx", type="build")
    depends_on("openmpi", type="build")
    depends_on("openblas", type="build")
    depends_on("suite-sparse", type="build")
    depends_on("metis", type="build")
    depends_on("parmetis", type="build")
    depends_on("gmp", type="build")
    
    # depends_on("texlive", type="build")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
