# Product backlog

Priorities use MoSCoW (Must, Should, Could). Each item should be represented as a GitHub issue when the project board is configured and linked from the sprint diary. Re-prioritise at every sprint review. The target sprints are provisional planning estimates.

**Definition of done:** code merged to main, tests passing, documented, referenced if adapted, results logged, backlog item closed.

| ID | Item (user story shortened) | Priority | Work package | Target sprint |
|---|---|---|---|---|
| PB-01 | As a student, I have a repo, environment and CI so work is versioned and testable | Must | WP1 | S0 |
| PB-02 | As a supervisor, I can access the repo and see title, vision and supervisor in the README | Must | WP1 | S0 |
| PB-03 | As a researcher, I log experiments with fixed seeds and configs | Should | WP1 | S1 |
| PB-04 | As a researcher, I have a dataset and licence register | Must | WP3 | S1 |
| PB-05 | As a researcher, I can download data via scripts and manifests (no raw data in Git) | Must | WP3 | S1-S2 |
| PB-06 | As a researcher, I generate images with open generators and log prompts and seeds | Must | WP3 | S1-S3 |
| PB-07 | As a researcher, I standardise format, size and compression so real and fake do not differ by shortcut | Must | WP3 | S3 |
| PB-08 | As a researcher, I have leave-one-generator-out splits | Must | WP3 | S3 |
| PB-09 | As a researcher, I train a CNN baseline | Must | WP4 | S2-S3 |
| PB-10 | As a researcher, I reproduce one published detector | Must | WP4 | S5 |
| PB-11 | As a researcher, I have an evaluation harness (accuracy, AUC, AP, ECE) | Must | WP4 | S3-S5 |
| PB-12 | As a researcher, I train a frozen-CLIP linear probe | Must | WP5 | S6 |
| PB-13 | As a researcher, I fine-tune a ViT detector | Should | WP5 | S6-S7 |
| PB-14 | As a researcher, I run leave-one-generator-out experiments for all detectors | Must | WP5 | S7-S9 |
| PB-15 | As a researcher, I test robustness to JPEG, resize and noise | Must | WP5 | S7-S8 |
| PB-16 | As a user, I get calibrated confidence (temperature scaling, reliability diagrams) | Should | WP6 | S8 |
| PB-17 | As a user, I get Grad-CAM explanations | Should | WP6 | S8 |
| PB-18 | As a user, I can see which region of an image was edited | Could | WP6 | S9-S10 |
| PB-19 | As a researcher, I run ablations and failure analysis | Must | WP7 | S9-S11 |
| PB-20 | As a student, I produce the poster draft then final poster | Must | WP8 | S8-S10 |
| PB-21 | As a user, I can try a simple demo app | Could | WP9 | S11-S12 |
| PB-22 | As a student, I record the 5-minute video | Must | WP11 | S12-S13 |
| PB-23 | As a student, I complete the report and ePortfolio with the signed GenAI declaration | Must | WP10-11 | S2-S13 |
| PB-24 | As a marker, I can clone the repo and run it from the README | Must | WP11 | S13 |
