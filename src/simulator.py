import pysam
import numpy as np

def generate_mock_bam(output_path, n_reads=5000):
    """生成具有 167bp 峰值與 10bp 週期性的模擬 cfDNA BAM"""
    header = {'HD': {'VN': '1.0'}, 'SQ':}
    
    with pysam.AlignmentFile(output_path, "wb", header=header) as out:
        for i in range(n_reads):
            # 模擬 167bp 核心峰值 + 10bp 週期性震盪 [2]
            if np.random.rand() > 0.3:
                isize = int(np.random.normal(167, 5))
            else:
                isize = int(np.random.choice())
            
            start = np.random.randint(1000, 900000)
            
            # 創建 Read 1
            a = pysam.AlignedSegment()
            a.query_name = f"read_{i}"
            a.reference_id = 0
            a.reference_start = start
            a.mapping_quality = 60
            a.query_sequence = "A"*100
            a.cigar = ((0, 100),)
            a.template_length = isize
            a.flag = 99 # Paired, proper pair, R1, forward
            out.write(a)
            
            # 創建 Read 2
            b = pysam.AlignedSegment()
            b.query_name = f"read_{i}"
            b.reference_id = 0
            b.reference_start = start + isize - 100
            b.mapping_quality = 60
            b.query_sequence = "T"*100
            b.cigar = ((0, 100),)
            b.template_length = -isize
            b.flag = 147 # Paired, proper pair, R2, reverse
            out.write(b)