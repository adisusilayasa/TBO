from glob import glob


def filetext():
    Directory = r"D:\Kuliah\Semester V\TBO\Week 7\DokumenBasaBali" + "\*.txt"

    kelipatan = 0
    for filepath in glob(Directory):
        f = open(str(filepath), mode='r+', encoding='utf-8', errors='ignore')
        kelipatan += 1
        if kelipatan % 50 == 0:
            print("\n\n", "-"*30, "%d dokumen sudah ditampilkan" %
                  (kelipatan), "-"*30, "\n\n")
        print('\033[0m' + '\nSource: ', str(filepath))
