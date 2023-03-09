"""
Functions for normalization
"""
import numpy as np

# Window function for ramn
def get_window(N, alpha=0.2):
    window = np.ones(N)
    x = np.linspace(-1., 1., N)
    ind1 = (abs(x) > 1 - alpha) * (x < 0)
    ind2 = (abs(x) > 1 - alpha) * (x > 0)
    window[ind1] = 0.5 * (1- np.cos(np.pi *(x[ind1]+1)/alpha))
    window[ind2] = 0.5 * (1- np.cos(np.pi *(x[ind2]-1)/alpha))

    return window

# Temporal normalization
# Including one-bit, clipping, running-absolute-mean-normalization 
def normalize(tr, clip_factor=6, clip_weight=10, norm_win=10, norm_method="one_bit"):
    if norm_method == "one_bit":
        tr.data = np.sign(tr.data)
        tr.data = np.float32(tr.data)

    elif norm_method == 'clipping':
        lim = clip_factor * np.std(tr.data)

        tr.data[tr.data > lim] = lim
        tr.data[tr.data < -lim] = -lim
    
    elif norm_method == "clipping_iter":
        lim = clip_factor * np.std(np.abs(tr.data))

        while tr.data[np.abs(tr.data) > lim] != []:
            tr.data[tr.data > lim] /= clip_weight
            tr.data[tr.data < -lim] /= clip_weight

    elif norm_method == "ramn":
        lwin = int(tr.stats.sampling_rate * norm_win)
        st = 0
        N = lwin
        while N < tr.stats.npts:
            win = tr.data[st:N]
            w = np.mean(np.abs(win))
            tr.data[st:N] /= w
            st += 1
            N += 1
        
        taper = get_window(tr.stats.npts)
        tr.data *= taper
        
    return tr

# Spectral normalization or whitening
# Just essential for broad seismograms
def whiten(tr, freqmin, freqmax):
    nsamp = tr.stats.sampling_rate
    n = len(tr.data)
    if n == 1:
        return tr
    else:
        frange = float(freqmax) - float(freqmin)
        nsmo = int(np.fix(min(0.01, 0.5 * (frange))* float(n)/nsamp))
        f = np.arange(n) * nsamp /(n -1.)
        JJ = ((f > float(freqmin)) & (f < float(freqmax))).nonzero()[0]

        # Fourier transform
        FFTs = np.fft.fft(tr.data)
        FFTsW = np.zeros(n) + 1j * np.zeros(n)

         
        smo1 = (np.cos(np.linspace(np.pi / 2, np.pi, nsmo+1))**2)
        FFTsW[JJ[0]:JJ[0]+nsmo+1] = smo1 * np.exp(1j * np.angle(FFTs[JJ[0]:JJ[0]+nsmo+1]))

        FFTsW[JJ[0]+nsmo+1:JJ[-1]-nsmo] = np.ones(len(JJ) - 2 * (nsmo+1))\
        * np.exp(1j * np.angle(FFTs[JJ[0]+nsmo+1:JJ[-1]-nsmo]))

        smo2 = (np.cos(np.linspace(0., np.pi/2., nsmo+1))**2.)
        espo = np.exp(1j * np.angle(FFTs[JJ[-1]-nsmo:JJ[-1]+1]))
        FFTsW[JJ[-1]-nsmo:JJ[-1]+1] = smo2 * espo

        whitedata = 2. * np.fft.ifft(FFTsW).real
        
        tr.data = np.require(whitedata, dtype="float32")

        return tr

