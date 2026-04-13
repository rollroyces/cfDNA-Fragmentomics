import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq

def plot_fragment_profile(sizes, motif_counts):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 圖 A: 片段長度分佈 (167bp 峰值)
    ax1.hist(sizes, bins=range(50, 400), density=True, color='steelblue', alpha=0.7)
    ax1.set_title("cfDNA Size Distribution")
    ax1.axvline(167, color='red', linestyle='--', label='167 bp')
    ax1.set_xlabel("Length (bp)")
    
    # 圖 B: FFT 頻譜分析 (驗證 10bp 週期性) [6]
    counts, _ = np.histogram(sizes, bins=range(50, 250))
    yf = np.abs(rfft(counts - np.mean(counts)))
    xf = rfftfreq(len(counts), 1)
    ax2.plot(xf[1:], yf[1:], color='darkorange')
    ax2.set_title("FFT Periodicity Analysis")
    ax2.axvline(0.1, color='green', linestyle=':', label='10bp peak') # 0.1 Hz = 1/10 bp
    ax2.set_xlabel("Frequency (1/bp)")
    
    plt.tight_layout()
    plt.show()