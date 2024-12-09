# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# DEFINE CHARACTERS
define k = Character("Bima", color="#472301")
define r = Character("Aryanto", color="#a8652e")
define i = Character('Ibu', color="#423d3d")
define a = Character('Ayah', color="#423d3d")

# IMAGE BACKGROUND
image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)
image acak2 = im.Scale("bg/acak2.jpg", 1920, 1080)
image acak3 = im.Scale("bg/acak3.webp", 1920, 1080)
image kamartidur = im.Scale("bg/kamar.jpg", 1920, 1080)
image ruangtamu = im.Scale("bg/living.jpg", 1920, 1080)
image ruangmakan = im.Scale("bg/living.jpg", 1920, 1080)
image depanrumah = im.Scale("bg/rumahkmilkecil.png", 1920,1080)
image rakbuku = im.Scale("bg/rakbuku.png", 1920,1080)
image gerbangsekolah = im.Scale("bg/GerbangSekolah.png", 1920,1080)
image sekolah_sore = im.Scale("bg/sekolahsore.jpg", 1920,1080)
image jalan = im.Scale("bg/jalansore.jpg", 1920,1080)

# IMAGE CHARA
image f_Bima = "chara/hf_Kamil.png"
image Bima = "chara/bu_kamil.png"

image f_Arya = "chara/sk_ridwan.png"
image Arya = "chara/bu_ridwan.png"

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
    scene black
    with fade
    play sound "audio/dentumanpistol.mp3"
    show Bima
    "DORR!"
    "(dentuman pistol)"
   
    scene kamartidur
    with dissolve

    "(seketika Bima bangun dari tidur bersamaan dengan suara pistol)"
    play sound "audio/nafasberat.mp3"
    "(nafas berat terengah-engah)"

    show f_Arya at Transform(xpos=0.5, ypos=0.15)
    with fade
    r "Mimpi buruk lagi ya lu?"

    menu:
        "Iya kak..":
            jump y1
        ".....":
            jump t1
    

label y1:
    hide f_Arya
    show Bima at left
    show Arya at right
    k "iya kak..."
    r "terus-terusan mimpi 
        buruk? kenapa sih?"
    k 'gapapa kok'
    r ' lu kalo ada apa-apa
        cerita aja ke gw. 
        gini-gini gw kakak lu'
    k 'iya, makasih ya'
    '(Bima berterimakasih)'

    jump m1

label t1:
    hide f_Arya
    show Bima at left
    show Arya at right
    k '...'
    r 'yeuu malah bengong'
    r ' lu kalo ada apa-apa
        cerita aja ke gw. 
        gini-gini gw kakak lu'
    k '...'
    '(tatapan kosong menyelimuti wajah Bima)'

    jump m1

label m1:
    hide Bima
    hide Arya

    i 'naaaak, Bima, Arya, ayo sarapan'
    a 'ayo turun nak. Jangan sampe telat sekolah'
    '(suara ayah ibu terdengar dari luar kamar)'

    show Bima at left
    k 'EH IYA SEKARANG JAM BERAPA?'
    '(panik karena bangun kesiangan)'
    show Arya at right
    r 'slow aja masih 5.30'
    '(Arya bersantai karena sudah siap-siap duluan)'
    hide Arya

    show Arya at right
    #[Arya sudah rapi dengan pakaian dan perlengkapannya]
    k 'MANA BISA GITU anjing, SEKOLAH KITA JAUH'
    r 'wkwkwk'
    #[Arya tertawa kecil]
    r 'dah sana buruan siap-siap, gw tunggu sambil sarapan'
    k 'oke hari ini jadwal kita olahraga, matematika, sama biologi'
    '(Bima sambil melihat selebaran jadwal yang nempel di dinding)'
    #[jadwal pelajaran sekolah SMA Cendekia Maju di selebaran kertas]
    k 'hmmmm berarti gw harus bawa buku, baju ganti, sama
            kalkulator'
    k 'pertama, buku yang harus gw bawa berarti buku olahraga, buku 
            matematika, buku biologi'
    
    #(mini game milih buku di rak)
    jump minibuku

