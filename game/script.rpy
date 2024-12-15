
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
image kamartidur = im.Scale("bg/kamar.png", 1920, 1080)
image kamar= im.Scale("bg/kamarmalam.png", 1920, 1080)
image ruangtamu = im.Scale("bg/Ruang Tamu.png", 1920, 1080)
image ruangmakan = im.Scale("bg/ruang makan.png", 1920, 1080)
image depanrumah = im.Scale("bg/rumahkmilkecil.png", 1920,1080)
image rumah_sore = im.Scale("bg/ruang makan malam.png", 1920,1080)
image rakbuku = im.Scale("bg/rakbuku.png", 1920,1080)
image gerbangsekolah = im.Scale("bg/GerbangSekolah.png", 1920,1080)
image sekolah_sore = im.Scale("bg/sekolahsore.jpg", 1920,1080)
image jalan = im.Scale("bg/jalansore.jpg", 1920,1080)
image dompet = im.Scale("bg/dompet.JPG", 1920,1080)
image jalanan_malam = im.Scale("bg/jalan malam.jpg", 1920,1080)
image jakarta_malam = im.Scale("bg/jakarta malem.jpg", 1920,1080)
image restoran_1 = im.Scale("bg/restoduduk.png", 1920,1080)
image kasir = im.Scale("bg/Restoran Kasir.png", 1920,1080)
image tokobaju = im.Scale("bg/tokobaju.png", 1920,1080)

# IMAGE CHARA
image Brama Glitch:
    At("chara/sma_kamil/k netral.png", glitch)
    pause 0.2
    At("chara/sma_kamil/k netral.png", animated_glitch)
    pause 0.2
    At("chara/sma_kamil/k netral.png", glitch)
    pause 0.1
    At("chara/sma_kamil/k netral.png", animated_glitch)
    pause 0.1
    At("chara/sma_kamil/k netral.png", glitch)
    pause 0.3
    At("chara/sma_kamil/k netral.png", animated_glitch)
    pause 1.0
    repeat
image Arya Marah Glitch:
    At("chara/sma_arya/RAGE.png", glitch)
    pause 0.2
    At("chara/sma_arya/RAGE.png", animated_glitch)
    pause 0.2
    At("chara/sma_arya/RAGE.png", glitch)
    pause 0.1
    At("chara/sma_arya/RAGE.png", animated_glitch)
    pause 0.1
    At("chara/sma_arya/RAGE.png", glitch)
    pause 0.3
    At("chara/sma_arya/RAGE.png", animated_glitch)
    pause 1.0
    repeat
image Arya Menangis Glitch:
    At("chara/sma_arya/CRYING.png", glitch)
    pause 0.2
    At("chara/sma_arya/CRYING.png", animated_glitch)
    pause 0.2
    At("chara/sma_arya/CRYING.png", glitch)
    pause 0.1
    At("chara/sma_arya/CRYING.png", animated_glitch)
    pause 0.1
    At("chara/sma_arya/CRYING.png", glitch)
    pause 0.3
    At("chara/sma_arya/CRYING.png", animated_glitch)
    pause 1.0
    repeat

image Pencuri:
    "chara/PENCURI/Neutral.png"
    zoom 0.75
image Pencuri Panik:
    "chara/PENCURI/Panic.png"
    zoom 0.75
image Pencuri Pistol:
    "chara/PENCURI/Pencuri rogoh tas.png"
    zoom 0.5
image Badge:
    "chara/AYAH PULICI/Belum isi foto.png"
    zoom 0.5
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

    scene dentuman
    play sound "audio/dentumanpistol.mp3"
    show Brama Glitch:
        xalign 0.5
        yalign 0
        zoom 1
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


image slide1 = im.Scale("text/X-SMA/Slide1.png", 1920, 1080)
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
    show slide1
    pause 1
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

image slide2 = im.Scale("text/X-SMA/Slide2.png", 1920, 1080)
label gerbangsekolah:
    scene black with fade
    show slide2
    pause 1
    scene gerbangsekolah with fade
    show Brama at lpos
    show Arya at arpos


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

