from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


class JokerFinder:
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver\\chromedriver.exe')
        self.places=['/istanbul/besiktas-yildiz','/istanbul/besiktas-visnezade-mah','/istanbul/besiktas-turkali-mah','/istanbul/besiktas-sinanpasa-mah','/istanbul/besiktas-muradiye-mah'
                     ,'/istanbul/arnavutkoy-ilcesi-adnan-menderes-mah',
                     '/istanbul/arnavutkoy-ilcesi-hadimkoy-hastane-mah',
                     '/istanbul/atakoy-1',
                     '/istanbul/atakoy-2',
                     '/istanbul/atakoy-3',
                     '/istanbul/atakoy-4',
                     '/istanbul/atakoy-5',
                     '/istanbul/atakoy-6',
                     '/istanbul/atakoy-7',
                     '/istanbul/atakoy-8',
                     '/istanbul/atakoy-9',
                     '/istanbul/atakoy-10',
                     '/istanbul/avcilar-ambarli-mah',
                     '/istanbul/avcilar-universite-mah',
                     '/istanbul/beylikduzu-yakuplu',
                     '/istanbul/beyoglu-firuzaga-mah',
                     "/istanbul/yesilyurt",
                     "/istanbul/yukari-dudullu",
                     "/istanbul/zeytinburnu-bestelsiz-mah",
                     "/istanbul/zeytinburnu-cirpici-mah",
                     "/istanbul/zeytinburnu-gokalp-mah",
                     "/istanbul/zeytinburnu-kazlicesme-mah",
                     "/istanbul/zeytinburnu-maltepe-mah-cevizlibag",
                     "/istanbul/zeytinburnu-maltepe-mah",
                     "/istanbul/zeytinburnu-merkezefendi-mah-cevizlibag",
                     "/istanbul/zeytinburnu-merkezefendi-mah",
                     "/istanbul/zeytinburnu-seyitnizam-mah",
                     "/istanbul/zeytinburnu-sumer-mah",
                     "/istanbul/zeytinburnu-telsiz-mah",
                     "/istanbul/zeytinburnu-veliefendi-mah",
                     "/istanbul/zeytinburnu-yenidogan-mah",
                     "/istanbul/zeytinburnu-yesiltepe-mah",
                     ]
        self.url= 'https://www.yemeksepeti.com'
        self.current_page= 0

    def login(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/a[28]').click()
        except Exception as e:
            pass
        username_field = self.driver.find_element_by_id('UserName')
        username_field.click()
        username_field.send_keys('mgokberkoguz1@gmail.com')
        password_field = self.driver.find_element_by_id('password')
        password_field.click()
        password_field.send_keys('159753')
        self.driver.find_element_by_id('ys-fastlogin-button').click()

    def change_page(self):
        self.current_page = ((self.current_page +1) % len(self.places)  )
        self.driver.get("https://www.yemeksepeti.com" + self.places[self.current_page])

    def search(self):
        pass

    def _run(self):
        self.driver.get("https://www.yemeksepeti.com" + self.places[self.current_page])
        self.login()
        while True:
            time.sleep(10)
            self.change_page()

JokerFinder()._run()
"""     
try:
    driver = webdriver.Chrome('chromedriver\\chromedriver.exe')
    driver.get("https://www.yemeksepeti.com/")
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/a[28]').click()
    username_field=driver.find_element_by_id('UserName')
    username_field.click()
    username_field.send_keys('mgokberkoguz1@gmail.com')
    password_field=driver.find_element_by_id('password')
    password_field.click()
    password_field.send_keys('159753')
    driver.find_element_by_id('ys-fastlogin-button').click()
    time.sleep(5)
except:
    driver.close()

try:
    element = driver.find_element_by_id('/html/body/header/div[2]/div/div/div[2]/span')
    #driver.execute_script("arguments[0].setAttribute('select2-selection__rendered','vote-link up voted')", element)
except Exception as e:
    print(e)
    #driver.close()
"""

"""
< optgrouplabel = "Diğer Semtler" >< optionvalue = "4f67d031-d26f-4b9f-a648-13dd88978279"data - url = "/istanbul/adatepe" > Adatepe < / option >< optionvalue = "fffb6cba-49b8-4f0b-b34f-0043f4418aa9"data - url = "/istanbul/akatlar" > Akatlar < / option > < optionvalue = "8dde7d50-03bd-4ed7-8aa8-ed16469a9b05"data - url = "/istanbul/alibeykoy" > Alibeyköy < / option >< option value = "6476ed83-619f-439c-b7ec-1704db5eb69a"data - url = "/istanbul/alibeykoy-finanskent" > Alibeyköy(Finanskent) < / option >< optionvalue = "5cb41661-c564-400a-bb1d-e43f954b6381"data - url = "/istanbul/altunizade" > Altunizade < / option >< optionvalue = "db0a63b6-2205-41f3-b462-248fb7577ff2"data - url = "/istanbul/anadoluhisari" > Anadoluhisarı < / option >< option value = "99086cbb-9da5-473c-8a7e-e6b50e279d37" data - url = "/istanbul/arnavutkoy-ilcesi-adnan-menderes-mah" > Arnavutköyİlçesi(AdnanMenderesMah.) < / option >
< optionvalue = "38c2e0d4-6d25-4462-8a17-4d318625287f"data - url = "/istanbul/arnavutkoy-ilcesi-anadolu-mah" > Arnavutköyİlçesi(AnadoluMah.) < / option >< optionvalue = "638bb478-4a98-4159-892e-07e3caf4ff92"data - url = "/istanbul/arnavutkoy-ilcesi-ataturk-mah" > Arnavutköyİlçesi(AtatürkMah.) < / option >
< optionvalue = "7b1f746c-f95a-47fa-bfca-71260d7915e6"data - url = "/istanbul/arnavutkoy-ilcesi-baklali-mah" > Arnavutköyİlçesi(BaklalıMah.) < / option >< optionvalue = "6ae9b295-bd81-4f5a-a322-71b08ab9af90"data - url = "/istanbul/arnavutkoy-ilcesi-balabanburun-mah" > Arnavutköyİlçesi(BalabanburunMah.) < / option >
< optionvalue = "42b4bcef-62d2-42a1-af0e-e9db363d87bb"data - url = "/istanbul/arnavutkoy-ilcesi-bogazkoy-istiklal-mah" > Arnavutköyİlçesi(BoğazköyİstiklalMah.) < / option >< optionvalue = "2976dd82-ad52-4a78-af8f-8be2d9c83fd8"data - url = "/istanbul/arnavutkoy-ilcesi-bolluca-mah" > Arnavutköyİlçesi(Bolluca
    
<optgroup label="Diğer Semtler">
<option value="4f67d031-d26f-4b9f-a648-13dd88978279" data-url="/istanbul/adatepe">Adatepe</option>
<option value="fffb6cba-49b8-4f0b-b34f-0043f4418aa9" data-url="/istanbul/akatlar">Akatlar</option>
<option value="8dde7d50-03bd-4ed7-8aa8-ed16469a9b05" data-url="/istanbul/alibeykoy">Alibeyköy</option>
<option value="6476ed83-619f-439c-b7ec-1704db5eb69a" data-url="/istanbul/alibeykoy-finanskent">Alibeyköy (Finanskent)</option>
<option value="5cb41661-c564-400a-bb1d-e43f954b6381" data-url="/istanbul/altunizade">Altunizade</option>
<option value="db0a63b6-2205-41f3-b462-248fb7577ff2" data-url="/istanbul/anadoluhisari">Anadoluhisarı</option>
<option value="99086cbb-9da5-473c-8a7e-e6b50e279d37" data-url="/istanbul/arnavutkoy-ilcesi-adnan-menderes-mah">Arnavutköy İlçesi (Adnan Menderes Mah.)</option>
<option value="38c2e0d4-6d25-4462-8a17-4d318625287f" data-url="/istanbul/arnavutkoy-ilcesi-anadolu-mah">Arnavutköy İlçesi (Anadolu Mah.)</option>
<option value="638bb478-4a98-4159-892e-07e3caf4ff92" data-url="/istanbul/arnavutkoy-ilcesi-ataturk-mah">Arnavutköy İlçesi (Atatürk Mah.)</option>
<option value="7b1f746c-f95a-47fa-bfca-71260d7915e6" data-url="/istanbul/arnavutkoy-ilcesi-baklali-mah">Arnavutköy İlçesi (Baklalı Mah.)</option>
<option value="6ae9b295-bd81-4f5a-a322-71b08ab9af90" data-url="/istanbul/arnavutkoy-ilcesi-balabanburun-mah">Arnavutköy İlçesi (Balabanburun Mah.)</option>
<option value="42b4bcef-62d2-42a1-af0e-e9db363d87bb" data-url="/istanbul/arnavutkoy-ilcesi-bogazkoy-istiklal-mah">Arnavutköy İlçesi (Boğazköy İstiklal Mah.)</option>
 <option value="2976dd82-ad52-4a78-af8f-8be2d9c83fd8" data-url="/istanbul/arnavutkoy-ilcesi-bolluca-mah">Arnavutköy İlçesi (Bolluca Mah.)</option>
<option value="67c0e7b8-0457-4df4-bfd8-032f18897e09" data-url="/istanbul/arnavutkoy-ilcesi-boyalik-mah">Arnavutköy İlçesi (Boyalık Mah.)</option>
<option value="9119860d-5041-4234-aa25-fe31a1684e40" data-url="/istanbul/arnavutkoy-ilcesi-cilingir-mah">Arnavutköy İlçesi (Çilingir Mah.)</option>
<option value="d51de694-30be-4269-94b0-773846ff845d" data-url="/istanbul/arnavutkoy-ilcesi-deliklikaya-mah">Arnavutköy İlçesi (Deliklikaya Mah.)</option>
<option value="08abced2-4dcb-4ca4-8ff1-5c3264e8b6c6" data-url="/istanbul/arnavutkoy-ilcesi-dursunkoy-mah">Arnavutköy İlçesi (Dursunköy Mah.)</option>
<option value="b00c5d07-613b-4850-a245-a6f2aed3277f" data-url="/istanbul/arnavutkoy-ilcesi-durusu-mah">Arnavutköy İlçesi (Durusu Mah.)</option>
<option value="e5e299b4-3c18-4624-aad2-6d166c4fb754" data-url="/istanbul/arnavutkoy-ilcesi-fatih-mah">Arnavutköy İlçesi (Fatih Mah.)</option>
<option value="d45a222e-d602-4ed1-a291-3d76f00800c0" data-url="/istanbul/arnavutkoy-ilcesi-hacimasli-mah">Arnavutköy İlçesi (Hacımaşlı Mah.)</option>
<option value="b6ff2239-cd0a-47fe-8073-1eba1dc55921" data-url="/istanbul/arnavutkoy-ilcesi-hadimkoy-hastane-mah">Arnavutköy İlçesi (Hadımköy Hastane Mah.)</option>
<option value="ba27c0d8-0fab-4c91-9a35-6545c3c4adb1" data-url="/istanbul/arnavutkoy-ilcesi-hadimkoy-mah">Arnavutköy İlçesi (Hadımköy Mah.)</option>
<option value="d01b259c-b169-47ee-afad-8edbb10a8303" data-url="/istanbul/arnavutkoy-ilcesi-haracci-mah">Arnavutköy İlçesi (Haraççı Mah.)</option>
<option value="9cc7d887-c176-4a76-b2a2-f6c25da669ea" data-url="/istanbul/arnavutkoy-ilcesi-hicret-mah">Arnavutköy İlçesi (Hicret Mah.)</option>
<option value="f73bbaa5-2d50-4be8-89e6-887db1a6077c" data-url="/istanbul/arnavutkoy-ilcesi-imrahor-mah">Arnavutköy İlçesi (İmrahor Mah.)</option>
<option value="1e9ec057-e50b-4198-ad00-961b2bc06b2e" data-url="/istanbul/arnavutkoy-ilcesi-islambey-mah">Arnavutköy İlçesi (İslambey Mah.)</option>
<option value="43efc985-a33f-4102-a1d5-bdb84ba6cc71" data-url="/istanbul/arnavutkoy-ilcesi-karaburun-mah">Arnavutköy İlçesi (Karaburun Mah.)</option>
<option value="07735ee0-d2c1-4a46-8db7-899d0fe55cc9" data-url="/istanbul/arnavutkoy-ilcesi-karlibayir-mah">Arnavutköy İlçesi (Karlıbayır Mah.)</option>
<option value="a2d54421-055f-4048-9407-4482dc0169ee" data-url="/istanbul/arnavutkoy-ilcesi-m-fevzi-cakmak-mah">Arnavutköy İlçesi (M. Fevzi Çakmak Mah.)</option>
<option value="d0a7c865-46b8-43fa-a5c3-925b809e1fe6" data-url="/istanbul/arnavutkoy-ilcesi-mavigol-mah">Arnavutköy İlçesi (Mavigöl Mah.)</option>
<option value="6e8f7256-5fc7-4e82-8377-009795861ebf" data-url="/istanbul/arnavutkoy-ilcesi-mehmet-akif-ersoy-mah">Arnavutköy İlçesi (Mehmet Akif Ersoy Mah.)</option>
<option value="53fa1f48-5703-4f49-a4aa-c496473966ef" data-url="/istanbul/arnavutkoy-ilcesi-merkez-mah">Arnavutköy İlçesi (Merkez Mah.)</option>
<option value="e153df0a-91f8-47a7-8ed7-4a97c53f4bf9" data-url="/istanbul/arnavutkoy-ilcesi-mustafa-kemal-pasa-mah">Arnavutköy İlçesi (Mustafa Kemal Paşa Mah.)</option>
<option value="f035bf3a-5c7e-4375-9331-bd712d9b60ba" data-url="/istanbul/arnavutkoy-ilcesi-nene-hatun-mah">Arnavutköy İlçesi (Nene Hatun Mah.)</option>
<option value="5d1ae380-f8b8-4341-acbe-04782aca7325" data-url="/istanbul/arnavutkoy-ilcesi-omerli-mah">Arnavutköy İlçesi (Ömerli Mah.)</option>
<option value="e5181d32-08cb-46a3-923e-5a4ddb4ab788" data-url="/istanbul/arnavutkoy-ilcesi-sazlibosna-mah">Arnavutköy İlçesi (Sazlıbosna Mah.)</option>
<option value="610537c7-1d50-4a91-ae3e-62b811d80919" data-url="/istanbul/arnavutkoy-ilcesi-tasoluk-mah">Arnavutköy İlçesi (Taşoluk Mah.)</option>
<option value="542bf07e-5500-44bf-bf71-755fb1844b2e" data-url="/istanbul/arnavutkoy-ilcesi-tayakadin-mah">Arnavutköy İlçesi (Tayakadın Mah.)</option>
<option value="bdbc2e88-d2fe-4ce3-bd47-c8a371f380df" data-url="/istanbul/arnavutkoy-ilcesi-terkos-mah">Arnavutköy İlçesi (Terkos Mah.)</option>
<option value="d417a8e3-8065-4b3a-a011-46b7c3b7f262" data-url="/istanbul/arnavutkoy-ilcesi-yassioren-mah">Arnavutköy İlçesi (Yassıören Mah.)</option>
<option value="1b822440-5c4b-4e11-9e9a-01969aebc9d5" data-url="/istanbul/arnavutkoy-ilcesi-yavuz-selim-mah">Arnavutköy İlçesi (Yavuz Selim Mah.)</option>
<option value="9205d431-ea41-40b3-96fd-9e7e202b4c69" data-url="/istanbul/arnavutkoy-ilcesi-yenikoy-mah">Arnavutköy İlçesi (Yeniköy Mah.)</option>
<option value="43be2a64-2858-4fd0-8268-a4a96cb391d7" data-url="/istanbul/arnavutkoy-ilcesi-yesilbayir-mah">Arnavutköy İlçesi (Yeşilbayır Mah.)</option>
<option value="b7b245a0-0053-4308-944f-a9ae1e39ee9e" data-url="/istanbul/arnavutkoy-ilcesi-yunus-emre-mah">Arnavutköy İlçesi (Yunus Emre Mah.)</option>
<option value="abab3976-15df-45c2-8db3-b1ac62b1db90" data-url="/istanbul/asagi-dudullu">Aşağı Dudullu</option>
<option value="b1a94e22-41ef-44f0-8479-28fe26c3c318" data-url="/istanbul/atakoy-1">Ataköy 1.</option>
<option value="1dc7dda4-b668-4fb6-88ef-e6837cb14d4b" data-url="/istanbul/atakoy-10">Ataköy 10.</option>
<option value="40e8f5d4-9224-4d93-a593-8760549d89cf" data-url="/istanbul/atakoy-11">Ataköy 11.</option>
<option value="ef63f055-1cd6-4fcb-b387-0d38a7299cd1" data-url="/istanbul/atakoy-2">Ataköy 2.</option>
<option value="7d4d4052-402a-428c-a3d4-3e00b480699d" data-url="/istanbul/atakoy-3">Ataköy 3.</option>
<option value="b735e339-352c-4d18-ac39-503fd717ef66" data-url="/istanbul/atakoy-4">Ataköy 4.</option>
<option value="3a9d92d2-e715-496d-953a-0e4d70b1eb74" data-url="/istanbul/atakoy-5">Ataköy 5.</option>
<option value="842fdac2-bdaa-4a6c-bbda-27ce3afead90" data-url="/istanbul/atakoy-6">Ataköy 6.</option>
<option value="c6b59db0-e386-43c5-b21d-5ccafa60bf67" data-url="/istanbul/atakoy-7">Ataköy 7.</option>
<option value="435c5cb2-e20b-4141-a88e-560b89a91697" data-url="/istanbul/atakoy-8">Ataköy 8.</option>
<option value="e562d3cc-8f38-488b-a049-601ea601b23e" data-url="/istanbul/atakoy-9">Ataköy 9.</option>
<option value="36b6d250-358f-443b-9b28-82f173c139c8" data-url="/istanbul/atakoy-konaklari">Ataköy Konakları</option>
<option value="b9aedab1-b6fe-4f5f-b60b-4021edc369b5" data-url="/istanbul/atasehir-barbaros-mah">Ataşehir (Barbaros Mah.)</option>
<option value="bcbacab2-e4d2-45df-b6d1-172d9b9001f1" data-url="/istanbul/atasehir-bati">Ataşehir (Batı)</option>
<option value="92f6d60b-849d-4c27-8fb4-474c356e2f57" data-url="/istanbul/atasehir-esatpasa-mah">Ataşehir (Esatpaşa Mah.)</option>
<option value="825a9c2e-af6d-4975-a17c-42f2f58e2b9e" data-url="/istanbul/atasehir-ferhatpasa-mah">Ataşehir (Ferhatpaşa Mah.)</option>
<option value="9508ca99-2cb0-4701-85b6-ec1a328f61ed" data-url="/istanbul/atasehir-fetih-mah">Ataşehir (Fetih Mah.)</option>
<option value="10ed6856-d220-4fab-adc7-4c4ef9be1a87" data-url="/istanbul/atasehir-merkez">Ataşehir (Merkez)</option>
<option value="f3953cd4-9eed-4d1b-957c-85dd4b97157d" data-url="/istanbul/atasehir-mevlana-mah">Ataşehir (Mevlana Mah.)</option>
<option value="9970722c-644e-404f-bab3-a5e1e2b72295" data-url="/istanbul/atasehir-mustafa-kemal-mah">Ataşehir (Mustafa Kemal Mah.)</option>
<option value="a733319b-7fbe-47f0-a5b0-b1b2ab5cb29b" data-url="/istanbul/atasehir-ornek-mah">Ataşehir (Örnek Mah.)</option>
<option value="705af9eb-ca43-42ab-b794-3dbaf426871c" data-url="/istanbul/atasehir-yeni-camlica">Ataşehir (Yeni Çamlıca)</option>
<option value="bc553dab-6419-4c68-b5c7-9840fd36d16b" data-url="/istanbul/atasehir-yenisahra-mah">Ataşehir (Yenisahra Mah.)</option>
<option value="2cdaf998-0345-4117-86ec-d34a4c31efc8" data-url="/istanbul/atasehir-yenisehir-mah">Ataşehir (Yenişehir Mah.)</option>
<option value="e305ff5b-e5f1-486f-8259-04ba5dfb67ec" data-url="/istanbul/avcilar-ambarli-mah">Avcılar (Ambarlı Mah.)</option>
<option value="f07c9e03-2818-456f-b10c-1058ae7cfa5b" data-url="/istanbul/avcilar-cihangir-mah">Avcılar (Cihangir Mah.)</option>
<option value="2fa758d6-dced-4485-a023-7ecf9e4d08da" data-url="/istanbul/avcilar-denizkoskler-mah">Avcılar (Denizköşkler Mah.)</option>
<option value="d63b53be-91c9-408b-b47a-552640d54624" data-url="/istanbul/avcilar-firuzkoy-mah">Avcılar (Firuzköy Mah.)</option>
<option value="f75a5e15-5e67-4ed1-bd60-97f095a9c3d1" data-url="/istanbul/avcilar-gumuspala-mah">Avcılar (Gümüşpala Mah.)</option>
<option value="f4188a72-05db-4ae7-b37d-2fb8f7d990f2" data-url="/istanbul/avcilar-merkez-mah">Avcılar (Merkez Mah.)</option>
<option value="fadcf25a-953b-4e88-a8fe-6f71816ff6e4" data-url="/istanbul/avcilar-mustafa-kemal-pasa-mah">Avcılar (Mustafa Kemal Paşa Mah.)</option>
<option value="61b2802f-c20c-451e-968f-ea0f15b7c1a7" data-url="/istanbul/avcilar-tahtakale-mah-ispartakule-evleri">Avcılar (Tahtakale Mah. - Ispartakule Evleri)</option>
<option value="aa64db55-5db9-4245-874f-d202fc25bc35" data-url="/istanbul/avcilar-tahtakale-mah">Avcılar (Tahtakale Mah.)</option>
<option value="59a1fbae-12e5-4ced-8ac1-2c0afa6aa689" data-url="/istanbul/avcilar-universite-mah">Avcılar (Üniversite Mah.)</option>
<option value="d7ff13a2-c3dd-498d-88eb-6b090b453079" data-url="/istanbul/avcilar-yesilkent-mah">Avcılar (Yeşilkent Mah.)</option>
<option value="ac9a385d-f7a0-46b5-a99a-a16130a64a39" data-url="/istanbul/avrupa-konutlari-tem">Avrupa Konutları (TEM)</option>
<option value="947574de-5073-48f5-8d48-03a12ced0442" data-url="/istanbul/ayazaga">Ayazağa</option>
<option value="c6a6633a-9fd9-4708-89bb-e72e5233f99c" data-url="/istanbul/bagcilar-100-yil-mah">Bağcılar (100. Yıl Mah.)</option>
<option value="2a1b932a-95b2-4f75-b2ea-27ed760636a4" data-url="/istanbul/bagcilar-basin-ekspres-yolu">Bağcılar (Basın Ekspres Yolu)</option>
<option value="23c68d21-c3df-4909-b411-6ee007ddab87" data-url="/istanbul/bagcilar-demirkapi-mah">Bağcılar (Demirkapı Mah.)</option>
<option value="f198fbe7-bb12-4db7-ae69-ee1d30cf2fff" data-url="/istanbul/bagcilar-evren-mah">Bağcılar (Evren Mah.)</option>
<option value="cb0e79de-e711-461c-b54e-c2a85c58d6f2" data-url="/istanbul/bagcilar-fatih-mah">Bağcılar (Fatih Mah.)</option>
<option value="5b804edb-27e7-44ce-8dc4-ee4f3374a8fc" data-url="/istanbul/bagcilar-fevzi-cakmak-mah-tabya">Bağcılar (Fevzi Çakmak Mah. - Tabya)</option>
<option value="f7afbbb7-ce17-4410-856a-533b3cf3e33e" data-url="/istanbul/bagcilar-goztepe-mah">Bağcılar (Göztepe Mah.)</option>
<option value="7e19e39c-e7e0-4129-bede-6a35fdff9862" data-url="/istanbul/bagcilar-gunesli-mah-basin-ekspres-yolu">Bağcılar (Güneşli Mah. - Basın Ekspres Yolu)</option>
<option value="fa77b037-cecf-440e-b492-1241821a0462" data-url="/istanbul/bagcilar-gunesli-mah-merkez">Bağcılar (Güneşli Mah. - Merkez)</option>
<option value="ed72399b-dfc3-4963-abbe-8d42d1519e3c" data-url="/istanbul/bagcilar-gunesli-mah-thy">Bağcılar (Güneşli Mah. - THY)</option>
<option value="3c8d5470-ad9c-4c7c-8833-34e6d80f1af9" data-url="/istanbul/bagcilar-istoc">Bağcılar (İstoç)</option>
<option value="b2362eb7-e53e-43f2-a59a-db6932ebe82d" data-url="/istanbul/bagcilar-kirazli-mah">Bağcılar (Kirazlı Mah.)</option>
<option value="7f8b6044-9cc8-4683-a8f3-607d9b9adf7c" data-url="/istanbul/bagcilar-mahmutbey-mah-basin-ekspres-yolu">Bağcılar (Mahmutbey Mah. - Basın Ekspres Yolu)</option>
<option value="66162f4f-f097-449a-b873-b440117fbe93" data-url="/istanbul/bagcilar-mahmutbey-mah">Bağcılar (Mahmutbey Mah.)</option>
<option value="d87267aa-d5a3-4d85-b58f-af033f0edbca" data-url="/istanbul/bagcilar-merkez">Bağcılar (Merkez)</option>
<option value="292a14f8-e6ab-4987-a31a-a47a8752dce0" data-url="/istanbul/bagcilar-y-selim-mah-ciftlik">Bağcılar (Y. Selim Mah - Çiftlik)</option>
<option value="cd877c55-0769-471c-90b1-2cb77894582e" data-url="/istanbul/bagcilar-yenigun-mah">Bağcılar (Yenigün Mah.)</option>
<option value="5b2db26e-8868-439e-a355-10ae7b6a68fb" data-url="/istanbul/bagcilar-yenimahalle-mah">Bağcılar (Yenimahalle Mah.)</option>
<option value="76d160fd-48a5-43d9-a8b4-43b8f2127a0a" data-url="/istanbul/bahcelievler-merkez">Bahçelievler (Merkez)</option>
<option value="0ef48836-0f9d-4c5e-99d9-8b26a5378d39" data-url="/istanbul/bahcelievler-siyavuspasa">Bahçelievler (Siyavuşpaşa)</option>
<option value="82bd3b7c-8271-4b49-9c7e-1abc57044cfd" data-url="/istanbul/bahcelievler-soganli">Bahçelievler (Soğanlı)</option>
<option value="13db8aba-5e88-4fe9-a659-d0d11c0989e7" data-url="/istanbul/bahcelievler-yayla">Bahçelievler (Yayla)</option>
<option value="f0c2c327-19af-4ae3-9da5-262158cc2ad8" data-url="/istanbul/bakirkoy-incirli">Bakırköy (İncirli)</option>
<option value="9f61d416-1348-415c-862b-8c093f793943" data-url="/istanbul/bakirkoy-kartaltepe-mah">Bakırköy (Kartaltepe Mah.)</option>
<option value="e2e846e4-b5c1-4c08-8491-58c0a85b8628" data-url="/istanbul/bakirkoy-merkez">Bakırköy (Merkez)</option>
<option value="96c75c2f-6f08-46ba-b16d-9d38618af580" data-url="/istanbul/bakirkoy-osmaniye-mah">Bakırköy (Osmaniye Mah.)</option>
<option value="7f799ed3-cee6-4214-ac62-e2efd05a03e4" data-url="/istanbul/bakirkoy-yenimahalle-mah">Bakırköy (Yenimahalle Mah.)</option>
<option value="8d1760d2-95f9-4d41-9a13-548a59750408" data-url="/istanbul/bakirkoy-zeytinlik-mah">Bakırköy (Zeytinlik Mah.)</option>
<option value="a0506658-dc40-455b-8dbb-6fda6cbfaf57" data-url="/istanbul/bakirkoy-zuhuratbaba-mah">Bakırköy (Zuhuratbaba Mah.)</option>
<option value="9ada8682-5103-44da-bb8a-a96c56402711" data-url="/istanbul/balmumcu">Balmumcu</option>
<option value="a860147e-ad4f-44c6-bd00-69ab45d94085" data-url="/istanbul/baltalimani">Baltalimanı</option>
<option value="91e0c79d-4e52-466e-a291-8d2a227f5bb2" data-url="/istanbul/basaksehir-altinsehir-mah">Başakşehir (Altınşehir Mah.)</option>
<option value="234aaf93-4be5-474f-9867-e5e86e92982e" data-url="/istanbul/basaksehir-bahcesehir-1-kisim-mah-estonsehir">Başakşehir (Bahçeşehir 1. Kısım Mah. - Estonşehir)</option>
<option value="3a13a032-d455-4cc2-8b9c-41f70d3ca007" data-url="/istanbul/basaksehir-bahcesehir-1-kisim-mah">Başakşehir (Bahçeşehir 1. Kısım Mah.)</option>
<option value="161c1c97-07f8-4457-b754-4fde1d959f98" data-url="/istanbul/basaksehir-bahcesehir-2-kisim-mah-bogazkoy">Başakşehir (Bahçeşehir 2. Kısım Mah. - Boğazköy)</option>
<option value="3c70fd22-6a73-4b6c-abe3-ce3eb2078d24" data-url="/istanbul/basaksehir-bahcesehir-2-kisim-mah">Başakşehir (Bahçeşehir 2. Kısım Mah.)</option>
<option value="88b114ad-a05b-49c8-baaa-a31860b2fb83" data-url="/istanbul/basaksehir-basak-mah-4-etap">Başakşehir (Başak Mah. - 4. Etap)</option>
<option value="d686e5b8-4848-4f6d-b1fe-2bbd02a22de7" data-url="/istanbul/basaksehir-basak-mah-5-etap">Başakşehir (Başak Mah. - 5. Etap)</option>
<option value="36cc1e85-0011-400e-9eaa-4344c41d45e7" data-url="/istanbul/basaksehir-basak-mah">Başakşehir (Başak Mah.)</option>
<option value="5b791ddc-5f35-4f0d-ab38-56515c3b3ce3" data-url="/istanbul/basaksehir-basaksehir-mah-1-etap">Başakşehir (Başakşehir Mah. - 1. Etap)</option>
<option value="c60eb663-dab4-461d-ac6a-e2ebc7d3a3e2" data-url="/istanbul/basaksehir-basaksehir-mah-2-etap">Başakşehir (Başakşehir Mah. - 2. Etap)</option>
<option value="838cecd6-4e8c-40bc-bfbf-766842d862ec" data-url="/istanbul/basaksehir-basaksehir-mah">Başakşehir (Başakşehir Mah.)</option>
<option value="4fcc28de-04cd-4d31-952e-a700c734a1c5" data-url="/istanbul/basaksehir-guvercintepe-mah">Başakşehir (Güvercintepe Mah.)</option>
<option value="bd0b93fa-9f95-467b-989b-5bf7087ed500" data-url="/istanbul/basaksehir-kayabasi-mah-kayasehir-11-12-13-23-bolge">Başakşehir (Kayabaşı Mah. - Kayaşehir 11/12/13/23. Bölge)</option>
<option value="d4aac127-bcad-4f5a-9d8f-23d52cb08cbf" data-url="/istanbul/basaksehir-kayabasi-mah-kayasehir-14-bolge">Başakşehir (Kayabaşı Mah. - Kayaşehir 14. Bölge)</option>
<option value="3b72a8e0-409f-482b-8416-0f86b0061e68" data-url="/istanbul/basaksehir-kayabasi-mah-kayasehir-16-bolge">Başakşehir (Kayabaşı Mah. - Kayaşehir 16. Bölge)</option>
<option value="4da2c871-215d-4ea8-b9bc-cd3c068ac300" data-url="/istanbul/basaksehir-kayabasi-mah-kayasehir-17-18-19-bolge">Başakşehir (Kayabaşı Mah. - Kayaşehir 17/18/19. Bölge)</option>
<option value="7a8bf154-6079-43a4-9704-fe5b85ff5393" data-url="/istanbul/basaksehir-kayabasi-mah-kayasehir-20-21-bolge">Başakşehir (Kayabaşı Mah. - Kayaşehir 20/21. Bölge)</option>
<option value="c86b5d28-68c1-46e0-8099-c91857874135" data-url="/istanbul/basaksehir-kayabasi-mah-kayasehir">Başakşehir (Kayabaşı Mah. - Kayaşehir)</option>
<option value="88e329dd-11c5-4b97-bdcc-0554ef00e4bb" data-url="/istanbul/basaksehir-sahintepe-mah">Başakşehir (Şahintepe Mah.)</option>
<option value="f5b95965-5a0a-419f-8cad-93a869283397" data-url="/istanbul/basaksehir-samlar-mah">Başakşehir (Şamlar Mah.)</option>
<option value="ce8aed10-28b3-44bf-a3d8-24ae31309489" data-url="/istanbul/basaksehir-ziya-gokalp-mah-ayazma-mevkii">Başakşehir (Ziya Gökalp Mah. - Ayazma Mevkii)</option>
<option value="1aa28771-a60e-49ca-b501-4c49caef5bb3" data-url="/istanbul/bayrampasa-altintepsi-mah">Bayrampaşa (Altıntepsi Mah.)</option>
<option value="212f1e02-360c-4b84-bb3a-98f0f481d3e5" data-url="/istanbul/bayrampasa-cevatpasa-mah">Bayrampaşa (Cevatpaşa Mah.)</option>
<option value="055509a3-8267-4842-b3dc-12954a6c68fe" data-url="/istanbul/bayrampasa-demirkapi">Bayrampaşa (Demirkapı)</option>
<option value="c318164c-c992-45f0-a4a6-7305b86a8fed" data-url="/istanbul/bayrampasa-ismetpasa-mah">Bayrampaşa (İsmetpaşa Mah.)</option>
<option value="9b8fd694-3770-4f90-a26b-079f38612057" data-url="/istanbul/bayrampasa-kartaltepe-mah">Bayrampaşa (Kartaltepe Mah.)</option>
<option value="1b526378-fb77-46e0-8b10-157f79a4b8cc" data-url="/istanbul/bayrampasa-kocatepe-mah">Bayrampaşa (Kocatepe Mah.)</option>
<option value="20cfbcd7-460c-44d6-922e-b539fedb7f53" data-url="/istanbul/bayrampasa-merkez">Bayrampaşa (Merkez)</option>
<option value="fec908ff-5053-4dbb-b86d-56820d01201b" data-url="/istanbul/bayrampasa-muratpasa-mah">Bayrampaşa (Muratpaşa Mah.)</option>
<option value="e30f7da4-70c0-41d1-a92a-c3d64fc2e074" data-url="/istanbul/bayrampasa-ortamahalle-mah">Bayrampaşa (Ortamahalle Mah.)</option>
<option value="d89d911a-e160-4421-9f9c-24263da26c8a" data-url="/istanbul/bayrampasa-terazidere-mah">Bayrampaşa (Terazidere Mah.)</option>
<option value="af2ac7dd-d834-47e5-a270-026f33eaa6fb" data-url="/istanbul/bayrampasa-vatan-mah">Bayrampaşa (Vatan Mah.)</option>
<option value="81659254-a885-4881-9473-6d78a132e66f" data-url="/istanbul/bayrampasa-yenidogan-mah">Bayrampaşa (Yenidoğan Mah.)</option>
<option value="faa523b1-c90a-4ed1-8b0c-e42e58842078" data-url="/istanbul/bayrampasa-yildirim-mah">Bayrampaşa (Yıldırım Mah.)</option>
<option value="d10b0d32-b711-4573-bef2-8fd68feb70de" data-url="/istanbul/bebek">Bebek</option>
<option value="d0b97a38-fc38-4f47-8b6a-98e6ce8b432c" data-url="/istanbul/besevler">Beşevler</option>
<option value="065be97a-0139-4c40-a4af-ee8d6b85018f" data-url="/istanbul/besiktas-akaretler">Beşiktaş (Akaretler)</option>
<option value="a6a21d02-2ce6-4d95-b324-7323fa77ed4a" data-url="/istanbul/besiktas-arnavutkoy-mah">Beşiktaş (Arnavutköy Mah.)</option>
<option value="d3761120-af5b-422d-ac13-4652b824c35c" data-url="/istanbul/besiktas-barbaros">Beşiktaş (Barbaros)</option>
<option value="cbe22b12-a067-4900-be6a-605b5a715a42" data-url="/istanbul/besiktas-merkez">Beşiktaş (Merkez)</option>
<option value="c24db467-5c29-431e-af5b-a9f19c03965a" data-url="/istanbul/besiktas-muradiye-mah">Beşiktaş (Muradiye Mah.)</option>
<option value="a2d700e2-e98f-4ad7-a850-3613f133a6e2" data-url="/istanbul/besiktas-sinanpasa-mah">Beşiktaş (Sinanpaşa Mah.)</option>
<option value="ae7e2478-6150-4773-a285-573a9a6b2528" data-url="/istanbul/besiktas-turkali-mah">Beşiktaş (Türkali Mah.)</option>
<option value="5fd688e3-5214-4cba-bf8e-dfdf816bff2f" data-url="/istanbul/besiktas-visnezade-mah">Beşiktaş (Vişnezade Mah.)</option>
<option value="c3cfaede-ddaf-4abe-8e8a-e6e67cfeb2b2" data-url="/istanbul/besiktas-yildiz">Beşiktaş (Yıldız)</option>
<option value="0fdae0c4-cbca-437b-896c-ce32e3f60c06" data-url="/istanbul/beykent">Beykent</option>
<option value="1065dc90-f759-474b-92d9-12b8b4832521" data-url="/istanbul/beykoz-acarkent">Beykoz (Acarkent)</option>
<option value="0e6ce901-0b95-4163-b5c4-cac176ad24a3" data-url="/istanbul/beykoz-akbabakoyu">Beykoz (Akbabaköyü)</option>
<option value="2106c33b-8c94-4a8b-929f-0e984c11102a" data-url="/istanbul/beykoz-beykoz-kon">Beykoz (Beykoz Kon.)</option>
<option value="2873bb23-ba9e-4bcd-b09a-a3df17bcdf8b" data-url="/istanbul/beykoz-cavusbasi">Beykoz (Çavuşbaşı)</option>
<option value="b49556f6-25d5-460a-9daa-fc78e9188eac" data-url="/istanbul/beykoz-cigdem-mah">Beykoz (Çiğdem Mah.)</option>
<option value="886ab41e-5b22-42b4-87ad-73c2a1781841" data-url="/istanbul/beykoz-cubuklu-mah">Beykoz (Çubuklu Mah.)</option>
<option value="dd5af8d6-b079-4cfc-8d98-12495e96c048" data-url="/istanbul/beykoz-goztepe-mah">Beykoz (Göztepe Mah.)</option>
<option value="44cd5bd6-a6d3-42d0-b263-3483111dbc2a" data-url="/istanbul/beykoz-incirlikoy-mah">Beykoz (İncirliköy Mah.)</option>
<option value="8b9ba20b-9fe8-47c6-a5c3-9961909ec3a7" data-url="/istanbul/beykoz-merkez">Beykoz (Merkez)</option>
<option value="ed2dc29f-f754-4680-8b99-14aa9310676e" data-url="/istanbul/beykoz-ortacesme">Beykoz (Ortaçeşme)</option>
<option value="888873bb-29eb-47c7-b126-76a732c7d645" data-url="/istanbul/beykoz-pasabahce-mah">Beykoz (Paşabahçe Mah.)</option>
<option value="f8857ae9-145e-4bb4-b2e8-f1f59e143222" data-url="/istanbul/beykoz-polonezkoy">Beykoz (Polonezköy)</option>
<option value="dfeaa571-7a60-4fa1-8884-e54c6f47df22" data-url="/istanbul/beykoz-ruzgarlibahce-mah">Beykoz (Rüzgarlıbahçe Mah.)</option>
<option value="c9c62f3d-3f7f-45b4-84b6-ba2f21bd13e8" data-url="/istanbul/beykoz-soguksu-mah">Beykoz (Soğuksu Mah.)</option>
<option value="23f160ee-46ab-49ef-974e-90b48ec5dbcb" data-url="/istanbul/beykoz-tokatkoy">Beykoz (Tokatköy)</option>
<option value="7986db58-1bcd-47ab-8809-0dcec0792e21" data-url="/istanbul/beykoz-vanikoy-mah">Beykoz (Vaniköy Mah.)</option>
<option value="f3138274-dd3b-436a-ace5-4396203339c8" data-url="/istanbul/beykoz-yalikoy-mah">Beykoz (Yalıköy Mah.)</option>
<option value="571e4bd4-fd4c-4d7a-9e0e-5d32aa899856" data-url="/istanbul/beylerbeyi">Beylerbeyi</option>
<option value="d50359c2-c4a5-4754-aaf0-51bbcc2edadd" data-url="/istanbul/beylikduzu-adnan-kahveci-mah">Beylikdüzü (Adnan Kahveci Mah.)</option>
<option value="2ac8d7f0-8c27-4df9-b4af-0070c92b43f7" data-url="/istanbul/beylikduzu-baris-mah">Beylikdüzü (Barış Mah.)</option>
<option value="932a8123-2747-48af-8f59-a0475c170056" data-url="/istanbul/beylikduzu-beykoop-mah">Beylikdüzü (Beykoop Mah.)</option>
<option value="acc72bca-fa40-4579-8fc8-2070c4c8f510" data-url="/istanbul/beylikduzu-buyuksehir-mah">Beylikdüzü (Büyükşehir Mah.)</option>
<option value="54cd4d1d-ccb7-4629-997e-5d590fe88c70" data-url="/istanbul/beylikduzu-cumhuriyet-mah">Beylikdüzü (Cumhuriyet Mah.)</option>
<option value="4abc0d81-516b-4bfb-b5fc-6ec94a96b42a" data-url="/istanbul/beylikduzu-gurpinar">Beylikdüzü (Gürpınar)</option>
<option value="87e01e82-39fa-4034-b94c-2033aad6d730" data-url="/istanbul/beylikduzu-ihlas-mar-evleri-1">Beylikdüzü (İhlas Mar. Evleri 1)</option>
<option value="76c7b13e-b260-4787-9d52-a703271afe95" data-url="/istanbul/beylikduzu-ihlas-mar-evleri-2">Beylikdüzü (İhlas Mar. Evleri 2)</option>
<option value="944d00ea-0b8e-438e-b1ad-31a11285b22f" data-url="/istanbul/beylikduzu-kavakli">Beylikdüzü (Kavaklı)</option>
<option value="5dba633d-40ed-4b9b-b221-0cef23863900" data-url="/istanbul/beylikduzu-merkez">Beylikdüzü (Merkez)</option>
<option value="3ba65627-114b-46d9-bf4f-3d0e22a6e8f5" data-url="/istanbul/beylikduzu-yakuplu">Beylikdüzü (Yakuplu)</option>
<option value="823406ce-6078-4f1d-9977-1a5deaec9095" data-url="/istanbul/beyoglu-arapcami-mah">Beyoğlu (Arapcami Mah.)</option>
<option value="6b747136-ec23-4829-bdca-f1daf32bcb3a" data-url="/istanbul/beyoglu-asmalimescit-mah">Beyoğlu (Asmalımescit Mah.)</option>
<option value="770ef28f-f245-4469-8f8e-7228bfad92f9" data-url="/istanbul/beyoglu-bedrettin-mah">Beyoğlu (Bedrettin Mah.)</option>
<option value="472c9609-b0c0-49f1-b1ae-1618c81bd7de" data-url="/istanbul/beyoglu-bereketzade-mah">Beyoğlu (Bereketzade Mah.)</option>
<option value="15e59aff-9ce8-4479-8fcc-19b8759ad43e" data-url="/istanbul/beyoglu-bostan-mah">Beyoğlu (Bostan Mah.)</option>
<option value="18cf0adf-ae3c-4c2f-b44c-00b160a3dfc1" data-url="/istanbul/beyoglu-bulbul-mah">Beyoğlu (Bülbül Mah.)</option>
<option value="33530ef1-7dae-432b-896b-66fdb1cee0bb" data-url="/istanbul/beyoglu-camiikebir-mah">Beyoğlu (Camiikebir Mah.)</option>
<option value="57a1bdb8-7640-4510-95e0-11dc19a86a1e" data-url="/istanbul/beyoglu-cihangir-mah-siraselviler">Beyoğlu (Cihangir Mah. - Sıraselviler)</option>
<option value="8fde22e3-af3a-4879-ab88-9c17c1eca07a" data-url="/istanbul/beyoglu-cihangir-mah">Beyoğlu (Cihangir Mah.)</option>
<option value="3d6c0fb9-b357-476f-9956-0f082410609f" data-url="/istanbul/beyoglu-catmamescit-mah">Beyoğlu (Çatmamescit Mah.)</option>
<option value="c2383726-440b-4a4d-9585-95b34e786766" data-url="/istanbul/beyoglu-cukur-mah">Beyoğlu (Çukur Mah.)</option>
<option value="4632c2f7-4972-436b-ab91-69fc6a77f252" data-url="/istanbul/beyoglu-emekyemez-mah">Beyoğlu (Emekyemez Mah.)</option>
<option value="ae60bb2a-b83e-4bbf-b421-b4a138bb868a" data-url="/istanbul/beyoglu-evliya-celebi-mah-sishane">Beyoğlu (Evliya Çelebi Mah. - Şişhane)</option>
<option value="81bdb6c1-3ee9-42cd-a3d9-8dc7991d436b" data-url="/istanbul/beyoglu-fetihtepe-mah">Beyoğlu (Fetihtepe Mah.)</option>
<option value="b76d58d4-e057-48fe-9c0d-3ab6ea927e2f" data-url="/istanbul/beyoglu-firuzaga-mah">Beyoğlu (Firüzağa Mah.)</option>
<option value="d9db6f1b-51f2-43d9-b6d2-cc300fbbb9bb" data-url="/istanbul/beyoglu-gumussuyu-mah-taksim">Beyoğlu (Gümüşsuyu Mah. - Taksim)</option>
<option value="53b6c81b-df5a-4223-b7b6-39543221fe25" data-url="/istanbul/beyoglu-gumussuyu-mah">Beyoğlu (Gümüşsuyu Mah.)</option>
<option value="09152f16-04a0-47a6-9ae7-08fa188ba7d9" data-url="/istanbul/beyoglu-haciahmet-mah">Beyoğlu (Hacıahmet Mah.)</option>
<option value="671a2abc-0887-4172-8ee3-8981014b6f20" data-url="/istanbul/beyoglu-hacimimi-mah">Beyoğlu (Hacımimi Mah.)</option>
<option value="15174975-d4ad-4979-ba19-e67951984e20" data-url="/istanbul/beyoglu-halicioglu-mah">Beyoğlu (Halıcıoğlu Mah.)</option>
<option value="a1348c1a-01df-490c-aa5e-dd2310e151cd" data-url="/istanbul/beyoglu-huseyinaga-mah">Beyoğlu (Hüseyinağa Mah.)</option>
<option value="413ca789-11d4-4432-92fd-fff837af9124" data-url="/istanbul/beyoglu-istiklal-mah">Beyoğlu (İstiklal Mah.)</option>
<option value="dbde4c6c-3cef-423f-bc1c-2abc86fcec02" data-url="/istanbul/beyoglu-kadimehmet-mah">Beyoğlu (Kadımehmet Mah.)</option>
<option value="fe2ac764-6e11-4786-880e-d9bf00588f8f" data-url="/istanbul/beyoglu-kalyoncukulluk-mah">Beyoğlu (Kalyoncukulluk Mah.)</option>
<option value="29740046-4416-4770-94f6-9a22fc048f3d" data-url="/istanbul/beyoglu-kamerhatun-mah">Beyoğlu (Kamerhatun Mah.)</option>
<option value="319f127e-bd11-4a51-9b39-85e1dcf20cfe" data-url="/istanbul/beyoglu-kaptanpasa-mah">Beyoğlu (Kaptanpaşa Mah.)</option>
<option value="2288b9d2-ea0c-42bb-9b12-ae550ce21134" data-url="/istanbul/beyoglu-katip-mustafa-celebi-mah">Beyoğlu (Katip Mustafa Çelebi Mah.)</option>
<option value="a8ee9496-9b72-4dd1-83c8-7f796d41f92d" data-url="/istanbul/beyoglu-kececipiri-mah">Beyoğlu (Keçeçipiri Mah.)</option>
<option value="d74f1f07-fd5d-49f2-b56a-a473fba10e6d" data-url="/istanbul/beyoglu-kemankes-mah">Beyoğlu (Kemankeş Mah.)</option>
<option value="e929f729-df21-4366-995b-113c6d815557" data-url="/istanbul/beyoglu-kilic-ali-pasa-mah">Beyoğlu (Kılıç Ali Paşa Mah.)</option>
<option value="add20367-639b-4dc0-aafa-e1af85ee1cb1" data-url="/istanbul/beyoglu-kocatepe-mah">Beyoğlu (Kocatepe Mah.)</option>
<option value="76967ddb-2524-41e2-bead-04b49a163b89" data-url="/istanbul/beyoglu-kulaksiz-mah">Beyoğlu (Kulaksız Mah.)</option>
<option value="22fb3e10-f8ed-4cb5-8a09-9ef67b59616d" data-url="/istanbul/beyoglu-kuloglu-mah">Beyoğlu (Kuloğlu Mah.)</option>
<option value="a27468ee-4285-4ef2-9e99-27466693d386" data-url="/istanbul/beyoglu-kucukpiyale-mah">Beyoğlu (Küçükpiyale Mah.)</option>
<option value="d4874840-4083-4c4f-ac9a-d27ffecead31" data-url="/istanbul/beyoglu-mueyyetzade-mah-karakoy">Beyoğlu (Müeyyetzade Mah. - Karaköy)</option>
<option value="29728fde-2643-4c05-b474-d9d9a09eb9d0" data-url="/istanbul/beyoglu-omeravni-mah-findikli">Beyoğlu (Ömeravni Mah. - Fındıklı)</option>
<option value="35977925-6b26-4764-8c9a-a63200244367" data-url="/istanbul/beyoglu-omeravni-mah-kabatas">Beyoğlu (Ömeravni Mah. - Kabataş)</option>
<option value="8f16e306-0ee3-414e-b785-f0a2e134f019" data-url="/istanbul/beyoglu-ornektepe-mah">Beyoğlu (Örnektepe Mah.)</option>
<option value="c7a5666f-e3fe-45e1-a17c-10cb34af57e2" data-url="/istanbul/beyoglu-piri-pasa-mah">Beyoğlu (Piri Paşa Mah.)</option>
<option value="ab78f759-43c7-4c46-901e-e7885d4baf81" data-url="/istanbul/beyoglu-piyale-pasa-mah">Beyoğlu (Piyale Paşa Mah.)</option>
<option value="7fd75861-eac1-4be6-ad2e-694bfd7c229e" data-url="/istanbul/beyoglu-purtelas-mah">Beyoğlu (Pürtelaş Mah.)</option>
<option value="2c5641dd-fb7c-4d30-bf2c-e3cf8f775a65" data-url="/istanbul/beyoglu-sururi-mah">Beyoğlu (Sururi Mah.)</option>
<option value="20b41fc6-ce73-41c6-b12e-87c1f148ae93" data-url="/istanbul/beyoglu-sutluce-mah">Beyoğlu (Sütlüce Mah.)</option>
<option value="c533eb30-105a-472c-bd8a-5b784b027913" data-url="/istanbul/beyoglu-sahkulu-mah">Beyoğlu (Şahkulu Mah.)</option>
<option value="0e2a20ef-cbac-4e99-ac75-25eb6feb8c12" data-url="/istanbul/beyoglu-sehitmuhtar-mah">Beyoğlu (Şehitmuhtar Mah.)</option>
<option value="29b43857-4915-4aec-a567-a88727a37500" data-url="/istanbul/beyoglu-tomtom-mah">Beyoğlu (Tomtom Mah.)</option>
<option value="e6469ddd-e859-4bdd-9357-c0e3092b5322" data-url="/istanbul/beyoglu-yahya-kahya-mah-kasimpasa">Beyoğlu (Yahya Kahya Mah. - Kasımpaşa)</option>
<option value="839c29d5-ace1-4bce-954c-471cdbbaa92b" data-url="/istanbul/beyoglu-yenisehir-mah">Beyoğlu (Yenişehir Mah.)</option>
<option value="8a086981-edbb-463e-918c-8f47283ad583" data-url="/istanbul/bulgurlu">Bulgurlu</option>
<option value="32735c02-58d4-4151-96e2-36e4329ed851" data-url="/istanbul/burgazada">Burgazada</option>
<option value="80c410d4-db26-43b5-99b3-c22fe9862ae2" data-url="/istanbul/buyuk-bakkalkoy">Büyük Bakkalköy</option>
<option value="041ffee2-83f8-4040-9ad7-9381178e0dba" data-url="/istanbul/buyukada">Büyükada</option>
<option value="1bb2106a-201b-4283-b542-7f9f1cb9b9c4" data-url="/istanbul/buyukcekmece-alkent-2000">Büyükçekmece (Alkent 2000)</option>
<option value="387483a3-9551-4e9e-a194-4abe74973d8b" data-url="/istanbul/buyukcekmece-ataturk-mah">Büyükçekmece (Atatürk Mah.)</option>
<option value="f0995fbb-67d2-421f-83a7-f2f48d0e4ccc" data-url="/istanbul/buyukcekmece-ekinoba">Büyükçekmece (Ekinoba)</option>
<option value="bc054e88-a4bc-493b-bfe8-27b6bc76d715" data-url="/istanbul/buyukcekmece-eml-bank-konutlari">Büyükçekmece (Eml. Bank Konutları)</option>
<option value="5c1509f6-6f75-467c-8d15-19ff6a3f7a58" data-url="/istanbul/buyukcekmece-guzelce-mah">Büyükçekmece (Güzelce Mah.)</option>
<option value="0a5a373e-c3d7-4873-a2f5-2db32b4e9850" data-url="/istanbul/buyukcekmece-kumburgaz-mah">Büyükçekmece (Kumburgaz Mah.)</option>
<option value="c1e7f15d-75d5-4b75-bcc5-1fdf54c622a0" data-url="/istanbul/buyukcekmece-merkez">Büyükçekmece (Merkez)</option>
<option value="82ff1430-5e16-4f5a-b320-9243123e2977" data-url="/istanbul/buyukcekmece-mimar-sinan-mah">Büyükçekmece (Mimar Sinan Mah.)</option>
<option value="103b3748-f98a-4b3a-af3e-6ba8472700b2" data-url="/istanbul/buyukcekmece-mimaroba">Büyükçekmece (Mimaroba)</option>
<option value="61d5a0ad-f95c-4a95-8898-cc647e745780" data-url="/istanbul/buyukcekmece-sinanoba">Büyükçekmece (Sinanoba)</option>
<option value="6787c0a4-d110-4e9f-b8d5-aa7c657a6246" data-url="/istanbul/buyukcekmece-tepekent-sitesi">Büyükçekmece (Tepekent Sitesi)</option>
<option value="ab114e2c-3fde-49e3-b14c-437c9a92d353" data-url="/istanbul/camlica-buyuk">Çamlıca (Büyük)</option>
<option value="b60af4ea-373e-425a-9385-0ed3bcf9addb" data-url="/istanbul/camlica-kucuk">Çamlıca (Küçük)</option>
<option value="c991f30b-30a4-45bf-a306-75148e938d68" data-url="/istanbul/catalca">Çatalca</option>
<option value="81852833-f448-45c5-b3d9-5620054933b1" data-url="/istanbul/cekmekoy-alemdag-mah">Çekmeköy (Alemdağ Mah.)</option>
<option value="58ede6bc-8c7d-4787-823a-7e3e376e6ed5" data-url="/istanbul/cekmekoy-aydinlar-mah">Çekmeköy (Aydınlar Mah.)</option>
<option value="d10f4ae9-d646-48cf-a73c-4f18eb4a74c4" data-url="/istanbul/cekmekoy-cumhuriyet-mah">Çekmeköy (Cumhuriyet Mah.)</option>
<option value="9bee4a2a-e90b-40ed-8f99-5a5074df39a9" data-url="/istanbul/cekmekoy-camlik-mah">Çekmeköy (Çamlık Mah.)</option>
<option value="97515fa5-055b-48c6-b1df-ed54f1c3c311" data-url="/istanbul/cekmekoy-catalcesme-mah-catalmese">Çekmeköy (Çatalçeşme Mah. - Çatalmeşe)</option>
<option value="8090d77a-1c3d-4956-9588-86a6d246470c" data-url="/istanbul/cekmekoy-cavusbasi-bolg-merkez-mah">Çekmeköy (Çavuşbaşı Bölg. - Merkez Mah.)</option>
<option value="f98a7430-d71d-4b32-a574-fef2484cbd62" data-url="/istanbul/cekmekoy-eksioglu-mah">Çekmeköy (Ekşioğlu Mah.)</option>
<option value="a7352f3c-440a-44bf-955d-31a77f1fca9c" data-url="/istanbul/cekmekoy-gungoren-mah">Çekmeköy (Güngören Mah.)</option>
<option value="d0ff3b79-d0a6-472d-b1dc-89f37dc5f5ab" data-url="/istanbul/cekmekoy-hamidiye-mah">Çekmeköy (Hamidiye Mah.)</option>
<option value="619ecb1c-57d8-481a-8418-daff78af7e91" data-url="/istanbul/cekmekoy-kirazlidere-mah">Çekmeköy (Kirazlıdere Mah.)</option>
<option value="1d836976-bb9e-460d-a3ee-5e14f0c5f805" data-url="/istanbul/cekmekoy-mehmet-akif-mah">Çekmeköy (Mehmet Akif Mah.)</option>
<option value="9f51fc52-1dd4-4b1a-8381-2219a075cea1" data-url="/istanbul/cekmekoy-merkez-mah">Çekmeköy (Merkez Mah.)</option>
<option value="7d1c5339-4738-4741-87f0-511c7143cc00" data-url="/istanbul/cekmekoy-mimar-sinan-mah">Çekmeköy (Mimar Sinan Mah.)</option>
<option value="733f1090-18cc-4774-8839-dd29fe3ac7a4" data-url="/istanbul/cekmekoy-nisantepe-mah">Çekmeköy (Nişantepe Mah.)</option>
<option value="4e96beef-f488-4771-8d33-d35c73cc2294" data-url="/istanbul/cekmekoy-omerli-mah">Çekmeköy (Ömerli Mah.)</option>
<option value="9474ba7f-84b3-4d41-98c8-a27c0429ee27" data-url="/istanbul/cekmekoy-resadiye-mah">Çekmeköy (Reşadiye Mah.)</option>
<option value="eac35187-5bf2-406e-ba90-4dc1ec218d20" data-url="/istanbul/cekmekoy-sogukpinar-mah">Çekmeköy (Soğukpınar Mah.)</option>
<option value="8c590438-2ca9-4b82-9b91-23129f60a491" data-url="/istanbul/cekmekoy-sultanciftligi-mah">Çekmeköy (Sultançiftliği Mah.)</option>
<option value="619cdc77-bba6-4464-ac12-79954410b770" data-url="/istanbul/cekmekoy-tasdelen-mah">Çekmeköy (Taşdelen Mah.)</option>
<option value="e300ffa8-e466-4a1a-bfc4-f527f82768d5" data-url="/istanbul/cengelkoy">Çengelköy</option>
<option value="e1b70ef8-2e20-4984-9f74-c1ba4b626a37" data-url="/istanbul/cengelkoy-doktorlar-sit">Çengelköy (Doktorlar Sit.)</option>
<option value="99e606a0-9ba9-45e0-b25c-c57eba318f80" data-url="/istanbul/cengelkoy-nato-yolu">Çengelköy (Nato Yolu)</option>
<option value="64921318-8482-4052-bd69-683b298472d7" data-url="/istanbul/cicekci">Çiçekçi</option>
<option value="3c9ec804-d7fa-49aa-9674-f0e7de0cd087" data-url="/istanbul/dikilitas">Dikilitaş</option>
<option value="29a52d7e-b8ae-4650-b1c4-575d0fca95ff" data-url="/istanbul/dragos">Dragos</option>
<option value="df57761a-1649-46fe-ad86-edf97a0c2737" data-url="/istanbul/emirgan">Emirgan</option>
<option value="444feeb1-e1d6-4bde-90b0-9b085cf84da0" data-url="/istanbul/esenler-birlik-mah">Esenler (Birlik Mah.)</option>
<option value="4a020a9f-7e28-48e3-a881-3b9d1d9d98be" data-url="/istanbul/esenler-davutpasa-mah">Esenler (Davutpaşa Mah.)</option>
<option value="05168c5f-d862-49f3-b859-118170848b08" data-url="/istanbul/esenler-fatih-mah">Esenler (Fatih Mah.)</option>
<option value="29b9a0e7-548e-4d2f-8ab4-950b70ce5014" data-url="/istanbul/esenler-havaalani-mah">Esenler (Havaalanı Mah.)</option>
<option value="98560a63-34a5-4b17-b28c-2f8253c321cd" data-url="/istanbul/esenler-k-karabekir-mah">Esenler (K. Karabekir Mah.)</option>
<option value="9f144f63-0bea-4ed2-aa47-44ef0b552ef5" data-url="/istanbul/esenler-karabayir-mah">Esenler (Karabayır Mah.)</option>
<option value="de86e131-9c28-4038-ae19-1d007ca42df9" data-url="/istanbul/esenler-kemer-mah-atisalani">Esenler (Kemer Mah. - Atışalanı)</option>
<option value="e4810716-f4e7-4f0e-bd59-0840b17d7794" data-url="/istanbul/esenler-menderes-mah">Esenler (Menderes Mah.)</option>
<option value="79bad55d-b4d2-429f-9522-170ce1a33197" data-url="/istanbul/esenler-merkez">Esenler (Merkez)</option>
<option value="b3002d28-80d7-4213-91d3-2e0ed25782d4" data-url="/istanbul/esenler-nine-hatun-mah">Esenler (Nine Hatun Mah.)</option>
<option value="67af4a93-5930-4399-a5ce-137d3d0c2f69" data-url="/istanbul/esenler-orucreis-mah">Esenler (Oruçreis Mah.)</option>
<option value="f0156a17-efd7-4abd-97b5-5c40388e19ca" data-url="/istanbul/esenler-tekstilkent">Esenler (Tekstilkent)</option>
<option value="46f4d34d-238f-4c78-9580-84c91ef2fb40" data-url="/istanbul/esenler-tuna-mah">Esenler (Tuna Mah.)</option>
<option value="157c08a6-23fa-4e95-8128-7c2a560cac36" data-url="/istanbul/esenler-turgutreis-mah">Esenler (Turgutreis Mah.)</option>
<option value="9b201b57-68d0-490e-ad36-d879387cb582" data-url="/istanbul/esenler-ucyuzlu">Esenler (Üçyüzlü)</option>
<option value="1402e44e-9a4c-4a5b-a006-42c00af9b718" data-url="/istanbul/esenyurt-ardicli-mah">Esenyurt (Ardıçlı Mah.)</option>
<option value="c5994d46-0402-4016-9655-b542fa59fb92" data-url="/istanbul/esenyurt-cumhuriyet-mah">Esenyurt (Cumhuriyet Mah.)</option>
<option value="725bc9f1-6053-4762-a458-20f2e7a1d04c" data-url="/istanbul/esenyurt-esenkent-mah">Esenyurt (Esenkent Mah.)</option>
<option value="fa600d4d-5977-4e5f-ab68-45e165bf0e41" data-url="/istanbul/esenyurt-guzelyurt-mah">Esenyurt (Güzelyurt Mah.)</option>
<option value="34645acd-9b14-4a83-8431-738e5b855eef" data-url="/istanbul/esenyurt-incirtepe-mah">Esenyurt (İncirtepe Mah.)</option>
<option value="83bbc3ec-3393-4385-b779-f9a795ceea66" data-url="/istanbul/esenyurt-kirac">Esenyurt (Kıraç)</option>
<option value="d36b2dd4-2f5a-4102-8845-f9094360e2e6" data-url="/istanbul/esenyurt-mehtercesme-mah">Esenyurt (Mehterçeşme Mah.)</option>
<option value="b62f6504-8a13-49e5-be2d-4ba161a1f72a" data-url="/istanbul/esenyurt-merkez">Esenyurt (Merkez)</option>
<option value="b65094ce-5ed0-4eca-bf1a-132da97df1e8" data-url="/istanbul/esenyurt-namik-kemal-mah">Esenyurt (Namık Kemal Mah.)</option>
<option value="5e0a0fc5-b0fc-47db-ade2-b7cb9528e9d6" data-url="/istanbul/esenyurt-saadetdere-mah">Esenyurt (Saadetdere Mah.)</option>
<option value="2d392a78-61ad-448a-933b-6532140eb94b" data-url="/istanbul/esenyurt-talatpasa-mah">Esenyurt (Talatpaşa Mah.)</option>
<option value="8363ed99-73f5-4411-84aa-751eea4d697c" data-url="/istanbul/esenyurt-yesilkent-mah">Esenyurt (Yeşilkent Mah.)</option>
<option value="32b6fe60-705b-4e98-be34-74738fed1252" data-url="/istanbul/etiler">Etiler</option>
<option value="f36b4f20-5320-45ce-954c-7524edae4803" data-url="/istanbul/etiler-fsm-mah">Etiler (FSM Mah.)</option>
<option value="0f0a18b2-13ee-47db-b5e3-6b40e131568c" data-url="/istanbul/eyup-aksemsettin-mah">Eyüp (Akşemsettin Mah.)</option>
<option value="317bd901-4835-4757-a636-1ab503653c0c" data-url="/istanbul/eyup-circir-mah">Eyüp (Çırçır Mah.)</option>
<option value="42747ed5-eaa3-49b5-9f41-a408c92616e9" data-url="/istanbul/eyup-dugmeciler-mah">Eyüp (Düğmeciler Mah.)</option>
<option value="c5965873-04c2-4a75-b098-dfe35c856c48" data-url="/istanbul/eyup-emniyettepe-mah">Eyüp (Emniyettepe Mah.)</option>
<option value="e65974b2-b8c5-424d-99aa-578162c4929b" data-url="/istanbul/eyup-esentepe-mah">Eyüp (Esentepe Mah.)</option>
<option value="3c872222-cabe-4644-b469-988d70a20a9e" data-url="/istanbul/eyup-guzeltepe-mah">Eyüp (Güzeltepe Mah.)</option>
<option value="f85ff7e1-78d5-40e9-855a-f1969010572f" data-url="/istanbul/eyup-islambey-mah">Eyüp (İslambey Mah.)</option>
<option value="714bc2d3-629d-4107-9d6c-2e036a88afb4" data-url="/istanbul/eyup-karadolap-mah">Eyüp (Karadolap Mah.)</option>
<option value="f11b98ff-65de-41bc-9536-ca0a28c463a5" data-url="/istanbul/eyup-merkez">Eyüp (Merkez)</option>
<option value="2b5b4b1a-9131-4a31-94e3-ed5796c29260" data-url="/istanbul/eyup-nisanca-mah">Eyüp (Nişanca Mah.)</option>
<option value="135982c0-2688-4e5a-bb08-d3de9a6a71f4" data-url="/istanbul/eyup-rami-mah">Eyüp (Rami Mah.)</option>
<option value="3e6d75e3-8eef-4f8d-931e-a4bd6ba8d39b" data-url="/istanbul/eyup-sakarya-mah">Eyüp (Sakarya Mah.)</option>
<option value="93a700ee-342e-4d2c-bb7c-f286e1795cc0" data-url="/istanbul/eyup-silahtaraga-mah">Eyüp (Silahtarağa Mah.)</option>
<option value="98c19f2a-e6f1-4827-9f1e-f83be1ffe1a4" data-url="/istanbul/eyup-topcular-mah">Eyüp (Topçular Mah.)</option>
<option value="f290ec13-a7ec-4c89-a872-22c8ebe19eb0" data-url="/istanbul/eyup-yesilpinar">Eyüp (Yeşilpınar)</option>
<option value="06775f55-97e7-4709-a75e-e1c8a1ac1243" data-url="/istanbul/fatih-aksaray-mah">Fatih (Aksaray Mah.)</option>
<option value="a86391f4-dcf8-4927-a0fa-cf4d37d0aa20" data-url="/istanbul/fatih-aksemsettin-mah">Fatih (Akşemsettin Mah.)</option>
<option value="970b9eeb-20a3-4903-8ed1-58d7758ebfaf" data-url="/istanbul/fatih-alemdar-mah">Fatih (Alemdar Mah.)</option>
<option value="2554d5e5-5e0f-4924-97a6-869731d8872f" data-url="/istanbul/fatih-ali-kuscu-mah">Fatih (Ali Kuşçu Mah.)</option>
<option value="5a02db7f-4ac7-47ca-8bf4-1724e05a3b5c" data-url="/istanbul/fatih-atikali-mah">Fatih (Atikali Mah.)</option>
<option value="956e6118-bb3d-4173-b439-3cc2f959e7ad" data-url="/istanbul/fatih-ayvansaray-mah">Fatih (Ayvansaray Mah.)</option>
<option value="d770066d-42a4-4e24-a647-25ddac8fa4a6" data-url="/istanbul/fatih-balabanaga-mah">Fatih (Balabanağa Mah.)</option>
<option value="2af54fda-98a5-4c42-b4a6-48460536e531" data-url="/istanbul/fatih-balat-mah">Fatih (Balat Mah.)</option>
<option value="96e980ac-562e-4f00-a6a4-f45ebaa98d3d" data-url="/istanbul/fatih-beyazit-mah">Fatih (Beyazıt Mah.)</option>
<option value="2b0262f8-c6a8-4fb9-9083-0a99afa01d31" data-url="/istanbul/fatih-binbirdirek-mah">Fatih (Binbirdirek Mah.)</option>
<option value="22677a60-c9d3-4940-b261-8e91d82a17cd" data-url="/istanbul/fatih-cankurtaran-mah">Fatih (Cankurtaran Mah.)</option>
<option value="0fedfcd7-c38e-4862-8865-1244591a27bb" data-url="/istanbul/fatih-cerrahpasa-mah">Fatih (Cerrahpaşa Mah.)</option>
<option value="50d384e9-d774-4596-91c7-7da546de0db8" data-url="/istanbul/fatih-cibali-mah-unkapani">Fatih (Cibali Mah. - Unkapanı)</option>
<option value="c7b9b7c6-d753-4771-af57-e725ce4bab82" data-url="/istanbul/fatih-demirtas-mah">Fatih (Demirtaş Mah.)</option>
<option value="90749ac0-92f6-4e6e-b868-7f05cfbf815f" data-url="/istanbul/fatih-dervisali-mah">Fatih (Dervişali Mah.)</option>
<option value="7eb0f4e0-c866-4a52-836a-9d5e721de921" data-url="/istanbul/fatih-emin-sinan-mah">Fatih (Emin Sinan Mah.)</option>
<option value="ef1dcc39-f16a-4a39-8366-b1961099e500" data-url="/istanbul/fatih-hacikadin-mah">Fatih (Hacıkadın Mah.)</option>
<option value="16dfd2ba-24b9-43eb-8584-02dac189a6ee" data-url="/istanbul/fatih-haseki-sultan-mah-findikzade">Fatih (Haseki Sultan Mah. - Fındıkzade)</option>
<option value="5ebf596f-79ab-4ed6-8e57-2792f8bf163d" data-url="/istanbul/fatih-hirka-i-serif-mah">Fatih (Hırka-i Şerif Mah.)</option>
<option value="1ddc44f0-6e8f-459c-95dc-cae11910ec11" data-url="/istanbul/fatih-hobyar-mah-bahcekapi">Fatih (Hobyar Mah. - Bahçekapı)</option>
<option value="f1c5085d-ce28-4bfa-a3fa-9ec6b3d7ed12" data-url="/istanbul/fatih-hobyar-mah-cagaloglu">Fatih (Hobyar Mah. - Cağaloğlu)</option>
<option value="478f9084-7e89-40e3-90aa-0676d45f160d" data-url="/istanbul/fatih-hoca-giyasettin-mah">Fatih (Hoca Gıyasettin Mah.)</option>
<option value="e62f978b-20b9-4070-a940-49186315359c" data-url="/istanbul/fatih-hoca-pasa-mah-sirkeci">Fatih (Hoca Paşa Mah. - Sirkeci)</option>
<option value="6b67dbc9-f504-40e7-a563-e8d4b424539a" data-url="/istanbul/fatih-iskenderpasa-mah">Fatih (İskenderpaşa Mah.)</option>
<option value="8d893650-c575-4ba7-a67c-0bcb14985aca" data-url="/istanbul/fatih-kalenderhane-mah-sehzadebasi">Fatih (Kalenderhane Mah. - Şehzadebaşı)</option>
<option value="412b4cce-54ef-47b5-b619-a42312c710ea" data-url="/istanbul/fatih-karagumruk-mah">Fatih (Karagümrük Mah.)</option>
<option value="52eb0c17-81dc-450a-bfc5-a7e8061ee7b9" data-url="/istanbul/fatih-katip-kasim-mah-yenikapi">Fatih (Katip Kasım Mah. - Yenikapı)</option>
<option value="f8612797-0419-4c35-87ac-dd813474bf62" data-url="/istanbul/fatih-kemal-pasa-mah">Fatih (Kemal Paşa Mah.)</option>
<option value="c4168c98-9f34-43cc-9781-09edbe1cd2c4" data-url="/istanbul/fatih-kocamustafapasa-mah">Fatih (Kocamustafapaşa Mah.)</option>
<option value="4b482a58-975c-4937-8ce7-2f77e6ea6415" data-url="/istanbul/fatih-kucuk-ayasofya-mah">Fatih (Küçük Ayasofya Mah.)</option>
<option value="23bc1616-4c94-4f59-bc3a-2c3bfae76a63" data-url="/istanbul/fatih-mercan-mah">Fatih (Mercan Mah.)</option>
<option value="908a1249-12ab-476e-9ca6-867462bc21aa" data-url="/istanbul/fatih-mesih-pasa-mah-laleli">Fatih (Mesih Paşa Mah. - Laleli)</option>
<option value="b8b6a0c9-b17d-4f39-9f0d-eb8e2e63a269" data-url="/istanbul/fatih-mevlanakapi-mah">Fatih (Mevlanakapı Mah.)</option>
<option value="ca6ae0bd-fdfd-4733-99ae-be80f2945892" data-url="/istanbul/fatih-mimar-hayrettin-mah">Fatih (Mimar Hayrettin Mah.)</option>
<option value="7e95fc02-cc67-492e-997b-27f4f3516bd7" data-url="/istanbul/fatih-mimar-kemalettin-mah">Fatih (Mimar Kemalettin Mah.)</option>
<option value="bc2b6295-6838-41df-ad5c-8d1dc1e83f01" data-url="/istanbul/fatih-molla-gurani-mah-findikzade">Fatih (Molla Gürani Mah. - Fındıkzade)</option>
<option value="4c669714-028a-4754-8064-f6c32b8a56a4" data-url="/istanbul/fatih-mollafeneri-mah-cemberlitas">Fatih (Mollafeneri Mah. - Çemberlitaş)</option>
<option value="dc860556-a31b-47bc-b8dd-d545b4c049a1" data-url="/istanbul/fatih-mollahusrev-mah">Fatih (Mollahüsrev Mah.)</option>
<option value="68060781-0bc5-47f3-8a7f-aba796190b26" data-url="/istanbul/fatih-muhsine-hatun-mah-kumkapi">Fatih (Muhsine Hatun Mah. - Kumkapı)</option>
<option value="7d298e35-8918-4a94-a792-a27dd669b09c" data-url="/istanbul/fatih-nisanca-mah">Fatih (Nişanca Mah.)</option>
<option value="1b36c94e-0fd0-4bee-9b7f-eadabc121738" data-url="/istanbul/fatih-rustem-pasa-mah">Fatih (Rüstem Paşa Mah.)</option>
<option value="05176e0c-2048-4c97-836c-bf682274928c" data-url="/istanbul/fatih-sarac-ishak-mah">Fatih (Saraç İshak Mah.)</option>
<option value="039ba2b5-8f4b-407f-b3f4-24110d27a451" data-url="/istanbul/fatih-saridemir-mah">Fatih (Sarıdemir Mah.)</option>
<option value="3f434978-a20c-44de-b0e5-e60300870290" data-url="/istanbul/fatih-seyyid-omer-mah-findikzade">Fatih (Seyyid Ömer Mah. - Fındıkzade)</option>
<option value="e2e6f2d5-baaa-4229-b007-a83b04d0261f" data-url="/istanbul/fatih-silivri-kapi-mah">Fatih (Silivri Kapı Mah.)</option>
<option value="2607e5ec-62eb-49b7-9139-f525e3a067f6" data-url="/istanbul/fatih-sultan-ahmet-mah">Fatih (Sultan Ahmet Mah.)</option>
<option value="d113f93d-f91c-4878-8294-b02b36e45fd3" data-url="/istanbul/fatih-sururi-mah">Fatih (Sururi Mah.)</option>
<option value="a7c9356a-57c0-4433-ac7f-27411c60fc21" data-url="/istanbul/fatih-suleymaniye-mah">Fatih (Süleymaniye Mah.)</option>
<option value="beeb2ae6-b62a-4783-9580-0c7b1fbdab86" data-url="/istanbul/fatih-sumbul-efendi-mah">Fatih (Sümbül Efendi Mah.)</option>
<option value="7df69dbe-3626-44fb-b06f-98186f9dde7b" data-url="/istanbul/fatih-sehremini-mah-capa">Fatih (Şehremini Mah. - Çapa)</option>
<option value="5529e65c-66ca-4833-b1d0-33a66fb8e4db" data-url="/istanbul/fatih-sehremini-mah-findikzade">Fatih (Şehremini Mah. - Fındıkzade)</option>
<option value="8923e0f9-75e0-411b-a78f-34cb160ec49b" data-url="/istanbul/fatih-sehsuvarbey-mah">Fatih (Şehsuvarbey Mah.)</option>
<option value="926d4393-ef1a-4ad7-b426-9bbe0e5fa870" data-url="/istanbul/fatih-tahtakale-mah">Fatih (Tahtakale Mah.)</option>
<option value="ada7a1d6-bcf3-45a5-8381-b49cb7cc872e" data-url="/istanbul/fatih-taya-hatun-mah">Fatih (Taya Hatun Mah.)</option>
<option value="bf642919-9826-47a2-adc8-ccc2ae0b80be" data-url="/istanbul/fatih-topkapi-mah">Fatih (Topkapı Mah.)</option>
<option value="7e2e2e0e-1913-4113-8ae5-a0cfb1dee16b" data-url="/istanbul/fatih-yavuz-sinan-mah">Fatih (Yavuz Sinan Mah.)</option>
<option value="84673e9d-8a4a-4244-9158-f3036170c3e9" data-url="/istanbul/fatih-yavuz-sultan-selim-mah">Fatih (Yavuz Sultan Selim Mah.)</option>
<option value="c0e028dc-cbe0-4161-a1fc-60564a20bf97" data-url="/istanbul/fatih-yedikule-mah">Fatih (Yedikule Mah.)</option>
<option value="12ba2be4-7d93-41c9-8956-93b704569031" data-url="/istanbul/fatih-zeyrek-mah-vefa">Fatih (Zeyrek Mah. - Vefa)</option>
<option value="80a159cd-b12e-44ff-9738-5a275a9eefbe" data-url="/istanbul/ferahevler">Ferahevler</option>
<option value="ca97f978-9072-4e40-889f-bdfa3133a278" data-url="/istanbul/florya">Florya</option>
<option value="d4cea2e5-b2d6-4f33-a6e4-113c9dc8303e" data-url="/istanbul/florya-basinkoy">Florya (Basınköy)</option>
<option value="63b97145-2f25-4a63-90e3-efd35c6e389c" data-url="/istanbul/gayrettepe">Gayrettepe</option>
<option value="50aac472-233e-46dc-b5f4-85e9a51155e8" data-url="/istanbul/gaziosmanpasa-b-hayr-pasa-mah">Gaziosmanpaşa (B. Hayr. Paşa Mah.)</option>
<option value="aa159eeb-aa65-4b72-a087-b7ed2c4da54e" data-url="/istanbul/gaziosmanpasa-baglarbasi-mah">Gaziosmanpaşa (Bağlarbaşı Mah.)</option>
<option value="21df4a17-3d7a-4bcd-b993-259ce5c621d2" data-url="/istanbul/gaziosmanpasa-besyuzevler">Gaziosmanpaşa (Beşyüzevler)</option>
<option value="b4aba2db-f968-490f-bc05-605f70925a0d" data-url="/istanbul/gaziosmanpasa-karadeniz-mah">Gaziosmanpaşa (Karadeniz Mah.)</option>
<option value="6f8af7fd-51f0-43e1-8009-5f8deeb891b8" data-url="/istanbul/gaziosmanpasa-karayollari-mah">Gaziosmanpaşa (Karayolları Mah.)</option>
<option value="26f00875-3274-46ca-b950-6dc7f34c8dbb" data-url="/istanbul/gaziosmanpasa-karlitepe-mah">Gaziosmanpaşa (Karlıtepe Mah.)</option>
<option value="2dc00a60-d835-44a5-945b-52165e9dc8c9" data-url="/istanbul/gaziosmanpasa-kucukkoy">Gaziosmanpaşa (Küçükköy)</option>
<option value="2af5c14f-1432-4a24-8f17-dbef4459f867" data-url="/istanbul/gaziosmanpasa-merkez">Gaziosmanpaşa (Merkez)</option>
<option value="238bfb40-9f5a-47ef-839d-745c752eeb9a" data-url="/istanbul/gaziosmanpasa-mevlana-mah">Gaziosmanpaşa (Mevlana Mah.)</option>
<option value="c278427f-0fa5-4e16-9de7-930a524e4567" data-url="/istanbul/gaziosmanpasa-pazarici-mah">Gaziosmanpaşa (Pazariçi Mah.)</option>
<option value="c1e66696-7824-4ef3-aac9-40ef578ab3f0" data-url="/istanbul/gaziosmanpasa-sarigol-mah">Gaziosmanpaşa (Sarıgöl Mah.)</option>
<option value="ce3f4561-57f5-47a8-aa70-4a063f6ecc5a" data-url="/istanbul/gaziosmanpasa-semsipasa-mah">Gaziosmanpaşa (Şemsipaşa Mah.)</option>
<option value="a5ddb0bc-7921-4669-91fd-2f6307f32aab" data-url="/istanbul/gaziosmanpasa-yeni-mah">Gaziosmanpaşa (Yeni Mah.)</option>
<option value="dae604f4-cc81-4dbd-8ab3-109b7d2f0417" data-url="/istanbul/gaziosmanpasa-yenidogan-mah">Gaziosmanpaşa (Yenidoğan Mah.)</option>
<option value="e6702fd5-4824-437c-9ccb-27f5a155ea0d" data-url="/istanbul/gaziosmanpasa-yildiztabya-mah">Gaziosmanpaşa (Yıldıztabya Mah.)</option>
<option value="c71de65b-5f04-4d8a-8185-cbbc5ee918fc" data-url="/istanbul/gokturk-beldesi">Göktürk Beldesi</option>
<option value="acae2237-9b70-4539-9d06-651b3239889e" data-url="/istanbul/gungoren-a-nafiz-gurman-mah">Güngören (A. Nafiz Gürman Mah.)</option>
<option value="c0fa8ccd-5e0d-4e52-9291-8017f6a9369a" data-url="/istanbul/gungoren-akincilar-mah">Güngören (Akıncılar Mah.)</option>
<option value="4ade5b02-9839-4238-a7bc-c348e4b6d88f" data-url="/istanbul/gungoren-gencosman-mah">Güngören (Gençosman Mah.)</option>
<option value="5cc4e962-4cba-4da9-8030-98b0337bbc3f" data-url="/istanbul/gungoren-gunestepe-mah">Güngören (Güneştepe Mah.)</option>
<option value="adbcb869-abc9-45c2-aa5e-fbd5dbdd5fa5" data-url="/istanbul/gungoren-guven-mah">Güngören (Güven Mah.)</option>
<option value="9b3cdc51-e9cd-435c-8bf7-55256b506413" data-url="/istanbul/gungoren-haznedar">Güngören (Haznedar)</option>
<option value="5aaa0fdd-3c63-417d-b36b-c596e5534884" data-url="/istanbul/gungoren-m-cakmak-mah">Güngören (M. Çakmak Mah.)</option>
<option value="21806120-d5a7-45f2-b732-bc5b4581d456" data-url="/istanbul/gungoren-m-nesih-ozmen-mah">Güngören (M. Nesih Özmen Mah.)</option>
<option value="8a68564e-574f-42b4-9f41-07bcc95c72bf" data-url="/istanbul/gungoren-merkez">Güngören (Merkez)</option>
<option value="94df62f7-5b54-4723-b915-76148dbb86c1" data-url="/istanbul/gungoren-sanayi-mah">Güngören (Sanayi Mah.)</option>
<option value="f92dc471-4e5c-41e5-abbb-332fdfe69110" data-url="/istanbul/gungoren-tozkoparan">Güngören (Tozkoparan)</option>
<option value="1f415d24-f7b5-4476-855f-69aa7b8e85a9" data-url="/istanbul/harem">Harem</option>
<option value="3e035f69-b22b-4e8b-9e5f-49c7e283217e" data-url="/istanbul/hisarustu">Hisarüstü</option>
<option value="83a43fb6-ecb1-4533-8bd2-98bb6d2b753a" data-url="/istanbul/icerenkoy">İçerenköy</option>
<option value="34dc4949-a1e1-4ca8-941e-b4848657d23b" data-url="/istanbul/icerenkoy-carrefour">İçerenköy (Carrefour)</option>
<option value="1d94436a-48da-4dfd-a1db-2b4bc7bf0353" data-url="/istanbul/incesu">İncesu</option>
<option value="689a89e0-c155-4e27-b197-8b8a07cc3061" data-url="/istanbul/istinye">İstinye</option>
<option value="db5acf78-a06e-437a-8709-350d677c24a4" data-url="/istanbul/istinye-pinar-mah">İstinye (Pınar Mah.)</option>
<option value="123d7485-2a4d-49d2-a666-934d1c449455" data-url="/istanbul/istinye-poligon-mah">İstinye (Poligon Mah.)</option>
<option value="3d33928b-30a0-4cea-a9d6-a4fc07c27717" data-url="/istanbul/kadikoy-19-mayis-mah">Kadıköy (19 Mayıs Mah.)</option>
<option value="3c2f70e3-b37f-4ec5-90d7-a875e1d6b0eb" data-url="/istanbul/kadikoy-acibadem-mah">Kadıköy (Acıbadem Mah.)</option>
<option value="14632161-148d-4802-89b0-9530aae92dc6" data-url="/istanbul/kadikoy-bostanci-mah-senesenevler">Kadıköy (Bostancı Mah. - Şenesenevler)</option>
<option value="318fd9a0-fb80-4f3f-8288-6f64d5b70c77" data-url="/istanbul/kadikoy-bostanci-mah-ust">Kadıköy (Bostancı Mah. - Üst)</option>
<option value="c470c585-741c-4965-8e8c-6b7970a0f9bf" data-url="/istanbul/kadikoy-bostanci-mah">Kadıköy (Bostancı Mah.)</option>
<option value="8515c9a2-d586-4790-a696-a633b44551cc" data-url="/istanbul/kadikoy-caddebostan-mah-ethemefendi">Kadıköy (Caddebostan Mah. - Ethemefendi)</option>
<option value="eb4f7e22-ec06-4a5d-9953-9c7c2debfe1f" data-url="/istanbul/kadikoy-caddebostan-mah">Kadıköy (Caddebostan Mah.)</option>
<option value="6fb210b5-9ba5-4b53-84b8-5aafe4632c05" data-url="/istanbul/kadikoy-caferaga-mah-moda">Kadıköy (Caferağa Mah. - Moda)</option>
<option value="86a35d24-14e8-475f-a624-eaf52c07cba9" data-url="/istanbul/kadikoy-dumlupinar-mah">Kadıköy (Dumlupınar Mah.)</option>
<option value="8a1d9955-8407-4aaf-8db2-87dd65e0552c" data-url="/istanbul/kadikoy-egitim-mah-kuyubasi">Kadıköy (Eğitim Mah. - Kuyubaşı)</option>
<option value="d9cc124c-e291-4902-9f98-9e0870098fa1" data-url="/istanbul/kadikoy-erenkoy-mah-ethemefendi">Kadıköy (Erenköy Mah. - Ethemefendi)</option>
<option value="b25c4f05-e0d2-4860-b4b5-6e0bf962787d" data-url="/istanbul/kadikoy-erenkoy-mah-ust">Kadıköy (Erenköy Mah. - Üst)</option>
<option value="c59bf141-ee3d-417c-a0f4-a0a25ba1367b" data-url="/istanbul/kadikoy-erenkoy-mah">Kadıköy (Erenköy Mah.)</option>
<option value="27e2adfa-73ca-4b39-81b5-14f33a4460a0" data-url="/istanbul/kadikoy-fenerbahce-mah-kalamis">Kadıköy (Fenerbahçe Mah. - Kalamış)</option>
<option value="6f756fa3-3e11-4882-999f-b0cd4eae4d2d" data-url="/istanbul/kadikoy-fenerbahce-mah-selamicesme">Kadıköy (Fenerbahçe Mah. - Selamiçeşme)</option>
<option value="1820b4bd-21bc-4271-8d8b-ba17f7cb2125" data-url="/istanbul/kadikoy-fenerbahce-mah">Kadıköy (Fenerbahçe Mah.)</option>
<option value="89701872-4be6-4a9d-8938-75b863b6f863" data-url="/istanbul/kadikoy-feneryolu-mah-cemenzar">Kadıköy (Feneryolu Mah. - Çemenzar)</option>
<option value="d2cc3bf3-10e8-479e-86af-cb80e285d5cc" data-url="/istanbul/kadikoy-feneryolu-mah">Kadıköy (Feneryolu Mah.)</option>
<option value="c4a9be7d-ab3f-490e-8916-411e9b16c23e" data-url="/istanbul/kadikoy-fikirtepe-mah">Kadıköy (Fikirtepe Mah.)</option>
<option value="60864cc5-d202-4f82-8f11-4f0d62e746c7" data-url="/istanbul/kadikoy-goztepe-mah-ciftehavuzlar">Kadıköy (Göztepe Mah. - Çiftehavuzlar)</option>
<option value="57e0a6f1-2b1c-4dd6-9e73-bd14bedcf784" data-url="/istanbul/kadikoy-goztepe-mah-ust">Kadıköy (Göztepe Mah. - Üst)</option>
<option value="6e142710-8ca2-4d62-8c55-97a398992a15" data-url="/istanbul/kadikoy-goztepe-mah">Kadıköy (Göztepe Mah.)</option>
<option value="a688dc98-101c-43cd-909e-7e2d69b46b84" data-url="/istanbul/kadikoy-hasanpasa-mah">Kadıköy (Hasanpaşa Mah.)</option>
<option value="0b6daa5e-aaac-4a53-956c-4ddfa5dd6472" data-url="/istanbul/kadikoy-kosuyolu-mah">Kadıköy (Koşuyolu Mah.)</option>
<option value="16b5f195-b7da-42cd-9809-e01e0b18cb74" data-url="/istanbul/kadikoy-kozyatagi-mah-aysekadin">Kadıköy (Kozyatağı Mah. - Ayşekadın)</option>
<option value="81590fca-cdb1-4ae5-844a-94e1b25689a3" data-url="/istanbul/kadikoy-kozyatagi-mah-kazasker">Kadıköy (Kozyatağı Mah. - Kazasker)</option>
<option value="d03ae1eb-5265-4bcb-ac77-b25a147fa59d" data-url="/istanbul/kadikoy-kozyatagi-mah">Kadıköy (Kozyatağı Mah.)</option>
<option value="cee714b8-7230-4a0a-ad76-4310a4dc4744" data-url="/istanbul/kadikoy-merdivenkoy-mah">Kadıköy (Merdivenköy Mah.)</option>
<option value="e90d52a0-65e1-463d-9031-ac6b19a1cd69" data-url="/istanbul/kadikoy-osmanaga-mah-bahariye">Kadıköy (Osmanağa Mah. - Bahariye)</option>
<option value="e0b46c42-6718-4c7c-95be-208e835acd6a" data-url="/istanbul/kadikoy-osmanaga-mah">Kadıköy (Osmanağa Mah.)</option>
<option value="bc8c6ac9-21d9-4bfe-a597-2081329b230c" data-url="/istanbul/kadikoy-rasimpasa-mah-haydarpasa">Kadıköy (Rasimpaşa Mah. - Haydarpaşa)</option>
<option value="af6becc6-8a19-44db-b488-a8e742a53d1d" data-url="/istanbul/kadikoy-rasimpasa-mah">Kadıköy (Rasimpaşa Mah.)</option>
<option value="b3b77d94-f31d-4cbe-8ca3-62fd59d0c78c" data-url="/istanbul/kadikoy-sahrayicedit-mah">Kadıköy (Sahrayıcedit Mah.)</option>
<option value="26580f76-0832-42ab-ac18-2c7603f0415c" data-url="/istanbul/kadikoy-suadiye-mah-saskinbakkal">Kadıköy (Suadiye Mah. - Şaşkınbakkal)</option>
<option value="b98c4128-9114-4445-95cf-495424234739" data-url="/istanbul/kadikoy-suadiye-mah">Kadıköy (Suadiye Mah.)</option>
<option value="4881619f-e728-4633-9e80-1d3653d93c12" data-url="/istanbul/kadikoy-zuhtupasa-mah-kiziltoprak">Kadıköy (Zühtüpaşa Mah. - Kızıltoprak)</option>
<option value="683bffe1-a7b5-40be-b5f7-44dce9e363b1" data-url="/istanbul/kadikoy-zuhtupasa-mah-ziverbey">Kadıköy (Zühtüpaşa Mah. - Ziverbey)</option>
<option value="0ab9cc77-17d6-4619-8a86-972cde409cee" data-url="/istanbul/kagithane-caglayan-mah">Kağıthane (Çağlayan Mah.)</option>
<option value="91483221-7ec0-4780-87b3-f2621adf6aaa" data-url="/istanbul/kagithane-celiktepe-mah">Kağıthane (Çeliktepe Mah.)</option>
<option value="b1d5c3c7-4b23-4abc-83b3-392bc5c3460d" data-url="/istanbul/kagithane-emniyetevleri-mah">Kağıthane (Emniyetevleri Mah.)</option>
<option value="289878bd-565e-4a61-9798-9bb89e5a465c" data-url="/istanbul/kagithane-gultepe-mah">Kağıthane (Gültepe Mah.)</option>
<option value="716d3995-b46e-44fa-b445-fa26106de10e" data-url="/istanbul/kagithane-gursel-mah">Kağıthane (Gürsel Mah.)</option>
<option value="2823d8b2-94e2-4d87-aabf-5352ea3d7e1d" data-url="/istanbul/kagithane-hamidiye-mah">Kağıthane (Hamidiye Mah.)</option>
<option value="9c3fa5c8-2066-49b5-a284-b01959b2f3bc" data-url="/istanbul/kagithane-harmantepe-mah">Kağıthane (Harmantepe Mah.)</option>
<option value="2730219b-8fe2-47f6-9df6-259c35027ed3" data-url="/istanbul/kagithane-hurriyet-mah">Kağıthane (Hürriyet Mah.)</option>
<option value="24e16286-342d-4803-a0a5-511ecc80e650" data-url="/istanbul/kagithane-mehmet-akif-ersoy-mah">Kağıthane (Mehmet Akif Ersoy Mah.)</option>
<option value="a8edfe02-c5bb-43e1-b2ec-08f2737d84cc" data-url="/istanbul/kagithane-merkez-mah">Kağıthane (Merkez Mah.)</option>
<option value="7f0fe717-d1a2-4f11-a748-a0a995729ba7" data-url="/istanbul/kagithane-nurtepe-mah">Kağıthane (Nurtepe Mah.)</option>
<option value="951c7a2f-f635-41a4-bbed-fd04186e501f" data-url="/istanbul/kagithane-ortabayir-mah">Kağıthane (Ortabayır Mah.)</option>
<option value="4fda408f-4a3f-455b-b24e-dde79441c17c" data-url="/istanbul/kagithane-seyrantepe-mah">Kağıthane (Seyrantepe Mah.)</option>
<option value="4f6dd75f-088b-478a-af73-08696bd27de4" data-url="/istanbul/kagithane-sultan-selim-sanayi-mah">Kağıthane (Sultan Selim / Sanayi Mah.)</option>
<option value="22c3c959-923e-4cd9-b018-d930eb12b982" data-url="/istanbul/kagithane-sirintepe-mah">Kağıthane (Şirintepe Mah.)</option>
<option value="cba8828f-60ec-4bdf-97cf-641d2c2d5db9" data-url="/istanbul/kagithane-talatpasa-mah">Kağıthane (Talatpaşa Mah.)</option>
<option value="5d7e5d01-c519-4eba-9268-c4388ae60722" data-url="/istanbul/kagithane-telsizler-mah">Kağıthane (Telsizler Mah.)</option>
<option value="01f5d0c7-9b1f-4b1f-a28b-cb7b9c4a7582" data-url="/istanbul/kagithane-yahya-kemal-mah-ayazma">Kağıthane (Yahya Kemal Mah. - Ayazma)</option>
<option value="db020ebf-a4b9-4527-884c-0da0925fb6c3" data-url="/istanbul/kagithane-yesilce-mah">Kağıthane (Yeşilce Mah.)</option>
<option value="570e8d20-f7a2-4f2b-a666-d5e0afa5f412" data-url="/istanbul/kandilli">Kandilli</option>
<option value="affa11b6-bcb0-406b-9d11-c8ad8b9667a0" data-url="/istanbul/kandilli-rasathane">Kandilli (Rasathane)</option>
<option value="948e0ee1-b0e2-4463-af0c-17983448330f" data-url="/istanbul/kanlica">Kanlıca</option>
<option value="90ffe1a4-b4d3-4dd8-8f26-edb4cd456314" data-url="/istanbul/kartal-cevizli-mah">Kartal (Cevizli Mah.)</option>
<option value="f0e11fc7-a784-4289-9c0f-fe2a2d93fa2a" data-url="/istanbul/kartal-cumhuriyet-mah">Kartal (Cumhuriyet Mah.)</option>
<option value="36436e4c-b5e6-4e91-a704-df30dad14891" data-url="/istanbul/kartal-cavusoglu-mah">Kartal (Çavuşoğlu Mah.)</option>
<option value="16eeff18-f759-4572-9708-4c80495f1206" data-url="/istanbul/kartal-esentepe-mah">Kartal (Esentepe Mah.)</option>
<option value="90ebfb8d-b5f5-44e1-9189-0b05538e2c0e" data-url="/istanbul/kartal-gumuspinar-mah">Kartal (Gümüşpınar Mah.)</option>
<option value="6c074fd3-a611-420a-a8a8-c39dd346a750" data-url="/istanbul/kartal-hurriyet-mah">Kartal (Hürriyet Mah.)</option>
<option value="fd8e3b28-9a21-49f9-ba53-22a3b4b8754a" data-url="/istanbul/kartal-karliktepe-mah">Kartal (Karlıktepe Mah.)</option>
<option value="acbf3e74-b57f-4407-821c-583074be7828" data-url="/istanbul/kartal-kordonboyu-mah">Kartal (Kordonboyu Mah.)</option>
<option value="be21799b-7100-493c-b1a4-526a9228ad46" data-url="/istanbul/kartal-merkez">Kartal (Merkez)</option>
<option value="128d33dd-ab8a-47a4-9fe3-56253cb12eac" data-url="/istanbul/kartal-orhantepe-mah">Kartal (Orhantepe Mah.)</option>
<option value="2cdcbff1-931f-4ea5-acef-043d2ff7a6dc" data-url="/istanbul/kartal-pendik">Kartal (Pendik)</option>
<option value="b7023dfb-19d1-4c9c-af6f-c5a611d3792a" data-url="/istanbul/kartal-petrol-is-mah">Kartal (Petrol-İş Mah.)</option>
<option value="278292fe-a7f7-418b-83bf-f664e06bf372" data-url="/istanbul/kartal-rahmanlar-atalar-mah">Kartal (Rahmanlar - Atalar Mah.)</option>
<option value="b7a9259e-aea2-4627-975a-33598d0b409b" data-url="/istanbul/kartal-soganlik-orta-mah">Kartal (Soğanlık Orta Mah.)</option>
<option value="50dc5ca0-cead-4d47-b6f2-09ad1241fbf9" data-url="/istanbul/kartal-soganlik-yeni-mah">Kartal (Soğanlık Yeni Mah.)</option>
<option value="511a971c-2553-4bfd-81ff-e6b201eec887" data-url="/istanbul/kartal-topselvi-mah">Kartal (Topselvi Mah.)</option>
<option value="607af33c-6a10-4b3e-aca0-379820e65baa" data-url="/istanbul/kartal-ugur-mumcu">Kartal (Uğur Mumcu)</option>
<option value="6833dffe-f661-459d-badc-78d244b8a7c4" data-url="/istanbul/kartal-yakacik-mah">Kartal (Yakacık Mah.)</option>
<option value="818ac0d5-68b8-432e-a370-08727c4faf45" data-url="/istanbul/kartal-yali-mah">Kartal (Yalı Mah.)</option>
<option value="390a7b3a-e2e2-43d3-a9c4-fce2a64a1c08" data-url="/istanbul/kartal-yukari-mah">Kartal (Yukarı Mah.)</option>
<option value="61480a83-5b1f-4c50-81b3-8bbee8f96ed5" data-url="/istanbul/kartal-yunus-mah">Kartal (Yunus Mah.)</option>
<option value="01850b75-8af6-47ba-bed2-486b5d07c802" data-url="/istanbul/kavacik">Kavacık</option>
<option value="ac63524a-18a0-48d0-8b90-98346517cc5b" data-url="/istanbul/kayisdagi">Kayışdağı</option>
<option value="9338bc1e-03f3-40e6-92f1-ab7e04c7b1e0" data-url="/istanbul/kayisdagi-inonu-mah">Kayışdağı (İnönü Mah.)</option>
<option value="52d1501b-90ba-4833-9aaf-cecc58038a39" data-url="/istanbul/kemerburgaz">Kemerburgaz</option>
<option value="f2b0fb12-3205-4fb2-8442-67eb661d4030" data-url="/istanbul/kinaliada">Kınalıada</option>
<option value="35ec0ab1-134f-4f10-a721-241a6d23bdf4" data-url="/istanbul/kisikli">Kısıklı</option>
<option value="403e8b2f-4dd4-4e18-98cf-92c43a5b1b94" data-url="/istanbul/kirecburnu">Kireçburnu</option>
<option value="8bcc6a51-3ecb-4b5e-9aad-52513b38ef3c" data-url="/istanbul/kocasinan">Kocasinan</option>
<option value="b3219838-1981-4b8b-a862-9aebae185cab" data-url="/istanbul/kurtkoy-harmandere-mah">Kurtköy (Harmandere Mah.)</option>
<option value="c1ea4c30-0a4c-46d8-927b-9ad3ca28e012" data-url="/istanbul/kurtkoy-merkez">Kurtköy (Merkez)</option>
<option value="1f33687b-eb81-4f02-9f18-f0c54f77e375" data-url="/istanbul/kurtkoy-seyhli-mah">Kurtköy (Şeyhli Mah.)</option>
<option value="78ef94f6-7f87-4d54-9959-45e99d55d9e2" data-url="/istanbul/kurtkoy-yenisehir-mah">Kurtköy (Yenişehir Mah.)</option>
<option value="0fa84fc5-8583-4da7-b30c-d2945e14278a" data-url="/istanbul/kurucesme">Kuruçeşme</option>
<option value="5efe5e9d-e529-466b-83cd-b3b5d00da231" data-url="/istanbul/kuzguncuk">Kuzguncuk</option>
<option value="db786062-b090-4b11-ad66-ec8f146bc01c" data-url="/istanbul/kucukbakkalkoy">Küçükbakkalköy</option>
<option value="7f42423d-c564-4fab-b21e-c92e8e91f983" data-url="/istanbul/kucukcekmece-atakent-mah-1-ikitelli-cad-bolgesi">Küçükçekmece (Atakent Mah. - 1. İkitelli Cad. Bölgesi)</option>
<option value="69ae4d5c-16a3-40ea-8c21-dda91242fc14" data-url="/istanbul/kucukcekmece-atakent-mah-atakent-3-etap-bolgesi">Küçükçekmece (Atakent Mah. - Atakent 3. Etap Bölgesi)</option>
<option value="e7a930bc-f7e5-4cb7-a791-d859df94bc8b" data-url="/istanbul/kucukcekmece-atakent-mah-avrupa-konutlari-bolgesi">Küçükçekmece (Atakent Mah. - Avrupa Konutları Bölgesi)</option>
<option value="b588ed74-b6b8-4d8b-a435-ca083393ac1f" data-url="/istanbul/kucukcekmece-atakent-mah-halkali-2-etap-bolgesi">Küçükçekmece (Atakent Mah. - Halkalı 2. Etap Bölgesi)</option>
<option value="7d964946-7819-49e6-941f-01204d007637" data-url="/istanbul/kucukcekmece-atakent-mah-istanbul-lounge-2-bolgesi">Küçükçekmece (Atakent Mah. - İstanbul Lounge 2 Bölgesi)</option>
<option value="86f8ac6d-eab6-445a-b13d-30b6f4affd0b" data-url="/istanbul/kucukcekmece-atakent-mah-istanbul-lounge-bolgesi">Küçükçekmece (Atakent Mah. - İstanbul Lounge Bölgesi)</option>
<option value="0812162e-8cb8-48fd-8bcf-b0d3b1a62224" data-url="/istanbul/kucukcekmece-atakent-mah-istanbul-saraylar-bolgesi">Küçükçekmece (Atakent Mah. - İstanbul Saraylar Bölgesi)</option>
<option value="023638e8-a902-49dc-8735-6369b5450659" data-url="/istanbul/kucukcekmece-atakent-mah-sinpas-bosphorus-bolgesi">Küçükçekmece (Atakent Mah. - Sinpaş Bosphorus Bölgesi)</option>
<option value="1ba42786-7ea7-4511-b8f9-7dd263ec36db" data-url="/istanbul/kucukcekmece-atakent-mah-soyak-olympiakent-bolgesi">Küçükçekmece (Atakent Mah. - Soyak Olympiakent Bölgesi)</option>
<option value="d86a5f5c-630a-4d61-a200-b1be083cfac0" data-url="/istanbul/kucukcekmece-atakent-mah-tema-park-bolgesi">Küçükçekmece (Atakent Mah. - Tema Park Bölgesi)</option>
<option value="b8b3a69d-68a6-422a-b019-6448f59457d5" data-url="/istanbul/kucukcekmece-atakent-mah-toki-fulya-evleri-bolgesi">Küçükçekmece (Atakent Mah. - Toki Fulya Evleri Bölgesi)</option>
<option value="56b25bc5-39f5-4999-a747-4c12e05a714f" data-url="/istanbul/kucukcekmece-atakent-mah-kanuni-s-suleyman-hastanesi-bolgesi">Küçükçekmece (Atakent Mah.-Kanuni S. Süleyman Hastanesi Bölgesi)</option>
<option value="23426d85-bb83-442a-860d-ab3a1779a13f" data-url="/istanbul/kucukcekmece-ataturk-mah-ikitelli-osb">Küçükçekmece (Atatürk Mah. - İkitelli OSB)</option>
<option value="ac428bb7-612c-45a1-9941-f41153989969" data-url="/istanbul/kucukcekmece-ataturk-mah">Küçükçekmece (Atatürk Mah.)</option>
<option value="1158e725-fe90-4377-8f25-a24d5f39e776" data-url="/istanbul/kucukcekmece-besyol-mah">Küçükçekmece (Beşyol Mah.)</option>
<option value="6eedc0e1-49b5-4532-bb11-21da907c1dbb" data-url="/istanbul/kucukcekmece-cennet-mah">Küçükçekmece (Cennet Mah.)</option>
<option value="fd256fb3-5092-4cd8-97a4-d2a601789f2e" data-url="/istanbul/kucukcekmece-cumhuriyet-mah">Küçükçekmece (Cumhuriyet Mah.)</option>
<option value="c1ae78cb-dacd-4887-9414-0cbba483a17e" data-url="/istanbul/kucukcekmece-fatih-mah">Küçükçekmece (Fatih Mah.)</option>
<option value="8d1ae31e-0d0b-408e-bbbd-b67be9373f35" data-url="/istanbul/kucukcekmece-fevzi-cakmak-mah">Küçükçekmece (Fevzi Çakmak Mah.)</option>
<option value="2d5e74ea-e9b9-411b-9541-b896ce2c8369" data-url="/istanbul/kucukcekmece-gultepe-mah">Küçükçekmece (Gültepe Mah.)</option>
<option value="0afb7be8-d15d-4589-94dd-3f54fbc8b08a" data-url="/istanbul/kucukcekmece-halkali-mah-avrupa-atakent-konutlari-bolgesi">Küçükçekmece (Halkalı Mah. - Avrupa Atakent Konutları Bölgesi)</option>
<option value="5eec4ac0-0e80-4a71-b415-e88db2b25733" data-url="/istanbul/kucukcekmece-halkali-merkez-mah-avrupa-konutlari-3-bolgesi">Küçükçekmece (Halkalı Merkez Mah. - Avrupa Konutları 3 Bölgesi)</option>
<option value="b1f5d554-9585-40be-b5da-ef42ec2cdf41" data-url="/istanbul/kucukcekmece-halkali-merkez-mah-basin-ekspres-yolu">Küçükçekmece (Halkalı Merkez Mah. - Basın Ekspres Yolu)</option>
<option value="4c91a846-6841-43fd-b2a7-8df40143bfe1" data-url="/istanbul/kucukcekmece-halkali-merkez-mah">Küçükçekmece (Halkalı Merkez Mah.)</option>
<option value="5da201ea-4855-4066-b394-72fec4c9bad0" data-url="/istanbul/kucukcekmece-inonu-mah">Küçükçekmece (İnönü Mah.)</option>
<option value="2a89dee8-9cb2-4575-b9de-4b4e097bfee1" data-url="/istanbul/kucukcekmece-istasyon-mah">Küçükçekmece (İstasyon Mah.)</option>
<option value="f74eb0ac-c483-4f25-bc8b-764b850d6dad" data-url="/istanbul/kucukcekmece-kanarya-mah">Küçükçekmece (Kanarya Mah.)</option>
<option value="8a1964cc-880f-4167-a5b6-064abf8c6fcb" data-url="/istanbul/kucukcekmece-kartaltepe-mah">Küçükçekmece (Kartaltepe Mah.) </option>
<option value="f392bdb3-1bb8-46b9-a5b0-2b80f5d9a860" data-url="/istanbul/kucukcekmece-kemalpasa-mah">Küçükçekmece (Kemalpaşa Mah.)</option>
<option value="797dbfed-76f8-40be-9182-0c18f1dc69b2" data-url="/istanbul/kucukcekmece-mehmet-akif-mah-bahariye-cad">Küçükçekmece (Mehmet Akif Mah. - Bahariye Cad.)</option>
<option value="00ffd16f-a5f5-40fb-81ec-a0879d7e1d36" data-url="/istanbul/kucukcekmece-mehmet-akif-mah">Küçükçekmece (Mehmet Akif Mah.)</option>
<option value="733271c3-4ff2-4070-9003-f2ec92e3a8e1" data-url="/istanbul/kucukcekmece-sogutlucesme-mah">Küçükçekmece (Söğütlüçeşme Mah.)</option>
<option value="37563979-cc7a-46e3-94d7-0f581041782e" data-url="/istanbul/kucukcekmece-sultanmurat-mah">Küçükçekmece (Sultanmurat Mah.)</option>
<option value="9005bef1-5514-4814-9ea1-fca6d0152655" data-url="/istanbul/kucukcekmece-tevfikbey-mah-sefakoy">Küçükçekmece (Tevfikbey Mah. - Sefaköy)</option>
<option value="629f53ed-51ce-4c36-b850-326988c46ace" data-url="/istanbul/kucukcekmece-tevfikbey-mah">Küçükçekmece (Tevfikbey Mah.)</option>
<option value="ef287d21-b418-4e19-94b2-73a134793ca8" data-url="/istanbul/kucukcekmece-yarimburgaz-mah">Küçükçekmece (Yarımburgaz Mah.)</option>
<option value="b4a20dbd-72c9-48c3-9e55-73aafdb38d2f" data-url="/istanbul/kucukcekmece-yenimahalle-mah">Küçükçekmece (Yenimahalle Mah.)</option>
<option value="1e5ed96d-f011-4cf4-b7b5-5ca3b6b0f0cb" data-url="/istanbul/kucukcekmece-yesilova-mah">Küçükçekmece (Yeşilova Mah.)</option>
<option value="ce316480-6f2f-4fa8-887f-184bb434fb41" data-url="/istanbul/levent">Levent</option>
<option value="c5459762-25d6-44c0-865c-e1c16e6dbd66" data-url="/istanbul/levent-levazim">Levent (Levazım)</option>
<option value="2e82e90e-f8f7-4a41-a8cf-7d7741629688" data-url="/istanbul/levent-yeni">Levent (Yeni)</option>
<option value="cbc270ad-81f7-42cb-9d10-fe349ef05356" data-url="/istanbul/levent-4">Levent 4.</option>
<option value="a43e816d-f5ae-4c19-a7a6-82a0e021c51e" data-url="/istanbul/maltepe-altaycesme-mah">Maltepe (Altayçeşme Mah.)</option>
<option value="ca983c8c-36e3-4763-8609-34ba194a8fdb" data-url="/istanbul/maltepe-altintepe-mah">Maltepe (Altıntepe Mah.)</option>
<option value="91b50fde-ac75-40a0-bfc7-a5fbc4267962" data-url="/istanbul/maltepe-aydinevler-mah">Maltepe (Aydınevler Mah.)</option>
<option value="f108b338-75f0-4821-91ec-42eed28643ce" data-url="/istanbul/maltepe-baglarbasi-mah">Maltepe (Bağlarbaşı Mah.)</option>
<option value="5729a9ea-8d68-4d5f-ade0-f69cb674f874" data-url="/istanbul/maltepe-basibuyuk-mah">Maltepe (Başıbüyük Mah.)</option>
<option value="a2b16d0b-61b0-4285-ac81-019dcdb94479" data-url="/istanbul/maltepe-cevizli-mah">Maltepe (Cevizli Mah.)</option>
<option value="7cc110f7-dfb9-43f7-9882-8240d3a36cad" data-url="/istanbul/maltepe-esenkent-mah">Maltepe (Esenkent Mah.)</option>
<option value="621755ce-cfc5-49d7-9b28-654908dd4f54" data-url="/istanbul/maltepe-feyzullah-mah">Maltepe (Feyzullah Mah.)</option>
<option value="fa138a1a-dd1b-41b4-9671-b8d3260b4cd5" data-url="/istanbul/maltepe-findikli-mah">Maltepe (Fındıklı Mah.)</option>
<option value="7e84f250-b420-4fde-b937-0c14263fd608" data-url="/istanbul/maltepe-girne-mah">Maltepe (Girne Mah.)</option>
<option value="b9b1b2b8-18f9-45d0-aa4a-e15ca6cf05ae" data-url="/istanbul/maltepe-gulsuyu-mah">Maltepe (Gülsuyu Mah.)</option>
<option value="0a02c559-ce8f-4449-a0d3-cc01f54e831a" data-url="/istanbul/maltepe-idealtepe-mah">Maltepe (İdealtepe Mah.)</option>
<option value="aee7c745-58e3-43a1-9e3c-c79548412786" data-url="/istanbul/maltepe-kucukyali-mah">Maltepe (Küçükyalı Mah.)</option>
<option value="05e7e932-4b60-4246-84ca-070f8c95654d" data-url="/istanbul/maltepe-merkez">Maltepe (Merkez)</option>
<option value="96d4546f-4877-45c8-9ebb-26657d3ca177" data-url="/istanbul/maltepe-yali-mah">Maltepe (Yalı Mah.)</option>
<option value="fc944122-2c28-4e41-a938-3659393af25c" data-url="/istanbul/maltepe-zumrutevler-mah">Maltepe (Zümrütevler Mah.)</option>
<option value="7d8ca232-65ae-4942-998c-469d6078dbc2" data-url="/istanbul/maslak">Maslak</option>
<option value="a2c2ffb0-31ff-4835-b883-de84f3b1bc1f" data-url="/istanbul/maslak-darussafaka">Maslak (Darüşşafaka)</option>
<option value="33433caf-9d48-44a2-97d3-ae8e3d512a55" data-url="/istanbul/maslak-itu-kampusu">Maslak (İTÜ Kampüsü)</option>
<option value="36db6efa-7904-4eee-baf1-c2446de33712" data-url="/istanbul/merter">Merter</option>
<option value="65b361e2-5bc4-4442-8918-4eed92b45076" data-url="/istanbul/mutlukoy">Mutluköy</option>
<option value="ca14f03b-6bf9-4ff5-b4a8-141a523871af" data-url="/istanbul/nakkastepe">Nakkaştepe</option>
<option value="37dccc8d-5f5f-4010-9df6-b9d1cd023367" data-url="/istanbul/ortakoy">Ortaköy</option>
<option value="a2bbe4fd-5470-4dc7-a144-8976c020a758" data-url="/istanbul/pendik-alt-kaynarca">Pendik (Alt Kaynarca)</option>
<option value="7f6540c3-d393-4c41-883c-b9fbbe7de0fe" data-url="/istanbul/pendik-bahcelievler-mah">Pendik (Bahçelievler Mah.)</option>
<option value="2154b135-95ce-47b9-be73-85be29510bf5" data-url="/istanbul/pendik-bati-mah">Pendik (Batı Mah.)</option>
<option value="2bf8287a-4e33-4814-9301-0169f58c1edc" data-url="/istanbul/pendik-camcesme-mah">Pendik (Çamçeşme Mah.)</option>
<option value="c33d0ba8-0a7b-45a7-9977-718db5f98b6a" data-url="/istanbul/pendik-dogu-mah">Pendik (Doğu Mah.)</option>
<option value="70a0db57-2635-405c-a388-04e4c26d541c" data-url="/istanbul/pendik-dolayoba">Pendik (Dolayoba)</option>
<option value="d35525ff-82c8-40c6-ac7b-20b99343044f" data-url="/istanbul/pendik-dumlupinar-mah">Pendik (Dumlupınar Mah.)</option>
<option value="d2b9fb30-69a8-48d0-b136-c885cd3044ce" data-url="/istanbul/pendik-esenler-mah">Pendik (Esenler Mah.)</option>
<option value="cbbdbe1c-1a5a-4e55-8d44-cee603e809ea" data-url="/istanbul/pendik-esenyali-mah">Pendik (Esenyalı Mah.)</option>
<option value="ae914444-8b55-4b34-9adc-e563725cf425" data-url="/istanbul/pendik-guzelyali-mah">Pendik (Güzelyalı Mah.)</option>
<option value="ddcff616-dd3f-4adf-bf2b-69a35380ba52" data-url="/istanbul/pendik-kavakpinar-mah">Pendik (Kavakpınar Mah.)</option>
<option value="a703b710-969f-4647-9568-80b373e498a8" data-url="/istanbul/pendik-merkez">Pendik (Merkez)</option>
<option value="1bd6c5cc-4895-4fcf-8e89-c836e455c04b" data-url="/istanbul/pendik-sapan-baglari-mah">Pendik (Sapan Bağları Mah.)</option>
<option value="e5eab6ba-a2fe-4e4c-a42f-29f1fcddd3f9" data-url="/istanbul/pendik-velibaba-mah">Pendik (Velibaba Mah.)</option>
<option value="a1806e71-5dce-4d92-b3eb-82138bde662c" data-url="/istanbul/pendik-yayalar-mah">Pendik (Yayalar Mah.)</option>
<option value="2d1f7b93-2002-40a1-9e82-72a50ab10ba7" data-url="/istanbul/pendik-yeni-mah">Pendik (Yeni Mah.)</option>
<option value="d2b32531-a8fe-4f1b-9a67-f67aeaaf668f" data-url="/istanbul/pendik-yesilbaglar-mah">Pendik (Yeşilbağlar Mah.)</option>
<option value="6797b5eb-b893-45fb-a7c4-677825d88f94" data-url="/istanbul/resitpasa">Reşitpaşa</option>
<option value="8be0b051-a432-4afb-844b-40a9f35febeb" data-url="/istanbul/rumelihisari">Rumelihisarı</option>
<option value="216f9f8e-944d-4d02-a626-7b6a390ed5ab" data-url="/istanbul/sancaktepe-abdurrahmangazi-mah">Sancaktepe (Abdurrahmangazi Mah.)</option>
<option value="2a1fc82d-a2ec-4abc-82bf-6ce8ecdfd1cb" data-url="/istanbul/sancaktepe-akpinar-mah">Sancaktepe (Akpınar Mah.)</option>
<option value="ea3c511d-905f-4326-8909-d30e10201ca6" data-url="/istanbul/sancaktepe-ataturk-mah">Sancaktepe (Atatürk Mah.)</option>
<option value="62dd96e5-63b0-4779-9ecc-17f7adbf95bb" data-url="/istanbul/sancaktepe-emek-mah">Sancaktepe (Emek Mah.)</option>
<option value="82adc45d-795f-4557-9681-189f72467b97" data-url="/istanbul/sancaktepe-eyup-sultan-mah">Sancaktepe (Eyüp Sultan Mah.)</option>
<option value="98cb374e-fa32-4032-8f08-25874910b5cd" data-url="/istanbul/sancaktepe-fatih-mah-ortadag">Sancaktepe (Fatih Mah. - Ortadağ)</option>
<option value="54b28fea-c251-498b-a842-a54e5d511548" data-url="/istanbul/sancaktepe-hilal-mah">Sancaktepe (Hilal Mah.)</option>
<option value="3532b879-587e-4713-94de-63d45e4fc73e" data-url="/istanbul/sancaktepe-inonu-mah">Sancaktepe (İnönü Mah.)</option>
<option value="d1fb627b-e199-4194-968f-466a08903b85" data-url="/istanbul/sancaktepe-kemal-turkler-mah">Sancaktepe (Kemal Türkler Mah.)</option>
<option value="d049df04-94e8-49f3-9735-bb604cbbabe3" data-url="/istanbul/sancaktepe-meclis-mah">Sancaktepe (Meclis Mah.)</option>
<option value="443ae7c1-4c04-4d53-94e3-ca667b6a0f2d" data-url="/istanbul/sancaktepe-merve-mah">Sancaktepe (Merve Mah.)</option>
<option value="e3c28294-934b-4ef6-8fe0-a9aed4a40775" data-url="/istanbul/sancaktepe-mevlana-mah">Sancaktepe (Mevlana Mah.)</option>
<option value="72217fe7-2640-4472-bfb9-eec2d0c52fd8" data-url="/istanbul/sancaktepe-osmangazi-mah">Sancaktepe (Osmangazi Mah.)</option>
<option value="f79a8a10-5af3-4911-ad00-3f4ab714d6a1" data-url="/istanbul/sancaktepe-pasakoy-mah">Sancaktepe (Paşaköy Mah.)</option>
<option value="3074e40d-2ae1-4966-9d75-e42656d2762f" data-url="/istanbul/sancaktepe-safa-mah">Sancaktepe (Safa Mah.)</option>
<option value="0c7ab2fd-3e50-4f4a-8fe7-b46124e2322f" data-url="/istanbul/sancaktepe-sarigazi-mah-samandira">Sancaktepe (Sarıgazi Mah. - Samandıra)</option>
<option value="6012b2cf-e4ea-4c61-9eb9-9cf855aebde2" data-url="/istanbul/sancaktepe-veysel-karani-mah">Sancaktepe (Veysel Karani Mah.)</option>
<option value="46e168f1-7e0b-47d7-afe3-cae08ab65e0b" data-url="/istanbul/sancaktepe-yenidogan-mah">Sancaktepe (Yenidoğan Mah.)</option>
<option value="6c839d8e-588f-48b6-a096-a8b67777ef9e" data-url="/istanbul/sancaktepe-yunusemre-mah">Sancaktepe (Yunusemre Mah.)</option>
<option value="56a3c455-997c-485a-83dc-3edc7ed61189" data-url="/istanbul/sariyer-acarlar">Sarıyer (Acarlar)</option>
<option value="f7865775-e847-4c8a-b585-963de686b3ef" data-url="/istanbul/sariyer-arikoy-semti">Sarıyer (Arıköy Semti)</option>
<option value="ca39893a-cbf5-469e-99dc-d7f7f423f3be" data-url="/istanbul/sariyer-bahcekoy-mah">Sarıyer (Bahçeköy Mah.)</option>
<option value="e17846c9-fba1-407d-9714-e63b0747fb95" data-url="/istanbul/sariyer-buyukdere">Sarıyer (Büyükdere)</option>
<option value="c3068ceb-f745-40d7-9f0f-9748389f695e" data-url="/istanbul/sariyer-demircikoy">Sarıyer (Demirciköy)</option>
<option value="ceae6513-cfbb-440e-afbb-f17152961fea" data-url="/istanbul/sariyer-kilyos">Sarıyer (Kilyos)</option>
<option value="43f5d4ca-190e-4d4e-9aa8-cff9de0f906d" data-url="/istanbul/sariyer-koc-univ">Sarıyer (Koç Üniv.)</option>
<option value="9af7a67a-4f61-45a5-9573-5cd238bf3f0c" data-url="/istanbul/sariyer-maden-mah">Sarıyer (Maden Mah.)</option>
<option value="5b1cf23e-9a96-4555-a8dc-6f453734d240" data-url="/istanbul/sariyer-merkez">Sarıyer (Merkez)</option>
<option value="9605810e-c78e-4c92-891e-f8d2a4ec66b2" data-url="/istanbul/sariyer-rumelifeneri-mah">Sarıyer (Rumelifeneri Mah.)</option>
<option value="2bc0ac19-2f92-4aad-b880-100590259dc2" data-url="/istanbul/sariyer-rumelikavagi-mah">Sarıyer (Rumelikavağı Mah.)</option>
<option value="073d45d7-ec71-477e-91d8-f4143b6e761c" data-url="/istanbul/sariyer-zekeriyakoy">Sarıyer (Zekeriyaköy)</option>
<option value="980c5931-2105-4de6-a580-9abe094bf1b1" data-url="/istanbul/silivri-alipasa-mah">Silivri (Alipaşa Mah.)</option>
<option value="437bd647-a978-4e69-b07d-e3c4f6be8285" data-url="/istanbul/silivri-cumhuriyet-mah">Silivri (Cumhuriyet Mah.)</option>
<option value="72f6cb41-ad4a-4204-b062-6a434a6e2f6a" data-url="/istanbul/silivri-gumusyaka-canta">Silivri (Gümüşyaka - Çanta)</option>
<option value="beb9f59d-2e0a-48f9-b849-aa61c44dbf49" data-url="/istanbul/silivri-gumusyaka-merkez">Silivri (Gümüşyaka Merkez)</option>
<option value="94f57c2c-82ea-4223-a1b7-cec5a69a6388" data-url="/istanbul/silivri-merkez">Silivri (Merkez)</option>
<option value="811aa53c-8607-4aac-875c-bf390a5e9607" data-url="/istanbul/silivri-mimar-sinan-mah">Silivri (Mimar Sinan Mah.)</option>
<option value="202d48a0-3f46-4002-a74b-041354d39440" data-url="/istanbul/silivri-selimpasa-mah">Silivri (Selimpaşa Mah.)</option>
<option value="cdbc390a-3b33-460f-9a0d-eeb9ffb43be9" data-url="/istanbul/silivri-semizkumlar-mah">Silivri (Semizkumlar Mah.)</option>
<option value="2fd20e91-fa96-45ec-8b3c-b4cd7dd0413c" data-url="/istanbul/silivri-yeni-mah">Silivri (Yeni Mah.)</option>
<option value="010035f4-7cc5-4dd1-bcef-6a132d4b2e26" data-url="/istanbul/sultanbeyli-abdurrahman-gazi-mah">Sultanbeyli (Abdurrahman Gazi Mah.)</option>
<option value="f603d6b1-db48-43ac-b43f-0328b597e965" data-url="/istanbul/sultanbeyli-adil-mah">Sultanbeyli (Adil Mah.)</option>
<option value="d8ce7576-6a5b-4a5b-b620-3afd07a79a75" data-url="/istanbul/sultanbeyli-ahmet-yesevi-mah">Sultanbeyli (Ahmet Yesevi Mah.)</option>
<option value="839e5780-f520-41f2-9e73-94a66822ca9a" data-url="/istanbul/sultanbeyli-aksemsettin-mah">Sultanbeyli (Akşemsettin Mah.)</option>
<option value="f348aa02-b09d-44f0-9a48-be40044ff57b" data-url="/istanbul/sultanbeyli-battalgazi-mah">Sultanbeyli (Battalgazi Mah.)</option>
<option value="6d114208-fe32-4f2f-89f2-60ef2f2f36be" data-url="/istanbul/sultanbeyli-fatih-mah">Sultanbeyli (Fatih Mah.)</option>
<option value="06bb3393-1d24-4cb2-872f-4b51f7fe6830" data-url="/istanbul/sultanbeyli-hamidiye-mah">Sultanbeyli (Hamidiye Mah.)</option>
<option value="40e4a715-f33a-427f-a118-b7cf9e7e406e" data-url="/istanbul/sultanbeyli-hasanpasa-mah">Sultanbeyli (Hasanpaşa Mah.)</option>
<option value="e0dc6011-24ac-491c-aca4-e93bb39452bb" data-url="/istanbul/sultanbeyli-mecidiye-mah">Sultanbeyli (Mecidiye Mah.)</option>
<option value="6b87d540-34ea-4da5-86c1-c58cdd0b12b2" data-url="/istanbul/sultanbeyli-mehmet-akif-mah">Sultanbeyli (Mehmet Akif Mah.)</option>
<option value="690572f7-38fd-4286-bb18-405ca8e9327a" data-url="/istanbul/sultanbeyli-mimar-sinan-mah">Sultanbeyli (Mimar Sinan Mah.)</option>
<option value="ee996578-5f77-421a-a95d-f452a0b470a6" data-url="/istanbul/sultanbeyli-necip-fazil-mah">Sultanbeyli (Necip Fazıl Mah.)</option>
<option value="34fbea52-aff9-4ba8-acec-38a9326dc863" data-url="/istanbul/sultanbeyli-orhangazi-mah">Sultanbeyli (Orhangazi Mah.)</option>
<option value="6c39c385-8eb6-45b7-89e9-0cfa3da80a0e" data-url="/istanbul/sultanbeyli-turgut-reis-mah">Sultanbeyli (Turgut Reis Mah.)</option>
<option value="5c4dee00-e0cc-4caf-8c85-8d03c6b94224" data-url="/istanbul/sultanbeyli-yavuz-selim-mah">Sultanbeyli (Yavuz Selim Mah.)</option>
<option value="2aa32eaf-9efe-45eb-ab82-f2d31db3da54" data-url="/istanbul/sultangazi-50-yil-mah">Sultangazi (50.Yıl Mah.)</option>
<option value="125fb626-5656-4531-a286-0f6904f141ee" data-url="/istanbul/sultangazi-75-yil-mah">Sultangazi (75.Yıl Mah.)</option>
<option value="1247bc74-97ce-4c59-b2d1-ce9c56ec7aea" data-url="/istanbul/sultangazi-cebeci-mah">Sultangazi (Cebeci Mah.)</option>
<option value="8a48e32b-f030-4377-8be9-a56a46b4a928" data-url="/istanbul/sultangazi-cumhuriyet-mah">Sultangazi (Cumhuriyet Mah.)</option>
<option value="63799261-7213-49bf-981b-ba421553502f" data-url="/istanbul/sultangazi-esentepe-mah">Sultangazi (Esentepe Mah.)</option>
<option value="3adf314f-7ad7-4e89-be86-e8f2b54895dd" data-url="/istanbul/sultangazi-eski-habibler-mah">Sultangazi (Eski Habibler Mah.)</option>
<option value="cb0c4a8f-7f54-4aeb-88cb-258421f122a7" data-url="/istanbul/sultangazi-gazi-mah">Sultangazi (Gazi Mah.)</option>
<option value="1b1e5509-ad8b-4def-8b38-63ac33e12e0f" data-url="/istanbul/sultangazi-habibler-mah">Sultangazi (Habibler Mah.)</option>
<option value="aede7493-ab2c-4dc4-8244-09064c8141de" data-url="/istanbul/sultangazi-ismet-pasa-mah-ordu-cad">Sultangazi (İsmet Paşa Mah. - Ordu Cad.)</option>
<option value="1a4ef38b-a25b-4a87-b916-eb8a60ed75c6" data-url="/istanbul/sultangazi-ismet-pasa-mah">Sultangazi (İsmet Paşa Mah.)</option>
<option value="e4d03526-d253-4593-89db-c82b3914867b" data-url="/istanbul/sultangazi-malkocoglu-mah">Sultangazi (Malkoçoğlu Mah.)</option>
<option value="64f323a5-6cca-4ec7-af51-abf6fc3c5e2c" data-url="/istanbul/sultangazi-sultanciftligi-mah-ordu-cad">Sultangazi (Sultançiftliği Mah. - Ordu Cad.)</option>
<option value="b09640fb-fce3-4d15-bea1-099b4105abba" data-url="/istanbul/sultangazi-sultanciftligi-mah">Sultangazi (Sultançiftliği Mah.)</option>
<option value="fd7b9641-c30c-4efd-ad9d-89ffae124f6d" data-url="/istanbul/sultangazi-ugur-mumcu-mah">Sultangazi (Uğur Mumcu Mah.)</option>
<option value="89305874-63f5-489a-85c5-7f1cd5423a27" data-url="/istanbul/sultangazi-yayla-mah">Sultangazi (Yayla Mah.)</option>
<option value="76267c6a-de1b-4a6e-9509-0a58671b5f02" data-url="/istanbul/sultangazi-yunus-emre-mah">Sultangazi (Yunus Emre Mah.)</option>
<option value="3f94f04d-65ff-4b78-ad48-e74463bfddb5" data-url="/istanbul/sultangazi-zubeyde-hanim-mah">Sultangazi (Zübeyde Hanım Mah.)</option>
<option value="19bdba21-970d-4dfa-901c-92af3d0b8ef2" data-url="/istanbul/sile">Şile</option>
<option value="3802c6c7-aeeb-4abf-b637-b13de90fd103" data-url="/istanbul/sile-agva">Şile (Ağva)</option>
<option value="e73a0852-d8a5-4d06-b0a1-1f5d65de3d73" data-url="/istanbul/sile-kumbaba">Şile (Kumbaba)</option>
<option value="3d136b9e-4082-4e89-aea1-5ba478a0002c" data-url="/istanbul/sirinevler">Şirinevler</option>
<option value="615a5e35-7096-4762-b000-e1fc44653deb" data-url="/istanbul/sisli-19-mayis-mah">Şişli (19 Mayıs Mah.)</option>
<option value="fe23f974-2ab6-4557-9d4e-b25af3c1aec8" data-url="/istanbul/sisli-bozkurt-mah-kurtulus">Şişli (Bozkurt Mah. - Kurtuluş)</option>
<option value="418b7c5f-dad2-4ce8-9c5f-238d72580780" data-url="/istanbul/sisli-cumhuriyet-mah-bomonti">Şişli (Cumhuriyet Mah. - Bomonti)</option>
<option value="98994d2a-a29f-4447-b834-0a51533e2434" data-url="/istanbul/sisli-duatepe-mah">Şişli (Duatepe Mah.)</option>
<option value="3cf966b7-1700-48b6-af60-e0d4785890c3" data-url="/istanbul/sisli-ergenekon-mah-dolapdere">Şişli (Ergenekon Mah. - Dolapdere)</option>
<option value="4568b4a3-ed5a-4f8e-bce9-44188aec4d48" data-url="/istanbul/sisli-ergenekon-mah-pangalti">Şişli (Ergenekon Mah. - Pangaltı)</option>
<option value="d921aa83-6fbf-442c-aeec-469994794c9c" data-url="/istanbul/sisli-esentepe-mah-plazalar">Şişli (Esentepe Mah. - Plazalar)</option>
<option value="9dade4d8-270f-4b7d-9c40-b7356c703118" data-url="/istanbul/sisli-esentepe-mah">Şişli (Esentepe Mah.)</option>
<option value="67ce3f1e-1bc7-4be3-b25e-d4c04ace963a" data-url="/istanbul/sisli-eskisehir-mah">Şişli (Eskişehir Mah.)</option>
<option value="87985184-2e37-4eaf-90c0-5f0478b587ae" data-url="/istanbul/sisli-ferikoy-mah">Şişli (Feriköy Mah.)</option>
<option value="640a2ce1-53b2-4fb2-b412-82e4980949aa" data-url="/istanbul/sisli-fulya-mah-ortaklar">Şişli (Fulya Mah. - Ortaklar)</option>
<option value="1eb99410-0d20-4581-993f-4b11136f0c5e" data-url="/istanbul/sisli-fulya-mah">Şişli (Fulya Mah.)</option>
<option value="beacd542-ecd8-41e0-b6ca-23abcb36565f" data-url="/istanbul/sisli-gulbahar-mah-gulbag">Şişli (Gülbahar Mah. - Gülbağ)</option>
<option value="214ecff1-fb1e-4a0f-86ae-9d59024a8405" data-url="/istanbul/sisli-halaskargazi-mah-osmanbey">Şişli (Halaskargazi Mah. - Osmanbey)</option>
<option value="3a62e435-dfcd-485f-a08a-da3512bf6554" data-url="/istanbul/sisli-halide-edip-adivar-mah">Şişli (Halide Edip Adıvar Mah.)</option>
<option value="f916ae36-3d14-46ff-b41f-49e8e5e3e940" data-url="/istanbul/sisli-halil-rifat-pasa-mah-perpa">Şişli (Halil Rıfat Paşa Mah. - Perpa)</option>
<option value="130d0710-d0e6-470d-bb57-93849ab321d6" data-url="/istanbul/sisli-harbiye-mah-macka">Şişli (Harbiye Mah. - Maçka)</option>
<option value="a321dde8-bd58-4952-8547-5662cb2cffe5" data-url="/istanbul/sisli-harbiye-mah">Şişli (Harbiye Mah.)</option>
<option value="265ff97e-1625-4e7c-baa1-777b30aac8d6" data-url="/istanbul/sisli-inonu-mah-elmadag">Şişli (İnönü Mah. - Elmadağ)</option>
<option value="c86ad2bb-6876-426c-a849-56831e7dbd98" data-url="/istanbul/sisli-izzet-pasa-mah">Şişli (İzzet Paşa Mah.)</option>
<option value="4a0c07e9-75f5-4458-9fba-c61dce5de63b" data-url="/istanbul/sisli-kaptanpasa-mah-okmeydani">Şişli (Kaptanpaşa Mah. - Okmeydanı)</option>
<option value="e9d002bc-4584-4623-ac47-dd6068152e66" data-url="/istanbul/sisli-kustepe-mah">Şişli (Kuştepe Mah.)</option>
<option value="72e0cb77-b0ca-498d-8cb4-28cbffd78c98" data-url="/istanbul/sisli-mahmut-sevket-pasa-mah">Şişli (Mahmut Şevket Paşa Mah.)</option>
<option value="d872b994-1a84-484a-b2a8-6c7b73b1c424" data-url="/istanbul/sisli-mecidiyekoy-mah-dereboyu">Şişli (Mecidiyeköy Mah. - Dereboyu)</option>
<option value="baa6ea5d-6a89-4afd-ad8d-f7d84815a936" data-url="/istanbul/sisli-mecidiyekoy-mah">Şişli (Mecidiyeköy Mah.)</option>
<option value="02fecf06-19f4-4c20-a9e3-3358901eb3b7" data-url="/istanbul/sisli-merkez-mah">Şişli (Merkez Mah.)</option>
<option value="09dfea80-e99a-4f67-8983-e751d990c13c" data-url="/istanbul/sisli-mesrutiyet-mah-nisantasi">Şişli (Meşrutiyet Mah. - Nişantaşı)</option>
<option value="bc72af8f-7681-4057-b173-fdc3debfb3fd" data-url="/istanbul/sisli-pasa-mah">Şişli (Paşa Mah.)</option>
<option value="6a06e72a-0039-4536-be5c-80a0f00888cc" data-url="/istanbul/sisli-tesvikiye-mah">Şişli (Teşvikiye Mah.)</option>
<option value="02b33b9a-4656-4507-a8a5-ce86e78b043f" data-url="/istanbul/sisli-yayla-mah">Şişli (Yayla Mah.)</option>
<option value="a83619d8-8f62-4b69-838a-6b520436df4f" data-url="/istanbul/tarabya">Tarabya</option>
<option value="964fdb36-ef15-4589-aa58-402681e06193" data-url="/istanbul/tuzla-akfirat-mah">Tuzla (Akfırat Mah.)</option>
<option value="863d6463-0751-482f-aba4-a44296fe8823" data-url="/istanbul/tuzla-anadolu-mah">Tuzla (Anadolu Mah.)</option>
<option value="3af97db2-90df-4895-bd2d-c672d227c33d" data-url="/istanbul/tuzla-aydinli-mah-birlik-osb">Tuzla (Aydınlı Mah. - Birlik OSB)</option>
<option value="dff57a21-62e3-4f45-aa4a-8032079bc621" data-url="/istanbul/tuzla-aydinli-mah-deri-osb-orhanli-girisi">Tuzla (Aydınlı Mah. - Deri OSB Orhanlı Girişi)</option>
<option value="a2187277-cc30-44cd-94dd-320f517535c6" data-url="/istanbul/tuzla-aydinli-mah-deri-osb">Tuzla (Aydınlı Mah. - Deri OSB)</option>
<option value="4ae8b0db-2a4d-4eb5-a8c3-cc0c6c8d8901" data-url="/istanbul/tuzla-aydinli-mah-istanbul-ay-osb">Tuzla (Aydınlı Mah. - İstanbul Ay OSB)</option>
<option value="943c9c44-1ef3-42cf-817e-9dfb2230092e" data-url="/istanbul/tuzla-aydinli-mah-kosb">Tuzla (Aydınlı Mah. - KOSB)</option>
<option value="e48c1df9-8e9e-40af-aa95-1e34d5fcf04f" data-url="/istanbul/tuzla-aydinli-mah-osb">Tuzla (Aydınlı Mah. - OSB)</option>
<option value="f7cda075-3d4d-4a3e-a591-e33c3a8a331a" data-url="/istanbul/tuzla-aydinli-mah-toki">Tuzla (Aydınlı Mah. - TOKİ)</option>
<option value="3ee75562-195d-43c4-9c20-b0bfac0e524e" data-url="/istanbul/tuzla-aydinli-mah">Tuzla (Aydınlı Mah.)</option>
<option value="6a0380cd-d488-4e1f-856d-222fe4c14aab" data-url="/istanbul/tuzla-aydintepe-mah">Tuzla (Aydıntepe Mah.)</option>
<option value="bef74fd4-a8f6-4066-94bc-08db19258ce2" data-url="/istanbul/tuzla-cami-mah">Tuzla (Cami Mah.)</option>
<option value="4665400d-0de0-4b6f-82ed-df7140ec9bb3" data-url="/istanbul/tuzla-evliya-celebi-mah">Tuzla (Evliya Çelebi Mah.)</option>
<option value="2c7788c4-0063-4cb6-8e0f-6350095a1a29" data-url="/istanbul/tuzla-fatih-mah">Tuzla (Fatih Mah.)</option>
<option value="35200cea-b7fb-4098-abaa-d9a78cbb3624" data-url="/istanbul/tuzla-icmeler-mah">Tuzla (İçmeler Mah.)</option>
<option value="3018a23f-ad32-4b3a-8489-6426c2b63eb6" data-url="/istanbul/tuzla-istasyon-mah">Tuzla (İstasyon Mah.)</option>
<option value="81e26df9-f7f0-4702-b66b-f9368f011c43" data-url="/istanbul/tuzla-mescit-mah">Tuzla (Mescit Mah.)</option>
<option value="7aac7f28-072b-4877-97fd-a56bf97d9f3b" data-url="/istanbul/tuzla-mimar-sinan-mah">Tuzla (Mimar Sinan Mah.)</option>
<option value="93ecb35c-d4b6-4482-8f8b-37dbe5d24643" data-url="/istanbul/tuzla-orhanli-mah">Tuzla (Orhanlı Mah.)</option>
<option value="e5e3a553-8323-4eeb-9b88-bae5b9ea6a19" data-url="/istanbul/tuzla-orta-mah">Tuzla (Orta Mah.)</option>
<option value="c6f181f4-a189-446a-8d9b-4477c2302671" data-url="/istanbul/tuzla-postane-mah">Tuzla (Postane Mah.)</option>
<option value="c03e68d0-31c5-44bd-bfb9-da74a6673d3b" data-url="/istanbul/tuzla-sifa-mah">Tuzla (Şifa Mah.)</option>
<option value="64af189f-296d-4764-abfe-bbfde0d6d16f" data-url="/istanbul/tuzla-tepeoren-mah-osb">Tuzla (Tepeören Mah. - OSB)</option>
<option value="3109d013-6f03-4660-b795-7aef29b92d86" data-url="/istanbul/tuzla-tepeoren-mah">Tuzla (Tepeören Mah.)</option>
<option value="3169d8b7-d651-4a91-9bdd-123c2cd26615" data-url="/istanbul/tuzla-yayla-mah">Tuzla (Yayla Mah.)</option>
<option value="bd8459fb-a786-4ab4-8c16-e1a2a3cdf4d2" data-url="/istanbul/ulus">Ulus</option>
<option value="f40ccabf-9095-402b-bc15-64979dd03666" data-url="/istanbul/umraniye-armaganevler-mah">Ümraniye (Armağanevler Mah.)</option>
<option value="d672039d-2f55-41aa-a309-3cf30ab8894f" data-url="/istanbul/umraniye-atakent-mah">Ümraniye (Atakent Mah.)</option>
<option value="dd51150a-4ab5-49c2-bbcf-dae0b8aa236a" data-url="/istanbul/umraniye-ataturk-mah">Ümraniye (Atatürk Mah.)</option>
<option value="e4fa62e6-4b12-4273-ae49-b8d63f1151e7" data-url="/istanbul/umraniye-cakmak-mah">Ümraniye (Çakmak Mah.)</option>
<option value="68d86674-db32-4788-ba1b-a3d17a460a1c" data-url="/istanbul/umraniye-camlik-mah">Ümraniye (Çamlık Mah.)</option>
<option value="3bf80bb8-e072-43c5-9d8e-6c41116d76f0" data-url="/istanbul/umraniye-dumlupinar-mah">Ümraniye (Dumlupınar Mah.)</option>
<option value="6fb91526-3650-483e-9d9a-eb34ec4c1eab" data-url="/istanbul/umraniye-elmalikent-mah">Ümraniye (Elmalıkent Mah.)</option>
<option value="e557a8e9-d8fd-49f4-bfaa-434995741dde" data-url="/istanbul/umraniye-esensehir-mah">Ümraniye (Esenşehir Mah.)</option>
<option value="7bd65b30-d41c-46ff-97ab-819a35758897" data-url="/istanbul/umraniye-ihlamurkuyu-mah">Ümraniye (Ihlamurkuyu Mah.)</option>
<option value="3df60bbf-5931-4472-9a6e-6ec1ffa00d80" data-url="/istanbul/umraniye-inkilap-mah">Ümraniye (İnkılap Mah.)</option>
<option value="52eabe9d-394f-46b7-9359-0883f1e7bd5b" data-url="/istanbul/umraniye-istiklal-mah">Ümraniye (İstiklal Mah.)</option>
<option value="a6c198c1-abbe-4ab3-9b7f-130743e8b175" data-url="/istanbul/umraniye-m-akif-mah">Ümraniye (M. Akif Mah.)</option>
<option value="ca46119c-828f-4321-b067-1863f3240744" data-url="/istanbul/umraniye-madenler-mah">Ümraniye (Madenler Mah.)</option>
<option value="23a1e012-c637-462e-86ca-1fde4db20c74" data-url="/istanbul/umraniye-merkez">Ümraniye (Merkez)</option>
<option value="8fa9db09-f11c-4c46-8108-999e674aebb1" data-url="/istanbul/umraniye-namik-kemal-mah">Ümraniye (Namık Kemal Mah.)</option>
<option value="dee94d57-89bd-4afe-a7d1-69be72272e19" data-url="/istanbul/umraniye-saray-mah">Ümraniye (Saray Mah.)</option>
<option value="dc72c58f-cbf5-4309-bae8-10d1f1fe51ce" data-url="/istanbul/umraniye-site-mah">Ümraniye (Site Mah.)</option>
<option value="8e53175b-3ae4-4ce7-8a32-5ca705c0755f" data-url="/istanbul/umraniye-serifali-mah">Ümraniye (Şerifali Mah.)</option>
<option value="6d9546ea-65df-49df-b0ab-d9fa22b2685c" data-url="/istanbul/umraniye-tatlisu-mah">Ümraniye (Tatlısu Mah.)</option>
<option value="f48627cb-49e9-4324-ad65-207fb3336b00" data-url="/istanbul/umraniye-tepeustu-mah">Ümraniye (Tepeüstü Mah.)</option>
<option value="2e55dae1-b552-44eb-bff4-080ebf29743b" data-url="/istanbul/umraniye-yamanevler-mah">Ümraniye (Yamanevler Mah.)</option>
<option value="86277509-7705-4265-ba65-9f242d83625b" data-url="/istanbul/umraniye-yavuzturk-mah">Ümraniye (Yavuztürk Mah.)</option>
<option value="bde84b54-979a-4d54-8952-7a4d6f77f6f2" data-url="/istanbul/umraniye-yenisehir-soyak">Ümraniye (Yenişehir Soyak)</option>
<option value="fdf24a9a-b52d-4e1f-b093-448ddbfad3ed" data-url="/istanbul/unalan">Ünalan</option>
<option value="0bee37b1-453c-4c1a-80bf-6171d2624b49" data-url="/istanbul/uskudar-a-mahmud-hudayi-mah">Üsküdar (A. Mahmud Hüdayi Mah.)</option>
<option value="f0360586-cdbc-4018-a765-5935fb699f74" data-url="/istanbul/uskudar-acibadem-mah">Üsküdar (Acıbadem Mah.)</option>
<option value="87183054-f7e2-4858-a8de-e781ec12b40a" data-url="/istanbul/uskudar-ahmediye-mah">Üsküdar (Ahmediye Mah.)</option>
<option value="9552a469-84bd-43c5-9a06-d51424f4bc4b" data-url="/istanbul/uskudar-ayazma-mah">Üsküdar (Ayazma Mah.)</option>
<option value="97e868f3-26e7-4a7d-b483-c198496ec937" data-url="/istanbul/uskudar-baglarbasi-mah">Üsküdar (Bağlarbaşı Mah.)</option>
<option value="d216d3e9-22c1-4967-aef5-f5916593a39f" data-url="/istanbul/uskudar-burhaniye-mah">Üsküdar (Burhaniye Mah.)</option>
<option value="926ecf6f-f467-43b8-8bec-a21cac4c0ba4" data-url="/istanbul/uskudar-emniyet-mah">Üsküdar (Emniyet Mah.)</option>
<option value="69408499-c591-415c-a74d-277d984b62c6" data-url="/istanbul/uskudar-ferah-mah">Üsküdar (Ferah Mah.)</option>
<option value="2fe35b03-9af4-48ee-b9aa-f079a94aee85" data-url="/istanbul/uskudar-fistikagaci-mah">Üsküdar (Fıstıkağacı Mah.)</option>
<option value="733d730c-ef29-4095-b55d-be06677b811b" data-url="/istanbul/uskudar-guzeltepe-mah">Üsküdar (Güzeltepe Mah.)</option>
<option value="eb8e9167-231d-400f-8e31-5535ac2278fc" data-url="/istanbul/uskudar-h-hesna-hatun-mah">Üsküdar (H. Hesna Hatun Mah.)</option>
<option value="190a5094-2355-49de-9b9b-b9d900bc99ee" data-url="/istanbul/uskudar-icadiye-mah">Üsküdar (İcadiye Mah.)</option>
<option value="3f61144f-3b5c-47db-9c82-92dfb6352517" data-url="/istanbul/uskudar-kirazlitepe-mah">Üsküdar (Kirazlıtepe Mah.)</option>
<option value="cc4d5701-31df-4cc3-b7dc-b3668368cba3" data-url="/istanbul/uskudar-kuleli-mah">Üsküdar (Kuleli Mah.)</option>
<option value="e2a9bede-b3aa-4248-9e58-418c8692cd36" data-url="/istanbul/uskudar-kucuksu-mah">Üsküdar (Küçüksu Mah.)</option>
<option value="595d8367-64f3-444e-83b8-83c648f80081" data-url="/istanbul/uskudar-kupluce-mah">Üsküdar (Küplüce Mah.)</option>
<option value="b2e1a7a7-90ad-4d70-9393-ce06865dbdfa" data-url="/istanbul/uskudar-merkez">Üsküdar (Merkez)</option>
<option value="8de5b5dc-d0d4-4f24-bf0e-a73705aab2ee" data-url="/istanbul/uskudar-mimar-sinan-mah">Üsküdar (Mimar Sinan Mah.)</option>
<option value="b6c0dad6-839b-4d16-8764-a8d0a966a962" data-url="/istanbul/uskudar-murat-reis-mah">Üsküdar (Murat Reis Mah.)</option>
<option value="bfbeeed5-dfb0-4a16-a1b8-98c749a69ae9" data-url="/istanbul/uskudar-pazarbasi-mah">Üsküdar (Pazarbaşı Mah.)</option>
<option value="7d989b43-6f01-4aad-85b8-5743b863d889" data-url="/istanbul/uskudar-salacak">Üsküdar (Salacak)</option>
<option value="08df2095-01ab-442b-af75-09198f5fd46c" data-url="/istanbul/uskudar-selimiye">Üsküdar (Selimiye)</option>
<option value="b719cfba-adc5-42ef-9ed6-aa14a190b0f1" data-url="/istanbul/uskudar-sultantepe-mah">Üsküdar (Sultantepe Mah.)</option>
<option value="15aba364-10fa-41dc-9596-9a269c57806a" data-url="/istanbul/uskudar-toygar-hamza-mah">Üsküdar (Toygar Hamza Mah.)</option>
<option value="9af9c48c-26e1-490a-a59c-cf4c49cc676f" data-url="/istanbul/uskudar-valide-i-atik-mah">Üsküdar (Valide-i Atik Mah.)</option>
<option value="b5d6238f-9a37-4e5d-a616-1c8599d4a7df" data-url="/istanbul/yamacli">Yamaçlı</option>
<option value="049f4485-1638-4649-96b5-d56a61c9e896" data-url="/istanbul/yenibosna">Yenibosna</option>
<option value="ef1b91a0-28a3-473b-a24e-af5b9b3f0489" data-url="/istanbul/yenibosna-basin-ekspres-yolu">Yenibosna (Basın Ekspres Yolu)</option>
<option value="3decaf27-0d5d-4df7-9592-81d729b636e0" data-url="/istanbul/yenibosna-cobancesme">Yenibosna (Çobançeşme)</option>
<option value="9e9b43cc-1c50-4d71-9ee7-f55e5cb34919" data-url="/istanbul/yenikoy">Yeniköy</option>
<option value="26abe267-2633-4afe-97f1-0d4e52f5ace5" data-url="/istanbul/yesilkoy">Yeşilköy</option>
<option value="58179e7b-5a7e-4259-a47b-a9495b15aab9" data-url="/istanbul/yesilkoy-ataturk-havalimani">Yeşilköy (Atatürk Havalimanı)</option>
<option value="8684148d-e67e-49a2-8664-e9c9ec5e45f7" data-url="/istanbul/yesilkoy-idtm">Yeşilköy (İDTM)</option>
"/istanbul/yesilyurt"
"/istanbul/yukari-dudullu"
"/istanbul/zeytinburnu-bestelsiz-mah"
"/istanbul/zeytinburnu-cirpici-mah"
"/istanbul/zeytinburnu-gokalp-mah"
"/istanbul/zeytinburnu-kazlicesme-mah"
"/istanbul/zeytinburnu-maltepe-mah-cevizlibag"
"/istanbul/zeytinburnu-maltepe-mah"
"/istanbul/zeytinburnu-merkezefendi-mah-cevizlibag"
"/istanbul/zeytinburnu-merkezefendi-mah"
"/istanbul/zeytinburnu-nuripasa-mah"
"/istanbul/zeytinburnu-seyitnizam-mah"
"/istanbul/zeytinburnu-sumer-mah"
"/istanbul/zeytinburnu-telsiz-mah"
"/istanbul/zeytinburnu-veliefendi-mah"
"/istanbul/zeytinburnu-yenidogan-mah"
"/istanbul/zeytinburnu-yesiltepe-mah"
</optgroup>
"""