label minibuku:
    scene rakbuku
    show Bima at right
    $ correct_books = ["Buku Olahraga", "Buku Matematika", "Buku Biologi"]  # Correct books
    $ chosen_books = []  # Store player's choices

    "Bima mulai memilih buku yang harus dibawa dari rak buku."

    while len(chosen_books) < 3:
        $ options = []

        # Dynamically construct options for the menu
        if "Buku Olahraga" not in chosen_books:
            $ options.append("Buku Olahraga")
        if "Buku Matematika" not in chosen_books:
            $ options.append("Buku Matematika")
        if "Buku Biologi" not in chosen_books:
            $ options.append("Buku Biologi")
        if "Buku Sejarah" not in chosen_books:
            $ options.append("Buku Sejarah")
        if "Buku Fisika" not in chosen_books:
            $ options.append("Buku Fisika")

        # Display the menu with available options
        menu:
            "Pilih buku untuk dibawa:"

            # Add each option dynamically
            "Buku Olahraga" if "Buku Olahraga" in options:
                $ chosen_books.append("Buku Olahraga")
                "Bima mengambil Buku Olahraga."

            "Buku Matematika" if "Buku Matematika" in options:
                $ chosen_books.append("Buku Matematika")
                "Bima mengambil Buku Matematika."

            "Buku Biologi" if "Buku Biologi" in options:
                $ chosen_books.append("Buku Biologi")
                "Bima mengambil Buku Biologi."

            "Buku Sejarah" if "Buku Sejarah" in options:
                $ chosen_books.append("Buku Sejarah")
                "Bima mengambil Buku Sejarah."

            "Buku Fisika" if "Buku Fisika" in options:
                $ chosen_books.append("Buku Fisika")
                "Bima mengambil Buku Fisika."

    # Check if the player's choices are correct
    $ correct_count = sum(1 for book in chosen_books if book in correct_books)

    if correct_count == 3:
        "Bima: Hmmm... Semua buku yang gw pilih udah bener."
        jump ruangmakan
    else:
        "Bima: Aduh, kayaknya ada buku yang salah deh."
        $ chosen_books = []
        jump minibuku
            
#minigame pilih baju blm
#minigame pilih kalkulator


# Label ruangmakan
label ruangmakan:
    scene ruangmakan with fade
    show Bima at left
    show Arya at right

    k "YANTOO!!!"
    r "APAA?!" 
    k "Kalkulator gw mana heh?"
    r "Apasih? Lu nuduh gw?"
    k "Ya siapa lagi weh, lu doang yang sering make barang gw."
    r "Sumpah demi Allah, gw kaga tau."
    k "Eh, gausa bawa-bawa nama Allah ya kalo bohong."
    r "Apaan sih lu ga jel..."

    # Ibu interjects
    i "Aduhh kalian ini gaada kerjaan yang lebih baik kah selain berantem terus?"
    i "Ibu berani sumpah tembok di rumah ini lebih sering dengerin kalian berantem daripada dengerin omongan baik."
    a "Udah nak, jangan berantem lagi."
    i "Marahin pak anaknya!"
    a "Bima, kalkulator kamu Ayah yang pinjam semalam waktu kamu tidur."
    a "Maaf ya nak, Ayah lupa ngembaliin kalkulator kamu ke tempatnya."
    k "Oalah, Ayah toh yang make. Hehehe."
    r "Oalah, Ayah toh yang make."
    k "Ih bacot lu!"
    r "Nye nye nye, lu yang bacot."
    i "Heh udah!"
    i "Sana kalian cepat siap-siap sekolah!"

    # Time skip
    scene black with fade
    pause 1
    "06.00 WIB, 9 September 1999"
    scene depanrumah with fade
    show Bima at left
    show Arya at right

    k "Arya, lu udah siap belom?"
    r "Udah, yok berangkat."
    k "Buuu, Yah. Kita berangkat yaa."
    a "Ya nak, hati-hati di jalan ya."
    i "Barang gaada yang ketinggalan?"
    r "Aku udah kebawa semua sih harusnya."
    k "Amannn."

    r "Mau lu atau gw yang bawa motor?" 

    menu:
        "gw aja gapapa, ntar baliknya lu":
            jump motorbima
        "lu aja yang bawa":
            jump motorarya

label motorbima:
    k "Gw aja gapapa, ntar baliknya lu."
    r "Oke deh, jangan bunuh gw di jalan tapi."
    k "Mana ada, gw adalah the best rider on the world!"
    r "The best bacot kali lu."
    jump gerbangsekolah

