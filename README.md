# OPM-Flow with Spack

## Dependencies

- Spack
- Nvidia CUDA Toolkit (if you want GPU support)

You can install spack by executing:

```bash
git clone --depth=2 --branch=releases/v1.0 https://github.com/spack/spack.git ~/spack
cd ~/spack

# Add spack to your path
. share/spack/setup-env.sh
```

## Instalation

- Add the opm-flow spack repository.

```bash
spack repo add --name opmflow https://github.com/rubaldoch/opm-flow-spack.git
```

- Check if the repo was added successfully with:

```bash
spack repo list
```

You will have an output similar to.

```bash
[user@khipu ~]$ spack repo list
[+] opmflow     v2.2    /home/user/.spack/package_repos/tlt3l5t/spack_repo/opmflow
[+] builtin     v2.2    /home/user/.spack/package_repos/fncqgg4/repos/spack_repo/builtin
```

- Install the opm-flow module packages:

```bash
spack install opm-common opm-grid opm-upscaling opm-simulators
```

- Then, load the installed packages

```bash
# For example, to load flow
spack load opm-simulators
```