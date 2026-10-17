# cfDNA-Fragmentomics-Toolkit — ARCHIVED on 2026-10-16

> ⚠️ **This repository is archived.** The cfDNA fragmentomics toolkit
> has been superseded by:
>
> - **`rollroyces/deepcatch`** — production-grade fragmentomics module
>   (`src/fragmentomics/`), 238 tests passing, 627-sample validated
>   cross-study AUC 0.967 ± 0.004.
> - **`rollroyces/cfdna-fragmentomics-pipeline`** — Snakemake-based
>   production pipeline (FSD + DELFI/WPS + 4-mer motifs + GC-correction,
>   AUC 0.9745 ± 0.0023 on 627 samples).

## What lived here

| What lived here                | Where it lives now                                                         |
|-------------------------------|------------------------------------------------------------------------------|
| `main.py` (BAM CLI)            | `deepcatch/src/fragmentomics/` (BAM mode, pysam-based)                       |
| `src/analyzer.py`             | `cfdna-fragmentomics-pipeline/scripts/auc_reproducibility_gate.py` etc.      |
| `src/simulator.py`            | `deepcatch/src/synthetic_data/MultiModalDataGenerator`                      |
| `src/visualizer.py`           | `deepcatch/notebooks/` + `cfdna-fragmentomics-pipeline/scripts/`            |

## Why archived?

This repo was the **initial toolkit** that proved the cfDNA fragmentomics
concept, before the production pipeline and the integrated DeepCatch framework
were built. Both successors ran the same algorithm on a real 627-sample
cross-study cohort; this repo's `main.py` and `src/` were the simplest possible
implementation but never had a real-data benchmark. Archive preserves the
git history without the dead-code confusion.

## What still works here?

- git history intact; SHA references continue to resolve.
- LICENSE added 2026-10-16 as part of the consolidation (this repo shipped
  without one before that point).

## Where to file a new issue?

- **cfDNA fragmentomics production pipeline**
  → https://github.com/rollroyces/cfdna-fragmentomics-pipeline/issues
- **Fragmentomics module in DeepCatch**
  → https://github.com/rollroyces/deepcatch/issues with the
    `fragmentomics` label.

---

*Archived 2026-10-16 as part of the CANCER-SEEK / fragmentomics consolidation.*

## License

MIT — see [`LICENSE`](LICENSE) (added 2026-10-16).
