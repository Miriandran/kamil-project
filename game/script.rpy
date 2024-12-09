# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# DEFINE CHARACTERS
define k = Character("Bima", color="#b42b2b")
define r = Character("Aryanto", color="#423d3d")
define i = Character('Ibu', color="#423d3d")
define a = Character('Ayah', color="#423d3d")

# IMAGE BACKGROUND
image kamartidur = im.Scale("bg/IstanaNegara.jpg", 1920, 1080)
image ruangtamu = im.Scale("bg/Mobil.png", 1920, 1080)
image acak1 = im.Scale("bg/acak1.png", 1920, 1080)
image acak2 = im.Scale("bg/acak2.png", 1920, 1080)
image acak3 = im.Scale("bg/acak3.png", 1920, 1080)
image acak4 = im.Scale("bg/acak4.png", 1920, 1080)

# IMAGE CHARA
image kamil = "chara/kamil.png"
image ridwan = "chara/ridwan.png"
image ibu = "chara/ibu.png"
image ayah = "chara/ayah.png"

label start:
# The game starts here.
    scene acak1
    with fade

    scene acak2
    with fade
    scene acak3
    with fade
    scene acak4
    with fade
    play sound "audio/dentumanpistol.mp3"
    "DORR!"
    "(dentuman pistol)"
   
    scene kamartidur
    with dissolve

    "(seketika kamil bangun dari tidur bersamaan dengan suara pistol)"
    play sound "audio/nafasberat.mp3"
    "(nafas berat terengah-engah)"

    show ridwan
    with fade
    r "Mimpi buruk lagi ya lu?"

    menu:
        "Iya kak..":
            jump y1
        ".....":
            jump t1

label y1:
    show kamil at left
    show ridwan at right
    k "iya kak..."
    r "terus-terusan mimpi 
        buruk? kenapa sih?"
    k 'gapapa kok'
    r ' lu kalo ada apa-apa
        cerita aja ke gw. 
        gini-gini gw kakak lu'
    k 'iya, makasih ya'
    '(kamil tersenyum berterimakasih)'

    jump m1

label t1:
    k '...'
    r 'yeuu malah bengong'
    r ' lu kalo ada apa-apa
        cerita aja ke gw. 
        gini-gini gw kakak lu'
    k '...'
    '(tatapan kosong menyelimuti wajah kamil)'

    jump m1

label m1:
    hide kamil
    hide ridwan

    i 'naaaak, Kamil, Ridwan, ayo sarapan'
    a 'ayo turun nak. Jangan sampe telat sekolah'
    '(suara ayah ibu terdengar dari luar kamar)'

    show kamil at left
    k 'EH IYA SEKARANG JAM BERAPA?'
    '(panik karena bangun kesiangan)'
    show ridwan at right
    r 'slow aja masih 5.30'
    '(ridwan bersantai karena sudah siap-siap duluan)'
    hide ridwan

    show ridwanrapi at right
    #[Ridwan sudah rapi dengan pakaian dan perlengkapannya]
    k 'MANA BISA GITU anjing, SEKOLAH KITA JAUH'
    r 'wkwkwk'
    #[Ridwan tertawa kecil]
    r 'dah sana buruan siap-siap, gw tunggu sambil sarapan'
    k 'oke hari ini jadwal kita olahraga, matematika, sama biologi'
    '(kamil sambil melihat selebaran jadwal yang nempel di dinding)'
    #[jadwal pelajaran sekolah SMA Cendekia Maju di selebaran kertas]
    k 'hmmmm berarti gw harus bawa buku, baju ganti, sama
            kalkulator'
    k 'pertama, buku yang harus gw bawa berarti buku olahraga, buku 
            matematika, buku biologi'
    
    #(mini game milih buku di rak)
    jump minibuku

label minibuku:
    #CODING GAME

# label benerbuku:
# label salahbuku:
# label minibaju:
# label benerbaju:
# label salahbaju:
# label minikalku:
# label benerkalku:
# label salahkalku:

# label ruangmakan:
#     (Kamil dateng ke ruangan meja makan nyamperin Ridwan)
#     k 'WANN' [ekspresi agak nyolot]
#     r 'apaaa?' [ekspresi bingung nyolot kek nih orang kenapa sih?]
#     k 'kalkulator gw mana heh?'
#     r 'apasih? lu nuduh gw?' 
#     k 'ya siapa lagi weh, lu doang yang sering make barang gw'
#     r 'sumpah demi Allah, gw kaga tau'
#     k 'eh gausa bawa-bawa nama Allah ya kalo bohong'
#     r 'apaan sih lu ga jel…'

