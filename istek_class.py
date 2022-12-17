class istek:

    def __init__(self,a={},deger={}):
        self.a = a
        self.deger = deger
    
    def ekle(self):
        properties = {}
        property_list = []
        while True:
            x = input("\nHangi ozelliği eklemek istersiniz: 1.Fiyat 2.Renk 3.Adet (eklemek istemiyorsanız 0 giriniz.)")
            prop_dict = {"1":"Fiyat", "2":"Renk", "3": "Adet"}
            try:
                if x == "0":
                    break
                elif x == "1":
                    self.deger = int(input("\nFiyatı? "))
                    properties["Fiyat"] = self.deger
                elif x == "2":
                    self.deger = str(input("\nRengi? "))
                    properties["Renk"] = self.deger
                elif x == "3":
                    self.deger = int(input("\nAdedi? "))
                    properties["Adet"] = self.deger
                else:
                    print("\n0 ile 3 seçenekleri arasından seçim yapınız.")
            except:
                print("\nİstenilen türde veri girilmedi...")
                break
                
        property_list.append(properties)    
        return property_list

    def menu(self):
        while True:
            choice = input("\nProgramdan çıkmak için 0, Ürün eklemek için 1 giriniz: ")
            if choice == "0":
                print("\nÇıkış yaptınız.\n")
                return False
            elif choice == "1":
                product = input("\nÜrün Adı ? ")
                return product
            else:
                print("\nHatalı giriş yaptınız. 0 ya da 1 arasında seçim yapnız.")

i = istek()
all_products = {}

while True:
    product = i.menu()
    if product == False:
        break
    all_products[product] = i.ekle()

#print("\nÜrünler ve Özellikleri: ", all_products) İstenirse bu şekilde düzensiz de yazdırılabilir.
for i in all_products:
    for j in all_products[i]:
        print(i,"\nFiyat: ",j.get("Fiyat", "Belirtilmemiş"),"\nRenk: ",j.get("Renk", "Belirtilmemiş"),"\nAdet: ",j.get("Adet", "Belirtilmemiş"),"\n")