label motorarya:
    k "Lu aja yang bawa."
    r "Eh nyuruh-nyuruh."
    r "Kemarin udah gw ya njing yang nyetir."
    k "Ya terus lu ngapain nawarin kocak?"
    r "Formalitas aja WKWKWKWK."
    k "Yeuuu, yaudah mana kuncinya."
    jump gerbangsekolah

label gerbangsekolah:
    scene gerbangsekolah with fade
    show Bima at left
    show Arya at right
    "06.30 depan gerbang sekolah, 9 September 1999"

    k "ANJINGGG!"
    r "Kenapaa?" 
    #[ekspresi muak kyk kenapa lagi ini orang]"
    k "Biologi! LAPORAN BIOLOGI GW!"
    r "…" 
    #[ekspresi menghela nafas]
    r "Terus gimana?"
    k "Harus dibawa anjing. Lu tau kan Bu Titiek orangnya killer."
    r "…"
    k "Gw harus balik pulang ngambil laporannya."
    r "Lu serius?"
    r "Gw jadi lu mending dihukum. Males anjing bolak-balik."
    k "Ga bisa gitu, gw harus balik."
    r "Lu becanda ya anjing, ini udah jam berapa?"

    k "Bisa. Gw bisa ngebut."
    r "Gila lu ya? Lu lupa 6 bulan lalu lu kecelakaan karena ngebut?"
    k "Yaelah itu gw cuman apes."
    r "Bukan apes. Lu emang ga bisa bawa motor ngebut, Bim."
    k "Yauda lah mau gimana lagi tapi ini laporan gw?"
    r "Haishhh."
    r "Udah sini aja, gw yang nyetir."
    r "Lu ga becus bawa motor ngebut."
    k "Eh, jangan. Lu masuk aja sana."
    k "Ini kesalahan gw, biar gw yang tanggung jawab."
    r "Lu goblok ya? Tanggung jawab ya tanggung jawab, tapi kecelakaan tetep mematikan anjing."
    k "Ini tanggung jawab gw. Lu ga harus ikut terseret, Arya!"
    r "Bacot lu. Ga usah sok idealis. Gw gamau lu kenapa-kenapa."
    k "Hrggghhh."
    k "Yauda ayok buruan."

    jump mininabrak

label mininabrak:
    # Placeholder for the mini-game outcome where the player makes a mistake and "nabrak."
    # Define this scene based on your mini-game logic.
    menu:
        '(gagal minigame (nabrak))':
            jump nabrak
        '(minigame berhasil)':
            jump ganabrak

label ganabrak:
    scene depanrumah with fade
    "06.44 sampai rumah."
    show Bima at left
    show Arya at right
    r "Wah gila, buruan ambil laporan lu."
    k "Iya, tunggu sini bentar ya." 
    "Bima masuk rumah."

    scene ruangtamu with fade
    show Bima at right
    i "Dek? Kenapa balik dek?"
    k "Laporan aku ketinggalan, Bu."
    i "Kan kan. Terus kakak kamu gimana?"
    k "Itu nunggu di depan. Aku langsung ya, Bu. Keburu telat."
    i "Iya, sana buru!"
    i "Hati-hati ya nak."

    scene gerbangsekolah with fade
    "06.59 gerbang sekolah."

    r "Anjing, hampir aja kita telat."
    k "Wah iya anjing, untung masih ada waktu."
    k "Makasih ya, Arya."
    r "Dah, buruan masuk. Lain kali traktir gw bakso."
    k "Iya iya, ntar jam istirahat."
    jump nemudompet

define s = Character('Satpam', color="#423d3d")