#     (ibu menginterupsi)
#     i ' aduhh kalian ini gaada kerjaan yang lebih baik kah selain 
#             berantem terus?'
#     i ' ibu berani sumpah tembok di rumah ini lebih sering dengerin 
#             kalian berantem daripada dengerin omongan baik (nada ngomel)'
#     a ' udah nak, jangan berantem lagi'
#     i ' marahin pak anaknya!'
#     a ' Kamil, kalkulator kamu Ayah yang pinjam semalam waktu kamu 
#             tidur'
#     a ' maaf ya nak, ayah lupa ngembaliin kalkulator kamu k e 
#             tempatnya'
#     k 'oalah, ayah toh yang make hehehe [ekspresi ketawa malu]'
#     r 'oalah, ayah toh yang make [ekspresi ngeledek kamil]'
#     k 'ih bacot lu'
#     r 'nye nye nye lu yang bacot'
#     i ' heh udah!'
#     i ' sana kalian cepat siap-siap sekolah!'

#     (time skip beberapa menit)
#     [06.00 WIB, 9 September 1999]

#     k 'Wann. lu udah siap belom?'
#     r 'Udah, yok berangkat'
#     k 'Buuu, Yah. Kita berangkat yaa'
#     a ' ya nak, hati-hati di jalan ya'
#     i ' barang gaada yang ketinggalan?'
#     r 'Aku udah kebawa semua sih harusnya'
#     k 'Amannn'

#     r 'Mau lu atau gw yang bawa motor?'

# label motorbima:
#     Kamil : gw aja gapapa, ntar 
#         baliknya lu
#     Ridwan: oke deh, jangan bunuh gw 
#             di jalan tapi 
#     Kamil : mana ada, gw adalah the 
#             best rider on the world
#     Ridwan: the best bacot kali lu

# label motorarya:

#     Kamil : lu aja yang bawa
#     Ridwan: eh nyuruh-nyuruh
#     Ridwan: kemarin udah gw ya njing 
#             yang nyetir
#     Kamil : ya terus lu ngapain 
#             nawarin kocak?
#     Ridwan: formalitas aja WKWKWKWK
#     Kamil : yeuuu, yaudah mana 
#             kuncinya

# label gerbangsekolah:
#     (time skip beberapa menit)
#     [6.30 depan gerbang sekolah, 9 September 1999]

#     Kamil : ANJINGGG
#     Ridwan: kenapaa? [ekspresi muak kyk kenapa lagi ini orang]
#     Kamil : Biologi! LAPORAN BIOLOGI GW!
#     Ridwan: … [ekspresi menghela nafas]
#     Ridwan: terus gimana?
#     Kamil : harus dibawa anjing. lu tau kan bu Titiek orangnya killer
#     Ridwan: …
#     Kamil : gw harus balik pulang ngambil laporannya
#     Ridwan: lu serius? 
#     Ridwan: gw jadi lu mending dihukum. males anjing bolak-balik
#     Kamil : ga bisa gitu, gw harus balik
#     Ridwan: lu becanda ya anjing, ini udah jam berapa?

#     Kamil : bisa. gw bisa ngebut
#     Ridwan: gila lu ya? lu lupa 6 bulan lalu lu kecelakaan karena 
#             ngebut?
#     Kamil : yaelah itu gw cuman apes
#     Ridwan: bukan apes. lu emang ga bisa bawa motor ngebut mil
#     Kamil : yauda lah mau gimana lagi tapi ini laporan gw?
#     Ridwan: Haishhh
#     Ridwan: udah sini aja gw yang nyetir
#     Ridwan: lu ga becus bawa motor ngebut
#     Kamil : eh, jangan. lu masuk aja sana
#     Kamil : ini kesalahan gw, biar gw yang tanggung jawab
#     Ridwan: lu goblok ya? tanggung jawab ya tanggung jawab, tapi 
#             kecelakaan tetep mematikan anjing
#     Kamil : ini tanggung jawab gw. lu ga harus ikut terseret wan!
#     Ridwan: Bacot lu. Ga usah sok idealis. Gw gamau lu kenapa-kenapa
#     Kamil : Hrggghhh
#     Kamil : yauda ayok buruan

