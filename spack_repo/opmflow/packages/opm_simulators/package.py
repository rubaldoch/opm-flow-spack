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
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.packages.boost.package import Boost
from spack.package import *


class OpmSimulators(CMakePackage, CudaPackage):
    """OPM Flow and experimental simulators, including components such as well models etc."""

    homepage = "https://opm-project.org"
    url = "https://github.com/OPM/opm-simulators/archive/refs/tags/release/2025.04/final.tar.gz"
    git = "https://github.com/OPM/opm-simulators.git"

    maintainers("rubaldoch")
    
    license("GPL-3.0-or-later", checked_by="rubaldoch")

    version("2025.04", sha256="02aa85b82c843ecde2640b6e9bdbfa1a5026fd46ee1fb564284784e5c359d233")

    # Configuration variants
    variant(
        "build_type",
        default="Release",
        description="The build type to build",
        values=("Debug", "Release", "DebugRelease"),
    )
    
    variant('mpi', default=True, description='Build with MPI.')
    variant('cuda', default=True, description='Build with CUDA.')
    variant("python", default=False, description="Compile with Python bindings")
    variant('chow_patel_ilu', default=False, description='Build with Chow-Patel ILU')
    variant('chow_patel_ilu_gpu', default=False, description='Build with Chow-Patel ILU on GPU.')
    variant('chow_patel_ilu_gpu_parallel', default=False, description='Try to use more parallelism on the GPU during Chow-Patel ILU decomposition?')
    variant('gpu_bridge', default=True, description='Build with GPU bridge (GPU/AMGCL solvers).')
    variant('amgx', default=False, description= 'Build with AMGX  support')
    variant('opencl', default=True, description='Build with OpenCL support.')
    variant('gpu_istl', default=True, description='Build with GPU bridge (GPU/AMGCL solvers).')
    variant('doc', default=False, description='Compile with documentation')
    

    # Define dependencies
    depends_on('cmake@3.10:', type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("openblas")
    depends_on(Boost.with_default_variants)
    depends_on("suite-sparse")

    depends_on("dune-common")
    depends_on("dune-istl")
    depends_on("dune-grid")
    depends_on("dune-geometry")

    depends_on("opm-common")
    depends_on("opm-grid")
  
    # Optional dependencies
    depends_on('mpi', when='+mpi')
    depends_on("python", when="+python")
    depends_on('amgx', when='+amgx')

    def cmake_args(self):
        spec = self.spec
        args = []

        if "+gpu_istl" in spec:
            args.append("-DUSE_OPENCL=OFF")
            args.append("-DUSE_GPU_BRIDGE=OFF")
            args.append("-DWITH_NATIVE=OFF")
            args.append("-DWITH_NDEBUG=ON")
        else:
            args.append(self.define_from_variant("DUSE_OPENCL", "opencl"),)
        

        # args = [
            
        #     self.define_from_variant("DUSE_GPU_BRIDGE", "gpubridge"),
        #     self.define_from_variant("DWITH_NATIVE", "native"),
        #     self.define_from_variant("USE_AMGX", "amgx"),

        #     self.define_from_variant("USE_CHOW_PATEL_ILU", "chow_patel_ilu"),
        #     self.define_from_variant("USE_CHOW_PATEL_ILU_GPU", "chow_patel_ilu_gpu"),
        #     self.define_from_variant("USE_CHOW_PATEL_ILU_GPU_PARALLEL", "chow_patel_ilu_gpu_parallel"),
        # ]

        # if spec.satisfies("+cuda"):
        #     # Set up the CUDA macros needed by the build
        #     args.append("-DWITH_CUDA=ON")
        #     cuda_arch_list = spec.variants["cuda_arch"].value
        #     cuda_arch = cuda_arch_list[0]
        #     if cuda_arch != "none":
        #         args.append(f"-DCUDA_FLAGS=-arch=sm_{cuda_arch}")
        # else:
        #     # Ensure build with CUDA is disabled
        #     args.append("-DWITH_CUDA=OFF")
        return args