label nabrak:
    scene depanrumah with fade
    show Bima at left
    show Arya at right
    "06.52 sampai rumah."

    r "Wah gila, buruan ambil, kita udah telat."
    k "Iya, tunggu sini bentar ya."
    "Bima masuk rumah."

    scene ruangtamu with fade
    show Bima at right
    i "Dek? Kenapa balik dek?"
    k "Laporan aku ketinggalan, Bu."
    i "Kan kan. Terus kakak kamu gimana?"
    k "Itu nunggu di depan. Aku langsung ya, Bu. Keburu telat."
    i "Iya, sana buru!"
    i "Hati-hati ya nak."

    scene gerbangsekolah with fade
    "07.07 gerbang sekolah."
    show Bima at left
    show Arya at right
    r "Waduh, mampus, kita telat."
    k "Wah iya anjing."
    show satpam at center
    s "Kenapa telat? Tunggu di luar dulu."
    k "Tapi Pak…"
    s "Ga ada tapi-tapi. Tunggu guru BK ke sini."
    hide satpam
    r "Yah, dihukum deh kita."
    k "Iya kak, gw minta maaf ya jadi bawa lu di sini."
    r "Dah gapapa. Udah makanan sehari-sehari ngadep guru BK."
    scene sekolah_sore with fade
    "16.36, 9 September 1999."
    show Bima at left 
    show Arya at right
    k "Wah akhirnya kelar juga sekolah hari ini."
    r "Iya, hectic banget hari ini sampe ngebut-ngebut di jalan."
    k "Heeh. Sampe harus kena hukuman karena telat, hahahaha."
    r "Hahahaha. Lu harus tau rasanya dihukum biar ga jadi siswa rajin mulu."
    k "Yok lah pulang. Capek."
    jump nemudompet

label nemudompet:
    # Show the wallet on the road
    scene jalan with fade
    show Bima at left 
    show Arya at right
    "Baru jalan bentar..."
    #"[Tunjukin ada dompet di jalan]"

    r "Eh apa itu?"
    k "Dompet?"
    r "Wah, lumayan. Rezeki nggak kemana."
    k "Eh, jangan ngaco lu. Itu punya orang."
    r "Yaelah, gini doang mah. Lumayan loh, hari gini dapet 23.000."

    # Present moral choice
    menu:
        "Biarkan Arya mengambil dompet":
            jump haram

        "Kembalikan dompet ke pemiliknya":
            jump moral

label haram:
    k "Tetep aja, Arya. Itu duit haram."
    r "Alah, Bim. Gausah ngomongin halal haram deh."
    # Add consequences for choosing this path
    "Bima merasa tidak nyaman dengan keputusan Arya, tapi memilih untuk diam."
    jump aaa

label moral:
    k "Nggak boleh, Arya. Ini sama aja nyuri."
    r "Mana ada, Bim. Duit hilang berarti udah bukan punya pemilik."
    k "Ya tetep aja. Kalau kita kehilangan dompet, pasti pengen yang nemu balikin, kan?"
    r "Hah, dasar lu terlalu lurus aja, Bim."
    "Arya mengalah dan setuju untuk mencari pemilik dompet."
    jump aaa


label aaa:
    # Scene starts with Arya and Bima talking
    scene jalan with fade
    r "Jaman gini hidup itu keras. Kita harus bisa bertahan dengan cara apapun."
    k "Tapi bukan berarti harus merugikan orang lain, Arya!"
    r "Bim, lu jangan sok idealis mulu deh. Realita hidup itu kayak gini."
    k "Tetep aja ini salah, Arya!"
    r "Bodo amat lah, apa urusan lu? Bukan duit lu juga!" # (ngotot)
    k "Ayah sama Ibu ga pernah ngajarin kayak gini, Arya!"
    r "Eh, lu tau apa soal Ayah sama Ibu? Gw yang lahir duluan, Bim!"
    k "…" # (kehabisan kata-kata untuk membujuk kakaknya) [ekspresi termenung agak kecewa]
    k "Lu pulang duluan aja, gw nyusul."
    r "Yeuu, bete lu?"
    k "Serah lu deh, gw pengen kencing." # (ketus)
    r "Yaelah, yauda sana. Gw tungguin."
    k "Oke."

    # Time skip to their return home
    scene rumah_sore with fade
    "16.42, 9 September 1999"

    a "Eehh, jagoan-jagoan Ayah udah pulang!"
    r "Hehe, iya Yah, udah kelar sekolahnya."
    k "…" # (masih speechless kelakuan Arya) [senyum aja]
    i "Tadi gimana sekolahnya? Sampe bolak-balik gitu kalian?"
    a "Tadi kalian balik pulang?"

    i "Iya Yah, tadi baru banget Ayah berangkat kerja mereka balik pulang."
    k "Iya Yah, hehe, laporan Bima ketinggalan."
    a "Wah kacau, lain kali bener-bener dicek ya, jangan sampe ada yang lupa."
    r "Walah, Ayah aja lupa ngembaliin kalkulator sampe tantrum tuh si anak."
    k "Diem ya lu."
    a "HAHAHAHA, namanya juga udah bapak-bapak pasti lupaan."

    # Transition to the birthday moment
    i "Ngomong-ngomong, Bima, Arya, kalian inget nggak sekarang hari apa?"
    r "Hari Kamis?"
    k "OH, HARI ULANG TAHUN AYAH!"
    r "OIYAA!"
    a "HAHAHAHA. Ternyata masih ada yang inget ulang tahun Ayah."
    i "Kita harus ucapin apa, nakk? Satu, dua, tiga…"
    "Selamat ulang tahun Ayahhh!"
    a "Hahahaha, terima kasih yaa nak, Ibu."
    i "Jadiii… buat ngerayain ulang tahun Ayah, kita mau makan-makan dimana inii??"
    a "Hahahaha, sok kalian tentukan. Ayah ngikut dan tinggal bayar aja. HAHAHAHA."

    menu:
        "Sate":
            jump sate

        "Sop Buntut":
            jump sopbuntut
    
