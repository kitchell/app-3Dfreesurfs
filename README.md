[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.98-blue.svg)](https://doi.org/10.25663/bl.app.98)

# app-3Dfreesurfs

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Creates 3D surface meshes for the FreeSurfer aparc+aseg labels (cortical and subcortical regions) with VTK marching cubes, in vtk, ply or stl format.**

Converts mri/aparc+aseg.mgz to NIfTI with FreeSurfer mri_label2vol, then builds a smoothed mesh for each of a fixed list of subcortical and Desikan-Killiany cortical labels with VTK, naming and colouring them from the FreeSurfer colour lookup table. Use it to visualise a FreeSurfer segmentation in 3D. The job checks for a fixed number of output files and fails if any are missing.

| | |
|---|---|
| 📥 **Inputs** | `neuro/freesurfer` |
| 📤 **Outputs** | `neuro/3Dsurfaces` |
| 🐳 **Container** | `brainlife/freesurfer:6.0.1` |
| ⚙️ **Resources** | 8 CPUs · 0.5 h walltime |
| 🔑 **Requires** | `FREESURFER_LICENSE` |
| 🔗 **Run it** | [doi.org/10.25663/bl.app.98](https://doi.org/10.25663/bl.app.98) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `freesurfer` | `neuro/freesurfer` | yes | FreeSurfer subject directory. Must contain mri/aparc+aseg.mgz. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `surfaces` | `neuro/3Dsurfaces` | One surface mesh per FreeSurfer label, with colour and name information. |

<details>
<summary><b>⚙️ Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `filetype` | enum | `vtk` | choose output filetype Options: `vtk`, `ply`, `stl`. |

</details>

<!-- brainlife-app:end -->

This application will create a 3D surface for 87 freesurfer labels from the aparc+aseg.mgz file.

### Author
- Lindsey Kitchell (kitchell@indiana.edu)

### Contributors
- Steven O'Reilly (stevengeeky@gmail.com)

### Funding 
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
We kindly ask that you cite the following when publishing papers and code using this code. 

1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Running the App 

### On Brainlife.io

You can submit this App online at [https://brainlife.io/app/5aa826baf315ba00317fe086#](https://brainlife.io/app/5aa826baf315ba00317fe086#) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
    "filetype": "vtk",
    "freesurfer": "../5b96d2cb161e01002a320742/5967bffa9b45c212bbec8958/output"
}
```
If you have singlarity install on your local machine:

3. Launch the App by executing `main`

```bash
./main
```

Otherwise:

3. execute convertfiles.sh and then main.py in python.

### Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brain-life/cli).


## Output

The output of this app will be a folder with a surface mesh file for each of the 87 freesrufer labels. 

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.  

  - Freesurfer: https://surfer.nmr.mgh.harvard.edu/
  - VTK: https://www.vtk.org/download/
  (easiest to just use Anaconda (https://www.anaconda.com/) which comes with vtk)
