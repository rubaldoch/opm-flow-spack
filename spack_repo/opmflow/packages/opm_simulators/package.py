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
    
    variant("mpi", default=True, description="Build with MPI.")
    variant("cuda", default=True, description="Build with CUDA.")
    variant("python", default=False, description="Compile with Python bindings")
    variant("chow_patel_ilu", default=False, description="Build with Chow-Patel ILU")
    variant("chow_patel_ilu_gpu", default=False, description="Build with Chow-Patel ILU on GPU.")
    variant("chow_patel_ilu_gpu_parallel", default=False, description="Try to use more parallelism on the GPU during Chow-Patel ILU decomposition?")
    variant("build_flow_alu_grid", default=False, description="Build flow blackoil with alu grid.")
    variant("damaris", default=False, description="Use the Damaris library for asynchronous I/O.")
    variant("gpu_bridge", default=True, description="Build with GPU bridge (GPU/AMGCL solvers).")
    variant("tracy_profiling", default=False, description="Enable tracy profiling.")
    variant("hip", default=False, description="Convert CUDA code to HIP (to run on AMD cards).")
    variant("amgx", default=False, description= "Build with AMGX  support")
    variant("hypre", default=False, description="Build with HYPRE library for linear solvers.")
    variant("opencl", default=True, description="Build with OpenCL support.")
    variant("gpu_istl", default=True, description="Build with GPU bridge (GPU/AMGCL solvers).")
    variant("doc", default=False, description="Compile with documentation")
    

    # Define dependencies
    depends_on("cmake@3.10:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("flexiblas")
    depends_on(Boost.with_default_variants)
    depends_on("suite-sparse")

    depends_on("dune-common")
    depends_on("dune-istl")
    depends_on("dune-grid")
    depends_on("dune-geometry")

    depends_on("opm-common")
    depends_on("opm-grid")
  
    # Optional dependencies
    depends_on("mpi", when="+mpi")
    depends_on("python", when="+python")
    depends_on("damaris", when="+damaris")
    depends_on("hypre", when="+hypre")
    depends_on("opencl", when="+opencl")
    depends_on("cuda", when="+cuda")
    depends_on("hip", when="+hip")
    depends_on("amgx", when="+amgx")

    def cmake_args(self):
        args = []
        if self.spec.satisfies("+gpu_istl"):
            args.append("-DUSE_OPENCL=OFF")
            args.append("-DUSE_GPU_BRIDGE=OFF")
            args.append("-DWITH_NDEBUG=ON")
            
            if self.spec.satisfies("+hip"):
                args.append("-DCONVERT_CUDA_TO_HIP=ON")
                args.append("-DCMAKE_HIP_PLATFORM=amd")
                args.append("-DUSE_HIP=1")
        else:
            if self.spec.satisfies("+python"):
                args.append("-DOPM_ENABLE_PYTHON=ON")
                args.append("-DOPM_ENABLE_PYTHON_TESTS=ON")
                args.append("-DOPM_INSTALL_PYTHON=ON")
            
            args.append(self.define_from_variant("USE_CHOW_PATEL_ILU", "chow_patel_ilu"))
            args.append(self.define_from_variant("USE_CHOW_PATEL_ILU_GPU", "chow_patel_ilu_gpu"))
            args.append(self.define_from_variant("USE_CHOW_PATEL_ILU_GPU_PARALLEL", "chow_patel_ilu_gpu_parallel"))
            
            args.append(self.define_from_variant("BUILD_FLOW_ALU_GRID", "build_flow_alu_grid"))
            args.append(self.define_from_variant("USE_DAMARIS_LIB", "damaris"))
            args.append(self.define_from_variant("USE_GPU_BRIDGE", "gpu_bridge"))
            args.append(self.define_from_variant("USE_TRACY_PROFILER", "tracy_profiling"))

            args.append(self.define_from_variant("CONVERT_CUDA_TO_HIP", "hip"))
            args.append(self.define_from_variant("USE_AMGX", "amgx"))
            args.append(self.define_from_variant("USE_HYPRE", "hypre"))
            args.append(self.define_from_variant("USE_OPENCL", "opencl"))

        if self.spec.satisfies("+cuda"):
            # Set up the CUDA macros needed by the build
            args.append("-DWITH_CUDA=ON")
            cuda_arch_list = self.spec.variants["cuda_arch"].value
            cuda_arch = cuda_arch_list[0]
            if cuda_arch != "none":
                args.append(f"-DCUDA_FLAGS=-arch=sm_{cuda_arch}")
        else:
            # Ensure build with CUDA is disabled
            args.append("-DWITH_CUDA=OFF")

        return args