label sate:
    k "Sate kayanya menarik deh Yah, udah lama ngga makan sate."
    r "Ah, tapi lagi pengen makanan berkuah. Sop buntut kali ya?"
    i "Hmmm, sop buntut oke sih."

    jump makanmakan

label sopbuntut:
    k "Sop buntut kayanya menarik deh Yah, udah lama ngga makan sop buntut."
    r "Ah, tapi lagi pengen makanan bakaran. Sate kali ya?"
    i "Hmmm, sate oke sih."

    jump makanmakan

label makanmakan:
    i "Yaudah yuk kita siap-siap dan beberes. Habis maghrib kita berangkat yaa!"
    k "Mau makan di mana kita, Bu?"
    i "Sarinah oke ngga, Ayah?"
    a "Yaaa… kalau Ayah sih oke aja asal belanjanya ngga sampai 1 juta. HAHAHAHAHA!"
    r "Ya kalau ada 1 juta mah mending buat beli TV lagi, taruh di kamar Arya."
    a "Yeuuu, enak aja kamu!"
    a "Udah, sana siap-siap."

    # Time skip to evening preparation
    "18.09, 9 September 1999, 162 menit sebelum dentuman"
    scene kamartidur with fade
    k "Kak, lu udah siap belom?"
    r "Lihat aja gw, udah cakep gini."
    k "Kali aja lu mau ngapain lagi kek."
    r "Ah, gw ngga seribet itu orangnya."
    k "Oh iya, ngomong-ngomong soal dompet tadi..."
    r "Udah lah, Bim, mau dipanjangin sampai kapan lagi?"
    k "Nggak gitu, gw mau ngomong sesuatu sama lu."
    r "Apa?"

    menu:
        "Reemburse dompet":
            jump reemburse

        "Arya salah":
            jump aryasalah

label reemburse:
    k "Sebenernya waktu gw tadi minta nyusul karena kencing, gw ketemu Ujang."
    r "Terus?"
    k "Dompet itu, ternyata dompet Ujang."
    r "Ujang anak bahasa itu?"
    k "Iya."
    r "Ngaku-ngaku aja kali. Orang di dompetnya gaada kartu identitas sama sekali."
    k "Tapi dia nyebutin ciri-ciri dompet yang sama persis, dan nominalnya sama persis yang lu ambil."
    r "Yaelah, terus gimana?"
    k "Dia bilang dia lagi butuh banget duitnya buat makan seminggu."
    k "Karena itu duit lu ambil, jadinya gw ga enak ke Ujang."
    r "Ngapain pake ga enak, yaudah lah itu kesialan Ujang."
    k "Mana bisa gitu Arya. Akhirnya duit Ujang gw ganti. Gw bilang gw yang nemu dompetnya."
    r "Lah, tapi kan dompetnya masih ada di gw. Gimana lu ngembaliinnya?"
    k "Iya, gw bilang dompetnya masih lu amanin, jadi duitnya dulu yang gw kasih ke dia."
    r "Berarti ini dompet mau dibalikin besok?"
    k "Iya. Sekalian gw sekarang mau minta duit gw lu balikin."
    r "Heuuuhh. Percuma tadi debat panjang lebar, ujung-ujungnya ga jadi rezeki."

    jump ibutibatiba

