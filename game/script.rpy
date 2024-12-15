
# ------------------------------------- X-SMA -------------------------------------
# DEFINE CHARACTERS
define k = Character("Brama", image="chara/sma_kamil/k", color="#472301")
define r = Character("Arya", color="#a8652e")
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
image Brama:
    "chara/sma_kamil/k netral.png"
    zoom 0.5

image Brama Marah:
    "chara/sma_kamil/k angry.png"
    zoom 0.5
image Brama Lega : 
    "chara/sma_kamil/k lega.png"
    zoom 0.5
image Brama Bingung :
    "chara/sma_kamil/k conf.png"
    zoom 0.5
image Brama Cemas :
    "chara/sma_kamil/k conf.png"
    zoom 0.5
image Brama Bahagia :
    "chara/sma_kamil/k happy.png"
    zoom 0.5
image Brama Kosong :
    "chara/sma_kamil/k kosong.png"
    zoom 0.5
image Brama Malu : 
    "chara/sma_kamil/k malu.png"
    zoom 0.5

image Arya :
    "chara/sma_arya/NEUTRAL.png"
    zoom 1.45
image Arya Marah:
    "chara/sma_arya/RAGE.png"
    zoom 1.45
image Arya Lega : 
    "chara/sma_arya/RELIEVED.png"
    zoom 1.45
image Arya Bingung :
    "chara/sma_arya/CONFUSED.png"
    zoom 1.45
image Arya Bahagia :
    "chara/sma_arya/HAPPY SMILE.png"
    zoom 1.45
image Arya Ketawa :
    "chara/sma_arya/HAPPY LAUGH.png"
    zoom 1.45
image Arya Menangis :
    "chara/sma_arya/CRYING.png"
    zoom 1.45
image Arya Kesal : 
    "chara/sma_arya/ANNOYED.png"
    zoom 1.45
image Arya Kesala : 
    "chara/sma_arya/ANNOYED NO EMOJI.png"
    zoom 1.45
image Arya Kecewa : 
    "chara/sma_arya/DISSAPOINTED.png"
    zoom 1.45
image Arya Kaget : 
    "chara/sma_arya/SHOCKED.png"
    zoom 1.45
image Arya Serius : 
    "chara/sma_arya/SERIOUS.png"
    zoom 1.45

image ibu = "chara/ibu.png" 
image ayah = "chara/ayah.png"

# buat brama
define cpos = Position(xalign=0.5, yalign=0)
define rpos = Position(xalign=0.9, yalign=0)
define lpos = Position(xalign=0,yalign=0)

# buat arya
define acpos = Position(xalign=0.5, yalign=0)
define arpos = Position(xalign=1.25, yalign=0)
define alpos = Position(xalign=0,yalign=0)

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
    show Brama Kosong at cpos with dissolve:
        zoom 2.5
    "DORR!"
    "(dentuman pistol)"
    show Brama Bingung at cpos:
        zoom 2.5
    k "...."
   
    scene kamartidur
    with dissolve

    "(seketika Brama bangun dari tidur bersamaan dengan suara pistol)"
    play sound "audio/nafasberat.mp3"
    "(nafas berat terengah-engah)"

    show Arya Serius at acpos

    with fade
    r "Mimpi buruk lagi ya lu?"

    menu:
        "Iya kak..":
            jump y1
        ".....":
            jump t1
    

label y1:
    show Brama at lpos
    show Arya at arpos

    show Brama Malu at lpos
    k "iya kak..."
    show Arya Bingung at arpos
    r "terus-terusan mimpi 
        buruk? kenapa sih?"
    show Brama Bahagia at lpos
    k 'gapapa kok'
    show Arya Lega at arpos
    r ' lu kalo ada apa-apa
        cerita aja ke gw. 
        gini-gini gw kakak lu'
    show Arya Bahagia at arpos
    k 'iya, makasih ya'
    '(Brama berterimakasih)'

    jump m1

label t1:
    show Brama at lpos
    show Arya at arpos
    show Brama Bingung at lpos
    k '...'
    show Arya Kesal at arpos
    r 'yeuu malah bengong'
    show Arya Lega at arpos
    r ' lu kalo ada apa-apa
        cerita aja ke gw. 
        gini-gini gw kakak lu'
    show Arya at arpos
    show Brama Kosong 
    k '...'
    hide Arya
    show Brama Kosong at cpos:
        zoom 2
    '(tatapan kosong menyelimuti wajah Brama)'

    jump m1

label m1:
    hide Brama
    hide Arya

    i 'naaaak, Brama, Arya, ayo sarapan'
    a 'ayo turun nak. Jangan sampe telat sekolah'
    '(suara ayah ibu terdengar dari luar kamar)'

    show Brama Bingung at lpos
    k 'EH IYA SEKARANG JAM BERAPA?'
    '(panik karena bangun kesiangan)'
    show Arya Bahagia at arpos
    r 'slow aja masih 5.30'
    '(Arya bersantai karena sudah siap-siap duluan)'
    hide Arya

    show Arya at arpos
    #[Arya sudah rapi dengan pakaian dan perlengkapannya]
    show Brama Marah at lpos
    k 'MANA BISA GITU anjing, SEKOLAH KITA JAUH'
    show Arya Ketawa at arpos
    r 'wkwkwk'
    #[Arya tertawa kecil]
    show Brama at lpos
    r 'dah sana buruan siap-siap, gw tunggu sambil sarapan'
    hide Arya
    show Brama Bingung at lpos
    k 'oke hari ini jadwal kita olahraga, matematika, sama biologi'
    '(Brama sambil melihat selebaran jadwal yang nempel di dinding)'
    #[jadwal pelajaran sekolah SMA Cendekia Maju di selebaran kertas]
    k 'hmmmm berarti gw harus bawa buku, baju ganti, sama
            kalkulator'
    k 'pertama, buku yang harus gw bawa berarti buku olahraga, buku 
            matematika, buku biologi'
    
    #(mini game milih buku di rak)
    jump minibuku

label minibuku:
    scene rakbuku
    show Brama at rpos
    $ correct_books = ["Buku Olahraga", "Buku Matematika", "Buku Biologi"]  # Correct books
    $ chosen_books = []  # Store player's choices

    "Brama mulai memilih buku yang harus dibawa dari rak buku."

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
                "Brama mengambil Buku Olahraga."

            "Buku Matematika" if "Buku Matematika" in options:
                $ chosen_books.append("Buku Matematika")
                "Brama mengambil Buku Matematika."

            "Buku Biologi" if "Buku Biologi" in options:
                $ chosen_books.append("Buku Biologi")
                "Brama mengambil Buku Biologi."

            "Buku Sejarah" if "Buku Sejarah" in options:
                $ chosen_books.append("Buku Sejarah")
                "Brama mengambil Buku Sejarah."

            "Buku Fisika" if "Buku Fisika" in options:
                $ chosen_books.append("Buku Fisika")
                "Brama mengambil Buku Fisika."

    # Check if the player's choices are correct
    $ correct_count = sum(1 for book in chosen_books if book in correct_books)

    if correct_count == 3:
        "Brama: Hmmm... Semua buku yang gw pilih udah bener."
        jump ruangmakan
    else:
        "Brama: Aduh, kayaknya ada buku yang salah deh."
        $ chosen_books = []
        jump minibuku
            
#minigame pilih baju blm
#minigame pilih kalkulator


