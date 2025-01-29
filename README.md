# spotDetection
Segmenting nuclei and detecting spots in microscopy images

Heavily based on scripts written by Lucien Hinderling for Anja, with later modifictions by Jenny Semple.

Lucien's orginal scripts can be found here:

```
/mnt/external.data/MeisterLab/lhinder/segmentation_3d_anja/code
```

Main changes on initial commit:
- organising code and removing redundancies
- using bioio library for images
- improving segmentation qc plots - adding xz and yz slices, adding label colors.
- adding GMM plot to try and find suitable threshold for spots
- qc plots of individual nuclei - solved varying nuclear size problem that cropped nuclei.
- qc plots for spots - spots plotted as ring to better see underlying image

## Installation

Using bioio library gives a more uniform input/output framework however it uses an old version of numpy which is tricky to keep compatible with other packages.

To be able to install the gpu version, need to ssh into izbdelhi and find the current version of cuda using

```
nvidia-smi
```
Currently I get version 12.7 

Then go to https://pytorch.org/get-started/locally/ where you can find the command lines to use.

Check if you see a cuda runtime package

```
nvcc --version
which nvcc
```
This can interfere with pytorch installation which automatically installs its own version of cuda runtime.
You might need to remove the path from the $PATH variable during installation. then it should work fine.

-----------------

The following is the set of commands to use to install environment:

```
mamba create -n lhcellpose python=3.10

mamba activate lhcellpose

mamba install pytorch torchvision pytorch-cuda=12.4 -c pytorch -c nvidia

mamba install -c conda-forge 'cellpose[gui]'

mamba install -c conda-forge napari pyqt matplotlib-scalebar edt trackpy seaborn numpy=1.26.4

pip install bioio bioio-nd2 bioio-tifffile
pip install plotly ipywidgets

```

And check the numpy version is 1.26.4 (older or newer versions seemed to give an error) with

```
mamba list
```

Test pytorch is working by starting command line python (just type 'python'), then:
```
import torch
torch.cuda.is_available()
```
This should give 'true'


## Running scripts

You need a job on gpu server for training the model, but probably not for running it.

ssh to izblisbon then start a remote job:

```
# for gpu job
salloc --gres=gpu:1 --mem=32GB --time=9:00:00 --ntasks=2

# for cpu job
salloc --mem=32GB --time=9:00:00 --ntasks=2
```

Then start remote vscode

```
code tunnel
```

On your local machine start vscode and on the bottom left hand corner click the blue >< symbol and choose "connect to tunnel..."
After connecting with your github account make sure to choose the lhcellpose environment as your python kernel (top right of notebook). 
