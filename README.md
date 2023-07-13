# Chenrec——cultural relic reconstruction system of non-lambertian body based on a defferentiable Monte Carlo renderer

Joint optimization of topology, materials and lighting from multi-view image observations 

For differentiable marching tetrahedons, we have adapted code from NVIDIA's [Extracting Triangular 3D Models, Materials, and Lighting From Images](https://github.com/NVlabs/nvdiffrec).

# Installation

Requires Python 3.6+, VS2019+, Cuda 11.3+ and PyTorch 1.10+

Tested in Anaconda3 with Python 3.9 and PyTorch 1.10

## One time setup (Windows)

Install the [Cuda toolkit](https://developer.nvidia.com/cuda-toolkit) (required to build the PyTorch extensions).
We support Cuda 11.3 and above.
Pick the appropriate version of PyTorch compatible with the installed Cuda toolkit.
Below is an example with Cuda 11.6

```
conda create -n dmodel python=3.9
activate dmodel
conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge
pip install ninja imageio PyOpenGL glfw xatlas gdown
pip install git+https://github.com/NVlabs/nvdiffrast/
pip install --global-option="--no-networks" git+https://github.com/NVlabs/tiny-cuda-nn#subdirectory=bindings/torch
imageio_download_bin freeimage
```

### Every new command prompt
`activate dmodel`

# Examples

*Our approach is designed for high-end NVIDIA GPUs with large amounts of memory.
To run on mid-range GPU's, reduce the batch size parameter in the .json files.*

Simple genus 1 reconstruction example:
```
python train.py --config configs/bob.json
```
Visualize training progress (only supported on Windows):
```
python train.py --config configs/bob.json --display-interval 20
```

Multi GPU example (Linux only. *Experimental: all results in the paper were generated using a single GPU*),
using [PyTorch DDP](https://pytorch.org/docs/stable/elastic/run.html#launcher-api)
```
torchrun --nproc_per_node=4 train.py --config configs/bob.json
```

The results will be stored in the `out` folder.

The [Elephant](https://3d.si.edu/object/3d/spouted-vessel-he-form-elephant-masks-taotie-dragons-and-snakes:d8c63598-4ebc-11ea-b77f-2e728ce88125) ,
[Baluster_vase](https://3d.si.edu/object/3d/baluster-vase-one-three-five-piece-garniture-f1980190-194:d8c62634-4ebc-11ea-b77f-2e728ce88125) ,
[Beaker-shaped vase](https://3d.si.edu/object/3d/beaker-vase-one-five-piece-garniture:446bedc0-76f1-4eb9-a30e-355be14e9e30) ,
[Incense](https://3d.si.edu/object/3d/lidded-incense-burner-xianglu-geometric-decoration-and-narrative-scenes:ce850625-2cf1-4c6f-9086-0d5845d9a664) ,
[Kylix](https://3d.si.edu/object/3d/kylix:547c78d1-620b-40c4-982e-01928870fef4) ,
[Pottery](https://3d.si.edu/object/3d/colonoware-pot-cooper-river-charleston-county-sc:79da3e3f-3ad7-41de-8956-e891d88a3c5f) ,
[Stoneware](https://3d.si.edu/object/3d/stoneware-jug-created-thomas-commeraw:82adf5d6-5ec4-46cc-9e68-6a4d7c5ea824) and
[Wine_container](https://3d.si.edu/object/3d/ritual-wine-container-fangyi-maskstaotie-serpents-and-birds:d8c62f94-4ebc-11ea-b77f-2e728ce88125)
models were created and released into the public domain (https://3d.si.edu).

The [Spot](http://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/index.html#spot) and
[Bob](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/index.html) models were
created and released into the public domain by [Keenan Crane](http://www.cs.cmu.edu/~kmcrane/index.html).

Included examples

- `spot.json` - Extracting a 3D model of the spot model. Geometry, materials, and lighting from image observations.
- `baluster_vase_p1.json` - Extracting the baluster_vase part1 model.
- `baluster_vase_p2.json` - Extracting the baluster_vase part2 model.
- `beaker-shaped_vase.json` - Extracting the beaker-shaped_vase model.
- `incense.json` - Extracting the incense model.
- `kylix.json` - Extracting the kylix model.
- `pottery.json` - Extracting the pottery model.
- `stoneware.json` - Extracting the stoneware model.
- `wine_container_p1.json` - Extracting the wine_container part1 model.
- `wine_container_p2.json` - Extracting the wine_container part2 model.
- `bob.json` - Simple example of a genus 1 model.