# Label ruangmakan
label ruangmakan:
    scene ruangmakan with fade
    show Brama Marah at lpos
    show Arya at arpos

    k "YANTOO!!!"
    show Arya Kaget at arpos
    r "APAA?!" 
    k "Kalkulator gw mana heh?"
    show Arya Kesal at arpos
    r "Apasih? Lu nuduh gw?"
    k "Ya siapa lagi weh, lu doang yang sering make barang gw."
    r "Sumpah demi Allah, gw kaga tau."
    k "Eh, gausa bawa-bawa nama Allah ya kalo bohong."
    r "Apaan sih lu ga jel..."

    # Ibu interjects
    show Brama at lpos
    show Arya at arpos
    i "Aduhh kalian ini gaada kerjaan yang lebih baik kah selain berantem terus?"
    i "Ibu berani sumpah tembok di rumah ini lebih sering dengerin kalian berantem daripada dengerin omongan baik."
    a "Udah nak, jangan berantem lagi."
    i "Marahin pak anaknya!"
    a "Brama, kalkulator kamu Ayah yang pinjam semalam waktu kamu tidur."
    a "Maaf ya nak, Ayah lupa ngembaliin kalkulator kamu ke tempatnya."
    show Brama Malu at lpos
    k "Oalah, Ayah toh yang make. Hehehe."
    show Arya Kesal at arpos
    r "Oalah, Ayah toh yang make. nyenyeneye"
    show Brama Marah at lpos
    k "Ih bacot lu!"
    r "Nye nye nye, lu yang bacot."
    i "Heh udah!"
    show Arya Bahagia at arpos
    show Brama at lpos
    i "Sana kalian cepat siap-siap sekolah!"
    

    # Time skip
    scene black with fade
    pause 1
    "06.00 WIB, 9 September 1999"
    scene depanrumah with fade
    show Arya at arpos
    show Brama Bingung at lpos
    k "Arya, lu udah siap belom?"
    show Arya Ketawa at arpos
    r "Udah, yok berangkat."
    show Arya at arpos
    show Brama Bahagia at lpos
    k "Buuu, Yah. Kita berangkat yaa."
    show Brama at lpos
    a "Ya nak, hati-hati di jalan ya."
    i "Barang gaada yang ketinggalan?"
    show Arya Ketawa at arpos
    r "Aku udah kebawa semua sih harusnya."
    show Arya at arpos
    show Brama Bahagia at lpos
    k "Amannn."
    show Brama Bingung at lpos
    show Arya Ketawa at arpos
    r "Mau lu atau gw yang bawa motor?" 

    menu:
        "gw aja gapapa, ntar baliknya lu":
            jump motorbima
        "lu aja yang bawa":
            jump motorarya

label motorbima:
    show Brama Bahagia at lpos
    k "Gw aja gapapa, ntar baliknya lu."
    show Brama at lpos
    r "Oke deh, jangan bunuh gw di jalan tapi."
    show Arya at arpos
    show Brama Bahagia at lpos
    k "Mana ada, gw adalah the best rider on the world!"
    show Arya Kesala at arpos
    r "The best bacot kali lu."
    jump gerbangsekolah

label motorarya:
    show Brama Lega at lpos
    k "Lu aja yang bawa."
    show Brama at lpos
    r "Eh nyuruh-nyuruh."
    r "Kemarin udah gw ya njing yang nyetir."
    show Brama Marah at lpos
    k "Ya terus lu ngapain nawarin kocak?"
    show Brama at lpos
    r "Formalitas aja WKWKWKWK."
    show Brama Marah at lpos
    k "Yeuuu, yaudah mana kuncinya."
    jump gerbangsekolah

label gerbangsekolah:
    scene gerbangsekolah with fade
    show Brama at lpos
    show Arya at arpos
    "06.30 depan gerbang sekolah, 9 September 1999"

    show Brama Marah at lpos
    k "ANJINGGG!"
    r "Kenapaa?" 
    #[ekspresi muak kyk kenapa lagi ini orang]"
    k "Biologi! LAPORAN BIOLOGI GW!"
    r "…" 
    #[ekspresi menghela nafas]
    r "Terus gimana?"
    show Brama Malu at lpos
    k "Harus dibawa anjing. Lu tau kan Bu Titiek orangnya killer."
    r "…"
    show Brama at lpos
    k "Gw harus balik pulang ngambil laporannya."
    r "Lu serius?"
    r "Gw jadi lu mending dihukum. Males anjing bolak-balik."
    k "Ga bisa gitu, gw harus balik."
    r "Lu becanda ya anjing, ini udah jam berapa?"
    show Brama Bahagia at lpos
    k "Bisa. Gw bisa ngebut."
    r "Gila lu ya? Lu lupa 6 bulan lalu lu kecelakaan karena ngebut?"
    show Brama Lega at lpos
    k "Yaelah itu gw cuman apes."
    r "Bukan apes. Lu emang ga bisa bawa motor ngebut, Bram."
    k "Yauda lah mau gimana lagi tapi ini laporan gw?"
    r "Haishhh."
    show Brama at lpos
    r "Udah sini aja, gw yang nyetir."
    r "Lu ga becus bawa motor ngebut."
    show Brama Malu at lpos
    k "Eh, jangan. Lu masuk aja sana."
    show Brama Lega at lpos
    k "Ini kesalahan gw, biar gw yang tanggung jawab."
    r "Lu goblok ya? Tanggung jawab ya tanggung jawab, tapi kecelakaan tetep mematikan anjing."
    show Brama Marah at lpos
    k "Ini tanggung jawab gw. Lu ga harus ikut terseret, Arya!"
    r "Bacot lu. Ga usah sok idealis. Gw gamau lu kenapa-kenapa."
    show Brama Marah at lpos
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
    show Brama Lega at lpos
    show Arya Bingung at arpos
    r "Wah gila, buruan ambil laporan lu."
    show Brama Malu at lpos
    k "Iya, tunggu sini bentar ya."
    "Brama masuk rumah."

    scene ruangtamu with fade
    show Brama Malu at rpos
    i "Dek? Kenapa balik dek?"
    show Brama Bingung at rpos
    k "Laporan aku ketinggalan, Bu."
    show Ibu at cpos
    i "Kan kan. Terus kakak kamu gimana?"
    show Brama Cemas at rpos
    k "Itu nunggu di depan. Aku langsung ya, Bu. Keburu telat."
    i "Iya, sana buru!"
    i "Hati-hati ya nak."

    scene gerbangsekolah with fade
    "06.59 gerbang sekolah."
    show Brama Lega at lpos
    show Arya Lega at arpos
    r "Anjing, hampir aja kita telat."
    show Brama Bahagia at lpos
    k "Wah iya anjing, untung masih ada waktu."
    show Brama Malu at lpos
    k "Makasih ya, Arya."
    show Arya Bahagia at arpos
    r "Dah, buruan masuk. Lain kali traktir gw bakso."
    show Brama Bahagia at lpos
    k "Iya iya, ntar jam istirahat."
    jump nemudompet

define s = Character('Satpam', color="#423d3d")

label nabrak:
    scene depanrumah with fade
    show Brama Cemas at lpos
    show Arya Kesal at arpos
    "06.52 sampai rumah."

    r "Wah gila, buruan ambil, kita udah telat."
    show Brama Malu at lpos
    k "Iya, tunggu sini bentar ya."
    "Brama masuk rumah."

    scene ruangtamu with fade
    show Brama Bingung at rpos
    i "Dek? Kenapa balik dek?"
    show Brama Malu at rpos
    k "Laporan aku ketinggalan, Bu."
    show Ibu at cpos
    i "Kan kan. Terus kakak kamu gimana?"
    show Brama Kosong at rpos
    k "Itu nunggu di depan. Aku langsung ya, Bu. Keburu telat."
    i "Iya, sana buru!"
    i "Hati-hati ya nak."

    scene gerbangsekolah with fade
    "07.07 gerbang sekolah."
    show Brama Cemas at lpos
    show Arya Kesala at arpos
    r "Waduh, mampus, kita telat."
    show Brama Kosong at lpos
    k "Wah iya anjing."
    show satpam at cpos
    s "Kenapa telat? Tunggu di luar dulu."
    show Brama Malu at lpos
    k "Tapi Pak…"
    s "Ga ada tapi-tapi. Tunggu guru BK ke sini."
    hide satpam
    show Arya Kesal at arpos
    r "Yah, dihukum deh kita."
    show Brama Kosong at lpos
    k "Iya kak, gw minta maaf ya jadi bawa lu di sini."
    show Arya Bahagia at arpos
    r "Dah gapapa. Udah makanan sehari-sehari ngadep guru BK."
    scene sekolah_sore with fade
    "16.36, 9 September 1999."
    show Brama Lega at lpos 
    show Arya Bahagia at arpos
    k "Wah akhirnya kelar juga sekolah hari ini."
    r "Iya, hectic banget hari ini sampe ngebut-ngebut di jalan."
    show Brama Bahagia at lpos
    k "Heeh. Sampe harus kena hukuman karena telat, hahahaha."
    show Arya Ketawa at arpos
    r "Hahahaha. Lu harus tau rasanya dihukum biar ga jadi siswa rajin mulu."
    show Brama Lega at lpos
    k "Yok lah pulang. Capek."
    jump nemudompet

