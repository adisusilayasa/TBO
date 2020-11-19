from glob import glob
# ganti directory folder di dalam string di bawah ini!
# P.S : Untuk (+ "\*.txt") dibiarkan saja
Directory = r"D:\Kuliah\Semester V\TBO\Week 7\DokumenBasaBali" + "\*.txt"


def find(array_user):
    sama = 0
    jumlah_file = 0
    kelipatan = 0

    # membuka dir penyimpanan file txt
    for filepath in glob(Directory):

        jumlah_file += 1
        kelipatan += 1
        if kelipatan % 50 == 0:
            print("-"*30, "%d dokumen sudah diperiksa" % (kelipatan), "-"*30)
        # proses sama string
        # looping x isi dari array_user
        for x in array_user:
            f = open(str(filepath), mode='r+',
                     encoding='utf-8', errors='ignore')

            # inisialisasi variable output
            i_found_you = 0
            file = f

            # inisialisasi state
            if (x != ' '):
                state = 0
                jumlah_state = len(x)

            # cek apakah inputan ada terdapat dalam artikel?
            j = 0
            for line in file:  # mengecek per baris
                for i in line:  # mengecek kata/string dalam baris
                    if state == 0:
                        if i == x[j]:
                            state += 1
                            j += 1
                    elif state != 0:
                        if state == jumlah_state:
                            i_found_you += 1
                            break
                        elif i == x[j]:
                            state += 1
                            j += 1
                        else:
                            state = 0
                            j = 0
                if i_found_you != 0:  # jika dalam suatu baris ditemukan string yang sama maka perulangan digentikan
                    break
                # end loop char in line
            if i_found_you != 0:
                temp = 0

                print("Input : ", x)
                print("State : ", end=" ")
                for m in range(len(x)+1):
                    print('q%d' % (m), end=" ")

                print("\nStart state : q0")

                print("Final state : q%d" % (len(list(x))))

                print("Delta :")
                for q in list(x):
                    print("δ (q%d,%s) = q%d" % (temp, q, temp+1))
                    temp += 1
                print('\n\033[1m.... ' + line[0:300])
                break
            # end loop line in file
        # end loop x in array_user

        if i_found_you != 0:
            sama += 1
            print('\033[0m' + '\nSource: ', str(filepath), "\n\n")
        # else:
        #     continue
        f.close()
    if sama > 0:
        print("\n", "-"*30, sama, " dari ",
              jumlah_file, " artikel ditemukan!", "-"*30)
    elif sama == 0:
        print("\n Tidak ada artikel yang ditemukan...")
    # end loop filepath
