from matwavlib import matwavlib as mw

def main():
    print("============= norm=True (default) =============")
    infilepath = "input-2ch.wav"
    outfilepath = "output-2ch.wav"
    y, fs = mw.wavread(infilepath)

    print("input Datatype:", y.dtype)

    mw.wavwrite(outfilepath, y, fs)
    # confirm output.wav data type
    yout, fsout = mw.wavread(outfilepath, norm=False) 
    print("output Datatype:", yout.dtype)
    print()
    print("============= norm=False and specified datatype of writefile ============")
    y, fs = mw.wavread(infilepath, norm=False)
    print("input Datatype:", y.dtype)

    mw.wavwrite(outfilepath, y, fs, ftype="int32")
    yout, fsout = mw.wavread(outfilepath, norm=False)
    # confirm output.wav data typ 
    print("output Datatype:", yout.dtype)

if __name__ == '__main__':
    main()