label nemudompet:
    # Show the wallet on the road
    scene jalan with fade
    show Brama Bingung at lpos 
    show Arya Bingung at arpos
    "Baru jalan bentar..."
    #"[Tunjukin ada dompet di jalan]"

    show Arya Bingung at arpos
    r "Eh apa itu?"
    show Brama Bingung at lpos
    k "Dompet?"
    show Arya Lega at arpos
    r "Wah, lumayan. Rezeki nggak kemana."
    show Brama Marah at lpos
    k "Eh, jangan ngaco lu. Itu punya orang."
    show Arya Kesal at arpos
    r "Yaelah, gini doang mah. Lumayan loh, hari gini dapet 23.000."

    # Present moral choice
    menu:
        "Biarkan Arya mengambil dompet":
            jump haram

        "Kembalikan dompet ke pemiliknya":
            jump moral

label haram:
    show Brama Cemas at lpos
    k "Tetep aja, Arya. Itu duit haram."
    show Arya Kesal at arpos
    r "Alah, Bram. Gausah ngomongin halal haram deh."
    # Add consequences for choosing this path
    "Brama merasa tidak nyaman dengan keputusan Arya, tapi memilih untuk diam."
    jump aaa

label moral:
    show Brama Marah at lpos
    k "Nggak boleh, Arya. Ini sama aja nyuri."
    show Arya Kesal at arpos
    r "Mana ada, Bram. Duit hilang berarti udah bukan punya pemilik."
    show Brama Kosong at lpos
    k "Ya tetep aja. Kalau kita kehilangan dompet, pasti pengen yang nemu balikin, kan?"
    show Arya Bingung at arpos
    r "Hah, dasar lu terlalu lurus aja, Bram."
    "Arya mengalah dan setuju untuk mencari pemilik dompet."
    jump aaa

label aaa:
    # Scene starts with Arya and Brama talking
    scene jalan with fade
    show Arya Kesal at arpos
    r "Jaman gini hidup itu keras. Kita harus bisa bertahan dengan cara apapun."
    show Brama Marah at lpos
    k "Tapi bukan berarti harus merugikan orang lain, Arya!"
    show Arya Bingung at arpos
    r "Bram, lu jangan sok idealis mulu deh. Realita hidup itu kayak gini."
    show Brama at lpos
    k "Tetep aja ini salah, Arya!"
    show Arya Kesal at arpos
    r "Bodo amat lah, apa urusan lu? Bukan duit lu juga!"
    show Brama Marah at lpos
    k "Ayah sama Ibu ga pernah ngajarin kayak gini, Arya!"
    show Arya Kesala at arpos
    r "Eh, lu tau apa soal Ayah sama Ibu? Gw yang lahir duluan, Bram!"
    show Brama Kosong at lpos
    k "…" # (kehabisan kata-kata untuk membujuk kakaknya)
    show Brama Bingung at lpos
    k "Lu pulang duluan aja, gw nyusul."
    show Arya Bingung at arpos
    r "Yeuu, bete lu?"
    show Brama at lpos
    k "Serah lu deh, gw pengen kencing."
    show Arya Kesal at arpos
    r "Yaelah, yauda sana. Gw tungguin."
    show Brama at lpos
    k "Oke."

    # Time skip to their return home
    scene rumah_sore with fade
    show Arya at arpos
    show Brama at lpos
    "16.42, 9 September 1999"

    show Ayah Bahagia at cpos
    a "Eehh, jagoan-jagoan Ayah udah pulang!"
    show Arya Lega at arpos
    r "Hehe, iya Yah, udah kelar sekolahnya."
    show Brama Bingung at lpos
    k "…" # (masih speechless kelakuan Arya)
    show Ibu at rpos
    i "Tadi gimana sekolahnya? Sampe bolak-balik gitu kalian?"
    show Ayah Bingung at cpos
    a "Tadi kalian balik pulang?"

    show Ibu Senyum at rpos
    i "Iya Yah, tadi baru banget Ayah berangkat kerja mereka balik pulang."
    show Brama Malu at lpos
    k "Iya Yah, hehe, laporan Brama ketinggalan."
    show Ayah Bingung at cpos
    a "Wah kacau, lain kali bener-bener dicek ya, jangan sampe ada yang lupa."
    show Arya Lega at arpos
    r "Walah, Ayah aja lupa ngembaliin kalkulator sampe tantrum tuh si anak."
    show Brama Bingung at lpos
    k "Diem ya lu."
    show Ayah Tertawa at cpos
    a "HAHAHAHA, namanya juga udah bapak-bapak pasti lupaan."

    # Transition to the birthday moment
    show Ayah Bahagia at cpos
    i "Ngomong-ngomong, Brama, Arya, kalian inget nggak sekarang hari apa?"
    show Arya Bingung at arpos
    r "Hari Kamis?"
    show Brama Bahagia at lpos
    k "OH, HARI ULANG TAHUN AYAH!"
    show Arya Kaget at arpos
    r "OIYAA!"
    show Ayah Tertawa at cpos
    a "HAHAHAHA. Ternyata masih ada yang inget ulang tahun Ayah."
    show Ibu Senyum at rpos
    i "Kita harus ucapin apa, nakk? Satu, dua, tiga…"
    "Selamat ulang tahun Ayahhh!"
    show Ayah Tertawa at cpos
    a "Hahahaha, terima kasih yaa nak, Ibu."
    show Ibu Senyum at rpos
    i "Jadiii… buat ngerayain ulang tahun Ayah, kita mau makan-makan dimana inii??"
    show Ayah Tertawa at cpos
    a "Hahahaha, sok kalian tentukan. Ayah ngikut dan tinggal bayar aja. HAHAHAHA."

    menu:
        "Sate":
            jump sate

        "Sop Buntut":
            jump sopbuntut
    
label sate:
    show Brama Bahagia at lpos
    k "Sate kayanya menarik deh Yah, udah lama ngga makan sate."
    show Arya Kesal at arpos
    r "Ah, tapi lagi pengen makanan berkuah. Sop buntut kali ya?"
    show Ibu at rpos
    i "Hmmm, sop buntut oke sih."

    jump makanmakan

