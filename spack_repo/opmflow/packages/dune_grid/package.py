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
#     spack install dune-grid
#
# You can edit this file again by typing:
#
#     spack edit dune-grid
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class DuneGrid(CMakePackage):
    """The Dune grid interface and some grid implementations."""

    homepage = "https://www.dune-project.org"
    url = "https://www.dune-project.org/download/2.10.0/dune-grid-2.10.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("GPL-2.0-or-later", checked_by="rubaldoch")

    version("2.10.0", sha256="2feb7c16d75048a80c570773431c587f6d14a4f9fabf7f1ad0a3fbacc7330056")

    depends_on("cxx", type="build")

    depends_on("openmpi", type="build")
    depends_on("openblas", type="build")
    depends_on("suite-sparse", type="build")
    depends_on("metis", type="build")
    depends_on("parmetis", type="build")
    depends_on("gmp", type="build")
    
    depends_on("dune-common", type="build")
    depends_on("dune-geometry", type="build")

# FIXME: Add dependencies if required.
    # depends_on("foo")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
