def get_info():

    import mmap
    import os
    import re
    from tkinter.filedialog import askdirectory
    filename = askdirectory()
    amount = 0
    found = []
    sn = re.compile(b'(\d\d\d\w\w\w\d\d\d\d)')


    for subdir, dirs, files in os.walk(filename):
        for file in files:
            filepath = subdir + os.sep + file
            #if not (not filepath.endswith(".mc")):
            f = open(filepath, 'r')
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            find_sn = sn.search(s)
            #loc_s = s.find(b'\x0cM2')
            print(find_sn)
            print(filepath)
            f.close()



get_info()