label sopbuntut:
    show Brama Bahagia at lpos
    k "Sop buntut kayanya menarik deh Yah, udah lama ngga makan sop buntut."
    show Arya Kesal at arpos
    r "Ah, tapi lagi pengen makanan bakaran. Sate kali ya?"
    show Ibu at rpos
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
    r "Udah lah, Bram, mau dipanjangin sampai kapan lagi?"
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
    r "Kenapa, Bram?"
    k "Gapapa, ga jadi Arya."
    r "Hufft."
    r "(Menghela nafas.)"
    r "Gini Bram, dunia ini ngga akan pernah adil Bram."
    r "Lu lihat aja para pejabat di Senayan sana."
    r "Lu lihat aja tahun kemarin gimana bobroknya presiden kita?"
    r "Kesengsaraan rakyat ga pernah mereka dengar, Bram!"
    r "Dunia ini ga akan pernah adil, Bram."
    r "Kehidupan ini ibarat bertahan di tengah hutan rimba."
    r "Lu harus bisa survive gimanapun caranya."
    r "Lihat tuh Ayah. Ayah jadi polisi harus jual sawah kakek dulu, Bram!"
    k "Tapi…"
    r "Tapi apa, Bram?"
    k "Lihat Pak Habibie, Arya. Rupiah kita sekarang menguat banget."
    k "Pak Habibie, Arya! Dia mau berjuang untuk masyarakat."
    k "Kalo ibarat lu kehidupan ini adalah hutan belantara, beliau masih bisa sukses tanpa harus merugikan orang lain, Arya!"
    r "Pak Habibie itu punya otak, Bram! Ga kaya aku yang goblok ini."
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
    a "Brama, kamu yang bawa mobilnya ya."
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
    #             "Brama menginjak pedal gas, kecepatannya sekarang [driving_speed] km/h."
    #         "Rem (Kurangi kecepatan)":
    #             $ driving_speed = max(0, driving_speed - 10)
    #             "Brama menginjak rem, kecepatannya sekarang [driving_speed] km/h."
    #         "Jaga kecepatan (Tetap stabil)":
    #             $ distance_covered += driving_speed // 15
    #             "Brama menjaga kecepatan stabil di [driving_speed] km/h."

    #     # Random events to make the mini-game challenging
    #     if renpy.random.randint(0, 10) < 3:
    #         "Ada lubang di jalan! Brama harus menghindar."
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

    # "Brama berhasil membawa mobil sampai tujuan dengan selamat!"


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
    
    k "Ayah, Ibu, Kak, mau pesen apa? Brama aja yang nulisin."
    # Start the mini-game to order food here.
    #call mini_game_order_food
    
    staff "Baik, mohon ditunggu sebentar ya..."
    i "Senengnyaa, jarang-jarang kita makan di restoran."
    a "Ya ngapain toh repot-repot ke restoran kalau masakan ibu itu yang terenak di dunia."
    i "Alah-alah masa sih ayah?"
    a "Loh iya dong, Arya, Brama, 20 tahun nikah sama ibu, ga pernah sekalipun ayah ngga habisin masakan ibu."
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
    i "Brama, Arya, minta tolong bayarin ke kasir ya, ini bawa dompet ibu."
    r "Siap."
    
    # At the cashier.
    scene kasir with fade
    k "Meja nomor 5, totalnya berapa kak?"
    staff "Totalnya jadi Rp120.000."
    k "Okee, ini kak."
    "Brama memberikan uang"
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
    
    # Arya tries to calm down Brama.
    k "Wah gw harus bilang ke ayah."
    r "Eh, tunggu Bram!"
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
    
    # Brama rushes to tell Ayah about the situation.
    scene kasir with fade
    k "YAHH! Ada pencuri yahh di toko seberang!!"
    a "Hmmmh? Gimana gimana?"
    k "Toko baju seberang yah, ada orang nyolong sepatu, Brama lihat dengan mata kepala sendiri."
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
    r "BRAMA!"
    r "BRAMA!"
    r "BRAMA, LIHAT YANG KAMU PERBUAT!!!"
    
    # Glitching effect to show the impact of the incident.
    # This leads into the next part of the story.

    return 
# JUMP to Y-BUMN


# # ------------------------------------- Y-BUMN Pre -------------------------------------
# # DEFINE CHARACTERS
define k = Character("Brama", color="#472301")
define r = Character("Arya", )
define o = Character("Others", )
define n = Character("Nina", )
define ist = Character("Istri", )
define ceo = Character("CEO", )
define ast = Character("Asisten", )
define skre = Character("Sekretaris", )
define an = Character("Andi", )
define m = Character("Mahfudz", )
define staffa = Character("Staff A", )
define staffb = Character("Staff B", )
define staffm = Character("Staff M", )
define staffr = Character("Staff R", )

# # IMAGE BACKGROUND
image kamartidur_y = im.Scale("bg/Rumah2 Tidur.png", 1920, 1080)
image ruangmakan_y = im.Scale("bg/Rumah2 Makan.png", 1920, 1080)
image kantorrumah_y = im.Scale("bg/Rumah2 Kantor.png", 1920, 1080)
image terasrumah_y = im.Scale("bg/Rumah2 Kamil Dewasa.png", 1920, 1080)
image bumnkantor = im.Scale("bg/BUMN Kantor.png", 1920, 1080)
image bumnlobi = im.Scale("bg/BUMN Lobi.png", 1920, 1080)
image bumnlorong = im.Scale("bg/BUMN Lorong.png", 1920, 1080)
image bumnrapat = im.Scale("bg/BUMN Rapat.png", 1920, 1080)

# # IMAGE CHARA
# image Brama


label ybumn:
    k "Orang mengatakan kematian itu adalah hal mutlak, tidak dapat dihindarkan"
    k "Tapi yang jadi pertanyaan adalah"
    k "Kematian seperti apa yang diikhlaskan semua orang?"

    #nunggu full face reveal depan cermin
    k "Kematian ayah harus terjadi karena keegoisan anaknya."
    k "..."
    k "Andai saja waktu dapat berputar."
    k "24 tahun telah berlalu.."
    k "Kedamaian dan kerelaan belum kunjung aku temukan."

    #Brama mendongak ke atas, tampilan dari samping
    #ruangan di kamar mandi
    k "Ayah, apakah engkau kecewa kepadaku?"
    k "Ayah, aku hanya berusaha melakukan yang terbaik."
    #Brama menunduk ke bawah, tampilan masih dari samping]
    k "Apa jalan yang aku pilih sudah benar?"
    k "..."
    #dari atas sampai sini ga ada image karakter yang muncul di kiri kanan, murni karakter background]

    #mulai sini balik ke biasanya, ada karakter di samping kiri kanan]
    o "Tidak salah untuk bersedih dan menyesal."
    o "Fitrah manusia sudah ditetapkan untuk memiliki perasaan."
    o "Sangat wajar jika kamu merasa terpuruk kehilangan ayah."
    o "Terlebih hal itu disebabkan oleh keputusanmu."
    k "..."
    o "Tetap ingatlah satu hal, Brama."
    o "Kamu sudah melakukan hal yang benar."
    o "Terkadang hal-hal yang terjadi berada di luar kendali kita."
    o "Tetaplah fokus pada nilai moral yang kamu perjuangkan."
    o "Tetaplah semangat."
    
    menu:
        "Terima":
            jump terima
        "Denial":
            jump denial

label terima:
    k "Kamu benar, Brama."
    k "Takdir tuhan selalu tidak dapat ditebak."
    k "Akan ada saatnya semua orang akan mati."
    k "Termasuk ayah."
    k "..."
    #(suddenly Brama crying) Brama meneteskan air mata]

    k "Tapi apakah aku harus melakukannya?"
    k "Apakah aku bisa merubah masa lalu?"
    jump nina

label denial:
    k "Engga, engga, engga!"
    k "Aku ga bisa harus menjalani ini!"
    k "Kenapa ya Allah??"
    #(start to cry) Brama meneteskan air mata]
    k "Kenapa engkau tidak menganugerahi aku otak bodoh dan apatis?"
    k "Ayah seharusnya tidak akan mati karena aku."
    k "..."
    #menunduk sedih]
    jump nina

label nina:
    #(Nina masuk ke kamar Brama dan memanggil Brama, ekspresi Brama kaget terbangun dari lamunannya)
    #{musik make netral}
    n "Nina  : Ayahhh!!"
    #(Brama memalingkan muka sekejap untuk menutupi air mata) muka Brama ditutupi tangan]
    k "Iya nak, kenapa nak?"
    n "Ayah-ayah, ayo buruan sarapan udah ditunggu sama bundaaa!"
    n "Bunda udah nunggu lama di meja makan ihh!"
    n "Ayah juga buruuuu, nanti telat berangkat kerjaa!"
    k "Oh hehehe, iya nina, sebentar ya ayah masih harus siap-siap dulu."
    k "Kamu turun duluan ya nak, Ayah 5 menit lagi turun ke bawah."
    k "Okay yah awas kalau lama."
    #Ekspresi kesal nina]
    k "Haduuhh aku tadi mikirin apa sampai ga sadar gini."
    k "Dah dah, mending aku turun sekarang, terus sarapan dengan anak dan istriku."

    #(time skip) (Brama pergi ke meja makan, istri dan nina udah duduk di kursi) (Brama dan keluarga lagi sarapan di meja makan, Istri bahagia menyambut Brama tapi anak kesal dengan Brama karena terlalu lama)
    #ruang makan]
    #{musik netral lagi}

    ist "Pagi ayah, ngapain aja sii lama banget di atasnya?"
    
    menu:
        "Cuci muka":
            jump cucimuka
        "benerin shower":
            jump benerinshower