image slide3 = im.Scale("text/X-SMA/Slide3.png", 1920, 1080)
image slide5 = im.Scale("text/X-SMA/Slide5.png", 1920, 1080)
label ganabrak:
    scene black with fade
    show slide3
    pause 1
    scene depanrumah with fade
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
    scene black with fade
    show slide5
    pause 1
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
image slide4 = im.Scale("text/X-SMA/Slide4.png", 1920, 1080)
image slide6 = im.Scale("text/X-SMA/Slide6.png", 1920, 1080)
image slide7 = im.Scale("text/X-SMA/Slide7.png", 1920, 1080)
label nabrak:
    scene black with fade
    show slide4
    pause 1
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
    scene black with fade
    show slide6
    pause 1
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

    scene black with fade
    show slide7
    pause 1
    scene sekolah_sore with fade
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
    hide Arya Bingung
    hide Brama Bingung
    scene dompet with fade
    k "Dompet?"
    scene jalan with fade
    show Brama Bingung at lpos
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

image slide8 = im.Scale("text/X-SMA/Slide8.png", 1920, 1080)
label aaa:
    # Scene starts with Arya and Brama talking
    scene jalan with fade
    show Brama at lpos
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
    scene black with fade
    show slide8
    pause 1
    scene rumah_sore with fade
    show Arya at alpos
    show Brama at lpos


    show Ayah Bahagia at cpos
    a "Eehh, jagoan-jagoan Ayah udah pulang!"
    show Arya Lega at alpos
    r "Hehe, iya Yah, udah kelar sekolahnya."
    show Arya at alpos
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
    show Arya Lega at alpos
    r "Walah, Ayah aja lupa ngembaliin kalkulator sampe tantrum tuh si anak."
    show Arya at alpos
    show Brama Bingung at lpos
    k "Diem ya lu."
    show Arya Bahagia at alpos
    show Ayah Tertawa at cpos
    a "HAHAHAHA, namanya juga udah bapak-bapak pasti lupaan."

    # Transition to the birthday moment
    show Ayah Bahagia at cpos
    i "Ngomong-ngomong, Brama, Arya, kalian inget nggak sekarang hari apa?"
    show Arya Bingung at alpos
    r "Hari Kamis?"
    show Brama Bahagia at lpos
    k "OH, HARI ULANG TAHUN AYAH!"
    show Arya Kaget at alpos
    r "OIYAA!"
    show Arya Bahagia at alpos
    show Ayah Tertawa at cpos
    a "HAHAHAHA. Ternyata masih ada yang inget ulang tahun Ayah."
    show Ibu Senyum at rpos
    i "Kita harus ucapin apa, nakk? Satu, dua, tiga…"
    show Arya Ketawa at alpos
    show Brama Bahagia at lpos
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
    show Arya Kesal at alpos
    r "Ah, tapi lagi pengen makanan berkuah. Sop buntut kali ya?"
    show Ibu at rpos
    i "Hmmm, sop buntut oke sih."

    jump makanmakan

label sopbuntut:
    show Brama Bahagia at lpos
    k "Sop buntut kayanya menarik deh Yah, udah lama ngga makan sop buntut."
    show Arya Kesal at alpos
    r "Ah, tapi lagi pengen makanan bakaran. Sate kali ya?"
    show Ibu at rpos
    i "Hmmm, sate oke sih."

    jump makanmakan
