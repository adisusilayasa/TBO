from proses import find


def masuk():
    # input
    input_user = ''
    while input_user == '':
        input_user = input("Masukan keyword pencarian: ")
        input_user = str(input_user)
        if input_user == '':
            print("Ulangi !")

    # array user memisahkan setiap kata dari input
    # misal input = Gatra Becik, maka array user = ['Gatra',' ','Becik']
    array_user = input_user.split()
    find(array_user)