label cucimuka:
    k "Nggapapa kok sayang, tadi aku cuci muka bentar."
    ist "Ohhh begituu."
    jump lanjutmakan

label benerinshower:
    k "Nggapapa kok sayang, tadi shower kita bocor."
    k "Jadi aku tadi benerin bentar."
    ist "Loh, rusaknya parah kah?"
    k "Engga kok, Alhamdulillah masih bisa diperbaiki."
    ist "Yauda deh syukurlah."
    jump lanjutmakan

label lanjutmakan:
    ist "Eh iya, yuk kita makannn!"
    ist "Nina udah nungguin ayah nih dari tadi nggak turun-turun."
    n "Iya nih ayah lama banget nggak tau apa kalau aku udah laper dan nungguin dari tadi."
    k "Hehehe iya sayang maaf ya ayah kelamaan siap-siapnya."
    k "Bunda masak apa pagi ini? Dari jauh aja aku bisa mencium aroma sedap masakan bunda."
    ist "Ih bisa aja kamu yah,"
    ist "Aku hari ini masak makanan kesukaan kamu banget nihh."
    ist "Ada udang saus padang sama ayam mentega."
    k "Wihhhhhhh."
    ist "Kamu mau makan sama yang mana yah?"

    menu:
        "Udang saus padang dan ayam mentega":
            jump dan
        "Ayam mentega atau udang saus padang":
            jump atau

label dan:
    k "Aku mau semuanya soalnya masakan kamu paling enak sedunia."
    ist "Dasar ayah pagi-pagi udah gombal."
    n "Iya nih ayah bisaan gombalnya huuuu."
    jump laptop

label atau:
    k "Aku mau ayam mentega/udang saus padang aja deh."
    k "Soalnya kan ayam mentega/udang saus padang kamu terenak di dunia."
    ist "Dasar ayah pagi-pagi udah gombal."
    n "Iya nih ayah bisaan gombalnya huuuu."
    jump laptop

label laptop:
    n "Ayah berangkat jam berapa? Ini udah 06.15 loh."
    n "Awas kena macet loh nanti di jalan."
    n "Terus jadi telat deh masuk kantornya."
    k "Eh iya bener juga makasih ya sayang udah diingetin."
    n "Ayah cek lagi semua barang-barang bawaan ayah jangan sampai ada yang ketinggalan."
    k "Iya sayang, ini udah ayah cek semuanya udah ada di tas ayah."
    k "Wah iyaa, laptop ayah!"
    k "Untung kamu ingetin, Nina."
    k "Kalau nggak laptop ayah bakal ketinggalan di rumah."
    k "Bunda lihat laptop ayah di mana nggak ya? Ayah lupa naruhnya."
    ist "Kemarin bukannya ayah pake di ruang kerja ya?"
    ist "Coba deh ayah cek juga di kamar kalau semisal di ruang kerja nggak ada."
    n "Tuhkan untung aja aku ingetin."
    n "Kalau nggak bisa-bisa ayah balik lagi ke rumah untuk ambil laptop doang."
    k "Iya sayang, makasii yaa."
    k "Laptop aku di mana ya?"
    k "Aku lupa terakhir kali make aku taruh mana ya?"

    menu:
        "Ruang kerja":
            jump ruangkerja
        "Kamar":
            jump ruangkamar

label ruangkerja:
    k "Laptop kemarin aku taruh mana ya?"
    k "Aduh, ruang kerja ini kok berantakan banget? Aku pasti lupa taruh di mana lagi. Coba periksa dulu…"
    k "Aha! Ini dia! Aku ingat tadi malam aku nge-charge laptop di sini. Untung ketemu."

label ruangkamar:
    k "Hmmm… laptopku di mana, ya?"
    k "Kemarin aku sempat taruh di sini…"
    k "Atau mungkin di meja kerja?"
    k "Oh, ini diaa. Ternyata tertumpuk oleh buku. Untung ketemu."


label berangkatkerja:
    k "Ninaaa, makasih yaa nakk udah diingetin."
    n "Iya, Ayah. Jangan sampai lupa lagi, ya!"
    k "Maaa, aku berangkat yaa!"
    ist "Iya sayangg, hati hatii!"

    k "Fyuh, akhirnya bisa sampai tepat waktu."
    staffa "Selamat pagi, Pak Brama."
    k "Selamat pagi."
    staffa "Saya ada kabar, Pak. Bisa berbicara sebentar?"
    k "Boleh, ada apa ya?"
    staffa "Jadi begini, Pak. Ada kabar bagus dari tim pemasaran."
    staffa "Sepertinya kerja sama dengan klien baru sudah hampir rampung."
    k "Oh iya? Bagus sekali."
    k "Kalau begitu, saya minta tolong pastikan semua dokumen kontraknya sudah dicek sebelum finalisasi ya."
    staffa "Baik, Pak."
    k "Ada lagi yang perlu saya tahu?"
    staffb "Pak, tadi pagi ada email dari tim IT tentang pembaruan sistem akuntansi kita."
    k "Oke, lanjut."
    staffb "Mereka butuh konfirmasi Bapak untuk lanjut ke tahap berikutnya."
    k "Oh iya, itu penting. Saya cek nanti. Terima kasih sudah mengingatkan."
    ast "Selamat pagi, Pak Brama. Hari ini ingin minum apa?"
    k "Oh selamat pagi, Mas."
    
    menu:
        "Kopi hitam":
            jump kopihitam
        "Teh hijau":
            jump tehhijau

label kopihitam:
    k "Hari ini biasa ya, kopi hitam tanpa gula."
    jump mulaikerja

label tehhijau:
    k "Saya pengen teh kayanya."
    ast "Maaf pak, stok teh kita kosong."
    k "Yasudah, seperti biasa aja."
    jump mulaikerja

