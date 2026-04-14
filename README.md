# cfDNA-Fragmentomics-Toolkit 🧬

[![License: MIT](https://pfst.cf2.poecdn.net/base/image/2c89badab92b5ee0afea1a6328677fab597eaa5d90b21f6a29384f9eaac3cbc0?pmaid=603603858)](https://opensource.org/licenses/MIT)
[![Bioinformatics: Liquid Biopsy](https://pfst.cf2.poecdn.net/base/image/92a219d7eb3e2de652006a105e74a74e8120ca93a45c0e83df737116153477fd?pmaid=603603857)](https://github.com)

A high-performance bioinformatics pipeline for analyzing cell-free DNA (cfDNA) fragmentation patterns. This toolkit implements state-of-the-art fragmentomics metrics, including size distribution, end-motif profiling, and motif diversity scores, to assist in liquid biopsy research and cancer detection.

---

## 🌟 Scientific Features

This toolkit extracts biological signals from cfDNA sequencing data by analyzing non-random fragmentation patterns:

- **Fragment Size Profiling:** Calculates insert sizes to distinguish between **"Normal"** cfDNA (symmetric peak at ~167bp) and **"Cancer"** cfDNA (shifted toward shorter fragments, ~145bp).
- **4-mer End-Motif Analysis:** Profiles 256 possible 5' terminal 4-mer sequences. It specifically monitors **DNASE1L3-associated motifs** (e.g., CCCA), which are significantly reduced in various cancer types.
- **Motif Diversity Score (MDS):** Quantifies the heterogeneity of fragment ends using normalized Shannon entropy. Elevated MDS indicates aberrant fragmentation pathways often seen in Hepatocellular Carcinoma (HCC).
- **10 bp Periodicity Analysis:** Validates the nucleosomal footprint of cfDNA using Fast Fourier Transform (FFT). A sharp peak at **0.1Hz** ($1/10bp$) serves as a crucial quality control metric for sample integrity.

---

## 🔬 Mathematical Framework

### Motif Diversity Score (MDS)
The MDS measures the randomness of the 256 motif frequencies ($P_i$) using the following formula:

$$MDS = -\frac{1}{\log_{2}(256)} \sum_{i=1}^{256} P_i \log_{2}(P_i)$$

> **Note:** A value of 1 represents a perfectly uniform distribution, while a lower value indicates a skewed preference for specific nuclease-driven motifs.

---

## 🚀 Quick Start

### 1. Installation
We recommend using **Mamba** for faster dependency resolution:

```bash

# Create environment

conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict

mamba create -n fragmentomics python=3.9 pysam numpy scipy matplotlib pandas seaborn tqdm

mamba activate fragmentomics

2. Validation with Mock Data
Generate synthetic BAM files that simulate realistic cfDNA distributions (167bp vs 145bp) to verify the pipeline:

bash
python src/simulator.py

3. Core Analysis
Analyze a sample BAM file using strict research-grade filters:

bash
python main.py --input data/sample.bam --output results/

🔍 Research-Grade Filters
Quality Filter	Value	Rationale
MAPQ	$\ge 30$	Excludes ambiguous alignments from repetitive regions.
Proper Pair Required	Yes	Ensures both reads represent a single physical DNA fragment.
Deduplication (Recommended)	Yes	Removes PCR artifacts that bias motif counts.
📂 Project Structure
plaintext
├── main.py                  # Entry point for the analysis pipeline
├── src/
│   ├── analyzer.py         # Core engine for motif and size extraction
│   ├── simulator.py        # cfDNA distribution and BAM simulator
│   └── visualizer.py       # FFT and Size distribution plotting tools
├── data/                    # Directory for BAM and FASTA (hg38) files
└── requirements.txt         # List of required Python packages

📚 References
Jiang et al. (2020). Plasma DNA End-Motif Profiling for Cancer Detection. Cancer Discovery.
Serpas et al. (2019). DNASE1L3-mediated cfDNA fragmentation. JCI Insight.
Cristiano et al. (2019). Genome-wide cell-free DNA fragmentation in patients with cancer. Nature.
📄 License
This project is licensed under the MIT License - see the LICENSE page for details.
