
def get_info():

    import mmap
    import os
    from tkinter.filedialog import askdirectory
    import re
    filename = askdirectory()
    amount = 0
    found = []
    info_cp = {"vers": b'(\D\d\d.\d\d.\d\d)',
               "model": b'(\D\D\d\d\D\D\D\d\D\D\d\D\D)',
               "serial": b'(\d\d\d\D\D\D\d\d\d\d)',
               "flash": b'(\d{5}-\d{5}-\d)'}
    ser = re.compile(info_cp['serial'])
    ver = re.compile(info_cp['vers'])
    mod = re.compile(info_cp['model'])
    fla = re.compile(info_cp['flash'])


    for subdir, dirs, files in os.walk(filename):
        for file in files:
            filepath = subdir + os.sep + file
            f = open(filepath, 'r')
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            print(filepath,
                  ser.findall(s),
                  ver.findall(s),
                  mod.findall(s),
                  fla.findall(s))
            found.append(filepath)
            f.close()


get_info()