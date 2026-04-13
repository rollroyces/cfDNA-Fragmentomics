import pysam
import numpy as np
from collections import Counter

class FragmentomicsEngine:
    def __init__(self, bam_path, fasta_path):
        self.bam = pysam.AlignmentFile(bam_path, "rb")
        self.fasta = pysam.FastaFile(fasta_path)
        self.motifs_256 =

    def process_region(self, chrom, start, end):
        sizes =
        motifs =
        
        for read in self.bam.fetch(chrom, start, end):
            # 1. 嚴格過濾：MAPQ >= 30, 必須是 Proper Pair [1, 5]
            if not (read.is_paired and read.is_proper_pair and read.mapping_quality >= 30):
                continue
            if read.is_secondary or read.is_supplementary:
                continue
                
            # 2. 提取片段長度 (Template Length) 
            # 只在 Read 1 (正鏈) 統計，避免重複計算
            if read.is_read1 and read.template_length > 0:
                isize = abs(read.template_length)
                if 50 <= isize <= 500:
                    sizes.append(isize)
            
            # 3. 提取 5' 末端 4-mer 基序 
            # 注意：需區分正負鏈以定位真正的片段末端
            try:
                if not read.is_reverse:
                    m_start = read.reference_start
                    motif = self.fasta.fetch(read.reference_name, m_start, m_start + 4).upper()
                else:
                    m_start = read.reference_end - 4
                    motif = self.fasta.fetch(read.reference_name, m_start, m_start + 4).upper()
                
                if 'N' not in motif and len(motif) == 4:
                    motifs.append(motif)
            except:
                continue
                
        return sizes, Counter(motifs)

    def calculate_mds(self, motif_counts):
        """計算基序多樣性分數 (MDS) - 基於 Shannon Entropy"""
        total = sum(motif_counts.values())
        if total == 0: return 0
        probs = [motif_counts[m] / total for m in self.motifs_256 if motif_counts[m] > 0]
        entropy = -np.sum(probs * np.log2(probs))
        return entropy / np.log2(256) # 正規化至 0-1