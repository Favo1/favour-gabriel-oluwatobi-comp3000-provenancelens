# Initial risk register

Likelihood and impact are qualitative Sprint 0 estimates. Review at each fortnightly sprint meeting. Any risk rated **High likelihood / High impact** must have a preventive action and a contingency.

| # | Risk | Likelihood | Impact | Prevention / mitigation and contingency | Status |
|---|---|---|---|---|---|
| 1 | Detector overfits to training generators and performs poorly on unseen generators | High | High | Design a leave-one-generator-out evaluation from the outset; keep a genuinely held-out generator set; report poor generalisation as a finding rather than tuning on the test set. | Open |
| 2 | Insufficient GPU or compute access | Medium | High | Start with smaller datasets and frozen backbones; benchmark on CPU where practical; investigate University facilities and approved hosted compute. Reduce model size or experiment count if access is limited. | Open |
| 3 | Dataset licensing, size or availability prevents planned experiments | Medium | Medium | Verify official terms before download; maintain alternative candidate datasets; reduce scope or use permitted synthetic data if a source is unavailable. | Open |
| 4 | Dataset artefacts or class imbalance cause shortcut learning | High | High | Standardise image formats, dimensions and compression; inspect class and source balance; use source-aware splits and robustness checks. If shortcuts remain, revise the dataset and report the limitation. | Open |
| 5 | Scope expands beyond the available time | Medium | Medium | Protect the core detector and evaluation as the minimum viable project; treat localisation and the demo as stretch goals and defer them if core objectives slip. | Open |
| 6 | Schedule disruption or delayed progress | Medium | High | Use fortnightly sprint goals, a visible backlog and regular supervisor meetings; re-prioritise early and use planned buffer time if a sprint is missed. | Open |
| 7 | Loss of source code, configurations or results | Low | High | Push work to the remote Git repository frequently; keep important configurations and small result summaries under version control; back up large artefacts separately. | Open |
| 8 | Experiments cannot be reproduced | Medium | Medium | Record seeds, package versions, data provenance, model checkpoints and configurations; repeat key runs where compute permits. | Open |
| 9 | Generative-image methods change during the project | Medium | Low | Set a literature review cut-off for the main evaluation and document later developments as context rather than continually expanding scope. | Open |
| 10 | Privacy or ethical concerns arise from images containing people | Low | Medium | Prefer appropriately licensed datasets with clear terms; avoid collecting new personal images; stop use of questionable material and seek supervisor/University guidance. | Open |
