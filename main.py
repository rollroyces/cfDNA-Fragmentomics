from src.simulator import generate_mock_bam
from src.analyzer import FragmentomicsEngine
from src.visualizer import plot_fragment_profile
import os

# 1. 準備數據 (如果沒有真數據，就生成模擬數據)
BAM_FILE = "data/sample.bam"
FASTA_FILE = "data/hg38.fa" # 需自行下載或指向正確路徑

if not os.path.exists(BAM_FILE):
    print("Generating mock data...")
    os.makedirs("data", exist_ok=True)
    generate_mock_bam(BAM_FILE)

# 2. 執行分析
print(f"Analyzing {BAM_FILE}...")
engine = FragmentomicsEngine(BAM_FILE, FASTA_FILE)
# 測試區域：chr1 1-1,000,000
sizes, motifs = engine.process_region("chr1", 0, 1000000)

# 3. 計算學術指標
mds = engine.calculate_mds(motifs)
print(f"Motif Diversity Score (MDS): {mds:.4f}")
print(f"Top 3 Motifs: {motifs.most_common(3)}")

# 4. 生成圖表
plot_fragment_profile(sizes, motifs)
