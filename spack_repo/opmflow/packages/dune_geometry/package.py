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
#     spack install dune-geometry
#
# You can edit this file again by typing:
#
#     spack edit dune-geometry
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class DuneGeometry(CMakePackage):
    """Includes everything related to the DUNE reference elements.
        This includes the reference elements themselves, 
        mappings on the reference elements (geometries), and quadratures."""

    homepage = "https://www.dune-project.org"
    url = "https://www.dune-project.org/download/2.10.0/dune-geometry-2.10.0.tar.gz"

    maintainers("rubaldoch")
    license("GPL-2.0-or-later", checked_by="rubaldoch")

    version("2.10.0", sha256="28e98ac930477e0c93e41d0bec74c472e48b9e9f11f16a07befb8791568b7303")

    variant('mpi', default=True, description='Build with MPI.')
    variant("scotch", default=True, description="With scotch/ptscotch decomposition")
    variant("suitesparse", default=True, description="With SuiteSparse support")
    variant("metis", default=True, description="With METIS support")
    variant("parmetis", default=True, description="With PARMETIS support")
    variant("gmp", default=True, description="With GMP support")
    variant("superlu", default=True, description="With SuperLU support")
    variant("docs", default=False, description="With documentation support")
    
    # Dependencies
    depends_on("cmake@3.16:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("flexiblas")
    
    # Optional dependencies
    depends_on("mpi", when="+mpi")
    depends_on("metis@5.0:", when="+metis")
    depends_on("parmetis@4.0:", when="+parmetis")
    depends_on("suite-sparse", when="+suitesparse")
    depends_on("gmp", when="+gmp")
    depends_on("superlu@5.0:", when="+superlu")
    depends_on("scotch", when="+scotch")
    depends_on("texlive", when="+docs")

    depends_on("dune-common")

    def cmake_args(self):
        args = []
        return args