#     (mini game nyetir ngebut)

# label mininabrak:
# label ganabrak:
#     (time skip)
#     [06.44 sampai rumah]

#     Ridwan: wah gila, buruan ambil 
#             laporan lu
#     Kamil : iya, tunggu sini bentar 
#             ya (kamil masuk rumah)
#     Ibu   : Dek? kenapa balik dek?
#     Kamil : Laporan aku ketinggalan 
#             bu
#     Ibu   : kan kan. terus kakak kamu
#             gimana?
#     Kamil : itu nunggu di depan. Aku 
#             langsung ya bu, keburu 
#             telat
#     Ibu   : iya, sana buru!
#     Ibu   : hati-hati ya nak
#     (time skip)
#     [06.59 gerbang sekolah]

#     Ridwan: anjing, hampir aja kita 
#             telat
#     Kamil : wah iya anjing, untung 
#             masih ada waktu
#     Kamil : makasih ya wan
#     Ridwan: dah, buruan masuk. Lain 
#             kali traktir gw bakso
#     Kamil : iya iya ntar jam 
#             istirahat

# label nabrak:
#     (time skip)
#     [06.52 sampai rumah]

#     Ridwan: wah gila, buruan ambil, 
#             kita udah telat
#     Kamil : iya, tunggu sini bentar 
#         ya (kamil masuk rumah)
#     Ibu   : Dek? kenapa balik dek?
#     Kamil : Laporan aku ketinggalan 
#             bu
#     Ibu   : kan kan. terus kakak kamu
#             gimana?
#     Kamil : itu nunggu di depan. Aku 
#         langsung ya bu, keburu 
#         telat
#     Ibu   : iya, sana buru!
#     Ibu   : hati-hati ya nak
#     (time skip)
#     [07.07 gerbang sekolah]

#     Ridwan: waduh, mampus, kita telat
#     Kamil : wah iya anjing
#     Satpam: kenapa telat? tunggu di 
#             luar dulu 
#     Kamil : tapi pak…
#     Satpam: ga ada tapi-tapi. Tunggu 
#             guru BK ke sini
#     Ridwan: yah, dihukum deh kita
#     Kamil : iya kak, gw minta maaf ya 
#             jadi bawa lu di sini
#     Ridwan: dah gapapa. udah makanan 
#             sehari-sehari ngadep guru 
#             BK

#     (time skip)
#     [16.36, 9 September 1999]

#     Kamil : wah akhirnya kelar juga 
#             sekolah hari ini
#     Ridwan: iya, hectic banget hari 
#             ini sampe ngebut-ngebut 
#             di jalan
#     Kamil : heeh. sampe harus kena 
#             hukuman karena telat 
#             hahahaha
#     Ridwan: hahahaha. lu harus tau 
#             rasanya dihukum biar ga 
#             jadi siswa rajin mulu
#     Kamil : yok lah pulang. capek

# label nemudompet:
#     (baru jalan bentar)
#     [tunjukin ada dompet di jalan]

#     Ridwan: eh apa itu?
#     Kamil : dompet?
#     Ridwan: wah lumayan rezeki ngga kemana
#     Kamil : eh jangan ngaco lu. itu punya orang
#     Ridwan: yaelah gini doang mah. lumayan loh hari gini dapet 23.000

# label haram:
#     Kamil : tetep aja wan. itu duit 
#             haram
#     Ridwan: Alah mil, gausa ngomongin 
#             halal haram deh


# label moral:
#     Kamil : ga boleh wan. ini sama 
#             aja nyuri
#     Ridwan: mana ada mil. duit hilang 
#             berarti udah bukan punya 
#             pemilik