label mulaikerja:
    ast "Baik pak, ada lagi yang perlu saya siapkan?"
    k "Oh iya, setelah ini saya langsung ke ruangan saya."
    k "Nanti langsung antarkan ke sana saja."
    ast "Baik pak."

    k "Nahh iya, hari ini aku harus meeting online. Hampir saja lupa…"
    ceo "Selamat pagi, semuanya."
    ceo "Sebelum kita mulai, saya ingin memberi tahu mengenai regenerasi tim kita."
    ceo "Izinkan saya memperkenalkan seorang kandidat untuk posisi strategis baru di perusahaan kita, Ibu Rosa."
    ceo "Beliau akan mengamati proses kita hari ini dan memberikan masukan di kemudian hari."
    rs "Terima kasih atas kesempatannya. Saya berharap bisa belajar banyak dari diskusi hari ini."
    ceo "Baik, mari kita langsung masuk ke pembahasan utama."
    ceo "Hari ini agenda kita akan mereview laporan keuangan tahunan."
    ceo "Kemudian saya ingin memastikan semuanya sudah sesuai sebelum pembukuan ditutup akhir bulan."
    ceo "Pak Brama, silakan memulai presentasi."
    k "Selamat pagi, Bapak/Ibu Direksi. Saya akan memaparkan laporan keuangan tahunan kita."
    k "Dimulai dari performa pendapatan selama tahun fiskal ini."
    k "Mohon perhatian ke slide berikut ini."
    k "Seperti yang terlihat, perusahaan mengalami kenaikan pendapatan sebesar 12% dibandingkan tahun lalu."
    k "Namun, kita juga melihat adanya peningkatan pengeluaran operasional sebesar 8%, terutama di kuartal terakhir."
    staffa "Kenaikan pengeluaran ini disebabkan oleh apa?"
    staffa "Apakah ada proyek besar yang menyedot biaya lebih besar dari anggaran?"
    k "Betul, ada dua proyek utama yang menjadi penyebab utama kenaikan biaya ini."
    k "Yaitu pengembangan produk baru dan ekspansi ke pasar luar negeri."
    k "Namun, tim keuangan kami telah memastikan bahwa semua alokasi biaya ini sesuai dengan perencanaan awal."
    staffb "Pak Brama, saya perlu melihat file detail pengeluaran kuartal keempat. Bisa kirimkan sekarang?"
    staffb "Terima kasih, Pak Brama. File ini sesuai dengan yang saya butuhkan."
    k "Baik, Bapak/Ibu. Selain laporan pengeluaran, kami juga melihat adanya peningkatan margin keuntungan bersih sebesar 3%."
    k "Ini berkat efisiensi dalam operasional dan optimalisasi proses produksi yang diterapkan sejak awal tahun."

    k "Fyuh, akhirnya selesai juga presentasi hari ini."
    k "Selanjutnya apa ya agendaku?"
    skre "Pak Brama, maaf mengganggu. Ada hal penting yang baru saja saya dapatkan."
    skre "Bapak perlu tahu ini sekarang."
    k "Iya, apa ada masalah?"
    skre "Ini terkait laporan tambahan dari tim audit."
    k "Lanjutkan."
    skre "Ada pembengkakan biaya di salah satu proyek besar kita, dan jumlahnya cukup signifikan."
    k "Bagaimana? Tolong diulangi."
    skre "Mohon maaf Pak, terdapat pembengkakan biaya pada salah satu proyek kita."
    k "…"
    skre "Sekali lagi mohon maaf Pak mengganggu waktunya."
    k "…"
    k "10 menit lagi silakan datang ke kantor saya."
    k "Kita bicarakan detail permasalahannya."
    skre "Baik Pak."

    k "Aduh, masalah apa lagi."
    k "Udah hampir tutup laporan tahunan."
    k "Yaa semoga seberat apa pun itu bisa diselesaikan."
    skre "Permisi, Pak."
    k "Iya, silakan."
    skre "Jadi, apakah kita sudah bisa membicarakan soal masalah pembiayaan proyek, Pak?"
    k "Iya, mari kita bicarakan."
    skre "Baik, Pak. Jadi pembiayaan proyek ekspansi perusahaan ke Singapura terjadi pembengkakan."
    skre "Biaya pelaksanaan ekspansi ini jauh dari rencana anggaran perusahaan."
    k "Hmmmmm, kasusnya seperti ini ya?"
    k "Kalau begitu, apakah cadangan keuangan perusahaan dapat menutupi kerugian itu?"
    skre "Berdasarkan perhitungan saya, keuangan kita tidak mencukupi itu."
    k "Waduh…"
    skre "Namun, masalah beratnya bukan pada hal itu saja, Pak."
    k "Oke, apa lagi masalahnya?"
    skre "Pak Bagas, salah satu yang bertanggung jawab pada pemilihan vendor."
    skre "Tim audit telah menemukan adanya indikasi kecurangan pemilihan vendor."
    skre "Sekaligus kecurangan operasional vendor."
    k "Sebentar, jadi Pak Bagas telah melakukan kecurangan?"
    skre "Benar, Pak."
    k "Terus-terus? Apa yang sudah dilakukan Pak Bagas?"
    skre "Lebih detailnya, direktur perusahaan vendor merupakan kerabat dekat Pak Bagas."
    skre "Dan setelah ditelusuri lebih jauh, saham perusahaan vendor rupanya dipegang oleh anak perusahaan turunan kompetitor kita."
    k "Oh, tunggu. Jadi Pak Bagas dalam hal ini bekerja sama dengan pesaing kita?"
    skre "Iya, Pak."
    k   "Baik, lalu apa kaitannya dengan pembiayaan kita?"
    skre "Dalam rencana anggaran yang diajukan oleh Pak Bagas, anggaran dibuat seminimal mungkin agar vendor dapat menjadi pilihan kita."
    k "Hmmm iya, saya ingat telah menandatangani RAB itu setelah berdiskusi dengan tim finansial."
    skre "Sekarang operasional ekspansi tidak dapat dilanjutkan karena dana yang telah kita siapkan sesuai RAB tidak memenuhi biaya asli ekspansi."

    menu:
        "Batalkan saja proyeknya":
            jump batalproyek
        "Jalan keluar?":
            jump jalankeluar

label batalproyek:
    k "Kalau begitu, kita batalkan saja proyek ekspansinya."
    skre "Tidak bisa, Pak."
    skre "Kita sudah menandatangani kontrak pengembangan dengan pihak Changi Airport."
    k "Hmmm…"
    k "Tunggu."
    k "Seharusnya kan ini masalah pihak Changi."
    k "Biaya operasional yang membengkak dari nilai kontrak seharusnya bukan jadi masalah kita."
    skre "Idealnya memang seperti itu, Pak."
    skre "Tapi sayangnya di MOU kontrak tidak dicantumkan demikian."
    k "Wah iya juga, aku baru ingat."
    jump rumit

label jalankeluar:
    k "Kamu ada ide untuk mengatasi masalah ini?"
    skre "Sebaiknya pembengkakan ini bisa kita atasi."
    skre "Kalau tidak, kita bisa merugi lebih banyak."
    jump rumit

label rumit:
    k "Hmmmmm."
    k "Ini rumit."
    k "Saya telah mengerti situasinya."
    k "Jadi saya simpulkan, Pak Bagas telah bekerja sama dengan kompetitor untuk menjatuhkan perusahaan ini melalui rekayasa anggaran."
    skre "Benar, Pak. Hal paling buruknya adalah RAB itu yang menandatangani adalah Pak Brama."
    skre "Artinya bila ekspansi ini gagal, Pak Brama dapat ikut terseret kasus penjatuhan perusahaan."
    k "Saya mengerti."
    k "Intinya, saya harus bertanggung jawab atas kecerobohan ini."
    k "Baik, terima kasih atas kabarnya."
    k "Tolong tinggalkan saya sendiri."
    skre "Baik, Pak."

    k "Ini masalah berat. Perjalanan hidupku sangat bergantung dengan momen ini."
    k "Bagaimana ya aku harus menyelesaikan ini?"
    k "Mungkin akan aku pastikan pada tim legal."

    menu:
        "Menelpon Pak Mahfudz":
            jump pakmahfudz
        "Bertanya ahli hukum di Kantor":
            jump ahlihukumkantor

label pakmahfudz:
    k "Halo, Pak Mahfudz."
    m "Halo, Pak Brama."
    k "Bagaimana, Pak, kabarnya? Apa bisa kita berdiskusi sejenak?"
    m "Maaf, Pak Brama, saya sedang rapat penting dengan anggota dewan."
    m "Sekiranya hal yang dibicarakan itu penting, saya sarankan berbicara dengan Pak Andi."
    k "Wah begitu ya, Pak."
    k "Baik, akan saya komunikasikan dengan Pak Andi."
    jump pakandi
    
label ahlihukumkantor:
    k "Kalau tidak salah ingat, penasihat hukum utama kantor sedang keluar kota."
    k "Mungkin aku bisa bertanya pada staf pembantunya di kantor ini."

    staffa "Ada yang bisa saya bantu, Pak?"
    k "Tolong panggilkan staf hukum."
    k "Mungkin staf pembantu Pak Mahfudz."
    staffa "Baik, Pak. Mohon ditunggu."
    k "Oke."

    staffm "Bapak mencari saya?"
    k "Iya, saya ada perlu."
    staffm "Baik, Pak. Apakah ini terkait hukum?"
    k "Iya."
    staffm "Baik, Pak. Tapi sebelum itu, saya ingin memohon maaf sebesar-besarnya."
    staffm "Barusan saya dihubungi Pak Mahfudz untuk segera menyusul ke Kalimantan."
    staffm "Meskipun begitu, akan saya antarkan kepada Pak Andi."
    staffm "Beliau kebetulan sedang tidak sibuk."
    k "Ya sudah kalau gitu."
    k "Nanti saya telepon dari kantor saya saja."
    k "Silakan segera bersiap menyusul Pak Mahfudz."
    staffm "Oh baik, Pak, kalau begitu."
    staffm "Saya izin duluan, Pak."
    k "Iya."
    jump pakandi