label aryasalah:
    k "…"
    k "(Bingung mau gimana ngomongnya.)"
    r "Kenapa, Bim?"
    k "Gapapa, ga jadi Arya."
    r "Hufft."
    r "(Menghela nafas.)"
    r "Gini Bim, dunia ini ngga akan pernah adil Bim."
    r "Lu lihat aja para pejabat di Senayan sana."
    r "Lu lihat aja tahun kemarin gimana bobroknya presiden kita?"
    r "Kesengsaraan rakyat ga pernah mereka dengar, Bim!"
    r "Dunia ini ga akan pernah adil, Bim."
    r "Kehidupan ini ibarat bertahan di tengah hutan rimba."
    r "Lu harus bisa survive gimanapun caranya."
    r "Lihat tuh Ayah. Ayah jadi polisi harus jual sawah kakek dulu, Bim!"
    k "Tapi…"
    r "Tapi apa, Bim?"
    k "Lihat Pak Habibie, Arya. Rupiah kita sekarang menguat banget."
    k "Pak Habibie, Arya! Dia mau berjuang untuk masyarakat."
    k "Kalo ibarat lu kehidupan ini adalah hutan belantara, beliau masih bisa sukses tanpa harus merugikan orang lain, Arya!"
    r "Pak Habibie itu punya otak, Bim! Ga kaya aku yang goblok ini."
    r "Bagi kami yang goblok ini akan terus-terusan dibodohi dan ga akan bisa maju."
    r "Cara satu-satunya bagi kami bisa bertahan hidup ya dengan mengusahakan segala cara!"

    jump ibutibatiba


# label ibutibatiba:
label ibutibatiba:
    i "Eeeh, ini ada apa ya ribut-ribut?" #(berbicara dari luar kamar)
    i "Udah siap belom kalian?"
    r "Udah, Bu." #(membalas dari dalam kamar)
    r "Nanti kita bahas lagi." 
    "(berbisik Arya)"
    r "Gw gamau kesenangan ulang tahun Ayah harus diganggu dengan masalah dompet."
    k "Ya."

    scene black with fade
    pause 0.5

    scene kamar_dengan_pintu_terbuka with fade
    k "Kita udah siap nih, Bu."
    i "Widihh, udah cakep-cakep nih."
    r "Ayah mana, Bu?"
    i "Ayah masih di kamar mandi, lagi mual-mual."
    
    a "Haloo, udah siap?" #(Ayah keluar dari kamar mandi)
    k "Ayah sakit? Ayah kalo ga enak badan ngga usah dipaksain makan di luar, yah."
    r "Iya, kita masih bisa ngerayain di rumah kok, Yah."
    i "Tuh kan, Ibu bilang apa tadi."
    a "Gapapa kok, Ayah lagi merasa ga enak aja perasaannya, ga tau kenapa ya."
    a "Apa mungkin Ayah ngga rela kehilangan uang sampe 1 juta? Hahahahaha."
    i "Ih Ayah, Ayah beneran gapapa?"
    a "Iya gapapa. Ayah sehat kok. Yok berangkat habis ini."
    k "Syukurlah. Yaudah, ayok kita berangkat."
    r "Yokkk!"
    a "Bima, kamu yang bawa mobilnya ya."
    k "Eh, kok aku, Yah? Kenapa ngga Kak Arya aja?"
    r "Udah lu aja, udah punya SIM juga."
    i "Ya sekali-kali lah, Nak. Mumpung udah ada SIM."
    i "Kasihan kakak kamu yang nyetir mulu."
    a "Hahahaha, Ayah juga pengen tau gimana skill kamu nyetir."
    k "Baikkk, siap komandan!"

    scene jalanan_malam with fade
    k "Oke, ayo kita mulai jalan. Doain aja semuanya lancar!"
    
    jump minigame_nyetir