image slide9 = im.Scale("text/X-SMA/Slide9.png", 1920, 1080)
label makanmakan:
    i "Yaudah yuk kita siap-siap dan beberes. Habis maghrib kita berangkat yaa!"
    k "Mau makan di mana kita, Bu?"
    i "Sarinah oke ngga, Ayah?"
    a "Yaaa… kalau Ayah sih oke aja asal belanjanya ngga sampai 1 juta. HAHAHAHAHA!"
    r "Ya kalau ada 1 juta mah mending buat beli TV lagi, taruh di kamar Arya."
    a "Yeuuu, enak aja kamu!"
    show Arya Ketawa at alpos
    a "Udah, sana siap-siap."

    # Time skip to evening preparation
    scene black with fade
    show slide9
    pause 1
    scene kamar with fade
    show Brama Bingung at lpos
    k "Kak, lu udah siap belom?"
    show Arya Ketawa at arpos
    r "Lihat aja gw, udah cakep gini."
    k "Kali aja lu mau ngapain lagi kek."
    show Arya Kesal at arpos
    r "Ah, gw ngga seribet itu orangnya."
    k "Oh iya, ngomong-ngomong soal dompet tadi..."
    show Brama at lpos
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
    show Brama Lega at lpos
    r "Terus?"
    k "Dompet itu, ternyata dompet Ujang."
    r "Ujang anak bahasa itu?"
    k "Iya."
    show Arya Kaget at arpos
    r "Ngaku-ngaku aja kali. Orang di dompetnya gaada kartu identitas sama sekali."
    k "Tapi dia nyebutin ciri-ciri dompet yang sama persis, dan nominalnya sama persis yang lu ambil."
    show Brama Malu at lpos
    r "Yaelah, terus gimana?"
    k "Dia bilang dia lagi butuh banget duitnya buat makan seminggu."
    k "Karena itu duit lu ambil, jadinya gw ga enak ke Ujang."
    show Arya Serius at arpos
    r "Ngapain pake ga enak, yaudah lah itu kesialan Ujang."
    k "Mana bisa gitu Arya. Akhirnya duit Ujang gw ganti. Gw bilang gw yang nemu dompetnya."
    show Arya Kesal at arpos
    r "Lah, tapi kan dompetnya masih ada di gw. Gimana lu ngembaliinnya?"
    k "Iya, gw bilang dompetnya masih lu amanin, jadi duitnya dulu yang gw kasih ke dia."
    show Brama Malu at lpos
    r "Berarti ini dompet mau dibalikin besok?"
    k "Iya. Sekalian gw sekarang mau minta duit gw lu balikin."
    r "Heuuuhh. Percuma tadi debat panjang lebar, ujung-ujungnya ga jadi rezeki."

    jump ibutibatiba

label aryasalah:
    k "…"
    show Brama Bingung at lpos
    k "(Bingung mau gimana ngomongnya.)"
    show Arya Serius at arpos
    r "Kenapa, Bram?"
    k "Gapapa, ga jadi Arya."
    show Arya Kecewa at arpos
    r "Hufft."
    r "(Menghela nafas.)"
    show Arya Serius at arpos
    r "Gini Bram, dunia ini ngga akan pernah adil Bram."
    r "Lu lihat aja para pejabat di Senayan sana."
    show Arya Marah at arpos
    r "Lu lihat aja tahun kemarin gimana bobroknya presiden kita?"
    r "Kesengsaraan rakyat ga pernah mereka dengar, Bram!"
    show Arya Serius at arpos
    r "Dunia ini ga akan pernah adil, Bram."
    show Arya Kaget at arpos
    r "Kehidupan ini ibarat bertahan di tengah hutan rimba."
    r "Lu harus bisa survive gimanapun caranya."
    show Arya Kesal at arpos
    r "Lihat tuh Ayah. Ayah jadi polisi harus jual sawah kakek dulu, Bram!"
    k "Tapi…"
    show Arya Serius at arpos
    r "Tapi apa, Bram?"
    k "Lihat Pak Habibie, Arya. Rupiah kita sekarang menguat banget."
    k "Pak Habibie, Arya! Dia mau berjuang untuk masyarakat."
    show Arya Kaget at arpos
    k "Kalo ibarat lu kehidupan ini adalah hutan belantara, beliau masih bisa sukses tanpa harus merugikan orang lain, Arya!"
    show Arya Serius at arpos
    r "Pak Habibie itu punya otak, Bram! Ga kaya aku yang goblok ini."
    r "Bagi kami yang goblok ini akan terus-terusan dibodohi dan ga akan bisa maju."
    r "Cara satu-satunya bagi kami bisa bertahan hidup ya dengan mengusahakan segala cara!"

    jump ibutibatiba