label pakandi:
    k "Halo, Pak Andi."
    an "Oh, halo, Pak."
    k "Bagaimana kabarnya, Pak?"
    an "Alhamdulillah, kabar baik."
    an "Jadi bagaimana, Pak? Ada yang bisa saya bantu?"
    k "Nah iya, jadi begini, Pak."
    k "Saya butuh konsultasi hukum terkait laporan keuangan perusahaan."
    k "Ada potensi pembengkakan biaya yang mencurigakan di salah satu proyek besar kita."
    k "Jika ada kesalahan atau masalah di sini, apakah ini bisa dianggap pelanggaran hukum?"
    an "Baik, Pak Brama, itu tergantung pada apa yang menyebabkan pembengkakan tersebut."
    an "Kalau ada bukti manipulasi data atau penggunaan dana yang tidak sesuai, ini bisa berujung pada investigasi hukum."
    an "Bahkan bisa jadi ada potensi pidana jika melibatkan fraud atau pencucian uang."
    k "…"
    k "Kalau kita tidak segera menutup pembukuan atau menutupi masalah ini, apakah kita bisa diselamatkan secara hukum?"
    an "Saya tidak bisa memberikan jaminan, Pak."
    an "Saran saya, segera lakukan audit internal menyeluruh sebelum hal ini diketahui pihak eksternal."
    an "Kalau ternyata masalahnya serius, mungkin kita perlu transparan dan melibatkan otoritas."
    k "Baik, Pak. Terima kasih atas masukannya."

    k "Ini masalah besar…"
    k "Kalau informasi kesalahan ini sampai keluar, saya yang akan dimintai tanggung jawab."

    k "…"
    k "Kayanya aku perlu break."
    k "Eh, sudah jam makan siang juga."
    k "Kemana ya enaknya?"

    menu:
        "Kantin":
            jump kantin
        "Kafe":
            jump kafe

label kantin:
    k "Mikirin masalah gini jadi laper."
    k "Oh iya, dengar-dengar ada stan baru di kantin."
    k "Jual apa ya dia kata sekretaris kemarin?"
    k "Oh iya, kebab mozarela."
    k "Menarik deh, mungkin aku harus coba cita rasa gen-Z."
    jump curhatarya

label kafe:
    k "Mikirin masalah gini jadi laper."
    k "Oh iya, dengar-dengar cafe di lantai bawah jualan menu baru."
    k "Kopi apa ya?"
    k "Duh lupa, padahal baru diomongin sama sekretaris kemarin."
    k "Yaudah lihat aja nanti di bawah."
    k "Sekalian makan bekal dari rumah."
    jump curhatarya

label curhatarya:
    r "Pak Brama, saudaraku!"
    k "..."
    r "Kelihatannya kamu lagi pusing berat."
    r "Ada masalah besar lagi, ya?"
    r "Ceritalah, Bim."
    r "Saudaramu ini direktur keuangan."
    r "Masalah bagi gw udah kayak makanan sehari-hari. Hahahaha!"
    k "..."

    menu:
        "cerita":
            jump cerita
        "Diam saja":
            jump diamsaja

label diamsaja:
    k "Aman aja kok, Ar."
    r "Udah lah, dikira bisa bohong ke abangmu ini?"
    r "Kita udah tumbuh bareng lama, loh."
    r "Dari kita kecil sampai…"
    r "Lihatlah sekarang."
    r "Kamu sudah sukses jadi direktur anak usaha Garuda."
    r "Dan aku, sekarang aku jadi direktur keuangan Garuda."
    r "Intinya begini."
    r "Kalau ada masalah, cerita saja ke aku."
    r "Mungkin meski aku tidak bisa kasih masukan sebagai saudara."
    r "Setidaknya aku bisa memberikan tanggapan sebagai stakeholder perusahaan ini."
    k "..."
    jump cerita

label cerita:
    k "Haduh iya nih."
    k "Masalah baru menimpa lagi."
    k "Sangatlah pusing."
    r "Emang ada masalah apa sih? Kok kayaknya berat banget."
    k "Jadi gini, Kak."
    k "Salah satu proyek kita ada yang bengkak anggarannya."
    k "Anggaran nggak sesuai dengan rencana awal."
    k "Bahkan berpotensi bikin perusahaan bangkrut."
    r "Wah, ini sih masalah serius banget."
    r "Sebentar, apa ini masalah ekspansi dapur katering ke bandara Changi?"
    k "Kok tahu?"
    r "Ayo lah, aku direktur keuangan."
    r "Aku bisa tahu kalau ada persoalan keuangan yang aneh."
    r "Ngomong-ngomong, udah ada investigasi belum mengenai hal itu?"

    menu:
        "Sudah":
            jump sudah
        "Jaga rahasia":
            jump jagarahasia

label sudah:
    k "Sekretaris aku udah coba investigasi."
    k "Rupanya ini ulah orang operasional."
    k "Namanya Bagas."
    k "Dia yang bagian milih vendor sekaligus yang nyusun rancangan anggaran."
    k "Jadi, rancangan anggaran proyek ekspansi sengaja dikecilkan."
    k "Kemudian vendor proyek ekspansi juga ternyata dari perusahaan pesaing."
    r "Hmmm begitu ya."
    r "Kalau begitu kenapa kamu setujui proposal anggaran itu?"
    k "Ah, itu kesalahanku kurang teliti."
    k "Saat itu aku terlalu banyak beban, Kak."
    k "Jadinya gini deh, buntutnya jadi nggak fokus ngurus dokumen."
    k "Intinya aku harus bisa mengatasi biaya membengkak itu supaya aku aman."
    jump lanjutcerita

label jagarahasia:
    k "Belum, Wan."
    k "Intinya dari pembengkakan biaya ini bikin kita butuh dana yang cukup besar."
    r "Kamu benar, Bim."
    r "Kalau aja sampai gagal mengatasi pembengkakan, perusahaan yang kamu pegang bisa rugi besar."
    k "Iya, aku ngerti soal itu."
    r "Tapi kalau hanya masalah itu, seharusnya saudaraku ini tidak segusar itu."
    r "Apa masih ada yang disembunyikan?"
    k "..."
    k "Aku kena jebakan orang."
    r "Apa?"
    k "Intinya aku harus bisa mengatasi biaya membengkak itu supaya aku aman."
    jump lanjutcerita

label lanjutcerita:
    r "Hmmm, begitu rupanya."
    r "Kalau gitu kita harus segera cari suntikan modal."
    r "Kamu sendiri udah nyoba nyari calon-calon investor yang sekiranya bisa buat investasi ke kita segera?"
    k "Belum sih, Wan."
    k "Tapi tadi aku dapat email dari PT. Angin Topan."
    k "Mereka menawarkan untuk menyuntikkan dana besar ke proyek kita."
    r "Wah bagus dong kalau gitu."
    r "Tunggu apa lagi?"
    r "Ini kesempatan besar buat nyelamatin perusahaan kamu."

    menu:
        "Ambil":
            jump ambil
        "Ragu":
            jump ragu

label ambil:
    k "Ini emang menarik sih."
    r "Tunggu apa lagi kalau begitu?"
    k "Iya sih, habis ini aku coba rapatin sama direksi yang lain."
    jump throwbackarya

label ragu:
    k "Tapi, Kak, apa nggak merasa aneh?"
    r "Aneh kenapa?"
    k "Kayak tiba-tiba banget pas di momen gini."
    r "Eh bagus dong."
    k "Iya sih, habis ini aku coba rapatin sama direksi yang lain."
    jump throwbackarya

label throwbackarya:
    staffr "Pagi, Pak Arya."
    r "Pagi, ada apa?"
    staffr "Saya mendapatkan informasi mengenai anak perusahaan Garuda."
    r "Anak perusahaan yang mana?"
    staffr "Penyedia katering, Pak."
    r "Ohhh, yang dipegang Brama adik aku?"
    staffr "Iya, Pak."
    r "Kenapa?"
    staffr "*mengulangi cerita yang disampaikan sekretaris ke Brama*"
    r "Hmmm begitu ya."
    r "Terima kasih atas informasinya."
    r "Tolong tinggalkan saya sendiri."
    staffr "Baik, Pak."

    r "Aduh, Brama ada aja."
    r "Berbuat apa kamu sampai terjebak di masalah gini."
    r "Kalau gini aku harus bantu dia."

    menu:
        "Minta bantuan direksi BUMN":
            jump bantuanbumn
        "Minta bantuan teman":
            jump bantuanteman

