# Architecture and initial technical decisions

## Proposed architecture

The intended pipeline separates data handling, model implementation, training and evaluation so components can be tested independently. The architecture is provisional and will be updated as implementation decisions are made.

```mermaid
flowchart LR
    A[Dataset manifests and preprocessing] --> B[Model implementations: CNN / ViT / CLIP]
    B --> C[Training and experiment configuration]
    C --> D[Evaluation: generalisation / robustness / calibration]
    D --> E[Visual explanation]
    E --> F[Optional demonstration application]
```

## Initial decisions

| Area | Initial decision | Rationale / status |
|---|---|---|
| Language | Python 3.11+ | Fits the proposed deep-learning and evaluation ecosystem; confirm against the available environment. |
| Deep-learning framework | PyTorch and torchvision | Proposed framework for implementing and comparing image models. |
| Model ecosystem | timm, OpenCLIP and Transformers | Candidate libraries for CNN, Vision Transformer and CLIP-based experiments; exact models remain to be selected. |
| Experiment configuration | YAML files under `configs/` | Keeps experiment parameters and random seeds visible and version-controlled. |
| Testing and style | pytest and Ruff | Automated tests and consistent linting are already configured in the starter repository. |
| Data management | Manifests in Git; raw images and large weights excluded | Avoids committing large or licence-restricted assets. |
| Tracking | Not selected | W&B is listed as an optional dependency; choose a tracker only if it adds value and review its data/privacy terms. |

## Decisions to revisit

Confirm model architectures, datasets, evaluation protocol, compute environment, experiment tracker and explanation method after the literature review and feasibility tests. Record alternatives and evidence for material changes here.