label ibutibatiba:
    i "Eeeh, ini ada apa ya ribut-ribut?" #(berbicara dari luar kamar)
    i "Udah siap belom kalian?"
    show Arya Serius at arpos
    r "Udah, Bu." #(membalas dari dalam kamar)
    show Arya Kesal at arpos
    r "Nanti kita bahas lagi." 
    "(berbisik Arya)"
    show Arya Serius at arpos
    r "Gw gamau kesenangan ulang tahun Ayah harus diganggu dengan masalah dompet."
    k "Ya."

    scene black with fade
    pause 0.5

    scene ruangtamu with fade
    show Brama Lega at lpos
    k "Kita udah siap nih, Bu."
    show Arya Bahagia at arpos
    i "Widihh, udah cakep-cakep nih."
    show Arya at arpos
    r "Ayah mana, Bu?"
    i "Ayah masih di kamar mandi, lagi mual-mual."
    
    show Arya Kaget at arpos
    a "Haloo, udah siap?" #(Ayah keluar dari kamar mandi)
    k "Ayah sakit? Ayah kalo ga enak badan ngga usah dipaksain makan di luar, yah."
    show Arya  at arpos
    r "Iya, kita masih bisa ngerayain di rumah kok, Yah."
    show Arya Kesal at arpos
    i "Tuh kan, Ibu bilang apa tadi."
    show Arya Bahagia at arpos
    a "Gapapa kok, Ayah lagi merasa ga enak aja perasaannya, ga tau kenapa ya."
    show Arya at arpos
    a "Apa mungkin Ayah ngga rela kehilangan uang sampe 1 juta? Hahahahaha."
    show Arya Kesal at arpos
    i "Ih Ayah, Ayah beneran gapapa?"
    a "Iya gapapa. Ayah sehat kok. Yok berangkat habis ini."
    k "Syukurlah. Yaudah, ayok kita berangkat."
    show Arya Bahagia at arpos
    r "Yokkk!"
    a "Brama, kamu yang bawa mobilnya ya."
    show Arya Kesala at arpos
    k "Eh, kok aku, Yah? Kenapa ngga Kak Arya aja?"
    show Arya Kesal at arpos
    r "Udah lu aja, udah punya SIM juga."
    show Arya Bahagia at arpos
    i "Ya sekali-kali lah, Nak. Mumpung udah ada SIM."
    i "Kasihan kakak kamu yang nyetir mulu."
    show Arya Ketawa at arpos
    a "Hahahaha, Ayah juga pengen tau gimana skill kamu nyetir."
    show Brama Lega at lpos
    k "Baikkk, siap komandan!"

    scene jalanan_malam with fade
    show Brama at lpos
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
    scene jakarta_malam
    show Brama Bahagia at lpos
    k "Alhamdulillah, udah sampe."
    # a sound of the car stopping.
    scene sarinah_dari_depan with fade
    show Arya Kaget at arpos
    i "Ayo nak, keburu tutup Sarinah-nya."
    
    a "Ngghroookk..." 
    #(Ayah ketiduran)R

    jump akhirsampe

label lamatpsampe:
    scene jakarta_malam
    show Brama Bingung at lpos
    k "Ini beloknya kemana ya?"
    show Arya Kesal at arpos
    r "Tau jalan ga sih lu?"
    show Arya Kesal at arpos
    i "Ayo nak, keburu tutup Sarinah-nya."
    a "Ngghroookk..." 

    jump akhirsampe

define pcpos = Position(xalign=0.5, yalign=0)
define pistol = Position(xalign=0.5, yalign=0.4)
define staff = Character('staff', color="#423d3d")
define x = Character('Pencuri', color="#423d3d")

image Pistol:
    "cutscene/x/pistol.png"
    zoom 1.5
image Pistol Nembak:
    "cutscene/x/pistolnembak.png"
    zoom 1.5
image dentuman = im.Scale("cutscene/x/bg.png", 1920, 1080)
image slide10 = im.Scale("text/X-SMA/Slide10.png", 1920, 1080)
image slide11 = im.Scale("text/X-SMA/Slide11.png", 1920, 1080)
image slide12 = im.Scale("text/X-SMA/Slide12.png", 1920, 1080)
image slide13 = im.Scale("text/X-SMA/Slide13.png", 1920, 1080)
image slide14 = im.Scale("text/X-SMA/Slide14.png", 1920, 1080)
image slide15 = im.Scale("text/X-SMA/Slide15.png", 1920, 1080)
image slide16 = im.Scale("text/X-SMA/Slide16.png", 1920, 1080)
image slide17 = im.Scale("text/X-SMA/Slide17.png", 1920, 1080)
image slide18 = im.Scale("text/X-SMA/Slide18.png", 1920, 1080)