# label aaa:
#     Ridwan: jaman gini hidup itu keras. kita harus bisa bertahan 
#             dengan cara apapun
#     Kamil : tapi bukan berarti harus merugikan orang lain wan!
#     Ridwan: mil, lu jangan sok idealis mulu deh. realita hidup itu 
#         kayak gini
#     Kamil : tetep aja ini salah wan!
#     Ridwan: bodo amat lah apa urusan lu? bukan duit lu juga (ngotot)
#     Kamil : Ayah sama ibu ga pernah ngajarin kayak gini wan!
#     Ridwan: eh, lu tau apa soal ayah sama ibu? gw yang lahir duluan mil!
#     Kamil : … (kehabisan kata-kata untuk membujuk kakaknya) 
#             [ekspresi termenung agak kecewa]
#     Kamil : lu pulang duluan aja, gw nyusul
#     Ridwan: yeuu, bete lu?
#     Kamil : serah lu deh, gw pengen kencing (ketus)
#     Ridwan: yaelah, yauda sana gw tungguin
#     Kamil : oke

#     (time skip)
#     [16.42, 9 September 1999]

#     Ayah  : eehh, jagoan-jagoan ayah udah pulang
#     Ridwan: hehe, iya yah udah kelar sekolahnya
#     Kamil : … (masih speechless kelakuan Ridwan) [senyum aja]
#     Ibu   : tadi gimana sekolahnya? sampe bolak-balik gitu kalian
#     Ayah  : tadi kalian balik pulang?

#     Ibu   : iya yah, tadi baru banget ayah berangkat kerja mereka balik 
#             pulang
#     Kamil : iya yah hehe, laporan kamil ketinggalan
#     Ayah  : wah kacau, lain kali bener-bener dicek ya jangan sampe ada 
#             yang lupa
#     Ridwan: Walah, ayah aja lupa ngembaliin kalkulator sampe tantrum tuh 
#             si anak
#     Kamil : diem ya lu
#     Ayah  : HAHAHAHA namanya juga udah bapak-bapak pasti lupaan
#     Ibu   : ngomong-ngomong, Kamil, Ridwan, kalian inget ngga sekarang 
#             hari apa?
#     Ridwan: hari kamis?
#     Kamil : OH HARI ULANG TAHUN AYAH!
#     Ridwan: OIYAA
#     Ayah  : HAHAHAHAHA. ternyata masih ada yang inget ulang tahun ayah
#     Ibu   : kita harus ucapin apa nakk? satu, dua, tiga…
#     kompak: selamat ulang tahun ayahhh!
#     Ayah  : hahahaha, terima kasih yaa nak, ibu
#     Ibu   : jadiii… buat ngerayain ulang tahun ayah kita mau makan-makan 
#             dimana inii??
#     Ayah  : hahahaha, sok kalian tentukan. Ayah ngikut dan tinggal bayar 
#             aja HAHAHAHA
# label sate:
#     Kamil : Sate kayanya menarik deh 
#             yah, udah lama ngga makan 
#             sate
#     Ridwan: Ah tapi lagi pengen 
#             makanan berkuah. Sop 
#             buntut kali ya?
#     Ibu   : hmmm, sop buntut oke sih

# label sopbuntut:
#     Kamil : Sop buntut kayanya 
#             menarik deh yah, udah 
#             lama ngga makan sop 
#             buntut
#     Ridwan: Ah tapi lagi pengen 
#         makanan bakaran. sate kali
#         ya?
#     Ibu   : hmmm, sate oke sih

# label makanmakan:
#     Ibu   : Yauda yuk kita siap-siap dan beberes. Habis maghrib kita 
#             berangkat yaa!
#     Kamil : Mau makan di mana kita bu?
#     Ibu   : Sarinah oke ngga Ayah?
#     Ayah  : yaaa… kalo ayah si oke aja asal belanjanya ngga sampe 1 juta 
#             HAHAHAHAHA
#     Ridwan: Ya kalo ada 1 juta mah mending buat beli TV lagi, taruh 
#             kamar Ridwan
#     Ayah  : Yeuuu, enak aja kamu
#     Ayah  : udah, sana siap-siap



#     (time skip)
#     [18.09, 9 September 1999, 162 menit sebelum dentuman]
#     [di dalam kamar]
#     Kamil : kak, lu udah siap belom?
#     Ridwan: lihat aja gw udah cakep gini
#     Kamil : kali aja lu mau ngapain lagi kek
#     Ridwan: ah, gw ga seribet itu orangnya
#     Kamil : oh iya, ngomong-ngomong soal dompet tadi
#     Ridwan: udah lah mil, mau dipanjangin sampe kapan lagi?
#     Kamil : ga gitu, gw mau ngomong sesuatu sama lu
#     Ridwan: apa?