label minigame_nyetir:
    menu:
        '(gagal minigame (lama sampai))':
            jump lamatpsampe
        '(minigame berhasil)':
            jump sampei
    # Setup for the driving mini-game
    # $ driving_speed = 0
    # $ distance_covered = 0
    # $ target_distance = 100  # Distance to complete the mini-game

    # # Start the mini-game
    # while distance_covered < target_distance:
    #     menu:
    #         "Gas (Percepat mobil)":
    #             $ driving_speed += 10
    #             $ distance_covered += driving_speed // 10
    #             "Bima menginjak pedal gas, kecepatannya sekarang [driving_speed] km/h."
    #         "Rem (Kurangi kecepatan)":
    #             $ driving_speed = max(0, driving_speed - 10)
    #             "Bima menginjak rem, kecepatannya sekarang [driving_speed] km/h."
    #         "Jaga kecepatan (Tetap stabil)":
    #             $ distance_covered += driving_speed // 15
    #             "Bima menjaga kecepatan stabil di [driving_speed] km/h."

    #     # Random events to make the mini-game challenging
    #     if renpy.random.randint(0, 10) < 3:
    #         "Ada lubang di jalan! Bima harus menghindar."
    #         menu:
    #             "Hindari ke kiri!":
    #                 $ driving_speed = max(0, driving_speed - 15)
    #                 "Berhasil menghindar, tapi kecepatannya berkurang!"
    #             "Hindari ke kanan!":
    #                 $ driving_speed = max(0, driving_speed - 15)
    #                 "Berhasil menghindar, tapi kecepatannya berkurang!"
    #             "Tidak hindar!":
    #                 $ distance_covered -= 10
    #                 "Mobil sedikit oleng! Jarak yang ditempuh berkurang."

    # "Bima berhasil membawa mobil sampai tujuan dengan selamat!"


label sampei:
    k "Alhamdulillah, udah sampe."

    # a sound of the car stopping.
    scene sarinah_dari_depan with fade
    i "Ayo nak, keburu tutup Sarinah-nya."
    a "Ngghroookk..." 
    #(Ayah ketiduran)

    jump akhirsampe

label lamatpsampe:
    # If the number of turns made is more than a certain threshold, show this part
    # if turns > 3:  # Assumes 'turns' is tracked during the mini-game
    k "Ini beloknya kemana ya?"
    r "Tau jalan ga sih lu?"
    i "Ayo nak, keburu tutup Sarinah-nya."
    a "Ngghroookk..." 
        #(Ayah ketiduran)
        
        # Achievement Unlocked when you get lost
        # $ achievement_unlocked = "Buta Map"
    jump akhirsampe

define staff = Character('staff', color="#423d3d")
define x = Character('Pencuri', color="#423d3d")

