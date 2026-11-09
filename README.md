# ProvenanceLens: Detecting AI-Generated and AI-Edited Images with Deep Learning

> COMP3000 Computing Project 2026–27 · BSc Computer Science (Artificial Intelligence) · University of Plymouth

| Project information | Details |
|---|---|
| Student | Favour Gabriel-Oluwatobi |
| Supervisor | Dr Vivek Singh |
| Module | COMP3000 Computing Project (40 credits) |
| Status | Sprint 0 – project initiation |
| Working title | ProvenanceLens: Detecting AI-Generated and AI-Edited Images with Deep Learning |

*The title and scope are provisional and may be refined with the supervisor as the project develops.*

## Project vision

**For** journalists, fact-checkers and everyday social-media users who need to assess the authenticity of digital images, **ProvenanceLens** is a deep-learning image-forensics project that will investigate whether an image is authentic, fully AI-generated or locally edited using generative AI. It will evaluate how well detection methods generalise to image generators that were not represented during training, and explore calibrated confidence scores and visual explanations to make results easier to interpret.

**Research question:** Which image features and training strategies allow an image detector to remain accurate when the generative model changes?

**Keywords:** AI-generated image detection; AI image editing; image forensics; deep learning; generator generalisation; robustness; confidence calibration; explainability.

## Aims and objectives

1. Establish a reproducible benchmark of real, AI-generated and AI-edited images, subject to dataset availability and licence conditions.
2. Implement and compare suitable CNN, Vision Transformer and frozen-CLIP approaches against at least one published baseline.
3. Evaluate generalisation to unseen generators, robustness to common image transformations, and confidence calibration.
4. Investigate visual explanations; edited-region localisation and a demonstration application are stretch objectives, dependent on time and results.

## Repository structure

```text
src/provenancelens/   Python package (data, models, evaluation, explainability, utilities)
configs/              Reproducible experiment configuration files
scripts/               Planned command-line entry points (not implemented yet)
tests/                 Automated unit tests
data/                  Dataset documentation and manifests; no raw images committed
results/               Small result tables and figures supporting the report
notebooks/             Exploratory notebooks; reusable logic belongs in src/
docs/                  Project vision, backlog, risks, architecture, ethics and project records
demo/                  Reserved for a possible demonstration application (stretch goal)
```

## Getting started

### Prerequisites

- Python 3.11 or later
- Git
- A virtual-environment tool (`venv` is included with Python)
- A CUDA-capable GPU is optional; CPU execution or a suitable hosted environment may be used for initial development.

### Set up the environment

Clone this repository using the HTTPS URL shown by the **Code** button on its GitHub page, then run the following from the repository directory:

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux (use this instead of the Windows command)
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the starter test suite:

```bash
pytest -q
```

The training and evaluation entry-point scripts are planned backlog work and are not part of the current starter implementation. Do not run experiment commands until those scripts have been implemented.

### Data

No research dataset has been selected, downloaded or included at project initiation. Before using a dataset, pretrained model or external code, check its terms of use and record its source, licence, intended use and access date in [docs/data-sources.md](docs/data-sources.md). See [data/README.md](data/README.md). Raw images and large model weights must not be committed to this repository.

## Reproducibility and evaluation

Experiment configurations are stored in `configs/` and use a fixed seed where supported. The baseline configuration is an initial template, not evidence that a complete training pipeline exists. Record environment versions, dataset versions, model/checkpoint provenance, configuration changes and experiment outputs as implementation proceeds. Experiment tracking is not yet integrated; the listed tracking package is optional until a tool is selected.

Planned evaluation includes classification metrics (for example accuracy, ROC-AUC and average precision), performance on held-out generators, robustness tests and calibration analysis. Metrics and protocols will be refined in the methodology and documented before results are interpreted.

## Technology stack

The current planned stack is Python 3.11+, PyTorch/torchvision, timm, OpenCLIP, Hugging Face Transformers, scikit-learn, NumPy, pandas, Pillow, Matplotlib, PyYAML, pytest and Ruff. These are proposed dependencies, not a claim that every component has already been integrated. See `requirements.txt` and [docs/architecture.md](docs/architecture.md); review dependency versions and licences before use.

## Project management

- [Product backlog](docs/backlog.md)
- [Sprint diary template](docs/sprint-diary/TEMPLATE.md)
- [Risk register](docs/risk-register.md)
- [Initial high-level plan](docs/gantt.md)
- [Architecture and design decisions](docs/architecture.md)
- [Project initiation submission checklist](docs/project-initiation-checklist.md)
- [Legal, ethical, social and professional considerations](docs/ethics-and-legal.md)

The backlog and plan are living documents and should be reviewed at each fortnightly sprint and supervisory meeting.

## Legal, ethical, social and professional considerations

Dataset, model and code licences must be checked before use and recorded in [docs/data-sources.md](docs/data-sources.md). The project will prioritise lawfully accessible research data, avoid collecting personal images, and avoid publishing functionality intended to help users evade detection. Detection outputs are probabilistic and must not be presented as proof of authenticity. Any research involving human participants requires the appropriate University ethics approval before it begins. Further details are in [docs/ethics-and-legal.md](docs/ethics-and-legal.md).

## Generative AI use

The COMP3000 brief identifies this assessment as **Assisted Work**. Generative AI use must be checked, understood and declared by the student. This repository includes [an AI-use log](docs/ai-use-log.md) to record assistance; the required signed declaration must also be completed and included with the relevant assessment submission. The log is a record, not a substitute for the University's declaration form.

## Third-party materials

At project initiation, no external dataset, pretrained checkpoint or third-party source-code repository has been incorporated into the project deliverable. The Python packages listed in `requirements.txt` are dependencies and remain subject to their respective upstream licences. Record the exact versions, sources and applicable licence notices before redistributing or incorporating third-party materials.

## Licence

Original project materials in this repository are released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** licence, subject to the scope and exclusions described in [docs/licensing.md](docs/licensing.md). Third-party dependencies, datasets, pretrained weights and other externally sourced materials are not relicensed by this notice and retain their own terms. The proposed licence should be confirmed with the project supervisor, as required by the COMP3000 assessment brief.
