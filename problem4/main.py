def muncul_sekali(angka):
    angka_list = [int(x) for x in angka]
    myset = set()
    
    for angka in angka_list:
        if angka_list.count(angka) == 1:
            myset.add(angka)
            
    return list(myset)
        

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]