label akhirsampe:
    i "Akhirnya, udah sampe juga."
    r "Fyuhhh, let’s go makannnn."

    # Transition to the restaurant scene
    scene restoran_1 with fade
    staff "Selamat datang. Ini untuk buku menunya. Pesanan langsung ditulis di sini ya…"
    
    k "Ayah, Ibu, Kak, mau pesen apa? Bima aja yang nulisin."
    # Start the mini-game to order food here.
    #call mini_game_order_food
    
    staff "Baik, mohon ditunggu sebentar ya..."
    i "Senengnyaa, jarang-jarang kita makan di restoran."
    a "Ya ngapain toh repot-repot ke restoran kalau masakan ibu itu yang terenak di dunia."
    i "Alah-alah masa sih ayah?"
    a "Loh iya dong, Arya, Bima, 20 tahun nikah sama ibu, ga pernah sekalipun ayah ngga habisin masakan ibu."
    r "Hahahaha, keliatan banget sih emang dari perutnya."
    a "HAHAHAHA!"
    k "Hahaha, ayah mah emang di mana-mana makannya banyak."
    i "Ih, percaya ga sih kalian, dulu ayah waktu masih bujang tuh badannya bagus tau."
    i "Ganteng dan gagah."
    i "Kalau sekarang, ih, gantengnya emang masih iya, tapi gagahnya berubah jadi gajah."
    a "HAHAHA, ah ibu ini bisa aja."
    
    # Staff brings the food.
    staff "Silakan… (menyajikan makanan)"
    staff "Untuk pesanannya sudah lengkap ya?"
    k "Mmmmm, udah kak, terima kasih ya…"
    staff "Terima kasih kembali."
    
    # Transition to eating and wrapping up at the restaurant.
    scene restoran_2 with fade
    a "Alhamdulillah kenyang."
    i "Alhamdulillah, seneng banget deh yah, makasih yaaa."
    k "Besok traktir sop buntut dong yah."
    a "Wah tunggu ayah gajian lagi ya hahahaha."
    i "Bima, Arya, minta tolong bayarin ke kasir ya, ini bawa dompet ibu."
    r "Siap."
    
    # At the cashier.
    scene kasir with fade
    k "Meja nomor 5, totalnya berapa kak?"
    staff "Totalnya jadi Rp120.000."
    k "Okee, ini kak."
    "Bima memberikan uang"
    staff "Uangnya pas ya? Terima kasih."
    k "Sama-sama kak."
    r "Mahal amat ya sampe abis segitu."
    k "Yaelah bro, kita makan di Sarinah, beli sate berapa banyak juga tadi?"
    r "Yaaa, iya sihh."
    
    # The tension builds up as they notice something strange outside.
    scene luar_restoran with fade
    k "Eh Arya, lihat deh toko baju sebrang."
    r "Iya? Kenapa?"
    k "Lihat orang baju item itu? Dia lagi nyolong sepatu ga sih?"
    k "TUH TUH TUH DIA UMPETIN DI TAS DIA SI SEPATUNYA!"
    r "EH IYA!"
    
    # Arya tries to calm down Bima.
    k "Wah gw harus bilang ke ayah."
    r "Eh, tunggu Bim!"
    k "Kenapa kak?"
    r "Udah biarin aja, ga usah ikut campur urusan orang."
    k "Urusan orang? Maksud lu?"
    r "Udah jangan ikut campur, biarin, itu urusan yang punya toko."
    k "Hahhh?? Lu udah gila ya? Itu kriminalitas anjing, sempet-sempetnya lu mikir gitu."
    r "Ya terus kenapa? Apa untungnya buat kita ngurusin dia?!"
    k "Lu beneran gila ya? Ayah kita polisi loh!"
    k "Ini udah jadi tanggung jawab ayah."
    r "Yaudah, biarin ngapa sih, ngerepotin aja tau ga sih."
    k "Gw gamau tau, gw harus kasih tau ayah."
    
    # Bima rushes to tell Ayah about the situation.
    scene kasir with fade
    k "YAHH! Ada pencuri yahh di toko seberang!!"
    a "Hmmmh? Gimana gimana?"
    k "Toko baju seberang yah, ada orang nyolong sepatu, Bima lihat dengan mata kepala sendiri."
    a "Bener Arya?"
    r "Iya yah."
    a "Wah ga bener nih, ayok kita samperin."
    i "Dek, emang ga ada satpamnya yang jaga? Ulang tahun ayah masa harus tetep kerja sih?"
    a "Udah lah bu, ini tanggung jawab ayah."
    a "Yang mana orangnya?"
    k "Itu yah, yang baju hitam."
    a "Mana? Ohhh, yang bawa tas itu?"

    # Transition to confrontation with the thief.
    scene luar_restoran_confrontation with fade
    a "Permisi mas, saya Kompol Susilo, Kapolsek Matraman." #
    #(showing badge)
    a "Saya menerima laporan kecurigaan tindakan pencurian yang melibatkan mas sebagai tersangka."
    a "Untuk itu akan saya periksa mas untuk meluruskan apakah dugaan benar atau salah."
    x "Wah, salam kenal pak Susilo. Izin meluruskan, saya tidak mencuri barang apapun di toko ini."
    a "Maka biarkan saya memeriksa agar dugaan bisa dibantah jika memang tidak ada bukti."
    staff "Bapak polisi?"
    a "Iya, ada yang bisa saya bantu?"
    staff "Kami kehilangan satu pasang sepatu di rak pajangan A9 pak, sepertinya mas ini adalah pelakunya."
    a "Mas… menanggapi ini, saya mohon mas untuk kooperatif."
    # Tension builds as X pulls a weapon.
    x "..." 
    #(panicked look)
    "Pencuri mengeluarkan pistol dari sabuknya."
    "DORR!"
    # *DENTUMAN GUNSHOT*

    # Transition to chaos after the gunshot.
    # scene glitch_transition with glitch
    r "AYAHHHHH!"
    r "BIMAA!"
    r "BIMAA!"
    r "BIMAA, LIHAT YANG KAMU PERBUAT!!!"
    
    # Glitching effect to show the impact of the incident.
    # This leads into the next part of the story.

    return