# label reemburse:
#     Kamil : Sebenernya waktu gw tadi 
#             minta nyusul karena 
#             kencing, gw ketemu Ujang 
#     Ridwan: terus?
#     Kamil : dompet itu, ternyata itu 
#             dompet Ujang
#     Ridwan: Ujang anak bahasa itu?
#     Kamil : iya
#     Ridwan: ngaku-ngaku aja kali. 
#             Orang di dompetnya gaada 
#             kartu identitas sama 
#             sekali
#     Kamil : tapi dia nyebutin 
#             ciri-ciri dompet yang 
#             sama persis, dan 
#             nominalnya sama persis 
#             yang lu ambil
#     Ridwan: ya elah, terus gimana?
#     Kamil : dia bilang dia lagi butuh 
#             banget duitnya buat makan 
#             seminggu
#     Kamil : karena itu duit lu ambil, 
#             jadinya gw ga enak ke 
#             ujang
#     Ridwan: ngapain pake ga enak, 
#             yauda lah itu kesialan 
#             ujang
#     Kamil : mana bisa gitu wan. 
#             Akhirnya duit ujang gw 
#             ganti. gw bilang gw yang 
#             nemu dompetnya
#     Ridwan: lah tapi kan dompetnya 
#             masih ada di gw. gimana 
#             lu ngembaliinnya?
#     Kamil : iya, gw bilang dompetnya 
#             masih lu amanin, jadi 
#             duitnya dulu yang gw 
#             kasih ke dia
#     Ridwan: berarti ini dompet mau 
#             dibalikin besok?
#     Kamil : iya. sekalian gw sekarang 
#             mau minta duit gw lu 
#             balikin
#     Ridwan: heuuuhh. percuma tadi 
#             debat panjang lebar 
#             ujung-ujungnya ga jadi 
#             rezeki 

# label aryasalah:
#     Kamil : … (bingung mau gimana ngomongnya)
#     Ridwan: kenapa mil?
#     Kamil : gapapa, ga jadi wan
#     Ridwan: hufft (menghela nafas)
#     Ridwan: gini mil, dunia ini ngga 
#             akan pernah adil mil
#     Ridwan: lu lihat aja para pejabat 
#             di senayan sana
#     Ridwan: Lu lihat aja tahun 
#             kemarin gimana bobroknya 
#             presiden kita?
#     Ridwan: Kesengsaraan rakyat ga 
#             pernah mereka dengar mil!
#     Ridwan: dunia ini ga akan pernah 
#             adil mil
#     Ridwan: kehidupan ini ibarat 
#             bertahan di tengah hutan 
#             rimba
#     Ridwan: lu harus bisa survive 
#             gimanapun caranya
#     Ridwan: lihat tu ayah. Ayah jadi 
#             polisi harus jual sawah 
#             kakek dulu mil!
#     Kamil : tapi…
#     Ridwan: tapi apa mil?
#     Kamil : lihat pak Habibie Wan. 
#             Rupiah kita sekarang 
#             menguat banget
#     Kamil : Pak Habibie wan! dia mau 
#             berjuang untuk masyarakat
#     Kamil : kalo ibarat lu kehidupan 
#             ini adalah hutan 
#             belantara, beliau masih 
#             bisa sukses tanpa harus 
#             merugikan orang lain wan!
#     Ridwan: Pak Habibie itu punya 
#             otak mil! ga kaya aku 
#             yang goblok ini
#     Ridwan: bagi kami yang goblok ini 
#             akan terus-terusan 
#             dibodohi dan ga akan bisa 
#             maju
#     Ridwan: cara satu-satunya bagi 
#             kami bisa bertahan hidup 
#             ya dengan mengusahakan
#             segala cara!

# label ibutibatiba:
#     Ibu   : eeeh, ini ada apa ya ribut-ribut? (berbicara dari luar 
#             kamar)
#     Ibu   : udah siap belom kalian?
#     Ridwan: Udah bu (membalas dari dalam kamar)
#     Ridwan: nanti kita bahas lagi (lanjut ke kamil)
#     Ridwan: gw gamau kesenangan ulang tahun ayah harus diganggu dengan 
#             masalah dompet
#     Kamil : ya