label akhirsampe:
    i "Akhirnya, udah sampe juga."
    r "Fyuhhh, let’s go makannnn."
    scene black with fade
    show slide10
    pause 1
    # Transition to the restaurant scene
    scene restoran_1 with fade
    staff "Selamat datang. Ini untuk buku menunya. Pesanan langsung ditulis di sini ya…"
    
    show Brama Bahagia at lpos
    k "Ayah, Ibu, Kak, mau pesen apa? Brama aja yang nulisin."
    # Start the mini-game to order food here.
    #call mini_game_order_food
    
    staff "Baik, mohon ditunggu sebentar ya..."
    i "Senengnyaa, jarang-jarang kita makan di restoran."
    a "Ya ngapain toh repot-repot ke restoran kalau masakan ibu itu yang terenak di dunia."
    i "Alah-alah masa sih ayah?"
    a "Loh iya dong, Arya, Brama, 20 tahun nikah sama ibu, ga pernah sekalipun ayah ngga habisin masakan ibu."
    show Arya Ketawa at arpos
    r "Hahahaha, keliatan banget sih emang dari perutnya."
    a "HAHAHAHA!"
    k "Hahaha, ayah mah emang di mana-mana makannya banyak."
    i "Ih, percaya ga sih kalian, dulu ayah waktu masih bujang tuh badannya bagus tau."
    i "Ganteng dan gagah."
    show Arya Kaget at arpos
    i "Kalau sekarang, ih, gantengnya emang masih iya, tapi gagahnya berubah jadi gajah."
    a "HAHAHA, ah ibu ini bisa aja."
    show Arya at arpos
    i "Iya, ayah kan dulu juga ga kalah keren dari Brama dan Arya."
    
    # Staff brings the food.
    staff "Silakan… (menyajikan makanan)"
    staff "Untuk pesanannya sudah lengkap ya?"
    k "Mmmmm, udah kak, terima kasih ya…"
    staff "Terima kasih kembali."
    
    # Transition to eating and wrapping up at the restaurant.
    scene black with fade
    show slide11
    pause 1
    scene restoran_1 with fade
    show Brama Lega at lpos
    show Arya Bahagia at arpos
    a "Alhamdulillah kenyang."
    i "Alhamdulillah, seneng banget deh yah, makasih yaaa."
    k "Besok traktir sop buntut dong yah."
    a "Wah tunggu ayah gajian lagi ya hahahaha."
    i "Brama, Arya, minta tolong bayarin ke kasir ya, ini bawa dompet ibu."
    show Arya Ketawa at arpos
    r "Siap."
    
    # At the cashier.
    scene black with fade
    show slide12
    pause 1
    scene kasir with fade
    show Brama  at lpos
    show Arya Bahagia at arpos
    k "Meja nomor 5, totalnya berapa kak?"
    staff "Totalnya jadi Rp120.000."
    show Brama Bahagia at lpos
    k "Okee, ini kak."
    "Brama memberikan uang"
    staff "Uangnya pas ya? Terima kasih."
    k "Sama-sama kak."
    show Brama  at lpos
    show Arya Kesala at arpos
    r "Mahal amat ya sampe abis segitu."
    show Brama Bahagia at lpos
    k "Yaelah bro, kita makan di Sarinah, beli sate berapa banyak juga tadi?"
    show Arya Lega at arpos
    r "Yaaa, iya sihh."

    scene black with fade
    show slide13
    pause 1
    # The tension builds up as they notice something strange outside.
    scene tokobaju with fade
    show Brama Bingung at lpos
    k "Eh Arya, lihat deh toko baju sebrang."
    show Arya Bingung at arpos
    r "Iya? Kenapa?"
    show Brama Marah at lpos
    k "Lihat orang baju item itu? Dia lagi nyolong sepatu ga sih?"
    k "TUH TUH TUH DIA UMPETIN DI TAS DIA SI SEPATUNYA!"
    show Arya Kaget at arpos
    r "EH IYA!"
    
    # Arya tries to calm down Brama.
    show Arya at arpos
    show Brama at lpos
    k "Wah gw harus bilang ke ayah."
    show Arya Serius at arpos
    r "Eh, tunggu Bram!"
    show Arya Kesal at arpos
    k "Kenapa kak?"
    r "Udah biarin aja, ga usah ikut campur urusan orang."
    show Brama Bingung at lpos
    k "Urusan orang? Maksud lu?"
    r "Udah jangan ikut campur, biarin, itu urusan yang punya toko."
    k "Hahhh?? Lu udah gila ya? Itu kriminalitas anjing, sempet-sempetnya lu mikir gitu."
    r "Ya terus kenapa? Apa untungnya buat kita ngurusin dia?!"
    show Brama Marah at lpos
    k "Lu beneran gila ya? Ayah kita polisi loh!"
    k "Ini udah jadi tanggung jawab ayah."
    show Arya Kesala at arpos
    r "Yaudah, biarin ngapa sih, ngerepotin aja tau ga sih."
    k "Gw gamau tau, gw harus kasih tau ayah."
    
    # Brama rushes to tell Ayah about the situation.
    scene black with fade
    show slide14
    pause 1
    scene kasir with fade
    show Brama Marah at lpos
    k "YAHH! Ada pencuri yahh di toko seberang!!"
    a "Hmmmh? Gimana gimana?"
    k "Toko baju seberang yah, ada orang nyolong sepatu, Brama lihat dengan mata kepala sendiri."
    a "Bener Arya?"
    show Arya Lega at arpos
    r "Iya yah."
    show Arya at arpos
    a "Wah ga bener nih, ayok kita samperin."
    i "Dek, emang ga ada satpamnya yang jaga? Ulang tahun ayah masa harus tetep kerja sih?"
    a "Udah lah bu, ini tanggung jawab ayah."
    a "Yang mana orangnya?"
    k "Itu yah, yang baju hitam."
    a "Mana? Ohhh, yang bawa tas itu?"

    # Transition to confrontation with the thief.
    scene black with fade
    show slide15
    pause 1
    scene tokobaju with fade
    a "Permisi mas, saya Kompol Susilo, Kapolsek Matraman." #
    show Badge at lpos
    a "Saya menerima laporan kecurigaan tindakan pencurian yang melibatkan mas sebagai tersangka."
    a "Untuk itu akan saya periksa mas untuk meluruskan apakah dugaan benar atau salah."
    hide Badge
    show Pencuri at pcpos
    x "Wah, salam kenal pak Susilo. Izin meluruskan, saya tidak mencuri barang apapun di toko ini."
    a "Maka biarkan saya memeriksa agar dugaan bisa dibantah jika memang tidak ada bukti."
    staff "Bapak polisi?"
    a "Iya, ada yang bisa saya bantu?"
    staff "Kami kehilangan satu pasang sepatu di rak pajangan A9 pak, sepertinya mas ini adalah pelakunya."
    a "Mas… menanggapi ini, saya mohon mas untuk kooperatif."
    show Pencuri Panik at pcpos

    # Tension builds as X pulls a weapon.
    x "..." 
    scene black with fade
    show slide16
    pause 0.5
    scene black with fade
    show slide17
    pause 0.5
    scene black with dissolve
    show slide18
    pause 1
    #(panicked look)
    show Pencuri Pistol at pcpos
    "Pencuri mengeluarkan pistol dari sabuknya."
    scene dentuman
    show Pistol at pistol
    pause 0.2
    show Pistol Nembak at pistol
    "DORR!"
    # *DENTUMAN GUNSHOT*

    # Transition to chaos after the gunshot.
    # scene glitch_transition with glitch
    hide Pistol Nembak
    show Arya Kaget at acpos:
        zoom 1.5
    r "AYAHHHHH!"
    hide Arya Kaget

    show Brama Glitch at cpos:
        zoom 1
    k "..."
    hide Brama Glitch
    show Arya Marah Glitch at acpos:
        zoom 2
    r "BRAMA!"
    r "BRAMA!"
    show Arya Menangis Glitch at acpos:
        zoom 2
    r "BRAMA, LIHAT YANG KAMU PERBUAT!!!"
    
    # Glitching effect to show the impact of the incident.
    # This leads into the next part of the story.

    return



