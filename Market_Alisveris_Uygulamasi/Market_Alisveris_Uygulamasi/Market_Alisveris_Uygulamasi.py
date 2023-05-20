import datetime
users={
    "users":[["meryem","4444"],["ahmet","İstinye123"]]
}
Envanter = {"kuşkonmaz": [6, 3], "brokoli": [20, 7], "havuç": [15, 5], "elmalar": [25, 15], "muz":
    [19, 18], "meyve": [23, 5], "yumurta": [44, 4], "karışık meyve suyu": [1, 19], "balık çubukları": [27, 10],
            " dondurma": [0, 4], "elma suyu": [33, 8], "portakal suyu": [32, 4], "üzüm suyu":
                [21, 16]}
def MenuYazdir():
    string="""
**** İstinye Online Market’e Hoşgeldiniz ****
Lütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın
    """
    print(string)
MenuYazdir()

page = True
while page:
    run = False
    control = True
    basket = []
    while control:
        username=input("Kullanıcı adı:")
        password=input("Şifre:")
        for x in users["users"]:
            if x[0]==username and  x[1]==password:
                run=True
                print(f"""
            Başarıyla giriş yapıldı!
            Hoşgeldiniz {username}! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.
                    """)
                control=False
        if run==False:
            print("Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!")

    def find(values, searchFor):
        products=[]
        for k in values:
            if searchFor in k:
                products.append(k)
        return products
    def receipt():
        x=1
        total=0
        print("""
            Makbuzunuz işleniyor ...
            ******* İstinye Online Market ********
            *************************************
                0850 283 6000
                istinye.edu.tr
            """)
        print(datetime.datetime.now())
        for i in basket:
            print(x, i[0], "fiyatı =", i[2], "$ miktar = ", i[3], "toplam=", int(i[2]) * i[3])
            x += 1
            total+=int(i[1]) * i[2]
        for i in basket:
            Envanter[i[0]][0] -= i[3]
        basket.clear()

    bulduMu=False
    while run:
        print("""
        Lütfen aşağıdaki hizmetlerden birini seçin:
        1. Ürün ara
        2. Sepete git
        3. Satın al
        4. Oturum Kapat
        5. Çıkış yap
        """)
        selection=int(input("Seçiminiz:"))
        if selection==1:
            search=input("Ne arıyorsunuz?")

            for i in Envanter.items():
                if search in i[0]:
                    bulduMu=True
            if bulduMu is False:
                search=input("Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir şey deneyin (Ana menü için 0 girin):")
                if search=="0":
                    continue



            found=find(Envanter, search)
            print(len(found),"benzer ürün bulundu.")
            counter=1
            selected=[]
            for i in Envanter.items():
                if search in i[0]:
                    print(counter,".",i[0],i[1][1],"$")
                    selected.append([i[0],i[1][0],i[1][1]])
                    counter+=1
            add_a_product=int(input("Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin):"))
            if add_a_product==0:
                continue
            selection_product=selected[add_a_product-1][0]
            amount=int(input(f"{selection_product} ekleniyor. Tutarı Girin:"))
            if int(Envanter[selection_product][0])>amount:
                print(selection_product,"sepetinize eklendi.")
                for i in selected:
                    if i[0]==selection_product:
                        i.append(amount)
                        basket.append(i)

                        print("Ana menüye geri dönülüyor ..")
            if int(Envanter[selection_product][0]) < amount:
                print("Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin.")
                amount = int(input(f"{selection_product} ekleniyor. Tutarı Girin:"))
                for i in selected:
                    if i[0] == selection_product:
                        i.append(amount)
                        basket.append(i)
                        print("Ana menüye geri dönülüyor ..")

        if selection==2:
            if len(basket) == 0:
                print("Sepetiniz de herhangi bir ürün bulunmamaktadır.")
            else:
                print("Sepetiniz şunları içerir:")
                x=1
                total=0
                for i in basket:
                    print(f"{x}. {i[0]} suyu fiyatı=={i[2]}$ miktar={i[3]} toplam={i[3]*i[2]}")
                    x+=1
                    total+=i[3]*i[2]
                print("Toplam",total,"$")
                print("""
                   Bir seçeneği seçiniz:
                       1. Tutarı güncelleyin
                       2. Bir öğeyi kaldırın
                       3. Satın al
                       4. ana menüye dön
                   """)
                secondselection=int(input("Seçiminiz:"))
                if secondselection==1:
                    x = 1
                    for i in basket:
                        print(f"{x}. {i[0]} suyu fiyatı=={i[2]}$ miktar={i[3]} toplam={i[3] * i[2]}")
                        x += 1
                    change=int(input("Lütfen miktarını değiştireceğiniz öğeyi seçin:"))
                    newAmount=int(input("Lütfen yeni miktarı yazın:"))
                    basket[change-1][3]=newAmount
                    print("Sepetiniz artık şunları içeriyor:")
                    x = 1
                    for i in basket:
                        print(f"{x}. {i[0]} suyu fiyatı=={i[2]}$ miktar={i[3]} toplam={i[3] * i[2]}")
                        x += 1
                if secondselection==2:
                    x = 1
                    for i in basket:
                        print(f"{x}. {i[0]} suyu fiyatı=={i[2]}$ miktar={i[3]} toplam={i[3] * i[2]}")
                        x += 1
                    remove = int(input("Kaldırılacak ürünü giriniz:"))
                    basket.pop(remove-1)
                    print("Ürün kaldırıldı.")
                    x = 1
                    for i in basket:
                        print(f"{x}. {i[0]} suyu fiyatı=={i[2]}$ miktar={i[3]} toplam={i[3] * i[2]}")
                        x += 1
                if secondselection==3:
                    receipt()
                if secondselection==4:
                    continue

        if selection==3:
            receipt()
        if selection==4:
            run=False


        if selection==5:
            page=False
            break