#     (kamil dan ridwan kelaur dari kamar)
#     Kamil : Kita udah siap nih bu
#     Ibu   : widihh, udah cakep-cakep nih 
#     Ridwan: Ayah mana bu? 
#     Ibu   : Ayah masih di kamar mandi lagi mual-mual
#     Ayah  : haloo, udah siap?
#     Kamil : Ayah sakit? ayah kalo ga enak badan gausa dipaksain makan di 
#             luar yah
#     Ridwan: iya, kita masih bisa ngerayain di rumah kok yah
#     Ibu   : tuh kan, ibu bilang apa tadi
#     Ayah  : gapapa kok, ayah lagi merasa ga enak aja perasaannya, gatau 
#             kenapa ya
#     Ayah  : apa mungkin ayah ngga rela kehilangan uang sampe 1 juta? 
#             hahahahaha
#     Ibu   : ih ayah, ayah beneran gapapa? 
#     Ayah  : iya gapapa. ayah sehat kok. yok berangkat habis ini
#     Kamil : syukurlah. yauda ayok kita berangkat
#     Ridwan: yokkk
#     Ayah  : Kamil, kamu yang bawa mobilnya ya
#     Kamil : eh kok aku yah? kenapa ngga kak ridwan aja?
#     Ridwan: udah lu aja, udah punya sim juga
#     Ibu   : ya sekali-kali lah nak, mumpung udah ada sim
#     Ibu   : kasihan kakak kamu yang nyetir mulu
#     Ayah  : hahahaha, ayah juga pengen tau gimana skill kamu nyetir
#     Kamil : baikkk, siap komandan

#     (mini game nyetir)

# label sampei:
#     Kamil : Alhamdulillah udah sampe

# label lamatpsampe:
#     (if lebih dari sekian kali belok)

#     Kamil : ini beloknya kemana ya?
#     Ridwan: tau jalan ga sih lu?
#     Ibu   : ayo nak, keburu tutup 
#             sarinahnya
#     Ayah  : nghroookk [ketiduran]

#     (achievement unlocked: buta map)
#     (by sistem arahin otomatis sampe)

# label akhirsampe:
# Ibu   : Akhirnya udah sampe juga
# Ridwan: fyuhhh, let’s go makannnn

# (sampai restoran memesan menu)
# [19.34, 9 September 1999, 77 menit sebelum dentuman]
# [scene di restoran]

# Staff : selamat datang. ini untuk buku menunya. pesanan langsung 
#         ditulis di sini ya…
# Kamil : Ayah, ibu, kak, mau pesen apa? kamil aja yang nulisin
# (mini game)

# Staff : baik, mohon ditunggu sebentar ya…
# Ibu   : senengnyaa, jarang-jarang kita makan di restoran
# Ayah  : ya ngapain toh repot-repot ke restoran kalo masakan ibu itu 
#         yang terenak di dunia
# Ibu   : alah-alah masa sih ayah?
# Ayah  : loh iya dong
# Ayah  : Ridwan, Kamil, 20 tahun nikah sama ibu, ga pernah sekalipun 
#         ayah ngga habisin masakan ibu
# Ridwan: hahahaha, keliatan banget sih emang dari perutnya
# Ayah  : HAHAHAHAHA (ketawa bapak-bapak lepas)
# Kamil : hahaha, ayah mah emang dimana-mana makannya banyak
# Ibu   : ih percaya ga sih kalian, dulu ayah waktu masih bujang tuh 
#         badannya bagus tau
# Ibu   : ganteng dan gagah
# Ibu   : kalo sekarang ih, gantengnya emang masih iya, tapi gagahnya 
#         berubah jadi gajah
# Ayah  : HAHAHAHA, ah ibu ini bisa aja 
# Staff : Silakan… (sembari mengantarkan makanan)
# Staff : untuk pesanannya sudah lengkap ya?
# Kamil : mmmmm udah kak, terima kasih ya…
# Staff : terima kasih kembali

# [20.45, 9 September 1999, 6 menit sebelum dentuman]
# Ayah  : Alhamdulillah kenyang
# Ibu   : Alhamdulillah, seneng banget deh yah, makasih yaaa
# Kamil : Besok traktir sop buntut dong yah
# Ayah  : Wah tunggu ayah gajian lagi ya hahahaha
# Ibu   : Kamil, Ridwan, minta tolong bayarin ke kasir ya, ini bawa 
#         dompet ibu
# Ridwan: siap