label bantuanbumn:
    r "Kayanya aku harus coba menghubungi orang tinggi BUMN deh."
    r "Hmmm, jadi direksi pusat nggak bisa bantu ya."
    r "Mungkin aku kontak temenku yang punya banyak duit aja."
    r "Kemarin dia bisa beli 2000 alat berat."
    r "Duitnya banyak sih, harusnya."
    jump lanjutthrwback

label bantuanteman:
    r "Kayanya aku harus coba menghubungi Suyono deh."
    r "Kemarin dia bisa beli 2000 alat berat."
    r "Duitnya banyak sih, harusnya."
    jump lanjutthrwback

label lanjutthrwback:
    r "Eh, tapi apa kata Brama yang sok idealis itu?"
    r "Kalau tahu apa yang aku lakuin gini bisa ditolak mentah-mentah bantuanku."
    r "Bodo amat lah, dunia emang gini."
    r "Mending untuk sekali-kali nerima bantuan koruptor daripada harus menderita."
    r "Asal koruptor ini pakai perusahaan samaran sih aman."
    r "Kasih nama PT. Angin Topan pasti Brama nggak tahu itu duit dari mana."
    jump balikkamil

label balikkamil:
    k "Baik, sekian rapat kita kali ini."
    k "Sebagai kesimpulan, keputusan belum bisa kita ambil."
    k "Meskipun begitu, saya ucapkan terima kasih pada bapak ibu yang telah memberikan masukan."
    k "Kepastian mengenai tawaran investasi PT. Angin Topan akan segera saya kabarkan."
    k "Silakan untuk meninggalkan ruangan."

    r "Bagaimana, Pak? Apakah dewan direksi menyetujui tawaran investor PT. Angin Topan?"
    k "Eh, Arya."
    k "Saya masih bingung terhadap keputusan apa yang harus saya ambil."
    k "Dewan direksi setuju untuk mengambil kesempatan ini."
    k "Mereka tidak mau perusahaan kita bangkrut dan karyawan kita kehilangan pekerjaan mereka."
    k "Kalau saya sendiri masih bingung karena saya punya feeling nggak enak."
    r "Udah lah, Bim."
    r "Kalau kata saya, terima saja tawaran itu."
    r "Emang kamu nggak kasihan apa buat keluarga karyawan yang bergantung pada pekerja kita untuk hidup sehari-hari?"
    r "Saya dengar-dengar juga ada kemungkinan tindak pidana manipulasi keuangan yang bisa menyeret nama kamu ke jalur hukum."
    r "Daripada kamu kena getahnya, mending bapak terima saja tawaran itu."

    menu:
        "Tolak":
            jump a
        "Terima":
            jump b

# # # ------------------------------------- A -------------------------------------
# # DEFINE CHARACTERS
# define b = Character("Brama", color="#472301")
# define o = Character("Other", color="#472301")
# define s = Character("Sekretaris", color="#472301")

# # IMAGE BACKGROUND
# image kantor = im.Scale("bg/kantor.jpg", 1920, 1080)

# # IMAGE CHARA
# image Brama:
#     "chara/Brama.png"
#     zoom 0.5
# image Brama Cemas:
#     "chara/sma_kamil/k angry.png"
#     zoom 0.5
# image Brama Shocked : 
#     "chara/sma_kamil/k lega.png"
#     zoom 0.5
# image Brama Serius :
#     "chara/sma_kamil/k conf.png"
#     zoom 0.5


# #Posisi2 yang di dettermined buat image dengan resolusi chara 1239 x 3508 px
# define cpos = Position(xalign=0.5, yalign=0)
# define rpos = Position(xalign=0.9, yalign=0)
# define lpos = Position(xalign=0,yalign=0)

# label start: #email_keputusan
#     scene kantor with fade
#     show Brama at cpos

#     "Suasana tegang, Brama sedang duduk di depan komputernya, mengetik email balasan untuk menolak tawaran investasi."

#     show Brama Cemas at cpos
#     b "Coba aja aku tahu lebih dalam tentang PT. Angin Topan..."
#     b "Kalau kayak gini aku harus cari dana tambahan ke mana lagi?"

#     show Other at left
#     o "Sudah, tenang saja Brama. Tetaplah berpegang teguh pada prinsipmu itu."
#     o "Ingatlah bahwa setiap permasalahan pasti akan ada solusinya."
#     o "Bagaimana jika feeling-mu itu benar?"
#     o "Bagaimana jika PT. Angin Topan justru membawa masalah lebih jauh?"
#     o "Coba pikirkan kemungkinan bahwa Angin Topan membawa uang haram."
#     o "Apa kamu nggak malu dengan keluarga kecilmu kalau nantinya tertangkap karena melakukan pencucian uang?"

#     show Brama Shocked at cpos
#     b "Benar juga... Kasihan dengan anak dan istriku."
#     b "Mereka pasti malu punya suami dan seorang ayah koruptor."
#     b "Semoga ada jalan untuk menyelesaikan permasalahan ini."

#     "Brama terlihat sangat gelisah. Ia memanggil sekretarisnya melalui telepon."

#     show Brama Serius at cpos
#     b "Sekretaris, tolong adakan rapat dewan direksi darurat 1 jam lagi dengan semua direksi."
#     b "Semua harus hadir untuk membahas persoalan ini."
#     b "Dan pastikan tidak ada pihak asing yang masuk ke kantor."
#     b "Saya nggak mau rapat terganggu, terlebih isu ini sangat penting."

#     show Sekretaris at right
#     s "Baik Pak, akan segera saya informasikan kepada seluruh direksi perusahaan."
#     s "Untuk keamanan, akan saya sampaikan ke pihak security di depan."

#     "Sekretaris keluar dari ruangan, meninggalkan Brama yang masih terlihat cemas."

#     return

# # ------------------------------------- B -------------------------------------
# # DEFINE CHARACTERS
# define k = Character("Brama", color="#472301")

# # IMAGE BACKGROUND
# image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)

# # IMAGE CHARA
# image Brama


# # ------------------------------------- C -------------------------------------
# # DEFINE CHARACTERS
# define k = Character("Brama", color="#472301")

# # IMAGE BACKGROUND
# image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)

# # IMAGE CHARA
# image Brama


# # ------------------------------------- D -------------------------------------
# # DEFINE CHARACTERS
# define k = Character("Brama", color="#472301")

# # IMAGE BACKGROUND
# image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)

# # IMAGE CHARA
# image Brama


# # ------------------------------------- E -------------------------------------
# # DEFINE CHARACTERS
# define k = Character("Brama", color="#472301")

# # IMAGE BACKGROUND
# image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)

# # IMAGE CHARA
# image Brama


# # ------------------------------------- F -------------------------------------
# # DEFINE CHARACTERS
# define k = Character("Brama", color="#472301")

# # IMAGE BACKGROUND
# image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)

# # IMAGE CHARA
# image Brama


# # ------------------------------------- G -------------------------------------
# # DEFINE CHARACTERS
# define k = Character("Brama", color="#472301")

# # IMAGE BACKGROUND
# image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)

# # IMAGE CHARA
# image Brama


# # ------------------------------------- H -------------------------------------
# # DEFINE CHARACTERS
# define k = Character("Brama", color="#472301")

# # IMAGE BACKGROUND
# image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)

# # IMAGE CHARA
# image Brama


# # ------------------------------------- I -------------------------------------
# # DEFINE CHARACTERS
# define k = Character("Brama", color="#472301")

# # IMAGE BACKGROUND
# image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)

# # IMAGE CHARA
# image Brama


# # ------------------------------------- J -------------------------------------
# # DEFINE CHARACTERS
# define k = Character("Brama", color="#472301")

# # IMAGE BACKGROUND
# image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)

# # IMAGE CHARA
# image Brama