# # ------------------------------------- Y-BUMN Pre -------------------------------------
# # DEFINE CHARACTERS
# define k = Character("Brama", color="#472301")

# # IMAGE BACKGROUND
# image acak1 = im.Scale("bg/acak1.webp", 1920, 1080)

# # IMAGE CHARA
# image Brama


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

init python:
    class glitch(renpy.Displayable):
        """
        `randomkey`
            Follows the rules of the random modume's seed function.
            If not set, a random seed is generated when the transform is applied,
            and stays the same afterwards.
            If you want the effect to be random for each render operation, set to None.

        `chroma`
            Boolean, whether to apply the chromatic aberration effect.

        `minbandheight`
            Minimum height of each slice.

        `offset`
            The offset of each slice will be between -offset and offset pixels.

        `nslices`
            Number of slicings to do (the number of slices will be nslices + 1).
            Setting this to 0 is not supported.
            None (the default) makes it random.
        """

        NotSet = object()

        def __init__(self, child, *, randomkey=NotSet, chroma=True, minbandheight=1, offset=30, nslices=None, **properties):
            super().__init__(**properties)
            self.child = renpy.displayable(child)
            if randomkey is self.NotSet:
                randomkey = renpy.random.random()
            self.randomkey = randomkey
            self.chroma = chroma
            self.minbandheight = minbandheight
            self.offset = offset
            self.nslices = nslices

        def render(self, width, height, st, at):
            child = self.child
            child_render = renpy.render(child, width, height, st, at)
            cwidth, cheight = child_render.get_size()
            if not (cwidth and cheight):
                return child_render
            render = renpy.Render(cwidth, cheight)
            randomobj = renpy.random.Random(self.randomkey)
            chroma = self.chroma and renpy.display.render.models
            offset = self.offset
            minbandheight = self.minbandheight
            nslices = self.nslices
            if nslices is None:
                nslices = min(int(cheight/minbandheight), randomobj.randrange(10, 21))

            theights = sorted(randomobj.randrange(int(cheight)+1) for k in range(nslices)) # y coordinates demarcating all the strips
            offt = 0 # next strip's lateral offset
            fheight = 0 # sum of the size of all the strips added this far
            while fheight<cheight:
                # theight is the height of this particular strip
                if theights:
                    theight = max(theights.pop(0)-fheight, minbandheight)
                else:
                    theight = cheight-theight

                slice_render = child_render.subsurface((0, fheight, cwidth, theight))

                if offt and chroma:
                    for color_mask, chponder in (((False, False, True, True), 1.25), ((False, True, False, True), 1.), ((True, False, False, True), .75)):
                        chroma_render = slice_render.subsurface((0, 0, cwidth, theight))
                        chroma_render.add_property("gl_color_mask", color_mask)
                        render.blit(chroma_render, (round(offt*chponder), round(fheight)))

                else:
                    render.blit(slice_render, (offt, round(fheight)))

                fheight += theight
                if offt:
                    offt = 0
                else:
                    offt = randomobj.randrange(-offset, offset+1)

            return render

        def visit(self):
            return [self.child]

    class animated_glitch(glitch):
        """
        Glitches in a way that changes over time, but consistently, unlike glitch(randomkey=None).
        Sets a timeout at the beginning. At the end of each timeout, sets a new one and changes the glitching.

        `timeout_base`
            The time in seconds between two changes of the glitching.
            Can be either single float (or integer) value, or a tuple of two values between which the timeout
            will be chosen following a uniform distribution, respecting the randomkey.
            Defaults to .1 second.

        `timeout_vanilla`
            The length in seconds of the periods of time over which the child will be shown without any glitch.
            Same values and meaning as `timeout_base`, except that if False, the child will never be shown without glitching.
            If `timeout_base` is passed, defaults to the same value. Otherwise, defaults to (1, 3).
        """

        def __init__(self, *args, timeout_base=None, timeout_vanilla=None, **kwargs):
            super().__init__(*args, **kwargs)
            if timeout_vanilla is None:
                if timeout_base is None:
                    timeout_vanilla = (1, 3)
                else:
                    timeout_vanilla = timeout_base
            if timeout_base is None:
                timeout_base = .1

            self.timeout_base = timeout_base
            self.timeout_vanilla = timeout_vanilla
            self.set_timeout(vanilla=(timeout_vanilla is not False))

        def set_timeout(self, vanilla, st=0):
            if vanilla:
                timeout = self.timeout_vanilla
            else:
                timeout = self.timeout_base

            if not isinstance(timeout, (int, float)):
                timeout = renpy.random.Random(self.randomkey).uniform(*timeout)

            self.timeout = timeout + st
            self.showing_vanilla = vanilla

        def render(self, width, height, st, at):
            vanilla = self.showing_vanilla

            if st >= self.timeout:
                randomkey = self.randomkey
                randomobj = renpy.random.Random(randomkey)
                self.randomkey = randomobj.random()

                # determine whether to show vanilla or not
                if vanilla or (self.timeout_vanilla is False):
                    # if we were showing it or if showing it is disabled
                    vanilla = False
                else:
                    vanilla = (randomobj.random() < .3)

                self.set_timeout(vanilla, st)

            renpy.redraw(self, st-self.timeout)

            if vanilla:
                return renpy.render(self.child, width, height, st, at)
            else:
                return super().render(width, height, st, at)

    class squares_glitch(renpy.Displayable):
        """
        `squareside`
            The size, in pixels, of the side of the squares the child image will be cut to. This will
            be adjusted so that all the "squares" (rectangles, really) have the same width and the
            same height, and that none is cut at the borders of the image. Defaults to 20 pixels.

        `chroma`
            The probability for each square to get a chromatic effect. Defaults to .25.

        `permutes`
            The percentage of squares which will be moved to another square's place. If not passed,
            defaults to a random value between .1 and .4.
        """

        NotSet = object()

        def __init__(self, child, *args, randomkey=NotSet, **kwargs):
            super().__init__()
            self.child = renpy.displayable(child)
            self.args = args
            if randomkey is self.NotSet:
                randomkey = renpy.random.random()
            self.randomkey = randomkey
            self.kwargs = kwargs

        def render(self, width, height, st, at):
            cwidth, cheight = renpy.render(self.child, width, height, st, at).get_size()
            return renpy.render(self.glitch(self.child,
                                            cwidth, cheight, renpy.random.Random(self.randomkey),
                                            *self.args, **self.kwargs),
                                width, height,
                                st, at)

        @staticmethod
        def glitch(child, cwidth, cheight, randomobj, squareside=20, chroma=.25, permutes=None):
            if not renpy.display.render.models:
                chroma = False
            if not (cwidth and cheight):
                return child

            ncols = round(cwidth/squareside)
            nrows = round(cheight/squareside)
            square_width = absolute(cwidth/ncols)
            square_height = absolute(cheight/nrows)

            lizt = []
            for y in range(nrows):
                for x in range(ncols):
                    lizt.append(Transform(child,
                                            crop=(absolute(x*square_width), absolute(y*square_height), square_width, square_height),
                                            subpixel=True,
                                            ))

            if permutes is None:
                permutes = randomobj.randrange(10, 40)/100 # between 10% and 40%
            permutes = round(permutes*ncols*nrows)
            permute_a = randomobj.sample(range(ncols*nrows), permutes)
            permute_b = randomobj.sample(range(ncols*nrows), permutes)

            for a, b in zip(permute_a, permute_b):
                lizt[a], lizt[b] = lizt[b], lizt[a]

            for k, el in enumerate(lizt):
                if randomobj.random() < chroma:
                    lizt[k] = Transform(el,
                                        gl_color_mask=(randomobj.random()<.33, randomobj.random()<.33, randomobj.random()<.33, True),
                                        # matrixcolor=HueMatrix(randomobj.random()*360),
                                        )

            return Grid(ncols, nrows, *lizt)

        def __eq__(self, other):
            return (type(self) == type(other)) and (self.args == other.args) and (self.kwargs == other.kwargs)