# [20.46, 9 September 1999, 5 menit sebelum dentuman]
# Kamil : meja nomor 5, totalnya berapa kak?
# Staff : totalnya jadi Rp120.000
# Kamil : okee, ini kak (menyerahkan uang)
# Staff : uangnya pas ya? terima kasih
# Kamil : sama-sama kak
# Ridwan: mahal amat ya sampe abis segitu
# Kamil : yaelah bro, kita makan di sarinah. beli sate berapa banyak 
#         juga tadi?
# Ridwan: yaaa iya sihh

# [20.48, 9 September 1999, 3 menit sebelum dentuman]
# Kamil : eh wan, lihat deh toko baju sebrang
# Ridwan: iya? kenapa?
# Kamil : lihat orang baju item itu? dia lagi nyolong sepatu ga sih?
# Kamil : TUH TUH TUH DIA UMPETIN DI TAS DIA SI SEPATUNYA
# Ridwan: EH IYA
# Kamil : wah gw harus bilang ke ayah
# Ridwan: eh, tunggu mil!
# Kamil : kenapa kakk?
# Ridwan: udah biarin aja, ga usah ikut campur urusan orang
# Kamil : urusan orang? maksud lu?
# Ridwan: udah jangan ikut campur, biarin, itu urusan yang punya toko
# Kamil : hahhh??
# Kamil : lu udah gila ya?
# Kamil : itu kriminalitas anjing, sempet-sempetnya lu mikir gitu
# Ridwan: ya terus kenapaa?? apa untungnya buat kita ngurusin dia?!
# Kamil : lu beneran gila ya? ayah kita polisi loh!
# Kamil : ini udah jadi tanggung jawab ayah
# Ridwan: yauda, biarin ngapa sih, ngerepotin aja tau ga sih
# Kamil : gw gamau tau, gw harus kasih tau ayah



# [20.49, 9 September 1999, 2 menit sebelum dentuman]
# (kamil bergegas menghampiri ayah)
# Kamil : YAHH! ada pencuri yahh di toko seberang!!
# Ayah  : hmmmh? gimana gimana?
# Kamil : Toko baju seberang yah, ada orang nyolong sepatu, kamil 
#         lihat dengan mata kepala sendiri
# Ayah  : bener ridwan?
# Ridwan: iya yah
# Ayah  : wah ga bener nih, ayok kita samperin
# Ibu   : dek, emang ga ada satpamnya yang jaga? ulang tahun ayah masa 
#         harus tetep kerja sih
# Ayah  : udah lah bu, ini tanggung jawab ayah
# Ayah  : yang mana orangnya?
# Kamil : itu yah yang baju hitam
# Ayah  : mana? ohhh yang bawa tas itu?

# [20.50, 9 September 1999, 1 menit sebelum dentuman]
# Ayah  : permisi mas, saya Kompol Susilo, Kapolsek Matraman
# [menunjukkan tanda pengenal]
# Ayah  : Saya menerima laporan kecurigaan tindakan pencurian yang 
#         melibatkan mas sebagai tersangka
# Ayah  : Untuk itu akan saya periksa mas untuk meluruskan apakah 
#         dugaannya benar atau salah
# X     : wah, salam kenal pak Susilo. izin meluruskan, saya tidak 
#         mencuri barang apapun di toko ini
# Ayah  : maka biarkan saya memeriksa agar dugaan bisa dibantah jika 
#         memang tidak ada bukti
# Staff : Bapak polisi?
# Ayah  : iya, ada yang bisa saya bantu?
# Staff : kami kehilangan satu pasang sepatu di rak pajangan A9 pak, 
#         sepertinya mas ini adalah pelakunya
# Ayah  : mas… menanggapi ini, saya mohon mas untuk kooperatif 
# [wajah X panik]
# [X membuka tas, siap mengeluarkan barang]
# [3]
# [2]
# [1]
# [pistol diacungkan pada ayah]
# (DOR!)(dentuman tembakan)
# (bunyi dengung ngiiiiinggg)
# [perlahan layar mulai glitching]
# Ridwan: AYAHHHHH
# Ridwan: KAMILLL
# Ridwan: KAMILLL
# Ridwan: KAMILLL, LIHAT YANG KAMU PERBUAT!!!
# [glitch total untuk transisi ke fase selanjutnya]

    return
``