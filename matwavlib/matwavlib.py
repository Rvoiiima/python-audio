import scipy.io.wavfile as sw
import numpy as np
    
def audio_normalize(y):
    """
    Audio data normalization between [-1, 1].

    Parameters
    ----------
    y: numpy.ndarray  size [1 x N]

    Returns
    ----------
    norm_y: numpy.ndarray
        normalized audio data the range is [-1, 1]

    """

    if y.dtype == "float32" or y.dtype == "float64":
        max_y = 1
    elif y.dtype == "uint8":
        y = y - 128 # convert unsigned to signed
        max_y = 128
    elif y.dtype == "int16":
        max_y = np.abs(np.iinfo(np.int16).min)
    elif y.dtype == "int32":
        max_y = np.abs(np.iinfo(np.int32).min)
    else:
        raise ValueError("%s can't use datatype for audio normalization. \
            Datatype must be [float32, float64, uint8, int16, int32]" % (y.dtype))
        max_y = np.abs(np.iinfo(np.int16).min)

    norm_y = y / max_y
    norm_y = y.astype(np.float32)
    return norm_y

def wavread(wavefile, norm=True):
    """
    read wavfile like matlab audioread() function.

    Parameters
    ----------
    wavefile: str
        wavefile path to read
    norm: bool, default:True
        audio data normalization settings
        call audio_normalize() function

    Returns
    ----------
    y: np.ndarray
        audio data
    fs: int
        sampling rate

    """
    fs, y = sw.read(wavefile)
    if norm:
        y = audio_normalize(y)
    return (y, fs)

def wavwrite(wavefile, data, fs, ftype="float32"):
    """
    write wavfile like matlab audiowrite() function.

    Parameters
    ----------
    wavefile: str
        wave filepath to write
    data: np.ndarray size [1 x N]
        data.dtype must be [float32, float64, uint8, int16, int32]
    fs: sampling rate to write wavefile
    ftype: str, default float32
        wave filetype specification.   
        support: [float32(defalut), uint8, int16, int32]
            int: integer PCM formats.
            float: floating-point formats.

    """

    if data.dtype != "float32":
        data = audio_normalize(data)

    if ftype == "float32":
        y = data
    elif ftype == "int32":
        y = np.int32(data * np.abs(np.iinfo(np.int32).min))
    elif ftype == "int16":
        y = np.int16(data * np.abs(np.iinfo(np.int16).min))
    elif ftype == "uint8":
        y = np.int8(data * 128)
        y = y + 128 #convert signed to unsigned
    else:
        print("warning: this function can't support", ftype, ".", wavefile, "was written as float32")
    
    sw.write(wavefile,fs,y)


if __name__ == "__main__":
    print("============= norm=True (default) =============")
    y, fs = wavread("input.wav")

    print("input Datatype:", y.dtype)

    wavwrite("output.wav", y, fs)
    # confirm output.wav data type
    yout, fsout = wavread("output.wav", norm=False) 
    print("output Datatype:", yout.dtype)
    print()
    print("============= norm=False and specified datatype of writefile ============")
    y, fs = wavread("input.wav", norm=False)
    print("input Datatype:", y.dtype)

    wavwrite("output.wav", y, fs, ftype="int32")
    yout, fsout = wavread("output.wav", norm=False)
    # confirm output.wav data typ 
    print("output Datatype:", yout.dtyp)
    