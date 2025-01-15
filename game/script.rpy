# # ------------------------------------- SCRIPT X - SMA -------------------------------------# #
# DEFINE CHARACTERS
define k = Character("Brama", color="#86ccec")
define r = Character("Arya", color="#ffd54a")
define i = Character('Ibu', color="#ffffff")
define ay = Character('Ayah', color="#ffffff")

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
image rakbuku = im.Scale("mini/buku/awal.jpg", 1920,1080)
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
    At("chara/kaos_bram/kosong.png", glitch)
    pause 0.2
    At("chara/kaos_bram/kosong.png", animated_glitch)
    pause 0.2
    At("chara/kaos_bram/kosong.png", glitch)
    pause 0.1
    At("chara/kaos_bram/kosong.png", animated_glitch)
    pause 0.1
    At("chara/kaos_bram/kosong.png", glitch)
    pause 0.3
    At("chara/kaos_bram/kosong.png", animated_glitch)
    pause 1.0
    repeat
image Arya Marah Glitch:
    At("chara/kaos_ar/kesal.png", glitch)
    pause 0.2
    At("chara/kaos_ar/kesal.png", animated_glitch)
    pause 0.2
    At("chara/kaos_ar/kesal.png", glitch)
    pause 0.1
    At("chara/kaos_ar/kesal.png", animated_glitch)
    pause 0.1
    At("chara/kaos_ar/kesal.png", glitch)
    pause 0.3
    At("chara/kaos_ar/kesal.png", animated_glitch)
    pause 1.0
    repeat
image Arya Menangis Glitch:
    At("chara/kaos_ar/marah.png", glitch)
    pause 0.2
    At("chara/kaos_ar/marah.png", squares_glitch)
    pause 0.2
    At("chara/kaos_ar/marah.png", glitch)
    pause 0.1
    At("chara/kaos_ar/marah.png", squares_glitch)
    pause 0.1
    At("chara/kaos_ar/marah.png", glitch)
    pause 0.3
    At("chara/kaos_ar/marah.png", squares_glitch)
    pause 1.0
    repeat

image Arya Serius Glitch:
    At("chara/sma_arya/SERIOUS.png", glitch)
    zoom 2
    pause 0.2
    At("chara/sma_arya/SERIOUS.png", animated_glitch)
    pause 0.2
    At("chara/sma_arya/SERIOUS.png", glitch)
    pause 0.1
    At("chara/sma_arya/SERIOUS.png", animated_glitch)
    pause 0.1
    At("chara/sma_arya/SERIOUS.png", glitch)
    pause 0.3
    At("chara/sma_arya/SERIOUS.png", animated_glitch)
    pause 1.0
    repeat

image Bramaos : 
    "chara/kaos_bram/biasa.png"
    zoom 3
image Bramaos K : 
    "chara/kaos_bram/kosong.png"
    zoom 3
image Bramaos M: 
    "chara/kaos_bram/marah.png"
    zoom 3
image Bramaos B: 
    "chara/kaos_bram/bahagia.png"
    zoom 3

image Aryaos: 
    "chara/kaos_ar/biasa.png"
    zoom 3
image Aryaos K: 
    "chara/kaos_ar/kesal.png"
    zoom 3
image Aryaos W: 
    "chara/kaos_ar/ketawa.png"
    zoom 3
image Aryaos M: 
    "chara/kaos_ar/marah.png"
    zoom 3

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
    "chara/sma_arya/DISAPPOINTED.png"
    zoom 1.45
image Arya Kaget : 
    "chara/sma_arya/SHOCKED.png"
    zoom 1.45
image Arya Serius : 
    "chara/sma_arya/SERIOUS.png"
    zoom 1.45

image Ayah : 
    "chara/ayah/biasa.png"
    zoom 1.45
image Ayahk : 
    "chara/ayah/kaget.png"
    zoom 1.45
image Ayah us: 
    "chara/ayah/serius.png"
    zoom 1.45
image Ayahw : 
    "chara/ayah/ketawa.png"
    zoom 1.45
image Ayahs : 
    "chara/ayah/senyum.png"
    zoom 1.45

image Ibu : 
    "chara/ibu/biasa.png"
    zoom 1.45
image Ibum : 
    "chara/ibu/marah.png"
    zoom 1.45
image Ibuf : 
    "chara/ibu/fikir.png"
    zoom 1.45
image Ibu malu : 
    "chara/ibu/malu.png"
    zoom 1.45
image Ibu sed : 
    "chara/ibu/sedih.png"
    zoom 1.45
image Ibus : 
    "chara/ibu/senyum.png"
    zoom 1.45
image Ibu us : 
    "chara/ibu/serius.png"
    zoom 1.45

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


    # Menampilkan disclaimer
    scene black
    show text "Semua nama, karakter, tempat, dan peristiwa dalam game ini bersifat fiksi. Jika terdapat kesamaan dengan nama, karakter, tempat, atau peristiwa nyata, hal tersebut hanyalah kebetulan belaka." with fade
    pause 3.0

   

    play music "audio/semoga tense.wav"

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
        zoom 3
    "(DENTUMAN PISTOL)"
    hide Brama Glitch
    show Bramaos at cpos:
        zoom 2.5
    k "...."
   
    scene kamartidur
    with dissolve
    stop music
    "(seketika Brama bangun dari tidur bersamaan dengan suara pistol)"
    play sound "audio/nafasberat.mp3"
    "(nafas berat terengah-engah)"

    show Arya Serius at acpos

    with fade
    r "Mimpi buruk lagi ya lu?"

    menu:
        "Iya kak..":
            play music "audio/idle.wav"
            jump y1
        ".....":
            play music "audio/idle.wav"
            jump t1
    

label y1:
    show Bramaos at lpos
    show Arya at arpos

    show Bramaos at lpos
    k "iya kak..."
    show Arya Bingung at arpos
    r "terus-terusan mimpi 
        buruk? kenapa sih?"
    show Bramaos B at lpos
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
    show Bramaos at lpos
    show Arya at arpos
    show Bramaos K at lpos
    k '...'
    show Arya Kesal at arpos
    r 'yeuu malah bengong'
    show Arya Lega at arpos
    r ' lu kalo ada apa-apa
        cerita aja ke gw. 
        gini-gini gw kakak lu'
    show Arya at arpos
    show Bramaos K 
    k '...'
    hide Arya
    show Bramaos K at cpos:
        zoom 2
    '(tatapan kosong menyelimuti wajah Brama)'

    jump m1

image jadwal = im.Scale("cutscene/x/jadwal.jpeg", 1920, 1080)
label m1:
    hide Bramaos
    hide Arya

    i 'naaaak, Brama, Arya, ayo sarapan'
    ay 'ayo turun nak. Jangan sampe telat sekolah'
    '(suara ayah ibu terdengar dari luar kamar)'

    show Bramaos M at lpos
    k 'EH IYA SEKARANG JAM BERAPA?'
    '(panik karena bangun kesiangan)'
    show Arya Bahagia at arpos
    r 'slow aja masih 5.30'
    '(Arya bersantai karena sudah siap-siap duluan)'
    hide Arya

    show Arya at arpos
    #[Arya sudah rapi dengan pakaian dan perlengkapannya]
    show Bramaos M at lpos
    k 'MANA BISA GITU anjing, SEKOLAH KITA JAUH'
    show Arya Ketawa at arpos
    r 'wkwkwk'
    #[Arya tertawa kecil]
    show Bramaos at lpos
    r 'dah sana buruan siap-siap, gw tunggu sambil sarapan'
    hide Arya
    show Bramaos at lpos
    k 'oke hari ini jadwal kita olahraga, matematika, sama biologi'
    '(Brama sambil melihat selebaran jadwal yang nempel di dinding)'
    show jadwal at left
    pause 2
    hide jadwal
    show Bramaos at lpos
    #[jadwal pelajaran sekolah SMA Cendekia Maju di selebaran kertas]
    k 'hmmmm berarti gw harus bawa buku, baju ganti, sama
            kalkulator'
    k 'pertama, buku yang harus gw bawa berarti buku olahraga, buku 
            matematika, buku biologi'
    
    #(mini game milih buku di rak)
    jump minibuku

image rakakhir = im.Scale("mini/buku/akhir.jpg", 1920,1080)
image rakbio = im.Scale("mini/buku/bioambil.jpg", 1920,1080)
image rakmtk = im.Scale("mini/buku/mtkambil.jpg", 1920,1080)
image rakolah = im.Scale("mini/buku/olahraga ambil.jpg", 1920,1080)
image rakbioolah = im.Scale("mini/buku/bioolah.jpg", 1920,1080)
image rakmtkolah = im.Scale("mini/buku/mtkolah.jpg", 1920,1080)
image rakmtkbio = im.Scale("mini/buku/mtkbio.jpg", 1920,1080)
label minibuku:
    scene rakbuku
    show Bramaos:
        xalign 0.9
        yalign -2.5
    $ correct_books = ["Buku Olahraga", "Buku Matematika", "Buku Biologi"]  # Correct books
    $ chosen_books = []  # Store player's choices

    "Brama mulai memilih buku yang harus dibawa dari rak buku."
    hide brama
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
        if "Buku PPKN" not in chosen_books:
            $ options.append("Buku PPKN")

        # Display the menu with available options
        menu:
            "Pilih buku untuk dibawa:"

            # Add each option dynamically
            "Buku PPKN" if "Buku PPKN" in options:
                $ chosen_books.append("Buku PPKN")
                "Brama mengambil Buku PPKN."

            "Buku Olahraga" if "Buku Olahraga" in options:
                $ chosen_books.append("Buku Olahraga")
                if "Buku Biologi" in options:
                    if "Buku Matematika" in options:
                        scene rakolah
                    else:
                        scene rakmtkolah
                elif "Buku Matematika" in options:
                    if "Buku Biologi" in options:
                        scene rakolah
                    else:
                        scene rakbioolah
                else:
                    scene rakakhir
                "Brama mengambil Buku Olahraga."

            "Buku Matematika" if "Buku Matematika" in options:
                $ chosen_books.append("Buku Matematika")
                if "Buku Olahraga" in options:
                    if "Buku Biologi" in options:
                        scene rakmtk
                    else:
                        scene rakmtkbio
                elif "Buku Biologi" in options:
                    if "Buku Olahraga" in options:
                        scene rakmtk
                    else:
                        scene rakmtkolah
                else:
                    scene rakakhir
                "Brama mengambil Buku Matematika."

            "Buku Sejarah" if "Buku Sejarah" in options:
                $ chosen_books.append("Buku Sejarah")
                "Brama mengambil Buku Sejarah."

            "Buku Biologi" if "Buku Biologi" in options:
                $ chosen_books.append("Buku Biologi")
                if "Buku Olahraga" in options:
                    if "Buku Matematika" in options:
                        scene rakbio
                    else:
                        scene rakmtkbio
                elif "Buku Matematika" in options:
                    if "Buku Olahraga" in options:
                        scene rakbio
                    else:
                        scene rakbioolah
                else:
                    scene rakakhir
                "Brama mengambil Buku Biologi."

            "Buku Fisika" if "Buku Fisika" in options:
                $ chosen_books.append("Buku Fisika")
                "Brama mengambil Buku Fisika."

    # Check if the player's choices are correct
    $ correct_count = sum(1 for book in chosen_books if book in correct_books)

    if correct_count == 3:
        "Brama: Hmmm... Semua buku yang gw pilih udah bener."
        jump kalku
    else:
        "Brama: Aduh, kayaknya ada buku yang salah deh."
        $ chosen_books = []
        jump minibuku
            
#minigame pilih baju blm
#minigame pilih kalkulator
image laci = im.Scale("cutscene/x/laci.png", 1920, 1080)
image atk = im.Scale("cutscene/x/atk.png", 1080, 720)
label kalku:
    scene kamartidur
    show Brama Bahagia at cpos
    k 'yes terakhir, kalkulator'
    hide Brama Bahagia
    show laci
    show atk:
        zoom 1
        xalign 0.5
        yalign 0.3
    k 'bukan ini deh, kok gaada ya'
    k 'aku yakin taruh sini kok'
    hide laci
    hide atk 
    show Brama Marah at cpos
    k 'wah ini pasti ulah Arya'
    '(Kamil pun datang ke ruangan meja makan nyamperin Ridwan)'
    jump ruangmakan

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
    show Ibum at Position(xalign=0.8, yalign=0.1)
    i "Aduhh kalian ini gaada kerjaan yang lebih baik kah selain berantem terus?"
    i "Ibu berani sumpah tembok di rumah ini lebih sering dengerin kalian berantem daripada dengerin omongan baik."
    show Ayah us at Position(xalign=0.3, yalign=0.1)
    show Ibu us at Position(xalign=0.8, yalign=0.1)
    ay "Udah nak, jangan berantem lagi."
    i "Marahin pak anaknya!"
    ay "Brama, kalkulator kamu Ayah yang pinjam semalam waktu kamu tidur."
    ay "Maaf ya nak, Ayah lupa ngembaliin kalkulator kamu ke tempatnya."
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
    stop music

    # Time skip
    play sound "audio/ngetik.mp3"
    scene black with fade
    show slide1
    pause 1
    stop sound
    scene depanrumah with fade
    show Arya at arpos
    show Brama Bingung at lpos
    play music "audio/idle.wav"
    k "Arya, lu udah siap belom?"
    show Arya Ketawa at arpos
    r "Udah, yok berangkat."
    show Arya at arpos
    show Brama Bahagia at lpos
    k "Buuu, Yah. Kita berangkat yaa."
    show Brama at lpos
    show Ayah at Position(xalign=0.3, yalign=0.1)
    ay "Ya nak, hati-hati di jalan ya."
    show Ibu at Position(xalign=0.8, yalign=0.1)
    i "Barang gaada yang ketinggalan?"
    show Arya Ketawa at arpos
    r "Aku udah kebawa semua sih harusnya."
    show Arya at arpos
    show Brama Bahagia at lpos
    k "Amannn."
    show Brama Bingung at lpos
    show Arya Ketawa at arpos
    hide Ayah
    hide Ibu
    r "Mau lu atau gw yang bawa motor?" 

    menu:
        "gw aja gapapa, ntar baliknya lu":
            jump motorbima
        "lu aja yang bawa":
            jump motorarya

define motorkamil = False
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
    define motorkamil = True
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
    define motorkamil = False
    jump gerbangsekolah

image slide2 = im.Scale("text/X-SMA/Slide2.png", 1920, 1080)
label gerbangsekolah:
    play sound "audio/trans1.wav"
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

init python:
    # Import the minigame logic
    # minigame.py

    # Minigame logic variables and functions
    bg_yoffset = 0
    player_x, player_y = 500, 600
    police_cars = [{"x": 300, "y": -100}]
    score = 0
    player_speed = 50
    police_speed = 60

    # def move_player(dx, dy):
    #     global player_x, player_y
    #     player_x = max(0, min(1500, player_x + dx))  # Keep within screen bounds
    #     player_y = max(100, min(375, player_y + dy))
    #     print(f"Player move to: ({player_x}, {player_y})")
    def move_player(dx, dy):
        global player_x, player_y

        # Define lane positions
        lane_1 = 255  # Middle of lane 1
        lane_2 = 720  # Middle of lane 2
        lane_3 = 1175  # Middle of lane 3
        lane_4 = 50   # Far left lane
        lane_5 = 1400  # Far right lane

        # Snap player to nearest lane
        if dx < 0:  # Moving left
            if player_x > lane_2:
                player_x = lane_2
            elif player_x > lane_1:
                player_x = lane_1
            elif player_x > lane_4:
                player_x = lane_4
        elif dx > 0:  # Moving right
            if player_x < lane_2:
                player_x = lane_2
            elif player_x < lane_3:
                player_x = lane_3
            elif player_x < lane_5:
                player_x = lane_5

        # Vertical movement (if needed)
        player_y = max(100, min(375, player_y + dy))
        print(f"Player move to: ({player_x}, {player_y})")

            

    def update_police_cars():
        global police_cars, player_x, player_y, police_speed
        # Smaller increments for smoother movement
        movement_increment = 50  # Change this value to adjust the speed of the movement
        
        for car in police_cars:
            car["y"] += movement_increment  # Move police car down by a small increment
            if car["y"] > 1000:  # Remove car if it goes off-screen
                police_cars.remove(car)

        # Spawn new police cars
        import random
        if random.random() < 0.02:
            # Randomly spawn cars at different x positions
            car_x = random.choice([300, 500, 700, 900, 1100,])  # Example x positions
            police_cars.append({"x": car_x, "y": -100})  # Start cars off-screen


    def check_collision():
        global player_x, player_y, police_cars
        for car in police_cars:
            if abs(car["x"] - player_x) < 80 and abs(car["y"] - player_y) < 80:
                return True  # Collision detected
        return False

    def check_collisionroad():
        global player_x, player_y, police_cars
        if player_x < 100 or player_x > 1300:
            return True  # Collision detected
        return False

    # Update road scrolling
    def update_background():
        global bg_yoffset
        bg_yoffset += 40
        if bg_yoffset >= 1080:
            bg_yoffset = 10

# The game starts here.

label mininabrak:
    stop music
    play music "audio/motor.mp3"
    scene black
    call screen chase_game

# Minigame Screens
screen scrolling_background:
    add "mini/nyetir/sh.png" ypos bg_yoffset zoom 2.5
    add "mini/nyetir/bg.png" ypos bg_yoffset zoom 2.5
    add "mini/nyetir/bg.png" ypos (bg_yoffset - 1080) zoom 2.5
    timer 0.039 repeat True action Function(update_background)
    

screen chase_game():
    use scrolling_background

    # Display score
    text "Score: [score]" at top

    # Display player car
    if motorkamil:
        add im.Scale("mini/nyetir/pergisekolah.png", 500, 700) pos (player_x, player_y)
    else:
        add im.Scale("mini/nyetir/ngambillaporan.png", 500, 700) pos (player_x, player_y)
    
    # Spawn police cars
    for car in police_cars:
        add im.Scale("mini/nyetir/r1.png", 500, 700) pos (car["x"], car["y"])
        add im.Scale("mini/nyetir/r2.png", 500, 700) pos (car["x"], car["y"])

    timer 0.1 repeat True action [
        Function(update_police_cars),
        If(check_collision(), Jump("nabrak")),
        If(check_collisionroad(), Jump("nabrak")),
        SetVariable("score", score + 1), 
        If(score >= 250, Jump("ganabrak")),

    ]

    key "K_LEFT" action Function(move_player, -player_speed, 0)
    key "K_RIGHT" action Function(move_player, player_speed, 0)

image slide3 = im.Scale("text/X-SMA/Slide3.png", 1920, 1080)
image slide5 = im.Scale("text/X-SMA/Slide5.png", 1920, 1080)
label ganabrak:
    stop music
    play music "audio/idle.wav"
    play sound "audio/trans1.wav"
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
    play sound "audio/ngetik.mp3"
    scene black with fade
    show slide5
    pause 1
    stop sound
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

define sat = Character('Satpam', color="#827a7a")
image slide4 = im.Scale("text/X-SMA/Slide4.png", 1920, 1080)
image slide6 = im.Scale("text/X-SMA/Slide6.png", 1920, 1080)
image slide7 = im.Scale("text/X-SMA/Slide7.png", 1920, 1080)
label nabrak:
    play sound "audio/ckit.mp3"
    stop music
    scene black with fade
    show slide4
    pause 1
    scene depanrumah with fade
    stop sound
    show Brama Cemas at lpos
    show Arya Kesal at arpos
    play music "audio/idle.wav"
    'sampai rumah'
    r "Wah gila, buruan ambil, kita udah telat gara lu nabrak si."
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
    play sound "audio/ngetik.mp3"
    scene black with fade
    show slide6
    pause 1
    stop sound
    scene gerbangsekolah with fade
    "07.07 gerbang sekolah."
    show Brama Cemas at lpos
    show Arya Kesala at arpos
    r "Waduh, mampus, kita telat."
    show Brama Kosong at lpos
    k "Wah iya anjing."
    show male at ncpos
    sat "Kenapa telat? Tunggu di luar dulu."
    show Brama Malu at lpos
    k "Tapi Pak…"
    sat "Ga ada tapi-tapi. Tunggu guru BK ke sini."
    hide male
    show Arya Kesal at arpos
    r "Yah, dihukum deh kita."
    show Brama Kosong at lpos
    k "Iya kak, gw minta maaf ya jadi bawa lu di sini."
    show Arya Bahagia at arpos
    r "Dah gapapa. Udah makanan sehari-sehari ngadep guru BK."
    play sound "audio/trans1.wav"
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
    stop music
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
    play music "audio/idle.wav"
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
    play sound "audio/ngetik.mp3"
    scene black with fade
    show slide8
    pause 1
    stop sound
    scene rumah_sore with fade
    show Arya at arpos
    show Brama at lpos


    show Ayahw at cpos
    ay "Eehh, jagoan-jagoan Ayah udah pulang!"
    show Arya Lega at arpos
    r "Hehe, iya Yah, udah kelar sekolahnya."
    show Arya at arpos
    show Brama Bingung at lpos
    k "…" # (masih speechless kelakuan Arya)
    show Ibu at rpos
    i "Tadi gimana sekolahnya? Sampe bolak-balik gitu kalian?"
    show Ayah at cpos
    ay "Tadi kalian balik pulang?"

    show Ibus at rpos
    i "Iya Yah, tadi baru banget Ayah berangkat kerja mereka balik pulang."
    show Brama Malu at lpos
    k "Iya Yah, hehe, laporan Brama ketinggalan."
    show Ayah at cpos
    ay "Wah kacau, lain kali bener-bener dicek ya, jangan sampe ada yang lupa."
    show Arya Lega at arpos
    r "Walah, Ayah aja lupa ngembaliin kalkulator sampe tantrum tuh si anak."
    show Arya at arpos
    show Brama Bingung at lpos
    k "Diem ya lu."
    show Arya Bahagia at arpos
    show Ayahw at cpos
    ay "HAHAHAHA, namanya juga udah bapak-bapak pasti lupaan."

    # Transition to the birthday moment
    show Ayahw at cpos
    i "Ngomong-ngomong, Brama, Arya, kalian inget nggak sekarang hari apa?"
    show Arya Bingung at arpos
    r "Hari Kamis?"
    show Brama Bahagia at lpos
    k "OH, HARI ULANG TAHUN AYAH!"
    show Arya Kaget at arpos
    r "OIYAA!"
    show Arya Bahagia at arpos
    show Ayahw at cpos
    ay "HAHAHAHA. Ternyata masih ada yang inget ulang tahun Ayah."
    show Ibus at rpos
    i "Kita harus ucapin apa, nakk? Satu, dua, tiga…"
    show Arya Ketawa at arpos
    show Brama Bahagia at lpos
    "Selamat ulang tahun Ayahhh!"
    show Ayahw at cpos
    ay "Hahahaha, terima kasih yaa nak, Ibu."
    show Ibus at rpos
    i "Jadiii… buat ngerayain ulang tahun Ayah, kita mau makan-makan dimana inii??"
    show Ayahw at cpos
    ay "Hahahaha, sok kalian tentukan. Ayah ngikut dan tinggal bayar aja. HAHAHAHA."

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
image slide9 = im.Scale("text/X-SMA/Slide9.png", 1920, 1080)
label makanmakan:
    i "Yaudah yuk kita siap-siap dan beberes. Habis maghrib kita berangkat yaa!"
    k "Mau makan di mana kita, Bu?"
    i "Sarinah oke ngga, Ayah?"
    ay "Yaaa… kalau Ayah sih oke aja asal belanjanya ngga sampai 1 juta. HAHAHAHAHA!"
    r "Ya kalau ada 1 juta mah mending buat beli TV lagi, taruh di kamar Arya."
    ay "Yeuuu, enak aja kamu!"
    show Arya Ketawa at arpos
    ay "Udah, sana siap-siap."
    stop music
    # Time skip to evening preparation
    play sound "audio/transserem.wav"
    scene black with fade
    show slide9
    pause 1
    play music "audio/idle.wav"
    scene kamar with fade
    show Bramaos at lpos
    k "Kak, lu udah siap belom?"
    show Aryaos W at rpos
    r "Lihat aja gw, udah cakep gini."
    k "Kali aja lu mau ngapain lagi kek."
    show Aryaos K at rpos
    r "Ah, gw ngga seribet itu orangnya."
    k "Oh iya, ngomong-ngomong soal dompet tadi..."
    show Bramaos K at lpos
    r "Udah lah, Bram, mau dipanjangin sampai kapan lagi?"
    k "Nggak gitu, gw mau ngomong sesuatu sama lu."
    r "Apa?"

    menu:
        "Reimburse dompet":
            jump reemburse

        "Arya salah":
            jump aryasalah

label reemburse:
    k "Sebenernya waktu gw tadi minta nyusul karena kencing, gw ketemu Ujang."
    show Bramaos B at lpos
    r "Terus?"
    k "Dompet itu, ternyata dompet Ujang."
    r "Ujang anak bahasa itu?"
    k "Iya."
    show Aryaos K at rpos
    r "Ngaku-ngaku aja kali. Orang di dompetnya gaada kartu identitas sama sekali."
    k "Tapi dia nyebutin ciri-ciri dompet yang sama persis, dan nominalnya sama persis yang lu ambil."
    show Bramaos at lpos
    r "Yaelah, terus gimana?"
    k "Dia bilang dia lagi butuh banget duitnya buat makan seminggu."
    k "Karena itu duit lu ambil, jadinya gw ga enak ke Ujang."
    show Aryaos at rpos
    r "Ngapain pake ga enak, yaudah lah itu kesialan Ujang."
    k "Mana bisa gitu Arya. Akhirnya duit Ujang gw ganti. Gw bilang gw yang nemu dompetnya."
    show Aryaos K at rpos
    r "Lah, tapi kan dompetnya masih ada di gw. Gimana lu ngembaliinnya?"
    k "Iya, gw bilang dompetnya masih lu amanin, jadi duitnya dulu yang gw kasih ke dia."
    show Bramaos at lpos
    r "Berarti ini dompet mau dibalikin besok?"
    k "Iya. Sekalian gw sekarang mau minta duit gw lu balikin."
    r "Heuuuhh. Percuma tadi debat panjang lebar, ujung-ujungnya ga jadi rezeki."

    jump ibutibatiba

label aryasalah:
    k "…"
    show Bramaos at lpos
    k "(Bingung mau gimana ngomongnya.)"
    show Aryaos  at rpos
    r "Kenapa, Bram?"
    k "Gapapa, ga jadi Arya."
    show Aryaos K at rpos
    r "Hufft."
    r "(Menghela nafas.)"
    show Aryaos at rpos
    r "Gini Bram, dunia ini ngga akan pernah adil Bram."
    r "Lu lihat aja para pejabat di Senayan sana."
    show Aryaos M at rpos
    r "Lu lihat aja tahun kemarin gimana bobroknya presiden kita?"
    r "Kesengsaraan rakyat ga pernah mereka dengar, Bram!"
    show Aryaos K at rpos
    r "Dunia ini ga akan pernah adil, Bram."
    show Aryaos W at rpos
    r "Kehidupan ini ibarat bertahan di tengah hutan rimba."
    r "Lu harus bisa survive gimanapun caranya."
    show Aryaos K at rpos
    r "Lihat tuh Ayah. Ayah jadi polisi harus jual sawah kakek dulu, Bram!"
    k "Tapi…"
    show Aryaos at rpos
    r "Tapi apa, Bram?"
    k "Lihat Pak Habibie, Arya. Rupiah kita sekarang menguat banget."
    k "Pak Habibie, Arya! Dia mau berjuang untuk masyarakat."
    show Aryaos M at rpos
    k "Kalo ibarat lu kehidupan ini adalah hutan belantara, beliau masih bisa sukses tanpa harus merugikan orang lain, Arya!"
    show Aryaos K at rpos
    r "Pak Habibie itu punya otak, Bram! Ga kaya aku yang goblok ini."
    r "Bagi kami yang goblok ini akan terus-terusan dibodohi dan ga akan bisa maju."
    r "Cara satu-satunya bagi kami bisa bertahan hidup ya dengan mengusahakan segala cara!"

    jump ibutibatiba

label ibutibatiba:
    i "Eeeh, ini ada apa ya ribut-ribut?" #(berbicara dari luar kamar)
    i "Udah siap belom kalian?"
    show Aryaos at rpos
    r "Udah, Bu." #(membalas dari dalam kamar)
    show Aryaos K at rpos
    r "Nanti kita bahas lagi." 
    "(berbisik Arya)"
    show Aryaos M at rpos
    r "Gw gamau kesenangan ulang tahun Ayah harus diganggu dengan masalah dompet."
    k "Ya."

    scene black with fade
    pause 0.5

    scene ruangtamu with fade
    show Bramaos at lpos
    k "Kita udah siap nih, Bu."
    show Aryaos W at rpos
    i "Widihh, udah cakep-cakep nih."
    show Aryaos at rpos
    r "Ayah mana, Bu?"
    i "Ayah masih di kamar mandi, lagi mual-mual."
    
    show Aryaos K at rpos
    ay "Haloo, udah siap?" #(Ayah keluar dari kamar mandi)
    k "Ayah sakit? Ayah kalo ga enak badan ngga usah dipaksain makan di luar, yah."
    show Aryaos  at rpos
    r "Iya, kita masih bisa ngerayain di rumah kok, Yah."
    show Aryaos K at rpos
    i "Tuh kan, Ibu bilang apa tadi."
    show Aryaos W at rpos
    ay "Gapapa kok, Ayah lagi merasa ga enak aja perasaannya, ga tau kenapa ya."
    show Aryaos at rpos
    ay "Apa mungkin Ayah ngga rela kehilangan uang sampe 1 juta? Hahahahaha."
    show Aryaos K at rpos
    i "Ih Ayah, Ayah beneran gapapa?"
    ay "Iya gapapa. Ayah sehat kok. Yok berangkat habis ini."
    k "Syukurlah. Yaudah, ayok kita berangkat."
    show Aryaos W at rpos
    r "Yokkk!"
    ay "Brama, kamu yang bawa mobilnya ya."
    show Aryaos K at rpos
    k "Eh, kok aku, Yah? Kenapa ngga Kak Arya aja?"
    r "Udah lu aja, udah punya SIM juga."
    show Aryaos W at rpos
    i "Ya sekali-kali lah, Nak. Mumpung udah ada SIM."
    i "Kasihan kakak kamu yang nyetir mulu."
    ay "Hahahaha, Ayah juga pengen tau gimana skill kamu nyetir."
    show Bramaos B at lpos
    k "Baikkk, siap komandan!"

    scene jalanan_malam with fade
    show Bramaos at lpos
    k "Oke, ayo kita mulai jalan. Doain aja semuanya lancar!"
    
    jump sampei

# label minigame_nyetir:
#     menu:
#         '(gagal minigame (lama sampai))':
#             jump lamatpsampe
#         '(minigame berhasil)':
#             jump sampei
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

image sarinah_dari_depan = im.Scale("bg/sarinah depan.jpg", 1920, 1080)
label sampei:
    scene jakarta_malam
    show Bramaos B at lpos
    k "Alhamdulillah, udah sampe."
    # a sound of the car stopping.
    scene sarinah_dari_depan with fade
    show Aryaos K at rpos
    i "Ayo nak, keburu tutup Sarinah-nya."
    
    ay "Ngghroookk..." 
    #(Ayah ketiduran)R

    jump akhirsampe

label lamatpsampe:
    scene jakarta_malam
    show Bramaos at lpos
    k "Ini beloknya kemana ya?"
    show Aryaos K at rpos
    r "Tau jalan ga sih lu?"
    i "Ayo nak, keburu tutup Sarinah-nya."
    ay "Ngghroookk..." 

    jump akhirsampe

define prpos = Position(xalign=0.9, yalign=0)
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
image staffsep:
    'chara/sepatu/NEUTRAL.png'
    zoom 1.6
image staffsepser:
    'chara/sepatu/SERIOUS.png'
    zoom 1.6

label akhirsampe:
    i "Akhirnya, udah sampe juga."
    r "Fyuhhh, let’s go makannnn."
    scene black with fade
    show slide10
    pause 1
    # Transition to the restaurant scene
    scene restoran_1 with fade
    show fem at nrpos
    staff "Selamat datang. Ini untuk buku menunya. Pesanan langsung ditulis di sini ya…"
    
    show Bramaos B at lpos
    k "Ayah, Ibu, Kak, mau pesen apa? Brama aja yang nulisin."
    # Start the mini-game to order food here.
    #call mini_game_order_food
    
    staff "Baik, mohon ditunggu sebentar ya..."
    hide fem
    i "Senengnyaa, jarang-jarang kita makan di restoran."
    ay "Ya ngapain toh repot-repot ke restoran kalau masakan ibu itu yang terenak di dunia."
    i "Alah-alah masa sih ayah?"
    ay "Loh iya dong, Arya, Brama, 20 tahun nikah sama ibu, ga pernah sekalipun ayah ngga habisin masakan ibu."
    show Aryaos W at rpos
    r "Hahahaha, keliatan banget sih emang dari perutnya."
    ay "HAHAHAHA!"
    k "Hahaha, ayah mah emang di mana-mana makannya banyak."
    i "Ih, percaya ga sih kalian, dulu ayah waktu masih bujang tuh badannya bagus tau."
    i "Ganteng dan gagah."
    show Aryaos K at rpos
    i "Kalau sekarang, ih, gantengnya emang masih iya, tapi gagahnya berubah jadi gajah."
    ay "HAHAHA, ah ibu ini bisa aja."
    show Aryaos at rpos
    i "Iya, ayah kan dulu juga ga kalah keren dari Brama dan Arya."
    
    # Staff brings the food.
    show fem at ncpos
    staff "Silakan… (menyajikan makanan)"
    staff "Untuk pesanannya sudah lengkap ya?"
    k "Mmmmm, udah kak, terima kasih ya…"
    staff "Terima kasih kembali."
    hide fem 
    
    # Transition to eating and wrapping up at the restaurant.
    scene black with fade
    show slide11
    pause 1
    scene restoran_1 with fade
    show Bramaos at lpos
    show Aryaos W at rpos
    ay "Alhamdulillah kenyang."
    i "Alhamdulillah, seneng banget deh yah, makasih yaaa."
    k "Besok traktir sop buntut dong yah."
    ay "Wah tunggu ayah gajian lagi ya hahahaha."
    i "Brama, Arya, minta tolong bayarin ke kasir ya, ini bawa dompet ibu."
    show Aryaos W at rpos
    r "Siap."
    stop music
    
    # At the cashier.
    play sound "audio/transserem.wav"
    scene black with fade
    show slide12
    pause 1
    scene kasir with fade
    show Bramaos  at lpos
    show Aryaos W at rpos
    k "Meja nomor 5, totalnya berapa kak?"
    show fem at ncpos
    staff "Totalnya jadi Rp120.000."
    show Bramaos B at lpos
    k "Okee, ini kak."
    "Brama memberikan uang"
    staff "Uangnya pas ya? Terima kasih."
    k "Sama-sama kak."
    hide fem
    scene restoran_1 with fade
    show Bramaos  at lpos
    show Aryaos K at rpos
    r "Mahal amat ya sampe abis segitu."
    show Bramaos B at lpos
    k "Yaelah bro, kita makan di Sarinah, beli sate berapa banyak juga tadi?"
    show Aryaos at rpos
    r "Yaaa, iya sihh."

    scene black with fade
    play sound "audio/transserem.wav"
    show slide13
    pause 1
    # The tension builds up as they notice something strange outside.
    scene tokobaju with fade
    show Bramaos at lpos
    k "Eh Arya, lihat deh toko baju sebrang."
    show Aryaos at rpos
    r "Iya? Kenapa?"
    show Bramaos M at lpos
    k "Lihat orang baju item itu? Dia lagi nyolong sepatu ga sih?"
    k "TUH TUH TUH DIA UMPETIN DI TAS DIA SI SEPATUNYA!"
    show Aryaos K at rpos
    r "EH IYA!"
    
    # Arya tries to calm down Brama.
    show Aryaos at rpos
    show Bramaos at lpos
    k "Wah gw harus bilang ke ayah."
    show Aryaos at rpos
    r "Eh, tunggu Bram!"
    show Aryaos K at rpos
    k "Kenapa kak?"
    r "Udah biarin aja, ga usah ikut campur urusan orang."
    show Bramaos K at lpos
    k "Urusan orang? Maksud lu?"
    r "Udah jangan ikut campur, biarin, itu urusan yang punya toko."
    k "Hahhh?? Lu udah gila ya? Itu kriminalitas anjing, sempet-sempetnya lu mikir gitu."
    r "Ya terus kenapa? Apa untungnya buat kita ngurusin dia?!"
    show Bramaos M at lpos
    k "Lu beneran gila ya? Ayah kita polisi loh!"
    k "Ini udah jadi tanggung jawab ayah."
    show Aryaos K at rpos
    r "Yaudah, biarin ngapa sih, ngerepotin aja tau ga sih."
    k "Gw gamau tau, gw harus kasih tau ayah."
    
    # Brama rushes to tell Ayah about the situation.
    play sound "audio/transserem.wav"
    show slide14
    pause 1
    scene kasir with fade
    show Bramaos M at lpos
    k "YAHH! Ada pencuri yahh di toko seberang!!"
    show Ayahk at rpos
    ay "Hmmmh? Gimana gimana?"
    k "Toko baju seberang yah, ada orang nyolong sepatu, Brama lihat dengan mata kepala sendiri."
    show Ayah us at rpos
    ay "Bener Arya?"
    show Aryaos K at Position(xalign=-0.1, yalign=0)
    r "Iya yah."
    show Aryaos at Position(xalign=-0.1, yalign=0)
    ay "Wah ga bener nih, ayok kita samperin."
    i "Dek, emang ga ada satpamnya yang jaga? Ulang tahun ayah masa harus tetep kerja sih?"
    ay "Udah lah bu, ini tanggung jawab ayah."
    ay "Yang mana orangnya?"
    k "Itu yah, yang baju hitam."
    ay "Mana? Ohhh, yang bawa tas itu?"

    # Transition to confrontation with the thief.
    play sound "audio/transserem.wav"
    scene black with fade
    show slide15
    pause 1
    scene tokobaju with fade
    show Ayah us at lpos
    ay "Permisi mas, saya Kompol Susilo, Kapolsek Matraman."
    hide Ayah
    show Badge at lpos
    ay "Saya menerima laporan kecurigaan tindakan pencurian yang melibatkan mas sebagai tersangka."
    hide Badge
    show Ayah us at lpos
    ay "Untuk itu akan saya periksa mas untuk meluruskan apakah dugaan benar atau salah."
    show Pencuri at prpos
    x "Wah, salam kenal pak Susilo. Izin meluruskan, saya tidak mencuri barang apapun di toko ini."
    ay "Maka biarkan saya memeriksa agar dugaan bisa dibantah jika memang tidak ada bukti."
    show staffsep at Position(xalign=1.5, yalign=0)
    staff "Bapak polisi?"
    show Ayahs at lpos
    ay "Iya, ada yang bisa saya bantu?"
    show staffsepser at Position(xalign=1.5, yalign=0)
    staff "Kami kehilangan satu pasang sepatu di rak pajangan A9 pak, sepertinya mas ini adalah pelakunya."
    show Ayah us at lpos
    ay "Mas… menanggapi ini, saya mohon mas untuk kooperatif."
    show Pencuri Panik at prpos

    # Tension builds as X pulls a weapon.
    play music "audio/semoga tense.wav"
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
    play sound "audio/dentumanpistol.mp3"
    "(DENTUMAN PISTOL)"
    # *DENTUMAN GUNSHOT*

    # Transition to chaos after the gunshot.
    # scene glitch_transition with glitch
    hide Pistol Nembak
    show Aryaos M at cpos:
        zoom 1.5
    r "AYAHHHHH!"
    hide Aryaos M

    show Brama Glitch at cpos:
        zoom 3
    k "..."
    hide Brama Glitch
    show Arya Marah Glitch at cpos:
        zoom 3
    r "BRAMA!"
    r "BRAMA!"
    show Arya Menangis Glitch at cpos:
        zoom 3
    r "BRAMA, LIHAT YANG KAMU PERBUAT!!!"
    stop music
    # Glitching effect to show the impact of the incident.
    # This leads into the next part of the story.

    jump ybumn



# # ------------------------------------- SCRIPT Y - BUMN -------------------------------------# #
# # DEFINE CHARACTERS
define o = Character("Others",  color="#e3bb96")
define n = Character("Nina",  color="#6ba7e3")
define ist = Character("Istri",  color="#ffffff")
define ceo = Character("CEO",  color="#ffffff")
define ast = Character("Asisten",  color="#ffffff")
define skre = Character("Sekretaris",  color="#ffffff")
define an = Character("Andi",  color="#ffffff")
define m = Character("Mahfudz",  color="#ffffff")
define staffa = Character("Staff A",  color="#ffffff")
define staffb = Character("Staff B",  color="#ffffff")
define staffm = Character("Staff M",  color="#ffffff")
define staffr = Character("Staff R",  color="#ffffff")
define dir_a = Character("Direktur A", color="#ffffff")
define rs = Character("Rosa", color="#ffffff")
#define narasi = Character("Narasi", color="#472301")

# # IMAGE BACKGROUND
image kamartidur_y = im.Scale("bg/rumahkamil/tidur.png", 1920, 1080)
image ruangmakan_y = im.Scale("bg/rumahkamil/makan.png", 1920, 1080)
image kantorrumah_y = im.Scale("bg/rumahkamil/kantor.png", 1920, 1080)
image terasrumah_y = im.Scale("bg/rumahkamil/teras.png", 1920, 1080)
image bumnkantor = im.Scale("bg/bumn/kantor.png", 1920, 1080)
image bumnlobi = im.Scale("bg/bumn/lobi.png", 1920, 1080)
image bumnlorong = im.Scale("bg/bumn/lorong.png", 1920, 1080)
image bumnrapat = im.Scale("bg/bumn/rapat.png", 1920, 1080)
image pov_arya = im.Scale("text/Y-BUMN/Slide1.PNG", 1920, 1080)
image pov_brama = im.Scale("text/Y-BUMN/Slide2.PNG", 1920, 1080)
image ngaca = im.Scale("tam/ngaca.png", 1920, 1080)

# # IMAGE CHARA
image Brama_y:
    "chara/brama.png"
    zoom 0.5

image abatik:
    "chara/aryabatik.png"
    zoom 1.5

image telfonkabel:
    "single asset/Telfon kabel.png"
    zoom 0.45

image Nina:
    "chara/Nina.png"  
    zoom 0.60

image Istri:
    "chara/istri/biasa.png"  
    zoom 1.6

image Istri s:
    "chara/istri/buka.png"  
    zoom 1.6

image Istri snark:
    "chara/istri/snark.png"  
    zoom 1.6

image male:
    "chara/male.png"  
    zoom 1.4
image male2:
    "chara/male.png"  
    zoom 1.4
image fem:
    "chara/fem.png"  
    zoom 1.4

#Posisi custom bikinan bisa apply to all
define cpos = Position(xalign=0.5, yalign=0)
define rpos = Position(xalign=0.9, yalign=0)
define lpos = Position(xalign=0.1,yalign=0)

# buat arya
define aycpos = Position(xalign=0.5, yalign=0)
define ayrpos = Position(xalign=1.2, yalign=0)
define aylpos = Position(xalign=0, yalign=0)

# buat telpon
define tlcpos = Position(xalign=0.5, yalign=0)
define tlrpos = Position(xalign=1.01, yalign=0.6)
define tllpos = Position(xalign=0,yalign=0)

# buat malefem
define ncpos = Position(xalign=0.5, yalign=-0.14)
define nrpos = Position(xalign=0.9, yalign=-0.14)
define nlpos = Position(xalign=0,yalign=-0.14)

label ybumn: #ybumn
    scene ngaca
    play music sad_bgm
    k "Orang mengatakan kematian itu adalah hal mutlak, tidak dapat dihindarkan."
    k "Tapi yang jadi pertanyaan adalah.."
    k "Kematian seperti apa yang diikhlaskan semua orang?"

    #nunggu full face reveal depan cermin
    b "Kematian ayah harus terjadi karena keegoisan anaknya."
    b "..."
    b "Andai saja waktu dapat berputar."
    b "24 tahun telah berlalu.."
    b "Kedamaian dan kerelaan belum kunjung aku temukan."

    #Brama mendongak ke atas, tampilan dari samping
    #ruangan di kamar mandi
    b "Ayah, apakah engkau kecewa kepadaku?"
    b "Ayah, aku hanya berusaha melakukan yang terbaik."
    #Brama menunduk ke bawah, tampilan masih dari samping]
    b "Apa jalan yang aku pilih sudah benar?"
    b "..."
    #dari atas sampai sini ga ada image karakter yang muncul di kiri kanan, murni karakter background]

    #mulai sini balik ke biasanya, ada karakter di samping kiri kanan]

    o "Tidak salah untuk bersedih dan menyesal."
    o "Fitrah manusia sudah ditetapkan untuk memiliki perasaan."
    o "Sangat wajar jika kamu merasa terpuruk kehilangan ayah."
    o "Terlebih hal itu disebabkan oleh keputusanmu."

    b "..."

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
    b "Kamu benar, Brama."
    b "Takdir tuhan selalu tidak dapat ditebak."
    b "Akan ada saatnya semua orang akan mati."
    b "Termasuk ayah."
    b "..."
    #(suddenly Brama crying) Brama meneteskan air mata]

    k "Tapi apakah aku harus melakukannya?"
    k "Apakah aku bisa merubah masa lalu?"
    stop music
    jump nina

label denial:
    b "Engga, engga, engga!"
    b "Aku ga bisa harus menjalani ini!"
    b "Kenapa ya Allah??"
    #(start to cry) Brama meneteskan air mata]
    b "Kenapa engkau tidak menganugerahi aku otak bodoh dan apatis?"
    b "Ayah seharusnya tidak akan mati karena aku."
    b "..."
    #menunduk sedih]
    stop music
    jump nina

label nina:
    play sound trans1
    scene kamartidur_y with fade
    #(Nina masuk ke kamar Brama dan memanggil Brama, ekspresi Brama kaget terbangun dari lamunannya)
    #{musik make netral}
    show Nina at cpos
    n "Ayahhh!!"
    play music idle

    show Brama_y at lpos
    show Nina at rpos
    b "Iya nak, kenapa nak?"
    n "Ayah-ayah, ayo buruan sarapan udah ditunggu sama bundaaa!"
    n "Bunda udah nunggu lama di meja makan ihh!"
    n "Ayah juga buruuuu, nanti telat berangkat kerjaa!"
    b "Oh hehehe, iya nina, sebentar ya ayah masih harus siap-siap dulu."
    b "Kamu turun duluan ya nak, Ayah 5 menit lagi turun ke bawah."
    n "Okay yah awas kalau lama."
    hide Nina
    #Ekspresi kesal nina]
    show Brama_y at cpos
    b "Haduuhh aku tadi mikirin apa sampai ga sadar gini."
    b "Dah dah, mending aku turun sekarang, terus sarapan dengan anak dan istriku."
    hide Brama_y
    #(time skip) (Brama pergi ke meja makan, istri dan nina udah duduk di kursi) (Brama dan keluarga lagi sarapan di meja makan, Istri bahagia menyambut Brama tapi anak kesal dengan Brama karena terlalu lama)
    #ruang makan]
    #{musik netral lagi}
    scene ruangmakan_y with fade
    show Istri s at cpos
    ist "Pagi ayah, ngapain aja sii lama banget di atasnya?"
    
    menu:
        "Cuci muka":
            jump cucimuka
        "benerin shower":
            jump benerinshower

label cucimuka:
    show Brama_y at lpos
    b "Nggapapa kok sayang, tadi aku cuci muka bentar."
    show Istri at cpos
    ist "Ohhh begituu."
    hide Brama_y
    jump lanjutmakan

label benerinshower:
    show Brama_y at lpos
    k "Nggapapa kok sayang, tadi shower kita bocor."
    k "Jadi aku tadi benerin bentar."
    ist "Loh, rusaknya parah kah?"
    k "Engga kok, Alhamdulillah masih bisa diperbaiki."
    ist "Yauda deh syukurlah."
    hide Brama_y
    jump lanjutmakan

label lanjutmakan:
    show Brama_y at lpos
    show Istri s at cpos
    ist "Eh iya, yuk kita makannn!"
    ist "Nina udah nungguin ayah nih dari tadi nggak turun-turun."
    show Istri at cpos
    show Nina at rpos
    n "Iya nih ayah lama banget nggak tau apa kalau aku udah laper dan nungguin dari tadi."
    k "Hehehe iya sayang maaf ya ayah kelamaan siap-siapnya."
    n "Bunda masak apa pagi ini? Dari jauh aja aku bisa mencium aroma sedap masakan bunda."
    show Istri s at cpos
    ist "Ih bisa aja kamu yah,"
    ist "Aku hari ini masak makanan kesukaan kamu banget nihh."
    ist "Ada udang saus padang sama ayam mentega."
    show Istri at cpos
    k "Wihhhhhhh."
    show Istri s at cpos
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
    scene ruangmakan_y with fade
    show Nina at cpos
    n "Ayah berangkat jam berapa? Ini udah 06.15 loh."
    n "Awas kena macet loh nanti di jalan."
    n "Terus jadi telat deh masuk kantornya."
    show Brama_y at lpos
    show Nina at rpos
    k "Eh iya bener juga makasih ya sayang udah diingetin."
    n "Ayah cek lagi semua barang-barang bawaan ayah jangan sampai ada yang ketinggalan."
    k "Iya sayang, ini udah ayah cek semuanya udah ada di tas ayah."
    k "Wah iyaa, laptop ayah!"
    k "Untung kamu ingetin, Nina."
    k "Kalau nggak laptop ayah bakal ketinggalan di rumah."
    k "Bunda lihat laptop ayah di mana nggak ya? Ayah lupa naruhnya."
    hide Nina
    show Istri s at rpos
    ist "Kemarin bukannya ayah pake di ruang kerja ya?"
    ist "Coba deh ayah cek juga di kamar kalau semisal di ruang kerja nggak ada."
    hide Istri s
    show Nina at rpos
    n "Tuhkan untung aja aku ingetin."
    n "Kalau nggak bisa-bisa ayah balik lagi ke rumah untuk ambil laptop doang."
    k "Iya sayang, makasii yaa."
    hide Nina
    show Brama_y at cpos
    k "Laptop aku di mana ya?"
    k "Aku lupa terakhir kali make aku taruh mana ya?"

    menu:
        "Ruang kerja":
            hide Brama_y
            jump ruangkerja
        "Kamar":
            hide Brama_y
            jump ruangkamar

label ruangkerja:
    scene kantorrumah_y with fade
    show Brama_y at cpos
    k "Laptop kemarin aku taruh mana ya?"
    k "Aduh, ruang kerja ini kok berantakan banget? Aku pasti lupa taruh di mana lagi. Coba periksa dulu…"
    k "Aha! Ini dia! Aku ingat tadi malam aku nge-charge laptop di sini. Untung ketemu."
    hide Brama_y
    jump berangkatkerja

label ruangkamar:
    scene kamartidur_y with fade
    show Brama_y at cpos
    k "Hmmm… laptopku di mana, ya?"
    k "Kemarin aku sempat taruh di sini…"
    k "Atau mungkin di meja kerja?"
    k "Oh, ini diaa. Ternyata tertumpuk oleh buku. Untung ketemu."
    hide Brama_y
    jump berangkatkerja


label berangkatkerja:
    scene terasrumah_y with fade
    show Brama_y at lpos
    k "Ninaaa, makasih yaa nakk udah diingetin."
    show Nina at rpos
    n "Iya, Ayah. Jangan sampai lupa lagi, ya!"
    hide Nina
    show Brama_y at cpos
    k "Maaa, aku berangkat yaa!"
    hide Brama_y
    show Istri s at lpos
    show Nina at rpos
    ist "Iya sayangg, hati hatii!"
    hide Brama_y
    play sound trans1
    stop music
    scene bumnlobi with fade
    show Brama_y at cpos
    play music office_bgm
    k "Fyuh, akhirnya bisa sampai tepat waktu."
    show male at nrpos
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
    show Brama_y at lpos
    show fem at ncpos
    staffb "Pak, tadi pagi ada email dari tim IT tentang pembaruan sistem akuntansi kita."
    k "Oke, lanjut."
    staffb "Mereka butuh konfirmasi Bapak untuk lanjut ke tahap berikutnya."
    k "Oh iya, itu penting. Saya cek nanti. Terima kasih sudah mengingatkan."
    hide fem
    hide male
    show male at lpos
    show Brama_y at cpos
    show fem at rpos
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

image email = im.Scale("tam/email.png", 1920, 1080)
image zoommeeting = im.Scale("tam/zoom.png", 1920, 1080)
image present = im.Scale("tam/present.png", 1920, 1080)
image folder = im.Scale("tam/folder.png", 1920, 1080)
image folderselect = im.Scale("tam/folders.png", 1920, 1080)
image file = im.Scale("tam/select.png", 1920, 1080)
image filesend = im.Scale("tam/send.png", 1920, 1080)
label mulaikerja:
    ast "Baik pak, ada lagi yang perlu saya siapkan?"
    k "Oh iya, setelah ini saya langsung ke ruangan saya."
    k "Nanti langsung antarkan ke sana saja."
    ast "Baik pak."
    hide Brama_y

    scene bumnkantor with fade
    show Brama_y at cpos
    k "hmmm..."
    scene email
    #(Kamil membaca email dengan serius. Di dalamnya ada laporan mengenai kondisi keuangan perusahaan dan persiapan untuk presentasi di meeting direksi)
    #[menunjukan screen tampilan email] → screenshot layar email di laptop gpp
    #[Kamil mengecek lampiran laporan tersebut, notifikasi tentang meeting yang akan dimulai dalam waktu 10 menit] → manipulasi aja seakan-akan ada email gini 
    #[scene notifikasi meeting]
    scene bumnkantor with fade
    show Brama_y at cpos
    k "Nahh iya, hari ini aku harus meeting online. Hampir saja lupa…"
    scene zoommeeting with fade
    play sound notif
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
    scene present with dissolve
    k "Seperti yang terlihat, perusahaan mengalami kenaikan pendapatan sebesar 12\% dibandingkan tahun lalu."
    k "Namun, kita juga melihat adanya peningkatan pengeluaran operasional sebesar 8\%, terutama di kuartal terakhir."
    dir_a "Kenaikan pengeluaran ini disebabkan oleh apa?"
    dir_a "Apakah ada proyek besar yang menyedot biaya lebih besar dari anggaran?"
    k "Betul, ada dua proyek utama yang menjadi penyebab utama kenaikan biaya ini."
    k "Yaitu pengembangan produk baru dan ekspansi ke pasar luar negeri."
    k "Namun, tim keuangan kami telah memastikan bahwa semua alokasi biaya ini sesuai dengan perencanaan awal."
    stop music
    r "Pak Brama, saya perlu melihat file detail pengeluaran kuartal keempat. Bisa kirimkan sekarang?"
    play sound ngetik
    scene folder with dissolve
    pause 1.0
    stop sound
    play sound click_button
    scene folderselect with dissolve
    pause 1.0
    play sound click_button
    scene file with dissolve
    pause 1.0
    play sound click_button
    scene filesend with dissolve
    pause 1.0
    play sound click_button
    # PAKE SOUND CLICK DIANTARA SCENE DIATAS
    play music office_bgm
    scene present with fade
    r "Terima kasih, Pak Brama. File ini sesuai dengan yang saya butuhkan."

    k "Baik, Bapak/Ibu. Selain laporan pengeluaran, kami juga melihat adanya peningkatan margin keuntungan bersih sebesar 3\%."
    k "Ini berkat efisiensi dalam operasional dan optimalisasi proses produksi yang diterapkan sejak awal tahun."

    scene bumnlorong with fade
    show Brama_y at cpos
    k "Fyuh, akhirnya selesai juga presentasi hari ini."
    k "Selanjutnya apa ya agendaku?"
    show Sekretaris at rpos
    show Brama_y at lpos
    skre "Pak Brama, maaf mengganggu. Ada hal penting yang baru saja saya dapatkan."
    skre "Bapak perlu tahu ini sekarang."
    k "Iya, apa ada masalah?"
    skre "Ini terkait laporan tambahan dari tim audit."

    k "Lanjutkan."
    skre "Ada pembengkakan biaya di salah satu proyek besar kita, dan jumlahnya cukup signifikan."
    k "Bagaimana? Tolong diulangi."
    stop music
    skre "Mohon maaf Pak, terdapat pembengkakan biaya pada salah satu proyek kita."
    k "…"
    play music "audio/semoga tense.wav"
    skre "Sekali lagi mohon maaf Pak mengganggu waktunya."
    k "…"
    k "10 menit lagi silakan datang ke kantor saya."
    k "Kita bicarakan detail permasalahannya."
    skre "Baik Pak."

    scene bumnkantor with fade
    show Brama_y at cpos
    k "Aduh, masalah apa lagi."
    k "Udah hampir tutup laporan tahunan."
    k "Yaa semoga seberat apa pun itu bisa diselesaikan."
    show Sekretaris at lpos
    show Brama_y at rpos
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
    stop music

    menu:
        "Menelpon Pak Mahfudz":
            jump pakmahfudz
        "Bertanya ahli hukum di Kantor":
            jump ahlihukumkantor

label pakmahfudz:
    hide Sekretaris
    show Brama_y at lpos
    show telfonkabel at tlrpos
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
    play sound trans1
    scene bumnlobi with fade
    show Brama_y at cpos
    show male at nrpos
    staffa "Ada yang bisa saya bantu, Pak?"
    k "Tolong panggilkan staf hukum."
    k "Mungkin staf pembantu Pak Mahfudz."
    staffa "Baik, Pak. Mohon ditunggu."
    k "Oke."
    scene bumnkantor with fade
    show Brama_y at cpos
    show fem at nlpos
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
    play music idle
    scene bumnkantor with fade
    show Brama_y at lpos
    show telfonkabel at tlrpos
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
    hide telfonkabel
    show Brama_y at cpos
    k "Ini masalah besar…"
    k "Kalau informasi kesalahan ini sampai keluar, saya yang akan dimintai tanggung jawab."
    play sound notif
    stop music
    #[screenshot notifikasi]
    #[header email: Our company is looking up for prospective investment]
    k "…"
    k "Kayanya aku perlu break."
    k "Eh, sudah jam makan siang juga."
    k "Kemana ya enaknya?"

    menu:
        "Kantin":
            jump kantin
        "Kafe":
            jump Cafe
image Kantin = im.Scale("tam/kantin.jpg", 1920, 1080)
label kantin:
    scene Kantin
    show Brama_y at cpos
    k "Mikirin masalah gini jadi laper."
    k "Oh iya, dengar-dengar ada stan baru di kantin."
    k "Jual apa ya dia kata sekretaris kemarin?"
    k "Oh iya, kebab mozarela."
    k "Menarik deh, mungkin aku harus coba cita rasa gen-Z."
    hide Brama_y
    #scene kantin
    jump curhatarya
image Cafe = im.Scale("tam/cafe.png", 1920, 1080)
label Cafe:
    scene Cafe
    show Brama_y at cpos
    k "Mikirin masalah gini jadi laper."
    k "Oh iya, dengar-dengar cafe di lantai bawah jualan menu baru."
    k "Kopi apa ya?"
    k "Duh lupa, padahal baru diomongin sama sekretaris kemarin."
    k "Yaudah lihat aja nanti di bawah."
    k "Sekalian makan bekal dari rumah."
    hide Brama_y
    #scene kafe
    jump curhatarya

label curhatarya:
    play music idle
    show Brama_y at lpos
    show abatik at rpos
    r "Pak Brama, saudaraku!"
    k "..."
    r "Kelihatannya kamu lagi pusing berat."
    r "Ada masalah besar lagi, ya?"
    r "Ceritalah, Bram."
    r "Saudaramu ini direktur keuangan."
    r "Masalah bagi gw udah kayak makanan sehari-hari. Hahahaha!"
    k "..."

    menu:
        "cerita":
            jump cerita
        "Diam saja":
            jump diamsaja

label diamsaja:
    play music idle
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
    play music idle
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
    r "Kamu benar, Bram."
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
    stop music
    menu:
        "Ambil":
            jump ambil
        "Ragu":
            jump ragu

label ambil:
    k "Ini emang menarik sih."
    r "Tunggu apa lagi kalau begitu?"
    k "Iya sih, habis ini aku coba rapatin sama direksi yang lain."
    hide Brama_y
    hide abatik
    jump throwbackarya

label ragu:
    k "Tapi, Kak, apa nggak merasa aneh?"
    r "Aneh kenapa?"
    k "Kayak tiba-tiba banget pas di momen gini."
    r "Eh bagus dong."
    k "Iya sih, habis ini aku coba rapatin sama direksi yang lain."
    hide Brama_y
    hide abatik
    jump throwbackarya

label throwbackarya:
    play sound trans1
    scene pov_arya with fade
    pause
    scene bumnkantor with fade
    show male at nlpos
    staffr "Pagi, Pak Arya."

    show abatik at aycpos
    play music office_bgm
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
    hide male
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
    play sound trans1
    scene pov_brama with fade
    pause
    scene bumnrapat with fade
    show Brama_y at cpos
    k "Baik, sekian rapat kita kali ini."
    k "Sebagai kesimpulan, keputusan belum bisa kita ambil."
    k "Meskipun begitu, saya ucapkan terima kasih pada bapak ibu yang telah memberikan masukan."
    k "Kepastian mengenai tawaran investasi PT. Angin Topan akan segera saya kabarkan."
    k "Silakan untuk meninggalkan ruangan."
    hide Brama_y
    
    show Brama_y at lpos
    show abatik at ayrpos
    r "Bagaimana, Pak? Apakah dewan direksi menyetujui tawaran investor PT. Angin Topan?"
    k "Eh, Arya."
    k "Saya masih bingung terhadap keputusan apa yang harus saya ambil."
    k "Dewan direksi setuju untuk mengambil kesempatan ini."
    k "Mereka tidak mau perusahaan kita bangkrut dan karyawan kita kehilangan pekerjaan mereka."
    k "Kalau saya sendiri masih bingung karena saya punya feeling nggak enak."
    r "Udah lah, Bram."
    r "Kalau kata saya, terima saja tawaran itu."
    r "Emang kamu nggak kasihan apa buat keluarga karyawan yang bergantung pada pekerja kita untuk hidup sehari-hari?"
    r "Saya dengar-dengar juga ada kemungkinan tindak pidana manipulasi keuangan yang bisa menyeret nama kamu ke jalur hukum."
    r "Daripada kamu kena getahnya, mending bapak terima saja tawaran itu."
    stop music
    menu:
        "Tolak":
            jump A 
        "Terima":
            jump B 
#----------------------------------

# # # ------------------------------------- SCRIPT A -------------------------------------# #
# DEFINE CHARACTERS
define b = Character("Brama", color="#86ccec")
define a = Character("Arya", color="#ffd54a")
define o = Character("Other", color="#99928c")
define s = Character("Sekretaris", color="#ffffff")
define dir_a = Character("Direktur A", color="#000000ff")
define dir_b = Character("Direktur B", color="#000000ff")
define dir_c = Character("Direktur C", color="#000000ff")
define sl = Character("Staff Lobi", color="#000000ff")
define p = Character("Petugas KPK", color="#000000ff")
define staffa = Character("Staff A",  color="#000000ff")
define moderator = Character("Moderator", color="#000000ff")
define diplomat = Character("Diplomat", color="#c00b0bff")

# IMAGE BACKGROUND
image kantor = im.Scale("bg/bumn/kantor.png", 1920, 1080)
image ruang_rapatbumn = im.Scale("bg/bumn/rapat.png", 1920, 1080)
image lobibumn = im.Scale("bg/bumn/lobi.png", 1920, 1080)
image lorongbumn = im.Scale("bg/bumn/lorong.png", 1920, 1080)
image ruang_rapat_menteri = im.Scale("bg/kmenteri/rapat.png", 1920, 1080)
image ruang_kerja_bram_pagi = im.Scale("bg/kmenteri/pagi.png", 1920, 1080)
image ruang_kerja_bram_malam = im.Scale("bg/kmenteri/malam.png", 1920, 1080)

# IMAGE CHARA
"""image BramaK:
    "chara/Brama.png"
    zoom 0.5
image Sekretaris:
    "chara/Sekre.png"
    zoom 0.65
image Direktur_A:
    "chara/dirA.png"
    zoom 1.6
image Direktur_C:
    "chara/moder.png"
    zoom 1.6"""
image BramaK:
    "chara/Brama.png"
    zoom 0.5
image BramaKNetral:
    "chara/bumn_brama/SERIOUS_NEUTRAL.png"
    zoom 0.5
image BramaKSenang:
    "chara/bumn_brama/HAPPY.png"
    zoom 0.5
image BramaKLega:
    "chara/bumn_brama/RELIEVED.png"
    zoom 0.5
image BramaKMarah:
    "chara/bumn_brama/ANGRY.png"
    zoom 0.5
image BramaKKosong:
    "chara/bumn_brama/EMPTY.png"
    zoom 0.5
image BramaKBingung:
    "chara/bumn_brama/CONFUSED.png"
    zoom 0.5

image AryaYNetral:
    "chara/bumn_arya/NEUTRAL.png"
    zoom 1.5
image AryaYKopi:
    "chara/bumn_arya/MENYESAP KOPI.png"
    zoom 1.5
image AryaYSenyum:
    "chara/bumn_arya/HAPPY SMILE.png"
    zoom 1.5
image AryaYKetawa:
    "chara/bumn_arya/HAPPY LAUGH.png"
    zoom 1.5
image AryaYSerius:
    "chara/bumn_arya/SERIOUS.png"
    zoom 1.5

image Istri:
    "chara/istri/biasa.png"  
    zoom 1.6
image Istri s:
    "chara/istri/buka.png"
    zoom 1.6
image Istri snark:
    "chara/istri/snark.png"  
    zoom 1.6

image telfonkabel:
    "single asset/Telfon kabel.png"
    zoom 0.45
image Sekretaris:
    "chara/Sekre.png"
    zoom 0.65
image Direktur_A:
    "chara/dirA.png"
    zoom 1.6
image Direktur_C:
    "chara/moder.png"
    zoom 1.6
image Diplomat:
    "chara/dcinas.png"
    zoom 1.2

image male:
    "chara/male.png"  
    zoom 1.8
image maleGlitch:
    zoom 1.8
    At("chara/male.png", glitch)
    pause 0.2
    At("chara/male.png", animated_glitch)
    pause 0.2
    At("chara/male.png", glitch)
    pause 0.1
    At("chara/male.png", animated_glitch)
    pause 0.1
    At("chara/male.png", glitch)
    pause 0.3
    At("chara/male.png", animated_glitch)
    pause 1.0
    repeat
image male2:
    "chara/male.png"  
    zoom 1.8
image fem:
    "chara/fem.png"  
    zoom 1.4

# buat brama
define cpos = Position(xalign=0.5, yalign=0)
define rpos = Position(xalign=0.9, yalign=0)
define lpos = Position(xalign=0,yalign=0)

# buat arya
define aycpos = Position(xalign=0.5, yalign=0)
define ayrpos = Position(xalign=1.25, yalign=0)
define aylpos = Position(xalign=0,yalign=0)

# buat telpon
define tlcpos = Position(xalign=0.5, yalign=0)
define tlrpos = Position(xalign=1.01, yalign=0.6)
define tllpos = Position(xalign=0,yalign=0)

label A: #email_keputusan
    scene kantor with fade
    show BramaK at cpos

    "Suasana tegang, Brama sedang duduk di depan komputernya, mengetik email balasan untuk menolak tawaran investasi."

    show BramaK at cpos
    b "Coba aja aku tahu lebih dalam tentang PT. Angin Topan..."
    b "Kalau kayak gini aku harus cari dana tambahan ke mana lagi?"
    o "Sudah, tenang saja Brama. Tetaplah berpegang teguh pada prinsipmu itu."
    o "Ingatlah bahwa setiap permasalahan pasti akan ada solusinya."
    o "Bagaimana jika feeling-mu itu benar?"
    o "Bagaimana jika PT. Angin Topan justru membawa masalah lebih jauh?"
    o "Coba pikirkan kemungkinan bahwa Angin Topan membawa uang haram."
    o "Apa kamu nggak malu dengan keluarga kecilmu kalau nantinya tertangkap karena melakukan pencucian uang?"

    b "Benar juga... Kasihan dengan anak dan istriku."
    b "Mereka pasti malu punya suami dan seorang ayah koruptor."
    b "Semoga ada jalan untuk menyelesaikan permasalahan ini."

    "Brama terlihat sangat gelisah. Ia memanggil sekretarisnya melalui telepon."

    show BramaK at rpos
    show Sekretaris at lpos
    b "Sekretaris, tolong adakan rapat dewan direksi darurat 1 jam lagi dengan semua direksi."
    b "Semua harus hadir untuk membahas persoalan ini."
    b "Dan pastikan tidak ada pihak asing yang masuk ke kantor."
    b "Saya nggak mau rapat terganggu, terlebih isu ini sangat penting."

    
    s "Baik Pak, akan segera saya informasikan kepada seluruh direksi perusahaan."
    s "Untuk keamanan, akan saya sampaikan ke pihak security di depan."

    "Sekretaris keluar dari ruangan, meninggalkan Brama yang masih terlihat cemas."

    jump rapat_dewan_direksi

image slideA = im.Scale("text/A/A.png", 1920, 1080)
image surattangkap = im.Scale("tam/surattangkap.png", 1920, 1080)
label rapat_dewan_direksi:
    scene ruang_rapatbumn with fade

    show BramaK at cpos
    b "Selamat siang bapak dan ibu dewan direksi."
    hide BramaK
    show Direktur_A at Position(xalign=0.1,yalign=0)
    show male at nrpos
    show fem at ncpos
    dir_a "Siang."
    dir_b "Siang."
    dir_c "Siang."
    hide Direktur_A 
    hide fem
    hide male

    show BramaK at cpos
    b "Pada rapat terbatas kali ini saya akan membahas kelanjutan persoalan yang sudah kita bahas sebelumnya."
    b "Perlu diingat, kita mendapatkan tawaran investasi dari PT. Angin Topan untuk membantu menutup pembengkakan biaya."
    b "Lebih tepatnya proyek ekspansi dapur di bandara Changi yang sedang kita jalankan."
    b "Meskipun pada rapat terbatas sebelumnya bapak ibu sekalian telah menyetujui untuk menerima tawaran investasi."
    b "Saya telah mencoba untuk pertimbangkan kembali mengenai risiko dengan legalitas hukum keputusan ini."
    b "Saya rasa, terlalu banyak yang harus kita korbankan jika kita menerima tawaran investasi itu."
    b "Sehingga dengan berat hati saya putuskan untuk menolak tawaran investasi ini."
    b "Karena hal juga tidak sesuai dengan prinsip pribadi saya."
    b "Mengingat kita juga tidak mengetahui kredibilitas PT. Angin Topan."
    b "Sehingga pada kesimpulannya kita harus tetap mengutamakan kejujuran dan keadilan dalam mengambil suatu tindakan."

    "Ruang rapat menjadi ribut dan ricuh."

    hide BramaK
    show Direktur_A at Position(xalign=0.1,yalign=0)
    show Direktur_C at Position(xalign=0.9,yalign=0)
    show male at ncpos

    dir_a "Mohon maaf pak Kamil, saya rasa ini tidak bisa menjadi keputusan sepihak bapak saja."
    dir_a "Karena ini menyangkut hajat hidup orang banyak dan demi keberlanjutan perusahaan."
    dir_b "Benar dengan yang dikatakan oleh direktur keuangan, saya tidak setuju dengan keputusan bapak barusan."
    dir_a "Apakah bapak tidak memikirkan bagaimana nasib para karyawan jika nantinya perusahaan ini bangkrut?"
    dir_a "Berdasarkan hasil audit tim keuangan pun sudah jelas bahwa pembengkakan biaya ini cukup membuat keuangan perusahaan menjadi minus."
    dir_a "Kita sudah tidak punya lagi sisa uang untuk melanjutkan proyek tersebut."

    "Di luar kantor terjadi kericuhan dan ramai dengan rombongan KPK yang akan menggeledah dan menangkap Kamil."

    scene lobibumn with fade
    show fem at ncpos
    show male2 at nlpos

    sl "Selamat siang, mohon maaf ini rame-rame bapak-bapak semua dari pihak mana dan ada keperluan apa datang kemari?"
    p "Siang, kami dari KPK akan melakukan penangkapan terhadap pak Kamil selaku direktur utama perusahaan katering Garuda."
    p "Berdasarkan hasil laporan dan penyelidikan kami bahwa di perusahaan ini terdapat indikasi tindak pidana manipulasi laporan keuangan yang melibatkan pak Kamil."
    sl "Mohon maaf pak, bapak tidak bisa masuk dikarenakan arahan dari pak Kamil seperti itu."

    "Pihak KPK tetap maksa masuk dan terjadi sedikit kericuhan."

    p "Ga bisa pak, ini sudah menjadi tugas kami untuk melakukan penggeledahan dan penangkapan pak Kamil."
    sl "Silahkan tunjukan surat perintah penggeledahan dan penangkapan."

    "Petugas menunjukkan surat perintah, beberapa orang pegawai KPK telah masuk ke kantor."

    p "Ini untuk surat perintah kami, silahkan bapak baca."
    scene surattangkap
    pause 1

    scene lorongbumn with fade
    show Sekretaris at cpos

    s "Aduh kenapa bisa secepat ini mereka menyadari permasalahan ini, mana direksi lagi pada rapat?"

    scene ruang_rapatbumn with fade
    show Direktur_C at Position(xalign=0.5,yalign=0)

    dir_c "Tenang bapak-bapak semua, apa yang pak Kamil sampaikan benar adanya."
    dir_c "Berdasarkan hasil rapat, dari divisi pengelolaan risiko menyatakan bahwa jika nantinya terbukti bahwa uang yang diinvestasikan merupakan hasil tindak pidana korupsi."
    dir_c "Maka nantinya yang terkena dampaknya tidak hanya kepada perusahaan saja tapi kepada kita semua yang berada di ruangan ini."
    hide Direktur_C
    "Kamil menyadari bahwa terjadi keributan di luar ruang rapat."
    show BramaK at cpos
    b "Tenang bapak-bapak semuanya, sepertinya rapat ini harus kita tunda lagi."
    b "Saya menyadari ada suatu keributan di …"
    hide BramaK
    "Tiba-tiba pegawai KPK masuk ke ruangan rapat."
    show male at ncpos
    p "Selamat siang, kami dari KPK akan melakukan penggeledahan terhadap kantor ini."
    p "Dan kepada saudara Kamil silahkan ikuti saya keluar ruangan."
    hide male
    "Suasana ruang rapat tegang dan Kamil cemas."
    show BramaK at lpos
    b "Saya Kamil, kalau boleh tau ini ada apa kenapa kalian tiba-tiba datang dan menggeledah kantor kami?"
    show male at nrpos
    p "Kami telah menerima laporan bahwa terdapat indikasi tindak pidana manipulasi keuangan terhadap salah satu proyek yang sedang dikerjakan."
    p "Berdasarkan hasil pengamatan kami juga bahwa hal tersebut juga disetujui oleh saudara Kamil selaku direktur utama perusahaan ini."
    p "Kami mohon kooperatifnya agar berjalan dengan lancar."
    hide male
    hide BramaK
    "Kamil pun berfikir."
    show BramaK at cpos
    b "(Wah ini gimana ceritanya mereka bisa secepat ini mencium permasalahan ini? Aduh aku harus apa ini?)"
    show BramaK at lpos
    show male at nrpos
    b "Baik pak."

    "Kamil pergi mengikuti pegawai KPK. Akhirnya Kamil dibawa ke kantor KPK untuk dimintai keterangan."
    scene black with fade
    show slideA
    pause 10

    return #Ending Penjara

# # ------------------------------------- Script B -------------------------------------
# IMAGE BACKGROUND
image istana_negara = im.Scale("bg/IstanaNegara.jpg", 1920, 1080)
image siaran_berita = im.Scale("bg/rumahkamil/tv.png", 1920, 1080)

# IMAGE TEXT
image slideB1 = im.Scale("text/B/Slide1.PNG", 1920, 1080)
image slideB2 = im.Scale("text/B/Slide2.PNG", 1920, 1080)
image slideB3 = im.Scale("text/B/Slide3.PNG", 1920, 1080)
image slideB4 = im.Scale("text/B/Slide4.PNG", 1920, 1080)
image slideB5 = im.Scale("text/B/Slide5.PNG", 1920, 1080)
image slideB6 = im.Scale("text/B/Slide6.PNG", 1920, 1080)
image slideB7 = im.Scale("text/B/Slide7.PNG", 1920, 1080)
image slideB8 = im.Scale("text/B/Slide8.PNG", 1920, 1080)
image slideB9 = im.Scale("text/B/Slide9.PNG", 1920, 1080)

label B:
  
    scene ruang_rapatbumn with fade
    show BramaK at cpos

    # (Ngomong dalam hati)
    b "(Aku harus lihat situasinya. Perusahaan ini adalah hidupku.)"
    b "(Kalau aku kehilangan dana ini, aku juga akan kehilangan segalanya. Tawaran dari PT Angin Topan ini jalan keluar terbaik.)"
    b "(Aku rasa mereka tidak akan mencurigai apa-apa kalau aku berhati-hati.)"
    hide BramaK

    show maleGlitch at cpos
    o "Tapi bukankah kita tidak mengetahui kredibilitas PT Angin Topan?"
    o "Brama, kalau kamu merasa ada yang salah, maka ikuti perasaanmu."
    hide maleGlitch

    show BramaK at cpos
    b "Tapi bagaimana dengan nasib karyawanku?"
    hide BramaK
    show maleGlitch at cpos
    o "Apakah menerima tawaran itu bisa menjawab semua permasalahan? Coba pikirkan kembali."
    hide maleGlitch

    show BramaK at cpos
    b "(...)"
    b "(Aku terlalu banyak khawatir. Ingat, ini bukan cuma tentang dirimu.)"
    b "(Ini juga tentang bagaimana orang yang hidup dari perusahaan ini.)"
    b "(Apa aku harus mengikuti jalan yang sepertinya salah demi menyelamatkan perusahaan?)"
    b "(Atau aku harus bertahan dengan prinsipku, walaupun aku tahu aku mungkin akan hancur?)"

    b "(Bagaimana dengan keluarga kecilku kalau aku menyerah pada ini?)"
    b "(Tapi kalau aku dipenjara, bagaimana aku bisa melindungi mereka?)"
    b "(Aku tidak punya pilihan lain, aku harus menyelamatkan semuanya, aku harus melakukannya.)"
    play sound ngetik
    # [Mengetik email balasan]
    "Brama mulai mengetik email balasan di laptopnya."
    
    b "Semoga ini tidak kembali menghantui aku di masa depan..."
    stop sound
    # Time skip
    play sound trans1
    scene slideB1 with fade
    pause
    play sound trans1
    scene slideB2 with fade
    pause
    play sound trans1
    scene slideB3 with fade
    pause
    play sound trans1
    scene slideB4 with fade
    pause
    play music idle
    scene istana_negara with fade
    show BramaKSenang at cpos
    b "Akhirnya saudaraku, kau hebat."
    b "Selamat ya Arya, telah menjadi menteri perdagangan."
    hide BramaKSenang
    show AryaYKetawa at cpos
    a "Ini berkatmu juga, Brama. Selalu support, kamu juga tidak kalah keren, telah menjadi menteri luar negeri."
    a "Selamat!"

    scene slideB5 with fade
    pause
    scene ruangmakan_y with fade
    show BramaKSenang at cpos
    b "Sayang, aku pulang..."
    hide BramaK

    show BramaKSenang at lpos
    show Istri s at ayrpos
    ist "Sayang, aku sangat bangga atas pencapaianmu, selamat ya!"
    ist "Hari ini pasti sangat melelahkan ya, aku buatkan kopi susu buat kamu sayang."
    hide BramaKSenang
    show BramaKLega at lpos
    b "Emm, enak sekali. Makasih ya sayang, ini berkatmu juga."

    # [Dilanjutkan Brama menonton TV]
    scene siaran_berita with fade
    show BramaKNetral at cpos
    b "Apa yang terjadi di Natuna?"
    hide BramaKNetral with fade

    show BramaK at lpos
    show Istri at ayrpos
    ist "Ayah, lihat ada kapal ditenggelamkan oleh pihak asing." 
    ist "Kasihan sekali bagaimana dengan keluarga mereka."

    b "Gawat, kejam sekali mereka kepada rakyat Indonesia. Aku harus segera mengambil tindakan!"

    scene slideB6 with fade
    pause
    scene kantor with fade #diplomat_call
    "(Diplomat Tiongkok sedang menghubungi Ridwan untuk membahas permasalahan yang sedang ramai)"

    show AryaYKopi at aylpos
    show Diplomat at rpos
    diplomat "Hi Mr. Arya, sorry for bothering your time but right now I have something important to discuss with you."
    a "Hi, it’s okay, I have free time for you."
    a "What do you want to talk about?"
    diplomat "It's about a problem on Natuna."
    diplomat "There’s a mistake that caused our coast guard to pass the Indonesian maritime border, which makes a little conflict with local fishermen and sink their ship."

    a "So, what can I do for you? There’s something free nowadays. What can I get if I help you?"

    diplomat "I want that this conflict isn’t prolonged so that it can give a domino effect to other sectors."
    diplomat "The relationship between Indonesia and China has been very good recently."
    diplomat "Don't let this make our relationship become worse."
    diplomat "I want you to lobby to the ministry of foreign to make a policy to protect our coast guard."
    diplomat "And I will guarantee you that this is the last time and no more like this will happen again."
    diplomat "What do you want from us?"
    diplomat "We can give you everything you want."
    diplomat "Just say it and we will fulfill what you asked."

    a "Okay, I will clear the problem."
    a "It’s easy to handle." #, my brother
    a "But I want you to get rid of my brother, Brama, in a soft way."
    a "So I can be the president for the next period."

    diplomat "Sure, we will give you another gift which is everything you want like money, etc." 

    # [Scene transition]
    play sound trans1
    scene black with fade
    show AryaYSerius at aycpos
    "(Rencana Arya mulai terbentuk di benaknya, dan dia tahu langkah selanjutnya yang harus diambil.)" 

    scene slideB7 with fade
    pause
    stop music
    scene ruangmakan_y with fade
    show BramaKBingung at cpos
    b "Aduh, baru bentar menjabat jadi Kemenlu, ada aja kerjaan yang harus dilakukan."
    hide BramaKBingung
    show BramaKNetral at cpos
    b "Tapi ini kasus cukup serius. Aku harus melakukan apa?"

    menu:
        "Bergegas pergi rapat":
            hide BramaKNetral
            jump pergirapat
        "Menghubungi Arya":
            hide BramaKNetral
            jump menghubungiarya

label pergirapat:
    show BramaKNetral at lpos
    play music idle
    b "Sayang, aku harus segera pergi ke kantor untuk membicarakan masalah ini."
    show Istri s at rpos
    ist "Boleh, ayah. Hati-hati ya di jalan."
    hide Istri s

    # [Telepon Sekretaris]
    b "Halo, Pak. Tolong segera dibuatkan rapat untuk membahas permasalahan ini ya."
    show telfonkabel at tlrpos
    staffa "Baik, akan segera saya informasikan mengenai ruangan di tempat meeting biasa ya, Pak."

    b "Baik, tolong disiapkan dan kabarkan pada yang lain."

    "Brama bergegas menuju kantor, merasa berat dengan tanggung jawab yang harus dihadapi."

    jump rapat_dewan_direksi2  # Melanjutkan ke rapat dewan direksi

label menghubungiarya:
    stop music
    play music office_bgm
    show BramaKNetral at lpos
    b "Aku membutuhkan Arya. Ini sangat kacau situasinya."

    # [Menelpon Arya]
    show telfonkabel at tlrpos
    b "Hallo, Arya. Ada apa, Brama?"

    b "Permasalahan dengan Tiongkok, mereka melakukan tindakan sangat kejam kepada rakyat Indonesia."

    a "APA! Kita harus mengadakan rapat segera."

    b "Aku akan mengadakan jadwal rapat pada hari ini."

    a "Tidak perlu tergesa-gesa, Brama."

    b "Tidak bisa, ini harus dibahas segera. Aku akan menuju kantor."

    "Brama menutup telepon dan bersiap-siap untuk pergi."

    jump rapat_dewan_direksi2  # Melanjutkan ke rapat dewan direksi

# Define the variable C
define C = False

label rapat_dewan_direksi2:
    play music office_bgm
    scene ruang_rapat_menteri with fade
    show BramaK at cpos
    show AryaYNetral at ayrpos
    show male at lpos

    "Suasana ruang rapat terbatas terlihat tegang. Sebuah layar besar di depan mereka menunjukkan peta perairan Natuna, dengan laporan insiden terbaru yang melibatkan kapal asing dari Tiongkok yang menenggelamkan kapal nelayan Indonesia."

    staffa "Pak Menteri, ini adalah laporan terbaru."
    staffa "Sebuah kapal nelayan dari Natuna tenggelam oleh kapal patroli asing."
    hide BramaK
    show BramaKNetral at cpos
    b "Bagaimana dengan keadaan orang di dalam kapal tersebut?"
    hide BramaKNetral
    show BramaK at cpos
    staffa "Lima nelayan selamat, tetapi mereka mengalami trauma berat."
    staffa "Ini bukan kejadian pertama, dan mereka semakin berani memasuki wilayah kita."
    hide BramaK
    show BramaKNetral at cpos
    b "Begitu ya?"
    hide BramaKNetral
    show BramaKMarah at cpos
    b "Kalau begitu, kita harus TENGGELAMKAN kapal mereka juga."
    b "Mereka tidak akan jera apabila tidak dengan tindakan yang agresif."
    hide AryaYNetral
    show AryaYKopi at ayrpos
    a "Brama, saya paham kemarahan masyarakat, tapi mari kita realistis."
    a "Kalau kita mengambil langkah agresif terhadap mereka, dampaknya pada ekonomi kita bisa fatal."
    hide AryaYKopi
    show AryaYNetral at ayrpos
    a "Mereka salah satu mitra dagang terbesar kita."
    a "Kalau hubungan ini memburuk, ekspor kita bisa hancur, dan itu akan memukul perekonomian nasional."
    hide AryaYNetral
    hide male
    stop music
    menu:
        "Tetap Idealis": #C
            $ C = True
            jump tetapidealis
        "Setuju dengan Arya":#D
            jump setujuarya

label tetapidealis:
    show AryaYNetral at ayrpos
    show male at lpos
    hide BramaKMarah
    show BramaKNetral at cpos
    b "Saya tahu itu, Arya."
    b "Tapi kita juga tidak bisa terus membiarkan kejadian ini."
    b "Rakyat kita di Natuna semakin kehilangan kepercayaan pada pemerintah."
    b "Mereka merasa kita tidak melindungi mereka."
    b "Pendapatan pajak dari sektor perikanan di sana juga terus menurun karena nelayan takut melaut."
    hide AryaYNetral
    show AryaYKopi at ayrpos
    a "Lalu apa saranmu, Brama? Kita menenggelamkan kapal asing?"
    a "Itu sama saja dengan mendeklarasikan perang secara tidak langsung."
    a "Ekonomi kita tidak siap menghadapi embargo atau retaliasi dagang."

    b "Masalahnya, Arya, ini bukan hanya tentang ekonomi."

    hide BramaKNetral
    show BramaKMarah at cpos
    b "Ini soal kedaulatan kita."
    b "Kalau mereka terus menekan, apa yang akan kita tinggalkan untuk generasi mendatang?"
    b "Uang bisa dicari, tapi bagaimana dengan rakyat dan kehormatan negara?"
    hide AryaYKopi
    show AryaYSerius at ayrpos
    a "Brama, jangan idealis di sini."
    a "Kita bicara soal realitas."

    # Continue the story based on the choice
    jump akhir_rapat

label setujuarya:
    show AryaYNetral at ayrpos
    show male at lpos
    hide BramaKMarah
    show BramaKNetral at cpos
    b "Ada benarnya yang kamu katakan, mereka juga menguasai jalur perdagangan terbesar."
    hide AryaYNetral
    hide male
    hide BramaKNetral
    show BramaKNetral at lpos
    show maleGlitch at rpos
    o "BRAMA, pikirlah kembali, bagaimana dengan rakyat di sana?"
    b "Tetapi langkah agresif ini akan membuat perpecahan antar negara."
    o "Kapal mereka ditenggelamkan dengan semena-mena."
    o "Mereka sedang melakukan kerja demi keluarga-keluarga mereka."
    o "Kau tidak berpikir, Brama?"

    b "Tapi aku setuju dengan pernyataan Arya, hal ini tidak bisa dilakukan."
    o "Kau tidak kasihan sebagai menteri pada rakyat Indonesia?"
    o "Dan, ingat Brama, rakyatmu keluargamu juga."
    hide maleGlitch
    hide BramaKNetral

    show AryaYNetral at ayrpos
    show male at lpos
    show BramaKNetral at cpos
    b "Arya, apakah kau memikirkan dampaknya juga terdapat masyarakat di sana?"
    a "Ya, tentu saja saya memikirkan mereka."
    a "Tapi apa boleh buat, ini demi menjaga hubungan yang baik sesama negara."
    hide AryaYNetral
    show BramaKBingung at cpos
    b "Tapi, Arya, bagaimana jika mereka terus menekan kita?"
    b "Jika kita hanya diam, apa yang akan terjadi pada nelayan kita?"

    a "Saya paham, Brama. Tapi kita harus cerdas dalam mengambil langkah."
    a "Diplomasi adalah kunci dalam situasi ini. Kita bisa melibatkan pihak internasional untuk menekan mereka secara hukum."

    b "Dan sementara itu, rakyat kita tetap menjadi korban?"
    b "Saya tidak bisa membiarkan hal itu."

    a "Tidak, Brama. Kita tidak akan membiarkan mereka."
    a "Kita bisa meningkatkan pengawasan di perairan kita, menambah kapal patroli, dan memperkuat koordin asi dengan angkatan laut."
    a "Dengan begitu, kita menunjukkan ketegasan tanpa memicu konflik langsung."

    b "Kau yakin langkah ini cukup untuk membuat mereka jera?"
    a "Ini adalah cara paling aman untuk melindungi kepentingan kita, baik di dalam negeri maupun di luar negeri."
    a "Jika kita memprovokasi mereka dengan tindakan agresif, kita berisiko menghadapi konsekuensi yang lebih besar, termasuk isolasi ekonomi."
    hide BramaKBingung
    show BramaK at cpos
    b "…"
    b "Baiklah, Arya. Saya mengerti logikamu. Kita akan menempuh jalur diplomasi dan memperkuat pertahanan kita di wilayah tersebut."

    a "Terima kasih, Brama. Dengan langkah ini, kita melindungi rakyat kita tanpa harus mengorbankan hubungan antarnegara."
    b "Tapi saya minta satu hal, Arya. Jangan biarkan ini hanya menjadi rencana di atas kertas."
    b "Pastikan semua langkah segera dilaksanakan."
    hide AryaYNetral
    show AryaYSenyum at ayrpos
    a "Tentu, Brama. Kita akan bergerak cepat."
    b "Kalau begitu, mari kita susun strategi ini dengan detail."
    b "Saya ingin semua pihak terkait dilibatkan dalam diskusi."

    jump akhir_rapat

label akhir_rapat:
    scene ruang_rapat_menteri with fade
    show male at cpos
    show BramaK at lpos
    show AryaYNetral at ayrpos
    play sound ngetok
    # [Pemimpin rapat ketok-ketok palu]
    "*tok tok tok tok*"

    moderator "Cukup saudara-saudara sekalian."
    moderator "Diskusi kita cukupkan."
    moderator "Kesepakatan keputusan akan kita diskusikan lebih lanjut bersama presiden beberapa hari lagi."

    # [Sesaat setelah rapat]
    scene lorongbumn with fade
    "*suara perut bunyi*"
    show BramaKBingung at cpos
    b "Perutku sudah bunyi, lapar sekali."
    b "Enaknya makan di mana ya?"

    menu:
        "Kantin Di Kantor":
            jump kantin2
        "Cafe dekat kantor":
            jump cafe
image Kantin = im.Scale("tam/kantin.jpg", 1920, 1080)
label kantin2:
    play music idle
    scene Kantin with fade
    show BramaKSenang at cpos
    b "Mmm, sepertinya makan Ayam saus mentega enak."
    b "Mas, mau ayam saus mentega 1 dan es teh 1 ya."
    hide BramaKSenang

    "(Ridwan melewati Brama tetapi dia tidak melihat Brama)"
    show AryaYNetral at aycpos
    a "..."
    hide AryaYNetral
    show BramaKSenang at cpos
    menu:
        "Menyapa Arya":
            jump menyapa_arya
        "Tidak menyapa Arya":
            jump tidak_menyapa_arya
image Cafe = im.Scale("tam/cafe.png", 1920, 1080)
label cafe:
    play music idle
    scene Cafe with fade
    show BramaKSenang at cpos
    b "Mmm, sepertinya makan Sop buntut enak dan segar."
    b "Mba, saya pesan sop buntut dan es kopinya 1 ya."
    hide BramaKSenang

    "(Ridwan melewati Brama tetapi dia tidak melihat Brama)"
    show AryaYNetral at aycpos
    a "..."
    hide AryaYNetral
    show BramaKSenang at cpos
    menu:
        "Menyapa Arya":
            jump menyapa_arya
        "Tidak menyapa Arya":
            jump tidak_menyapa_arya

label menyapa_arya:
    hide BramaKSenang
    show BramaKSenang at lpos
    b "Arya……!"
    show AryaYKetawa at ayrpos
    a "Eh, Brama! Kamu juga makan di sini?"
    b "Iya nih, kebetulan lapar banget makannya kesini."
    a "Oala, aku ikut makan di sini juga ya."
    b "Iya, boleh, Arya. Sini aja."
    hide BramaKSenang
    # Continue the story after they sit together
    jump lanjut_makan

label tidak_menyapa_arya:
    hide BramaKSenang
    show BramaK at cpos
    b "Mmmm, aku tidak perlu menyapanya…"
    hide BramaK

    show AryaYKetawa at aycpos
    a "Brama…!"
    hide AryaYKetawa

    show BramaKNetral at lpos
    show AryaYKetawa at ayrpos
    b "Eehh.. Arya, kamu makan di sini juga?"
    a "Iya, tadi bosen sama makanan di kantin jadi kesini."
    b "Oala, sini duduk di sini aja."
    a "Eh iyaa, boleh, aku ikut makan di sini ya, Brama?"
    hide BramaKNetral

    # Continue the story after they sit together
    jump lanjut_makan

label lanjut_makan:
    hide AryaYKetawa
    "(Brama dan Arya duduk bersama, menikmati makanan mereka sambil berbincang-bincang.)"

    show BramaKBingung at lpos
    b "Oh iya, Arya, maaf ya untuk tadi."
    b "Aku terbawa emosi, pikiranku sedang berantakan."

    show AryaYKetawa at ayrpos
    a "Eh iyaa, santai aja, ko."
    a "Aku ingin kamu memutuskan permasalahan Laut Cina Selatan ini dengan lebih tenang dan rasional, Brama."

    b "Iya, Arya. Aku akan pertimbangkan dari seluruh aspek, baik yang kamu sampaikan kemarin."

    show AryaYKopi at ayrpos
    a "Hal yang kusampaikan tidak semata-mata hanya ingin memperoleh keuntungan."
    a "Tetapi aku memikirkan keterjalinan hubungan yang baik antar negara nantinya, Brama."

    hide BramaKBingung
    show BramaKNetral at lpos
    b "Baik, Arya. Akan ku coba pikirkan lagi mengenai hal tersebut."
    b "Terima kasih ya."

    # [Makanan datang, mereka pun makan bersama]
    "(Makanan yang dipesan pun datang, dan mereka mulai makan bersama.)"
    hide BramaKNetral
    hide AryaYKopi

    show BramaKLega at lpos
    b "Aduh, kenyangnya. Oiya, Arya, aku izin pergi ke kantor duluan ya, ada pekerjaan yang harus diselesaikan."
    show AryaYKetawa at ayrpos
    a "Oh iya, boleh, Brama. Sampai ketemu di kantor."

    # [Brama pergi dengan pikiran yang dipenuhi oleh permasalahan yang dihadapi]
    "Brama pergi dengan pikiran yang dipenuhi oleh permasalahan yang dihadapi."
    stop music

    jump dialogchoiceB
label dialogchoiceB:
    if C:
        jump C
    else:
        jump D
#----------------------------------

# # ------------------------------------- SCRIPT C -------------------------------------# #
# DEFINE CHARACTERS
define kades = Character("Kades",  color="#000000ff")

# IMAGE BACKGROUND
image slideC1 = im.Scale("text/C/Slide1.PNG", 1920, 1080)
image slideC2 = im.Scale("text/C/Slide2.PNG", 1920, 1080)
image pesawat = im.Scale("bg/pesawat.png", 1920, 1080)
# IMAGE CHARA
image Kades:
    "chara/nelayana.png"
    zoom 2.6

# IMAGE TEXT
image slideC1 = im.Scale("text/C/Slide1.PNG", 1920, 1080)
image slideC2 = im.Scale("text/C/Slide2.PNG", 1920, 1080)

label C:
    scene slideC1 with fade
    pause
    scene ruang_kerja_bram_pagi with fade
    show BramaKKosong at cpos
    b "Apakah aku mengambil keputusan yang benar?"
    b "Menantang mereka dengan idealismeku mungkin hanya akan menghancurkan lebih banyak hal..."

    show BramaKKosong at lpos
    show maleGlitch at rpos
    o "Tapi jika aku terus diam, lalu siapa yang akan berdiri untuk mereka?"
    o "Kehormatan negara bukan sesuatu yang bisa dijual."
    b "Tapi… apa aku bisa memikul konsekuensinya?"

    # [Foto keluarga]
    
    o "Lihat anakmu… apa kamu tidak ingin dia tumbuh di negara yang kuat, di mana rakyatnya dihormati?"

    b "Tapi… apa aku akan menjadi ayah yang bertanggung jawab kalau pilihanku ini menghancurkan segalanya?"

    "*tok..tok..tok..*"
    hide BramaKKosong
    show BramaKMarah at lpos
    b "Siapa ya di pagi hari sudah mengetuk ruang kerjaku?"
    hide BramaKMarah
    hide maleGlitch
    show BramaKMarah at cpos
    menu:
        "Membuka Pintu":
            jump membuka_pintu
        "Mengabaikannya":
            jump mengabaikannya

label membuka_pintu:
    hide BramaKMarah
    show BramaKNetral at cpos
    b "Sebentar, siapa di sana?"
    hide BramaKNetral
    show AryaYNetral at aycpos
    a "Pagi, Brama. Maaf pagi-pagi mengganggu aktivitasmu."
    hide AryaYNetral
    show BramaKNetral at cpos
    b "Ada apa, Arya? Silahkan masuk."
    hide BramaKNetral
    jump setelah_masuk

label mengabaikannya:
    b "Aduh, siapa yang mengetuk sepagi ini?"
    b "Aku tidak perlu membukanya, masih banyak pekerjaan yang perlu diselesaikan."
    hide BramaKMarah
    "*tok..tok..tok..*"
    show BramaKMarah at cpos
    b "Ya ampun, suaranya mengganggu hingga tidak bisa melanjutkan pekerjaanku."
    hide BramaKMarah
    show BramaKNetral at cpos
    b "Eh, Arya, ada apa…?"
    hide BramaKNetral
    show AryaYNetral at aycpos
    a "Pagi, Brama. Maaf pagi-pagi mengganggu aktivitasmu."
    hide AryaYNetral
    show BramaKNetral at cpos
    b "Iya, tak apa. Silahkan duduk."
    hide BramaKNetral

label setelah_masuk:
    show BramaK at lpos
    show AryaYNetral at ayrpos
    a "Brama, aku tahu kau pasti memikirkannya."
    a "Dengar, aku tidak ke sini untuk berdebat."
    a "Tapi... aku ingin kita bicara dengan kepala dingin."
    hide BramaK
    show BramaKKosong at lpos
    b "…"
    hide AryaYNetral
    show AryaYSenyum at ayrpos
    a "Aku tahu kau punya idealisme yang kuat."
    a "Itu salah satu hal yang selalu aku kagumi darimu."
    a "Tapi terkadang, Brama… dunia ini tidak selalu hitam dan putih."
    a "Kita harus pragmatis."
    hide BramaKKosong
    show BramaKNetral at lpos
    b "Pragmatis seperti apa, Arya?"
    b "Menutup mata terhadap kezaliman dan kehilangan kedaulatan demi angka di laporan ekonomi meningkat?"
    hide AryaYSenyum
    show AryaYNetral at ayrpos 
    a "Bukan begitu."
    a "Tapi kita harus realistis."
    a "Kalau kita melawan mereka dengan cara frontal, apa yang akan terjadi?"
    a "Mereka bisa menghancurkan kita."
    a "Negara ini masih bergantung pada investasi asing, dan kau tahu itu."
    hide BramaKNetral
    show BramaK at lpos
    b "…"
    hide BramaK
    show BramaKNetral at lpos
    b "Jadi kita membiarkan mereka melakukan apa pun yang mereka mau?"
    hide BramaKNetral
    show BramaKMarah at lpos
    b "Aku tidak bisa."
    hide AryaYNetral
    show AryaYSerius at ayrpos
    a "Brama! Aku tidak ingin melihatmu dihancurkan oleh keputusan bodoh."
    a "Cobalah lihat gambaran besarnya!"
    a "Brama, ini bukan soal siapa yang benar."
    a "Ini soal siapa yang akan bertahan."
    hide BramaKMarah
    show BramaKKosong at lpos
    b "…"
    b "…"
    b "…"

    a "Brama, kau tahu aku nggak akan pernah menyarankan sesuatu yang buruk untukmu."
    a "Kau mungkin tidak menyukai caraku."
    hide AryaYSerius
    show AryaYNetral at ayrpos 
    a "Tapi aku hanya ingin memastikan kita semua tetap bertahan."
    a "Bukankah itu yang penting?"

    b "…"
    hide BramaKKosong
    show BramaKNetral at lpos
    b "Tapi bertahan dengan cara apa, Arya?"
    b "Dengan menjual prinsip kita?"
    b "Dengan membiarkan orang-orang itu terus menghancurkan kedaulatan kita?"

    a "…"
    a "Kau harus melihat gambaran besar, Brama."
    a "Ini bukan soal menyerah atau menjual prinsip."
    hide AryaYNetral
    show AryaYSerius at ayrpos
    a "Ini soal bertahan di medan perang yang tidak adil."
    hide AryaYSerius
    show AryaYNetral at ayrpos
    a "Kita melawan, tapi dengan cara yang cerdas."
    a "Kalau kau terlalu frontal, mereka akan menghancurkanmu sebelum kau sempat melakukan apa pun."
    hide AryaYNetral
    hide BramaKNetral

    show BramaK at cpos
    # [Brama beranjak dari kursinya mendekati jendela. Ia menatap ke luar.]
    "Brama beranjak dari kursinya dan mendekati jendela, menatap ke luar."
    
    menu:
        "Bertanya":
            jump bertanya
        "Tegaskan!":
            jump tegas

label bertanya:
    hide BramaK
    show BramaKNetral at lpos
    show AryaYNetral at ayrpos
    b "Arya, kita tidak bisa terus berpikir bahwa semua akan selesai dengan sendirinya."
    b "Sampai kapan kita terus bergantung, Arya?"
    b "Kalau kita tidak mulai sekarang, kapan kita akan membangun kemandirian itu?"
    b "Rakyat kita di Natuna sudah lama berteriak, tapi kita terus diam dengan alasan yang sama."
    hide BramaKNetral
    show BramaK at lpos
    a "Saya tidak bilang kita diam saja."
    a "Mungkin kita bisa meningkatkan patroli, memastikan kehadiran militer lebih terasa di sana."
    a "Tapi untuk tindakan agresif seperti menenggelamkan kapal mereka?"
    a "Itu langkah yang terlalu jauh."

    jump bramaberbeda

label tegas:
    hide BramaK
    show BramaKMarah at lpos
    show AryaYNetral at ayrpos
    b "Arya, kita tidak bisa terus berpikir bahwa semua akan selesai dengan sendirinya."
    b "Kalau kita tidak mulai mengambil keputusan sekarang, kita hanya akan menunda masalah."
    b "Orang-orang di Natuna butuh bukti, bukan janji lagi."
    hide BramaKMarah
    show BramaK at lpos
    a "Saya mengerti keresahan itu, Brama."
    a "Mungkin kita bisa mulai dengan pendekatan diplomatik yang lebih tegas."
    a "Tapi kalau kita langsung bertindak tanpa mempertimbangkan konsekuensinya, itu hanya akan memperkeruh situasi."

    jump bramaberbeda

label bramaberbeda:
    b "…"
    a "Brama, kau berbeda. Aku tahu itu."
    a "Kau punya hati, dan itu yang membuatmu lebih baik."
    hide AryaYNetral
    show AryaYSerius at ayrpos
    a "Kadang, kau harus mengotori tanganmu untuk bisa membersihkan lumpur yang lebih besar."
    hide BramaK
    show BramaKKosong at lpos
    b "…"
    hide AryaYSerius
    show maleGlitch at rpos
    o "BRAMA, jangan terpengaruh. Kau harus teguh pada prinsip awalmu yang sudah benar."

    b "…"
    hide maleGlitch
    show AryaYKopi at ayrpos
    a "Masih terdapat 5 hari lagi untuk kau memutuskan segalanya."
    a "Aku bicara soal bertahan, Brama."
    a "Bertahan untuk terus membangun negeri ini."
    a "Kalau kita kalah dalam perang ekonomi, bahkan kedaulatan yang kau perjuangkan itu tidak akan ada artinya."
    hide AryaYKopi
    show AryaYNetral at ayrpos
    a "Kita harus realistis."
    a "Gunakan diplomasi, mainkan strategi, jangan bertarung di medan yang jelas-jelas bukan keunggulan kita."
    a "Jangan lupa, batas waktu 5 hari lagi."
    a "Aku yakin kau akan mengambil keputusan yang benar."
    a "Aku pamit dulu, sampai jumpa nanti."
    hide AryaYNetral
    hide BramaKKosong
    show BramaK at cpos
    menu:
        "Ragu":
            jump ragu3
        "Arya masuk akal":
            jump arya_masuk_akal3

label ragu3:
    hide BramaK
    show BramaKNetral at cpos
    b "Arya mungkin benar."
    b "Kalau kita terlalu keras, kita bisa kehilangan semuanya."
    hide BramaKNetral
    show BramaKNetral at lpos

    show maleGlitch at rpos
    o "Tapi… bagaimana kamu bisa berdiri di depan rakyatmu nanti kalau kamu menyerah sekarang?"
    o "Apa yang akan mereka lihat darimu sebagai pemimpin?"

    jump merenung

label arya_masuk_akal3:
    hide BramaK
    show BramaKNetral at cpos
    b "Arya mungkin punya poin yang baik."
    b "Tindakan yang terlalu gegabah bisa membuat kita kehilangan apa yang sudah kita perjuangkan."
    hide BramaKNetral
    show BramaKNetral at lpos

    show maleGlitch at rpos
    o "Tapi jika kamu berhenti sekarang, bagaimana rakyatmu akan percaya lagi?"
    o "Apa yang akan kamu tunjukkan sebagai pemimpin mereka?"

    jump merenung

label merenung:
    hide BramaKNetral
    show BramaK at lpos
    o "Brama, cobalah merenung."
    o "Ini tentang hajat hidup masyarakat Natuna."
    o "Kamu harus berempati pada mereka."
    o "Ke sana lah! Berbincanglah dengan mereka."
    hide BramaK
    show BramaKNetral at lpos
    b "Iya, aku rasa aku harus berbicara dengan masyarakat lokal."
    o "Lakukan segera!"

    scene slideC2 with fade
    pause
    scene black with fade
    "*suara pesawat take-off*"
    scene pesisir with fade

    # [Mengikuti suara hatinya, Brama memutuskan untuk berangkat ke Natuna untuk berbincang langsung dengan masyarakat lokal]
    show pakades at cpos
    kades "Selamat datang, Pak Menteri."
    kades "Terima kasih sudah meluangkan waktu datang ke sini."
    kades "Kami sudah lama menunggu seseorang dari pusat untuk melihat langsung kondisi kami."
    hide pakades
    show BramaKSenang at cpos
    b "Saya yang seharusnya berterima kasih, Pak."
    b "Ini tanggung jawab saya untuk mendengar langsung keluhan bapak dan warga di sini."
    hide BramaKSenang
    show BramaKSenang at lpos
    show pakades at rpos
    kades "Pak Menteri, kami sudah kehabisan cara."
    hide BramaKSenang
    show BramaK at lpos
    kades "Kapal-kapal asing itu bukan hanya mencuri ikan kami, tapi juga menenggelamkan perahu-perahu kecil milik nelayan."
    kades "Satu-satunya yang kami miliki untuk mencari nafkah hanyalah laut."
    kades "Kami melawan sebisa mungkin, tapi apa daya…"
    kades "Kami tidak punya kekuatan seperti mereka."
    kades "Banyak rakyat yang mengungkapkan kapal mereka baru saja ditenggelamkan, Pak."
    kades "Mereka hampir tidak selamat."
    kades "Anak mereka yang baru masuk sekolah tidak tahu apa yang harus dimakan besok kalau ini terus terjadi."
    hide pakades
    hide BramaK
    show BramaK at cpos
    menu:
        "Berikan janji":
            jump berikan_janji
        "Tunjukkan empati":
            jump tunjukkan_empati

label berikan_janji:
    hide BramaK
    show BramaKNetral at lpos
    show pakades at rpos
    b "Saya mendengar semuanya, Pak."
    b "Saya tidak bisa bayangkan bagaimana beratnya hidup kalian di sini."
    b "Percayalah, pemerintah pusat tidak akan tinggal diam."
    b "Kami akan memastikan perairan kita aman dan hak kalian sebagai warga negara dilindungi."

    kades "Tapi, Pak Menteri… apa itu bukan hanya janji?"
    kades "Sudah berapa kali kami dijanjikan perlindungan, tapi tidak ada yang benar-benar berubah."
    kades "Kapal asing itu masih berkeliaran, dan hidup kami masih terancam."

    jump kembali_ke_script_utama

label tunjukkan_empati:
    hide BramaK
    show BramaKNetral at lpos
    show pakades at rpos
    b "Saya mendengar keluhan bapak dan warga di sini dengan sangat serius."
    b "Saya bisa merasakan betapa beratnya beban yang harus kalian pikul."
    b "Saya tidak datang ke sini hanya untuk berbicara, saya ingin membawa solusi nyata."
    hide BramaKNetral
    show BramaK at lpos
    kades "Pak Menteri, kami ingin percaya."
    kades "Tapi setiap kali ada kunjungan, selalu ada janji, dan setelah itu kami ditinggalkan sendirian lagi."
    kades "Sementara itu, kapal-kapal asing masih mengambil apa yang seharusnya milik kami, bahkan merusak hidup kami."
    hide BramaK
    show BramaKNetral at lpos
    b "Saya paham keraguan bapak, dan itu wajar."
    b "Tapi kali ini, saya pastikan ada langkah konkret."
    b "Kami akan meningkatkan patroli, memberikan dukungan hukum, dan memastikan pelaku ditindak."
    hide BramaKNetral
    show BramaK at lpos
    kades "Kami akan menunggu tindakan itu, Pak Menteri."
    kades "Tapi tolong, jangan sampai kami hanya menjadi korban lagi tanpa keadilan."

    jump kembali_ke_script_utama

label kembali_ke_script_utama:
    b "…"
    hide BramaK
    show BramaKNetral at lpos
    b "Saya tidak akan memberi janji kosong, Pak."
    b "Saya akan membawa suara bapak dan semua warga di sini langsung ke pusat."
    b "Jika perlu, saya sendiri yang akan memimpin pembicaraan ini di forum internasional."
    b "Kedaulatan negara kita tidak bisa ditawar."
    hide BramaKNetral
    show BramaK at lpos
    kades "Pak Menteri, jangan hanya bicara soal forum internasional."
    kades "Kami butuh tindakan sekarang. Berapa banyak lagi kapal kami yang harus tenggelam?"
    kades "Berapa banyak lagi keluarga yang harus kehilangan ayah mereka di laut?"
    hide pakades
    hide BramaK
    show BramaK at cpos
    menu:
        "Saya usahakan":
            jump saya_usahakan
        "Mari bersinergi":
            jump mari_bersinergi

label saya_usahakan:
    hide BramaK
    show BramaKNetral at lpos
    show pakades at rpos
    b "Bapak benar. Kita tidak bisa menunggu terlalu lama."
    b "Saya akan segera mengatur agar kapal patroli ditambah di Natuna."
    b "Tapi saya juga butuh dukungan kalian."
    b "Jangan pernah takut untuk melaporkan setiap pelanggaran."
    b "Ini perjuangan kita bersama."
    hide BramaKNetral
    show BramaK at lpos
    kades "Pasti, Pak!"
    hide BramaK
    show BramaKNetral at lpos
    b "Pak, terakhir, saya mohon… jika ada perkembangan atau ancaman baru, segera kabari saya."
    b "Saya tidak ingin ada korban lagi di sini."
    hide BramaKNetral
    show BramaK at lpos
    kades "Kami percaya pada Bapak, Pak Menteri."
    kades "Tapi tolong, jangan kecewakan kami lagi."
    hide BramaK
    show BramaKNetral at lpos
    b "Terima kasih atas kepercayaannya, akan saya lakukan yang terbaik."

    jump kembali_ke_script_utama_2

label mari_bersinergi:
    hide BramaK
    show BramaKNetral at lpos
    show pakades at rpos
    b "Bapak benar. Kita harus bergerak lebih cepat untuk melindungi wilayah kita."
    b "Namun, perlindungan ini tidak hanya soal kapal patroli. Kita juga perlu memperkuat kesadaran masyarakat di Natuna."
    b "Saya akan meminta pelatihan tambahan bagi nelayan agar mereka siap menghadapi situasi darurat."
    hide BramaKNetral
    show BramaK at lpos
    kades "Itu langkah yang bagus, Pak Menteri. Tapi, kami juga butuh kepastian."
    kades "Nelayan kami tidak bisa hanya bergantung pada pelatihan, mereka butuh pengamanan nyata di laut."
    hide BramaK
    show BramaKNetral at lpos
    b "Tentu, Pak. Kapal patroli akan segera kami tambahkan, tapi ini perjuangan jangka panjang."
    b "Mohon kerja sama dan kesiagaan dari Bapak dan warga di sini. Kita tidak boleh lengah."
    hide BramaKNetral
    show BramaK at lpos
    kades "Kami akan mendukung semampu kami, Pak Menteri. Yang penting, jangan biarkan kami menghadapi ini sendirian."
    hide BramaK
    show BramaKNetral at lpos
    b "Saya berjanji akan terus memantau situasi di sini. Jika ada perkembangan atau ancaman baru, kabari saya segera."

    kades "Baik, Pak. Kami percaya pada Bapak, tapi buktikan bahwa kami tidak salah berharap."
    hide BramaK
    show BramaKSenang at lpos
    b "Terima kasih atas kepercayaan ini. Saya tidak akan mengecewakan kalian."

    jump kembali_ke_script_utama_2

label kembali_ke_script_utama_2:
    hide BramaKSenang
    show BramaKNetral at lpos
    b "Kalau begitu, saya izin pamit kembali ke Jakarta."
    b "Mohon ditunggu untuk koordinasi dan informasi lebih lanjut."
    hide BramaKNetral
    show BramaK at lpos
    kades "Baik, Pak. Terima kasih banyak atas perhatiannya kepada kami."

    # [Scene dalam pesawat]
    scene pesawat with fade
    show BramaKNetral at cpos
    b "Mereka semua menggantungkan harapan pada saya."
    hide BramaKNetral
    show BramaKBingung at cpos
    b "Tapi apa yang bisa saya lakukan?"
    b "Diplomasi butuh waktu, sementara mereka sudah kehilangan segalanya."
    b "Apakah ini saatnya saya harus mengambil langkah yang lebih keras…?"
    b "Meski itu berarti membawa negara ini ke risiko yang lebih besar?"

    # [Keesokan harinya]
    scene ruang_kerja_bram_malam with fade
    show AryaYKopi at ayrpos
    show BramaK at lpos
    a "Kau masih di sini, Brama? Sudah larut malam."
    a "Aku pikir kau sudah pulang."
    hide BramaK
    show BramaKBingung at lpos
    b "Ada terlalu banyak hal di kepala."
    b "Tidur rasanya bukan pilihan malam ini."
    hide AryaYKopi
    show AryaYSenyum at ayrpos
    a "Aku tahu kau selalu memikirkannya dengan serius."
    a "Itu yang aku kagumi darimu."
    hide AryaYSenyum
    show AryaYNetral at ayrpos
    a "Tapi kau tidak bisa terus-menerus memikul semua ini sendirian."
    hide BramaKBingung
    show BramaK at lpos
    b "…"
    hide BramaK
    show BramaKNetral at lpos
    b "Mereka menggantungkan harapan pada kita, Arya."
    b "Masyarakat Natuna… mereka benar-benar terdesak."
    hide BramaKNetral
    show BramaKKosong at lpos
    b "Bagaimana aku bisa pulang dan tidur dengan tenang sementara mereka bahkan tidak tahu apakah mereka bisa makan esok hari?"
    hide BramaKKosong
    show BramaK at lpos
    hide AryaYNetral
    show AryaYKopi at ayrpos
    a "Aku mengerti. Aku sudah mendengar semuanya."  
    a "Tapi Brama, aku harus mengingatkanmu lagi."
    hide AryaYKopi
    show AryaYSerius at ayrpos
    a "Langkah gegabah tidak akan menyelesaikan apa-apa." 
    a "Kau tahu risiko yang akan kita hadapi jika bertindak terlalu keras."
    hide BramaK
    show BramaKMarah at lpos
    b "Risiko itu sudah mereka hadapi setiap hari, Arya." 
    b "Kapal mereka tenggelam. Hidup mereka hancur."
    b "Jika aku diam, aku sama saja dengan membiarkan semua itu terus terjadi." 
    hide BramaKMarah
    show BramaK at lpos
    hide AryaYSerius
    show AryaYNetral at ayrpos
    a "Aku tidak bilang kita diam. Aku bilang, kita harus pintar."  
    a "Diplomasi itu alat yang sulit, tapi itu satu-satunya jalan yang tidak menghancurkan kita semua.  "
    a "Kau tahu bagaimana negara ini masih bergantung pada pihak luar." 
    a "Jika kita kehilangan mereka, situasi bisa lebih buruk daripada sekarang."
    hide BramaKMarah
    show BramaKBingung at lpos
    b "Tapi apakah diplomasi akan cukup? "
    b "Setiap detik yang kita habiskan untuk berbicara, mereka kehilangan lebih banyak.  "
    b "Bagaimana aku bisa menghadapi mereka lagi jika aku tidak membawa perubahan nyata? " 
    hide AryaYNetral
    show AryaYKopi at ayrpos
    a "Diplomasi mungkin lambat, tapi itu lebih aman daripada langkah frontal yang bisa menghancurkan kita. " 
    a "Kita perlu strategi.  "
    a "Jika kau terlalu keras sekarang, kita mungkin tidak akan punya kesempatan untuk memperbaiki keadaan di masa depan."  
    hide BramaKBingung
    show BramaKNetral at lpos
    b "Lalu, sampai kapan kita menunggu? "
    b "Sampai kapan kita hanya menjadi pemain kecil di medan yang dikuasai orang lain?  "
    hide AryaYKopi
    show AryaYSenyum at ayrpos
    a "Sampai kita cukup kuat untuk melawan.  "
    a "Brama, kau harus memikirkan ini secara jangka panjang.  "
    hide AryaYSenyum
    show AryaYNetral at ayrpos
    a "Masyarakat Natuna membutuhkanmu, tapi mereka juga membutuhkan negara ini tetap berdiri. " 
    a "Jangan mengambil langkah yang bisa membuat kita kehilangan segalanya. " 
    hide BramaKNetral
    show BramaKBingung at lpos
    b "Aku tidak tahu, Arya."  
    b "Bagaimana jika aku salah?"  
    b "Bagaimana jika pilihan ini malah memperpanjang penderitaan mereka?"  
    hide BramaKBingung
    show BramaK at lpos
    hide AryaYNetral
    show AryaYSenyum at ayrpos
    a "Kau tidak sendirian dalam hal ini."  
    a "Aku di sini untuk mendukungmu, dan begitu juga yang lainnya."  
    a "Tapi aku mohon, pertimbangkan ini baik-baik."  
    a "Jangan biarkan emosimu mengaburkan pandanganmu."  
    hide BramaK
    show BramaKNetral at lpos
    b "Aku akan memikirkannya, Arya."  
    b "Aku tahu kau hanya ingin yang terbaik, tapi aku masih belum tahu apakah yang terbaik itu cukup untuk mereka. " 
    hide AryaYSenyum
    show AryaYKopi at ayrpos
    a "Kau punya lima hari lagi untuk memutuskan, Brama."  
    a "Gunakan waktu itu dengan bijak."  
    a "Aku percaya kau akan mengambil langkah yang benar."  
    hide BramaKNetral
    show BramaKLega at lpos
    b "Terima kasih, Arya. Aku berharap aku bisa sebijak yang kau pikirkan."  
    hide AryaYKopi
    show AryaYKetawa at ayrpos
    a "Kau lebih bijak dari yang kau sadari, Brama." 
    a "Jangan terlalu keras pada dirimu sendiri."
    hide AryaYKetawa
    hide BramaKLega
    show BramaK at cpos
    menu:
        "Perjuangkan Natuna":
            jump E
        "Ikuti Arya":
            jump F

# # ------------------------------------- SCRIPT D -------------------------------------# #
image pesisir = im.Scale("bg/Natuna.png", 1920, 1080)
image chaos = im.Scale("bg/chaos.png", 1920, 1080)
define warga_a = Character("Warga", color="#bae6ff")
image pakades:
    "chara/pakades.png"
    zoom 1.5
# IMAGE TEXT
image slideD1 = im.Scale("text/D/Slide1.PNG", 1920, 1080)
image slideD2 = im.Scale("text/D/Slide2.PNG", 1920, 1080)
image slideD3 = im.Scale("text/D/Slide3.PNG", 1920, 1080)
image slideD4 = im.Scale("text/D/Slide4.PNG", 1920, 1080)
image slideD5 = im.Scale("text/D/Slide5.PNG", 1920, 1080)
image slideD6 = im.Scale("text/D/Slide6.PNG", 1920, 1080)
image slideD7 = im.Scale("text/D/Slide7.PNG", 1920, 1080)

label D:
    scene ruang_kerja_bram_pagi with fade
    show BramaK at cpos
    b "Apa yang dikatakan oleh Arya tadi ada benarnya juga."
    b "Tapi apakah hal tersebut merupakan yang terbaik bagi masyarakat dan negara?"
    b "Apa jadinya jika aku tetap ngotot untuk memaksakan kehendakku?"
    b "Apalagi sampai nekat melakukan konfrontasi secara langsung terhadap frigate China."
    b "Sudah pasti ekonomi negara ini bisa kacau."
    hide BramaK
    show maleGlitch at cpos
    o "Brama, sadar lah!!! Keputusan yang kamu ambil saat ini sangat merugikan bagi rakyat."
    o "Mereka bertaruh nyawa demi mencari sesuap nasi dan dibayangi oleh kapal asing yang semena-mena."
    o "Apa kamu tidak kasihan dengan mereka, Brama?"
    o "Bagaimana kalau kejadian ini terus berulang dan menghilangkan nyawa mereka?"
    hide maleGlitch
    show BramaK at cpos
    b "Tindakan yang telah aku ambil merupakan yang terbaik bagi kita semua."
    b "Aku tidak bisa mengorbankan ekonomi dan kestabilan negara ini hanya untuk menembaki kapal-kapal itu."
    hide BramaK
    show maleGlitch at cpos   
    o "Sungguh jahatnya dirimu, Brama."
    o "Di mana sisi kemanusiaanmu itu?"
    o "Apakah kau mulai ragu terhadap dirimu sendiri hingga kau tidak mengutamakan keadilan dan kepentingan rakyat?"
    hide maleGlitch
    show BramaK at cpos
    b "…"

    scene slideD1 with fade
    pause
    scene ruang_rapat_menteri with fade
    show AryaYSenyum at aycpos
    a "Brama, tindakan yang anda ajukan tadi sungguh ide cerdas."
    a "Kita harus mengutamakan hubungan kedua negara."
    a "Jangan sampai perekonomian kita hancur cuma gara-gara hal ini."

    menu:
        "Tekankan transparansi":
            jump tekankan_transparansi
        "Tekankan kerja sama":
            jump tekankan_kerja_sama

label tekankan_transparansi:
    scene ruang_rapat_menteri with fade
    show BramaKSenang at cpos
    b "Eh iya, terima kasih, Arya. Kamu benar-benar mengingatkanku soal tanggung jawab yang lebih besar."
    b "Kalau waktu itu aku terlalu emosional, mungkin kita malah menghadapi situasi yang lebih kacau sekarang."
    show BramaKSenang at lpos
    show AryaYSenyum at ayrpos
    a "Betul, Brama. Kadang sulit untuk menahan emosi saat menghadapi masalah besar seperti ini."
    a "Tapi itulah tugas kita, memastikan setiap keputusan membawa dampak positif, bukan sekadar reaksi sesaat."
    a "Bagaimanapun, yang kita lakukan ini untuk menjaga masa depan negara, bukan hanya menyelesaikan masalah sesaat."

    b "Kamu benar, Arya. Tapi aku masih merasa khawatir tentang bagaimana masyarakat akan menerima ini."
    b "Mereka butuh hasil nyata, bukan sekadar janji diplomasi."

    a "Itu tugas kita selanjutnya, Brama."
    a "Pastikan langkah-langkah yang sudah direncanakan, seperti peningkatan patroli dan perlindungan nelayan, benar-benar berjalan. Masyarakat butuh melihat bukti nyata."

    b "Iya, itu harus jadi prioritas. Kalau masyarakat merasa terlindungi, mereka akan lebih mendukung langkah kita."
    b "Tapi aku harap kita bisa segera menyampaikan ini kepada Presiden."

    a "Pasti, Brama. Dengan dukungan Presiden, rencana ini bisa lebih kuat."
    a "Dan jangan lupa, transparansi dengan masyarakat itu kunci."
    a "Kita harus terus berkomunikasi dengan mereka."

    b "Benar, Arya. Terima kasih atas pandanganmu. Aku rasa, tanpa masukanmu, aku mungkin sudah mengambil langkah yang bisa merugikan banyak pihak."

    a "Sama-sama, Brama. Kita ada di sini untuk saling mengingatkan."
    a "Yang penting, kita tetap bekerja untuk kebaikan bersama."

    jump kembali_ke_rumah

label tekankan_kerja_sama:
    scene ruang_rapat_menteri with fade
    show BramaKSenang at cpos
    b "Eh iya, terima kasih, Arya. Kamu benar-benar membuka mataku soal risiko yang mungkin terjadi."
    b "Kalau waktu itu aku tetap keras kepala, mungkin dampaknya akan jauh lebih buruk bagi negara kita."
    show BramaKSenang at lpos
    show AryaYSenyum at ayrpos
    a "Ah, nggak perlu berlebihan, Brama. Yang penting, kita bisa menjaga keseimbangan antara kedaulatan negara dan hubungan internasional."
    a "Kalau kita berhasil mengelola ini dengan baik, saya yakin masyarakat juga akan melihat manfaatnya dalam jangka panjang."

    b "Betul, Arya. Tapi, aku tahu pasti akan ada kritik. Apalagi dari mereka yang merasa kita kurang tegas."

    a "Itu wajar, Brama. Kita tidak bisa memuaskan semua pihak."
    a "Tapi kalau hasil akhirnya baik untuk rakyat dan negara, itu yang paling penting."
    a "Saya percaya, kalau Presiden dan masyarakat melihat rencana ini dijalankan dengan serius, mereka akan mendukung."

    b "Iya, Arya. Semoga langkah ini menjadi titik awal perubahan yang lebih baik. Terima kasih sudah mendukungku berpikir lebih bijak."

    a "Sama-sama, Brama. Ini tanggung jawab kita bersama untuk menjaga stabilitas negara."

    jump kembali_ke_rumah

label kembali_ke_rumah:
    scene terasrumah_y with fade
    show BramaK at cpos
    b "Sayang, aku pulang."
    show BramaK at rpos
    show Istri s at lpos
    ist "Eh sayang, udah pulang. Bagaimana pekerjaan hari ini sayang?"
    hide Istri s 
    show Istri at lpos
    ist "Dilihat-lihat dari raut wajah, kayaknya ini hari yang melelahkan ya di kantor?"
    b "Iya sayang, kok kamu peka banget sih sama suami mu ini, hari ini hari yang berat."
    b "Tadi aku habis rapat terbatas dengan beberapa menteri, kami membahas mengenai LCS."
    hide Istri
    show Istri s at lpos
    ist "Wah, aku yang mendengarkan saja bisa membayangkan betapa capeknya, apalagi kamu yang ngejalanin ya sayang."
    hide Istri s 
    show Istri at lpos
    b "Oiya, Nina di mana? Kok aku tidak melihatnya dari tadi?"
    hide Istri
    show Istri s at lpos
    ist "Nina belum pulang sayang, dia lagi di jalan pulang sehabis les."
    hide Istri s 
    show Istri at lpos
    b "Paling sebentar lagi sampai rumah."
    hide Istri
    show Istri s at lpos
    ist "Sekarang kamu bebersih sambil nunggu Nina pulang, terus kita makan malam bersama, okay?"
    hide BramaK
    show BramaKSenang at rpos
    b "Oke sayang."

    scene slideD2 with fade
    pause
    scene ruangmakan_y with fade
    show BramaK at lpos
    show Istri at cpos
    show Nina at rpos
    b "Istri dan anakku sayang, ayah lusa mau pergi beberapa hari ke sana."
    b "Ada pekerjaan yang harus ayah selesaikan di sana."
    hide Istri 
    show Istri s at cpos
    ist "Pasti soal kapal nelayan di situ ya, yah?"
    hide Istri s 
    show Istri at cpos
    hide BramaK 
    show BramaKSenang at lpos
    b "Iya sayang, aku harus ke sana untuk mengecek keadaan masyarakat di sana."
    hide BramaKSenang 
    show BramaK at lpos
    n "Hati-hati ya, yah. Awas ditenggelamkan sama coast guard China."
    hide BramaK 
    show BramaKSenang at lpos
    b "Aduh, bisaan anak ayah satu ini. Iya, ayah akan hati-hati di sana."
    hide BramaKSenang 
    show BramaK at lpos
    hide Istri 
    show Istri s at cpos
    ist "Iya, ayah hati-hati ya. Semoga masalah ini cepat selesai."
    hide Istri s 
    show Istri at cpos
    hide BramaK 
    show BramaKSenang at lpos
    b "Iya sayang, makasih."
    jump keesokan_harinya

label keesokan_harinya:
    scene slideD3 with fade
    pause
    scene pesisir with fade
    show BramaKSenang at cpos
    b "Selamat siang bapak ibu masyarakat. Perkenalkan saya Brama selaku menteri luar negeri."
    b "Kehadiran saya di sini adalah untuk mendengarkan dan berdiskusi kepada bapak-bapak dan ibu-ibu."
    b "Bahasannya mengenai laut yang diganggu oleh kapal China."
    show BramaKSenang at lpos
    show pakades at ayrpos
    kades "Selamat datang, Pak Menteri."
    kades "Terima kasih sudah meluangkan waktu datang ke sini."
    kades "Kami sudah lama menunggu seseorang dari pusat untuk melihat langsung kondisi kami."

    b "Saya yang seharusnya berterima kasih, Pak."
    b "Ini tanggung jawab saya untuk mendengar langsung keluhan bapak dan warga di sini."

    kades "Pak Menteri, kami sudah kehabisan cara."
    kades "Kapal-kapal asing itu bukan hanya mencuri ikan kami, tapi juga menenggelamkan perahu-perahu kecil milik nelayan."
    kades "Satu-satunya yang kami miliki untuk mencari nafkah hanyalah laut."
    kades "Kami melawan sebisa mungkin, tapi apa daya… kami tidak punya kekuatan seperti mereka."

    menu:
        "Yakinkan mereka":
            jump yakinkan_mereka
        "Arya masuk akal":
            jump arya_masuk_akal

label yakinkan_mereka:
    b "Saya mengerti perasaan Bapak dan warga di sini."
    b "Saya sendiri marah setiap kali mendengar kejadian seperti ini."
    b "Tapi kita harus menghadapi ini dengan kepala dingin."

    kades "Kepala dingin, Pak Menteri? Kami sudah cukup sabar!"
    kades "Apa lagi yang harus kami tunggu? Kapal-kapal asing itu semakin merajalela!"

    b "Saya paham, Pak. Justru itulah mengapa saya di sini."
    b "Saya ingin memastikan suara Bapak dan masyarakat sampai ke tingkat internasional."
    b "Dengan diplomasi, kita bisa mempermalukan China di hadapan dunia."
    b "Bukankah itu lebih efektif daripada konfrontasi langsung yang justru bisa merugikan kita sendiri?"

    kades "Tapi, Pak, selama proses itu berjalan, nelayan kami terus menjadi korban."
    kades "Apa gunanya bicara di tingkat internasional kalau kami menderita?"

    b "Itu kekhawatiran yang wajar, Pak. Tapi mari kita pikirkan ini."
    b "Jika kita memulai tindakan agresif, apakah Bapak siap melihat eskalasi yang bisa membuat ini menjadi medan konflik?"
    b "Jika itu terjadi, bukan hanya nelayan yang terancam, tapi seluruh masyarakat."

    kades "Jadi, maksud Pak Menteri, kami harus menyerah?"

    b "Tentu saja tidak, Pak. Justru saya sedang memperjuangkan jalan yang lebih aman dan bermartabat bagi kita semua."
    b "Saya juga sedang berkoordinasi untuk meningkatkan bantuan pusat, termasuk kapal patroli dan perlindungan hukum bagi nelayan."

    kades "Itu terdengar seperti janji lama, Pak Menteri. Kami ingin bukti nyata."

    b "Dan Bapak akan mendapatkannya. Tapi saya mohon pengertian, Bapak."
    b "Jika kita bertindak sembrono, kita tidak hanya mempertaruhkan hubungan dagang dengan China, tetapi juga masa depan anak-anak kita di sini."
    b "Apa yang akan mereka warisi jika ini menjadi zona konflik?"

    jump kembali_ke_script

label arya_masuk_akal:
    b "Saya memahami rasa frustrasi Bapak dan seluruh warga. Kondisi ini memang sangat tidak adil bagi kita."
    b "Namun, saya ingin berbagi bahwa pendekatan kita harus strategis."

    kades "Strategis seperti apa, Pak Menteri? Apakah hanya dengan kata-kata? Sementara nelayan kami terus menjadi korban."

    b "Bukan hanya kata-kata, Pak. Kami sedang merancang langkah diplomasi yang melibatkan pihak internasional."
    b "Dengan cara ini, kita bisa menekan China secara hukum tanpa memicu konflik langsung."

    kades "Pak Menteri, dengan segala hormat, apakah diplomasi itu akan cukup?"
    b "Kapal-kapal asing itu tidak pernah peduli dengan peringatan."
    b "Mereka terus datang, dan kami di sini yang harus menanggung akibatnya."

    b "Saya tidak mengatakan ini mudah, Pak Kades. Namun, tindakan agresif terhadap China bisa berdampak buruk bagi kita semua."
    b "Mereka adalah mitra dagang terbesar kita, dan konflik langsung bisa mem engaruhi perekonomian nasional, termasuk wilayah ini."

    kades "Jadi, kami harus terus hidup dalam ketakutan, Pak? Apakah nyawa nelayan kami tidak lebih penting daripada ekonomi?"

    b "Saya tidak mengatakan begitu, Pak. Nyawa warga adalah prioritas saya."
    b "Kami akan menambah kapal patroli, memperkuat pengawasan, dan memberikan pelatihan kepada nelayan untuk mengurangi risiko."
    b "Tapi kita harus berhati-hati agar tidak memicu ketegangan internasional yang lebih besar."

    kades "Kapal patroli? Itu seperti membangun dinding yang tidak pernah selesai, Pak Menteri."
    kades "Kami butuh tindakan yang lebih nyata dan tegas!"

    b "Pak Kades, saya memahami amarah Bapak, tapi kita harus melihat ini secara keseluruhan."
    b "Jika kita memilih konfrontasi, risikonya terlalu besar."
    b "Saya yakin, dengan tekanan diplomasi, kita bisa menyelesaikan ini secara berimbang."

    jump kembali_ke_script

label kembali_ke_script:
    scene chaos with fade

    warga_a "Dasar pemerintah egois!!! Mereka tidak memikirkan rakyatnya yang di sini!"
    warga_a "Kami di sini setiap hari bertaruh dengan nyawa setiap kali bertemu dengan mereka."
    warga_a "Bahkan kapal kami tak segan-segan mereka tenggelamkan di wilayah negara kita sendiri."
    warga_a "Tapi apa nyatanya pemerintah malah berpihak pada aseng?"

    warga_a "SETUJU! Negara tidak peduli terhadap rakyatnya sendiri tapi malah memikirkan kantongnya sendiri!"
    # [Keadaan menjadi anarkis dan Kamil segera meninggalkan tempat dengan pengawalan ketat]
    # {suara chaos demo anarkis}
    scene slideD4 with fade
    pause
    # [Polisi menghadang massa yang semakin menggila dan berujung pada sedikit kerusuhan yang menyebabkan beberapa masyarakat mengalami luka-luka]
    # {ditambah suara sirine polisi}
    scene slideD5 with fade
    pause
    # -time skip-
    scene slideD7 with fade
    pause
    scene kantor with fade
    show BramaKNetral at cpos
    b "Apa tindakan yang aku lakukan ini merupakan yang terbaik?"
    b "Lantas mengapa banyak yang menolak?"
    hide BramaKNetral
    show maleGlitch at cpos
    o "Apa yang kamu lakukan merupakan hal yang salah, Brama."
    o "Ini tidak sesuai dengan prinsip pribadimu."
    o "Kau rela mengorbankan rakyat demi kepentingan pribadimu."
    hide maleGlitch
    show BramaKNetral at cpos
    b "Tidak. Aku tidak mengorbankan mereka dan tidak untuk kepentingan pribadiku."
    b "Ini semua demi rakyat dan negara. Tau apa mereka soal politik dan ekonomi?"
    hide BramaKNetral
    show maleGlitch at cpos
    o "Mereka mungkin tidak berpendidikan tinggi seperti dirimu."
    o "Tapi apakah mereka pantas dikorbankan begitu saja?"
    o "Apa kau tidak kasihan dengan keluarganya?"
    o "Di mana sisi kemanusiaanmu itu, Brama?"
    hide maleGlitch
    show BramaKNetral at cpos
    b "Aku akan tetap menjalankan rencana yang sudah disetujui dengan presiden apapun itu caranya."
    b "Aku tidak akan membiarkan konflik ini membawa buruk bagi perekonomian dan hubungan kedua negara."
    hide BramaKNetral
    show maleGlitch at cpos
    o "Kau memang sudah berubah, Brama."
    o "Mana Brama yang ku kenal itu yang mengutamakan keadilan dan kepentingan rakyat?"
    o "Rakyat juga butuh kehadiran negara untuk melindungi mereka."

    menu:
        "Mantab ikuti Arya":
            jump H
        "Ragu":
            jump G
image keesokan_harinya = im.Scale("text/E/slide1.png", 1920, 1080)

# # ------------------------------------- SCRIPT E -------------------------------------# #
label E:
    play music office_bgm
    scene black with fade
    show keesokan_harinya
    pause 1
    scene ruang_kerja_bram_pagi with fade
    show BramaKBingung at cpos
    b "Apa yang sebenarnya harus kulakukan?"
    b "Semua fakta ada di depan mata."
    b "Aspirasi rakyat tidak bisa diabaikan, tapi tekanan Arya semakin berat."
    b "Apa aku benar-benar mampu menghadapi ini seorang diri?"
    b "Mereka menggantungkan harapan padaku…"
    b "Rakyat di Natuna, kepala desa, anak-anak kecil yang masa depannya bergantung pada keputusan ini."
    b "Bagaimana mungkin aku menyerah?"
    b "Arya tidak tahu apa-apa tentang tanggung jawab ini."
    b "Dia hanya memikirkan angka dan strategi."
    b "Tapi aku tahu, aku di sini bukan untuk melayani kepentingan jalur diplomasi."
    b "Aku ada di sini untuk mempertahankan prinsip dan martabat bangsa."
    stop music
    hide BramaKBingung
    play sound ngetok
    "tok…tok…tok…"
    show BramaKBingung at rpos
    show AryaYSenyum at alpos with fade
    play music office_bgm
    a "Brama…"

    b "Eh Arya, masuk."

    a "Brama, aku butuh kepastian."
    b "Kau benar-benar menolak kesepakatan damai dengan China?"
    hide BramaKBingung
    hide AryaYSenyum
    menu:
        "Tolak mentah":
            jump tolak_mentah
        "Kita tidak boleh menyerah":
            jump tidak_boleh_menyerah

label tolak_mentah:
    show BramaKNetral at rpos
    show AryaYSerius at alpos
    b "Ya, Arya. Aku menolaknya."

    a "Jadi benar."
    a "Kau memilih rakyat Natuna daripada peluang untuk menghentikan konflik ini dengan cara damai?"

    b "Pilihan itu tidak benar-benar damai, Arya."
    b "Kesepakatan itu sama saja membiarkan kedaulatan kita diinjak-injak."

    a "Brama, kau sadar apa yang kau lakukan?"
    a "Kau mempertaruhkan stabilitas negara ini."
    a "Jika kita melawan mereka, konsekuensinya akan jauh lebih besar dari yang bisa kau bayangkan."

    b "Kalau kita terus menyerah, kapan kita akan mulai berdiri di atas kaki sendiri?"
    b "Ini bukan hanya soal stabilitas, Arya."
    b "Ini tentang harga diri bangsa."

    a "Kau terlalu idealis, Brama."
    a "Dunia ini tidak bekerja seperti itu."
    a "Kita harus memilih pertarungan yang bisa kita menangkan."

    b "Aku sudah memilih, Arya."
    b "Aku akan berdiri bersama rakyat Natuna."
    hide BramaKNetral
    hide AryaYSerius
    jump pindahidealis

label tidak_boleh_menyerah:
    show BramaKNetral at rpos
    show AryaYSerius at alpos
    b "Aku tidak bisa menerima kesepakatan itu, Arya."

    a "Jadi, kau memilih jalan ini, meskipun kita tahu konsekuensinya akan sangat berat?"

    b "Jalan yang mereka tawarkan bukanlah damai, Arya."
    b "Itu penyerahan diri."

    a "Penyerahan diri? Kau tahu ini bukan soal kalah atau menang, Brama. Ini soal bertahan."

    b "Bertahan dengan menyerahkan kedaulatan kita?"
    b "Itu bukan bertahan, Arya. Itu kehancuran yang tertunda."

    a "Apa kau sadar apa yang sedang kau lakukan?"
    a "Kau mempertaruhkan masa depan negara ini untuk sesuatu yang mungkin tidak bisa kita menangkan!"

    b "Kalau kita terus menyerah dan bergantung, kapan kita akan memulai langkah untuk benar-benar berdaulat?"
    b "Harga diri bangsa ini tidak boleh terus dipertaruhkan hanya karena ketakutan."

    a "Kau terlalu keras kepala."
    a "Dunia tidak bekerja seperti idealismemu, Brama. Kita harus pragmatis."



    b "Mungkin aku memang keras kepala, Arya."
    b "Tapi aku tidak akan berpaling dari rakyat Natuna."
    b "Aku tahu ini tidak mudah, tapi mereka pantas untuk diperjuangkan."

    jump pindahidealis

label pindahidealis:
    show BramaKNetral at rpos
    show AryaYSerius at alpos
    a "Kau benar-benar keras kepala. Kau tahu, kau bukan hanya mempertaruhkan posisi menteri di sini."
    hide BramaKNetral
    show BramaKBingung at rpos 
    b "Apa maksudmu?"
    hide AryaYSerius
    show AryaYSenyum at alpos
    a "Kau ingat proyek dapur di Changi dulu?"
    a "Kau tahu dari mana uang untuk menyelamatkan ekspansi itu berasal?"
    hide AryaYSenyum
    hide BramaBingung
    menu:
        "Investor besar":
            jump investor_besar
        "Investor yang tepat":
            jump investor_yang_tepat

label investor_besar:
    show BramaKBingung at rpos 
    show AryaYNetral at alpos
    b "Tentu saja. Dari PT Angin Topan. Mereka adalah investor besar."

    a "Kau benar-benar tidak tahu, ya?"
    a " PT Angin Topan itu bukan sekadar investor biasa."
    a "Itu adalah topeng untuk mencuci uang seorang koruptor."
    hide BramaKBingung
    show BramaKMarah at rpos
    b "Apa?"

    a "Ya. Mereka menyuntikkan uang itu ke proyekmu, dan aku yang mengatur semuanya agar terlihat legal."
    a "Kalau ini sampai terbongkar, kau tahu apa yang akan terjadi, bukan?"

    b "Tidak, ini tidak mungkin. Kau pasti bercanda, Arya."

    a "Aku tidak bercanda."
    a "Dan kalau kau terus memaksakan idealismemu, aku tidak punya pilihan lain selain membuka ini ke publik."

    b "Kau… Kau menyembunyikan ini dariku?"

    a "Aku melakukannya untuk menyelamatkanmu, Brama."
    a "Dan sekarang, aku minta kau berpikir baik-baik."
    a "Jangan buat keputusan bodoh yang akan menghancurkan kita semua."

    b "Jadi ini ancaman, Arya?"

    a "Ini peringatan, Brama."
    a "Aku tidak ingin kau hancur. Tapi kau harus realistis."

    b "Kalau itu yang harus terjadi, biarlah."
    b "Aku tidak tahu soal asal-usul uang itu, tapi kalau ini adalah konsekuensi dari kesalahan masa lalu, aku akan menanggungnya."

    a "Kau serius? Kau benar-benar tidak peduli kalau ini akan menghancurkanmu?"

    b "Aku peduli, Arya."
    b "Tapi aku lebih peduli pada mereka yang sudah terlalu lama hidup dalam ketidakadilan."
    b "Aku tidak bisa mengabaikan rakyat Natuna."

    a "Kau akan menghancurkan dirimu sendiri, Brama."
    a "Dan mungkin negara ini juga."

    b "Kalau itu harga yang harus kubayar untuk melakukan hal yang benar, maka biarlah."

label investor_yang_tepat:
    show BramaKBingung at rpos 
    show AryaYNetral at alpos
    b "Tentu saja. Dari PT Angin Topan. Mereka adalah investor besar yang datang di saat yang tepat."

    a "\"Investor besar,\" katamu? Brama, PT Angin Topan itu topeng."
    a "Itu digunakan untuk mencuci uang seorang koruptor besar di negeri ini."
    hide BramaKBingung
    show BramaKMarah at rpos
    b "Apa yang kau bicarakan, Arya? Kau tidak serius, kan?"

    a "Aku sangat serius."
    a "Dan aku yang mengatur semuanya waktu itu agar uang itu terlihat legal, supaya proyekmu tidak runtuh."

    b "Ini… tidak mungkin. Kenapa kau tidak memberitahuku?"

    a "Karena aku tahu kau tidak akan setuju, Brama!"
    a "Tapi aku melakukannya untuk menyelamatkanmu."
    hide BramaKMarah
    show BramaKMarah at rpos
    b "Kau menyebut ini menyelamatkan?"
    b "Kau menyeretku ke dalam sesuatu yang kotor tanpa memberiku pilihan!"

    a "Dengarkan aku, Brama. Ini sudah berlalu, dan semuanya baik-baik saja selama ini."

    b "Jangan buat keputusan yang akan menggali luka lama ini."
    b "Aku tidak tahu tentang ini sebelumnya."
    b "Tapi jika yang kau katakan benar, ini masalah besar, Arya."

    a "Dan jika kau memaksa melawan China, aku tidak punya pilihan selain membuka ini ke publik."
    a "Aku tidak ingin, tapi aku tidak bisa membiarkan kau menghancurkan segalanya."

    b "Jadi, ini ancaman?"

    a "Ini kenyataan, Brama. Aku tidak mau ini terjadi, tapi kau memaksaku."

    b "Aku mengerti maksudmu, Arya."
    b "Tapi ini bukan tentang ancaman atau masa lalu."
    b "Ini tentang keputusan yang harus aku buat sekarang."

    a "Dan keputusan itu bisa menghancurkan kita semua, Brama. Kau tahu itu."
    hide BramaKMarah
    show BramaKBingung at rpos 
    b "Aku tidak tahu harus berkata apa, Arya. Aku merasa dikhianati oleh kebenaran ini."
    b "Tapi aku juga tahu satu hal, aku tidak bisa mengabaikan apa yang terjadi di Natuna."
    hide AryaYNetral
    show AryaYSerius at alpos
    a "Jadi kau akan tetap maju? Kau akan menanggung semuanya sendiri?"
    hide BramaKBingung
    show BramaKNetral at rpos 
    b "Aku akan menanggung apa pun konsekuensinya."
    b "Jika aku harus membayar kesalahan masa lalu untuk memperjuangkan yang benar hari ini, aku siap."

    a "Kau gila, Brama. Tapi kalau itu keputusanmu, aku hanya berharap kau tahu apa yang kau lakukan."

    b "Aku juga berharap begitu, Arya."
    b "Tapi satu hal yang pasti, aku tidak akan meninggalkan rakyat Natuna."

    a "…"
    a "Brama…"

    b "Apa?"

    a "Aku teringat perkataan Imam Syafi’i."
    a "Beliau mengatakan bahwa 'Aku mampu berdebat dengan 10 orang berilmu, tapi aku pasti tak menang dengan seorang yang bodoh.'"
    a "Aku rasa aku mengerti sekarang."

    b "…"

    b "Sampai jumpa esok di rapat presiden."
    hide BramaKNetral
    hide AryaYSerius

    # [Keesokan harinya]
    scene ruang_rapat_menteri with fade
    show AryaYNetral at arpos
    show BramaKNetral at lpos with fade
    a "Brama, bagus kau datang. Kita perlu bicara soal langkah selanjutnya."
    a "Ingat, kita harus membuat semua pihak senang, terutama mereka yang punya pengaruh besar di sektor ekonomi."

    b "Tidak, Arya. Kita akan melakukan apa yang benar. Bukan untuk mereka, tapi untuk rakyat."
    b "Aku tidak peduli lagi dengan semua tekanan atau ancaman yang kau berikan. Keputusanku sudah bulat."
    hide AryaYNetral
    show AryaYKetawa at arpos
    a "Hahahaha."
    a "Jangan gegabah, Brama. Kau tahu ini bukan hanya soal idealisme."
    a "Ini soal kelangsungan hubungan kita dengan negara-negara besar."
    hide BramaKNetral
    hide AryaYKetawa
    show AryaYSerius at arpos
    show BramaKKosong at lpos
    b "Kalau itu artinya aku harus kehilangan posisiku, aku terima."
    b "Tapi aku tidak akan mengorbankan prinsipku hanya demi angka atau hubungan pragmatis."
    b "Aku di sini untuk melindungi rakyat, bukan melayani mereka yang sudah punya terlalu banyak kuasa."
    stop music
    a "…"

    # [Lanjutkan dengan alur cerita sesuai kebutuhan]
    # Misalnya, melanjutkan ke pertemuan dengan presiden atau situasi lain yang relevan.
    jump I

# # ------------------------------------- SCRIPT F -------------------------------------# #
# IMAGE TEXT
image slideF1 = im.Scale("text/F/Slide1.PNG", 1920, 1080)
image slideF2 = im.Scale("text/F/Slide2.PNG", 1920, 1080)
image slideF3 = im.Scale("text/F/Slide1.PNG", 1920, 1080)

label F:
    scene slideF1 with fade
    pause
    scene ruang_kerja_bram_pagi with fade
    show BramaKNetral at cpos
    b "Apa yang sebenarnya harus kulakukan?"
    b "Semua fakta ada di depan mata."
    b "Aspirasi rakyat tidak bisa diabaikan, tapi tekanan Arya semakin berat."
    hide BramaKNetral
    show BramaKBingung at cpos
    b "Apa aku benar-benar mampu menghadapi ini seorang diri?"
    b "Mereka menggantungkan harapan padaku…"
    b "Rakyat di Natuna, kepala desa, anak-anak kecil yang masa depannya bergantung pada keputusan ini."
    b "Bagaimana mungkin aku menyerah?"
    b "Arya tidak tahu apa-apa tentang tanggung jawab ini."
    hide BramaKBingung
    show BramaKMarah at cpos
    b "Dia hanya memikirkan angka dan strategi."
    b "Tapi aku tahu, aku di sini bukan untuk melayani kepentingan jalur diplomasi."
    b "Aku ada di sini untuk mempertahankan prinsip dan martabat bangsa."

    "*tok…tok…tok…*"
    hide BramaKMarah
    show AryaYNetral at aycpos
    a "Brama…"
    hide AryaYNetral
    show BramaKNetral at cpos
    b "Eh Arya, masuk."
    hide BramaKNetral
    show AryaYNetral at aycpos
    a "Brama, aku butuh kepastian."
    hide AryaYNetral
    show BramaKMarah at lpos
    show AryaYNetral at ayrpos
    b "Kau benar-benar menolak kesepakatan damai dengan China?"
    b "Kita sudah membahas semuanya."
    b "Aku tidak akan mengubah keputusanku."
    hide BramaKMarah
    show BramaK at lpos
    a "Tidak, ini tentang sesuatu yang lebih besar yang seharusnya kau sudah menyadarinya juga sekarang."
    a "Kau ingat proyek dapur di Changi dulu?"
    a "Kau tahu dari mana uang untuk menyelamatkan ekspansi itu berasal?"

    b "…"
    hide AryaYNetral 
    show AryaYSenyum at ayrpos
    a "Kau benar-benar tidak tahu, ya?"
    hide AryaYSenyum
    show AryaYNetral at ayrpos
    a "PT Angin Topan itu bukan sekadar investor biasa."
    hide AryaYNetral
    show AryaYSerius at ayrpos
    a "Itu adalah topeng untuk mencuci uang seorang koruptor."
    hide BramaK
    show BramaKMarah at lpos
    b "Apa?!"

    a "Bagaimana publik akan melihatnya jika informasi ini bocor?"
    a "Media akan menyebutnya sebagai korupsi terselubung, dan kamu tidak bisa membela diri."

    b "Jadi ini cara kerjamu sekarang, Arya? Menggunakan ancaman untuk memaksakan keinginanmu?"

    a "Aku tidak mengancammu, Brama. Aku memberimu kenyataan."
    a "Kalau kau terus bersikeras dengan idealismemu, ini akan menjadi akhir, bukan hanya untukmu, tapi juga untukku."

    b "Kau pikir aku tidak tahu risikonya? Tapi ini tentang memperjuangkan yang benar, Arya."

    a "Aku mengerti, Brama. Aku tahu kau punya prinsip. Tapi lihatlah gambaran yang lebih besar."
    a "Jika ini terbongkar, apa yang akan terjadi pada Natuna? Pada rakyat yang kau perjuangkan?"
    hide BramaKMarah
    show BramaKKosong at lpos 
    b "…"
    b "Mereka akan kehilangan kepercayaan…"
    hide AryaYSerius
    show AryaYKopi at ayrpos
    a "Tepat. Apa yang terjadi jika kepercayaan itu runtuh?"
    a "Kau akan dilihat bukan sebagai pahlawan, tapi sebagai penipu."
    a "Semua yang kau lakukan untuk Natuna akan sia-sia."
    hide BramaKKosong
    show BramaKMarah at lpos
    b "Kau mencoba memanipulasi aku, Arya."
    hide AryaYKopi
    show AryaYSerius at ayrpos
    a "Tidak, aku mencoba menyelamatkanmu—menyelamatkan kita."
    a "Aku tahu kau ingin memperjuangkan Natuna, dan aku tidak menentangnya."
    a "Tapi caramu sekarang hanya akan menghancurkan segalanya."
    hide BramaKMarah
    show BramaKKosong at lpos 
    b "Jadi, apa yang kau inginkan aku lakukan?"
    hide AryaYSerius
    show AryaYKopi at ayrpos
    a "Lakukan pendekatan diplomatis, setidaknya untuk sementara."
    a "Jangan terburu-buru membuat keputusan yang akan menjadi bumerang."
    a "Biarkan kita menyusun strategi yang tidak hanya mempertahankan prinsipmu, tapi juga menyelamatkan posisi kita."
    hide BramaKKosong
    show BramaKMarah at lpos
    b "Diplomasi tidak akan mengubah apa pun. Mereka hanya memanfaatkan kelemahan kita."
    
    a "Maka buat mereka berpikir kau bukan ancaman. Biarkan mereka lengah."
    hide AryaYKopi
    show AryaYSenyum at ayrpos
    a "Waktu akan memberikan kita ruang untuk bertindak lebih cerdas."
    
    b "Kau pikir ini akan berhasil?"
    hide AryaYSenyum
    show AryaYNetral at ayrpos
    a "Aku tidak tahu, Brama. Tapi ini lebih baik daripada menghancurkan segalanya dengan satu keputusan gegabah."
    hide BramaKMarah
    show BramaK at lpos
    b "…"
    hide BramaK
    show BramaKNetral at lpos
    b "Aku akan mempertimbangkannya, Arya. Tapi ingat, aku tidak akan mengkhianati prinsipku."
    hide BramaKNetral
    show BramaK at lpos
    hide AryaYNetral
    show AryaYKetawa at ayrpos
    a "Itu cukup untuk saat ini, Brama."
    hide AryaYKetawa 
    show AryaYSenyum at ayrpos
    a "Kita bisa melewati ini bersama, asal kau tetap berpikir jernih."
    hide BramaK 
    show BramaKMarah at lpos
    b "Aku berharap kau benar, Arya. Karena aku sudah lelah dengan semua ini."
    hide AryaYSenyum
    show AryaYKopi at ayrpos
    a " Kita akan menemukan jalan, Brama. Kita selalu bisa."

    scene slideF2 with fade
    pause
    scene ruangmakan_y with fade
    show BramaKNetral at lposs
    b "…"
    b "…"
    b "…"
    hide Istri
    show Istri s at rpos
    i "Sayangku, ada apa? Kau kelihatan sangat terbebani."
    show Istri at rpos
    hide Istri s
    b "Arya… Dia memperingatkan tentang risiko besar jika aku tetap bersikeras."
    b "Dia juga mengingatkanku pada kalian, pada anak-anak kita."
    hide Istri
    show Istri s at rpos
    i "Apa yang dia katakan?"
    hide Istri s    
    show Istri at rpos

    b "Dia mengungkit sesuatu dari masa lalu… proyek di Changi, tentang bagaimana aku menyelamatkannya."
    b "Dia bilang ada ancaman besar yang bisa menghancurkan kita semua kalau aku terus maju dengan keputusan ini."
    hide Istri
    show Istri s at rpos
    i "Jadi dia mencoba menakut-nakutimu?"
    hide Istri s
    show Istri at rpos
    
    b "Dia bilang ini bukan ancaman, tapi kenyataan."
    b "Aku mulai merasa… mungkin dia benar."
    b "Kalau aku melawan, kita mungkin kehilangan semuanya."
    hide Istri
    show Istri s at rpos
    i "Sayang, aku tahu kau ingin melindungi kami."
    i "Tapi apakah kau yakin menyerah pada tekanan itu adalah solusi yang benar?"
    hide Istri s
    show Istri at rpos
    
    b "Aku tidak tahu, Sayang. Aku hanya… lelah."
    b "Kadang aku merasa ini bukan soal benar atau salah lagi. Ini soal bertahan."
    hide Istri
    show Istri s at rpos
    i "Sayang, kau selalu berkata bahwa hidup ini tentang prinsip."
    i "Tentang melakukan apa yang benar, bahkan ketika itu sulit."
    i "Apa yang terjadi dengan keyakinan itu?"
    hide Istri s
    show Istri at rpos
    
    b "Keyakinan itu masih ada… tapi melihat kalian, memikirkan apa yang bisa terjadi… aku takut."
    b "Aku takut membuat keputusan yang akan menghancurkan keluarga kita."
    b "Aku takut semua terulang seperti tragedi yang menimpa ayah dulu."
    hide Istri
    show Istri s at rpos
    i "Sayang, aku tahu kau memikirkan kami, tapi jangan jadikan kami alasan untuk mengabaikan nuranimu."
    i "Anak-anak kita akan belajar dari apa yang kamu lakukan."
    i "Apakah kau ingin mereka melihat ayahnya menyerah pada tekanan atau berdiri teguh pada apa yang ia percayai?"
    hide Istri s
    show Istri at rpos
    
    b "Aku tidak ingin mereka melihat ayahnya gagal, Sayang. Aku ingin melindungi mereka."
    hide Istri
    show Istri s at rpos
    i "Melindungi bukan berarti mengorbankan dirimu sendiri."
    i "Kau selalu mengajarkan bahwa kita harus berani menghadapi konsekuensi dari tindakan kita."
    i "Lakukan apa yang menurutmu benar, Sayang. Aku akan selalu di sisimu."
    hide Istri s
    show Istri at rpos
    
    b "Tapi bagaimana kalau aku salah? Bagaimana kalau aku menghancurkan segalanya?"
    hide Istri
    show Istri s at rpos
    i "Setidaknya kau mencoba, Sayang. Setidaknya kau tidak meninggalkan prinsipmu."
    i "Itu jauh lebih berarti daripada menyerah hanya untuk mencari jalan mudah."
    hide Istri s
    show Istri at rpos
    
    b "Kau tidak takut?"
    i "Aku takut, Sayang. Tapi aku lebih takut melihatmu menyesali keputusanmu sendiri di masa depan."
    hide Istri s
    show Istri at rpos
    
    b "Aku akan memikirkannya, Sayang."
    b "Tapi aku tidak tahu apakah aku masih bisa bertahan dengan idealisme ini."
    hide Istri
    show Istri s at rpos
    i "Kau sudah bertahan sejauh ini."
    i "Aku tahu kau kuat. Tidurlah, Sayang."
    i "Kau akan tahu apa yang harus dilakukan."
    hide Istri s
    show Istri at rpos
    
    show BramaKLega at lpos
    b "Terima kasih, Sayang."
    i "Selalu."
    hide Istri s
    show Istri at rpos

    scene slideF3 with fade
    pause
    scene ruang_rapat_menteri with fade
    show BramaK at lpos
    show Diplomat at rpos
    diplomat "Mr. Brama, we only wish to build a better relationship with your country."
    diplomat "We respect your principles, but the world needs cooperation, not conflict. You agree, don’t you?"
    diplomat "If you need anything, I can help you in everything if you agree."
    show BramaKNetral at lpos
    b "Well, I'll consider it first. Thank you."
    diplomat "I’ll wait for the good news, I hope you change your mind and consider it."

    scene ruang_rapat_menteri with fade
    show BramaKBingung at lpos
    b "Ya ampun begitu pusing diriku."
    b "Apakah jika aku mengambil tawaran ini keluarga, karir, dan segalanya akan terselamatkan?"
    show maleGlitch at rpos
    o "Brama, tidak semudah itu."
    o "Ingat, kau harus mempertimbangkan rakyat Natuna di sana yang memerlukan bantuanmu dan tindakan nyatamu."

    b "Tetapi karier, anakku, dan istriku ini menyangkut mereka semua."
    b "Brama, bagaimana jika aku harus dipenjara. Siapa yang akan bertanggung jawab terhadap mereka?"

    o "Brama, mana idealismu, tunjukkan. Kau ini kenapa?!"
    hide BramaKBingung
    show BramaKMarah at lpos
    b "Ya ini demi masa depanku, tidak bisa, aku harus mengambil kesepakatan ini!"
    hide maleGlitch
    show AryaYSenyum at ayrpos
    a "Brama, bagus kau datang. Kita perlu bicara soal langkah selanjutnya."
    a "Ingat, kita harus membuat semua pihak senang, terutama mereka yang punya pengaruh besar di sektor ekonomi."
    show BramaKNetral at lpos
    b "Eh, Arya. Aku sudah mempertimbangkan keputusanku."
    b "Aku rasa kamu benar. Kita harus realistis dalam menghadapi ini."
    hide AryaYSenyum
    show AryaYKetawa at ayrpos
    a "Ah Brama, saudaraku."
    a "Aku senang kamu bisa memutuskan yang terbaik."
    a "Kalau begitu mari kita lanjutkan pembahasan dengan Ibu Presiden."

    # [Lanjutkan dengan alur cerita sesuai kebutuhan]
    jump J

# # ------------------------------------- SCRIPT G -------------------------------------# #
image slideG1 = im.Scale("text/G/Slide1.PNG", 1920, 1080)
label G:
    scene slideG1 with fade
    pause
    scene ruang_kerja_bram_pagi with fade
    show BramaK at cpos
    b "Tujuan yang ingin aku capai memang baik, tapi… apakah caraku sudah benar?"
    hide BramaK
    show maleGlitch at cpos    
    o "Kau tahu jawabannya, Brama. Kalau caramu benar, kenapa hatimu terasa ragu?"
    hide maleGlitch
    show BramaK at cpos
    b "Karena aku tidak melihat pilihan lain. Jalan ini terasa satu-satunya yang masuk akal."
    hide BramaK
    show maleGlitch at cpos    
    o "Benarkah? Atau itu hanya apa yang ingin kau percayai?"
    hide maleGlitch
    show BramaK at cpos
    b "Aku sudah mempertimbangkan semuanya. Bagaimana efek jangka panjangnya, bagaimana reaksi orang-orang…"
    b "Aku tahu ini sulit, tapi bukankah keputusan besar selalu sulit?"
    hide BramaK
    show maleGlitch at cpos
    o "Sulit, ya. Tapi sulit bukan berarti benar."
    o "Apakah kau yakin dengan menyerah pada tekanan, kau benar-benar menyelesaikan masalah?"
    hide maleGlitch
    show BramaK at cpos
    b "…"
    b "Aku… aku hanya ingin menjaga semuanya tetap stabil."
    hide BramaK
    show maleGlitch at cpos
    o "Stabilitas seperti apa yang kau kejar, Brama?"
    o "Stabilitas yang datang dari mengabaikan hati nuranimu?"
    o "Stabilitas yang mengorbankan martabat rakyatmu?"
    hide maleGlitch
    show BramaK at cpos
    b "Tapi bagaimana kalau aku salah?"
    b "Bagaimana kalau keputusanku membawa lebih banyak kehancuran?"
    hide BramaK
    show maleGlitch at cpos 
    o "Kau takut salah, itu wajar. Tapi kau sudah tahu mana yang benar."
    o "Takut tidak akan mengubah kenyataan, Brama."
    hide maleGlitch
    show BramaK at cpos
    b "Jadi menurutmu, aku harus tetap bertahan?"
    hide BramaK
    show maleGlitch at cpos
    o "Kau tahu jawabannya, Brama."
    o "Kau berdiri di sini bukan untuk menyerah."
    o "Kau sudah melihat penderitaan mereka. Kau tahu apa yang harus kau lakukan."
    o "Jika kau menyerah, apa yang kau katakan pada dirimu sendiri nanti?"
    o "Apa yang kau katakan pada rakyat Natuna?"
    o "Bahwa kau menyerah karena takut?"
    hide maleGlitch
    show BramaK at cpos
    b "Aku… aku tidak bisa membiarkan itu terjadi."
    hide BramaK
    show maleGlitch at cpos
    o "Tepat. Kau tidak bisa."
    hide maleGlitch
    show BramaK at cpos
    b "Aku hanya ingin melindungi semuanya… keluarga, rakyat, negara ini…"
    hide BramaK
    show maleGlitch at cpos
    o "Dan kau tahu, melindungi mereka tidak berarti menyerah."
    o "Melindungi mereka berarti berdiri untuk apa yang benar, meskipun itu sulit."
    hide maleGlitch
    show BramaK at cpos
    b "Kau benar. Aku tidak bisa menyerah begitu saja."
    hide BramaK
    show maleGlitch at cpos
    o "Kau tidak pernah bisa menyerah, Brama. Itu bukan dirimu."
    hide maleGlitch
    show BramaK at cpos
    b "Baiklah. Aku tahu apa yang harus kulakukan."
    hide BramaK
    show maleGlitch at cpos
    o "Ingat, Brama. Keberanianmu adalah harapan mereka."
    o "Jangan biarkan itu pudar."
    hide maleGlitch
    show BramaK at cpos
    b "Aku akan tetap pada pendirianku. Apapun yang terjadi."
    hide BramaK
    show maleGlitch at cpos
    o "Dan itulah yang menjadikanmu pemimpin sejati, Brama."
    hide maleGlitch
    show BramaK at cpos
    "{tok…tok…tok…}"
    a "Brama…"
    hide BramaK
    show BramaKSenang at cpos
    b "Oh, masuk Arya."
    hide BramaKSenang
    show BramaK at rpos
    show AryaYNetral at aylpos
    a "Bagaimana update dari masyarakat Natuna sana?"
    b "Yaa seperti biasa, mereka menginginkan keadilan."

    menu:
        "Tolak mentah":
            jump tolak_mentah2
        "Kita tidak boleh menyerah":
            jump tidak_boleh_menyerah2

label tolak_mentah2:
    a "Jadi, apa pilihan finalmu?"
    hide BramaK
    show BramaKNetral at rpos
    b "Aku menolak saranmu, aku akan memperjuangkan keadilan."
    hide AryaYNetral
    show AryaYSerius at aylpos
    a "Kau memilih rakyat Natuna daripada peluang untuk menghentikan konflik ini dengan cara damai?"
    hide BramaKNetral
    show BramaKMarah at rpos
    b "Pilihan itu tidak benar-benar damai, Arya."
    b "Kesepakatan itu sama saja membiarkan kedaulatan kita diinjak-injak."
    hide BramaKMarah
    show BramaKNetral at rpos
    a "Brama, kau sadar apa yang kau lakukan?"
    a "Kau mempertaruhkan stabilitas negara ini."
    a "Jika kita melawan mereka, konsekuensinya akan jauh lebih besar dari yang bisa kau bayangkan."
    hide BramaKNetral
    show BramaKMarah at rpos
    b "Kalau kita terus menyerah, kapan kita akan mulai berdiri di atas kaki sendiri?"
    b "Ini bukan hanya soal stabilitas, Arya."
    b "Ini tentang harga diri bangsa."
    hide BramaKMarah
    show BramaKNetral at rpos
    a "Kau terlalu idealis, Brama."
    a "Dunia ini tidak bekerja seperti itu."
    a "Kita harus memilih pertarungan yang bisa kita menangkan."
    hide BramaKNetral
    show BramaKSenang at rpos
    b "Aku sudah memilih, Arya."
    b "Aku akan berdiri bersama rakyat Natuna."

    jump pindahidealis

label tidak_boleh_menyerah2:
    a "Jadi, apa pilihan finalmu?"
    hide BramaK
    show BramaKNetral at rpos
    b "Aku menolak saranmu, aku akan memperjuangkan keadilan."
    hide AryaYNetral
    show AryaYSerius at aylpos
    a "Jadi, kau memilih jalan ini, meskipun kita tahu konsekuensinya akan sangat berat?"
    hide BramaKNetral
    show BramaK at rpos
    b "Jalan yang mereka tawarkan bukanlah damai, Arya."
    b "Itu penyerahan diri."
    hide AryaYNetral
    show AryaYSerius at aylpos
    a "Penyerahan diri? Kau tahu ini bukan soal kalah atau menang, Brama. Ini soal bertahan."
    hide BramaK
    show BramaKNetral at rpos
    b "Bertahan dengan menyerahkan kedaulatan kita? Itu bukan bertahan, Arya. Itu kehancuran yang tertunda."
    hide BramaKNetral
    show BramaK at rpos
    a "Apa kau sadar apa yang sedang kau lakukan?"
    a "Kau mempertaruhkan masa depan negara ini untuk sesuatu yang mungkin tidak bisa kita menangkan!"
    hide BramaK
    show BramaKNetral at rpos
    b "Kalau kita terus menyerah dan bergantung, kapan kita akan memulai langkah untuk benar-benar berdaulat?"
    b "Harga diri bangsa ini tidak boleh terus dipertaruhkan hanya karena ketakutan."
    hide BramaKNetral
    show BramaK at rpos
    a "Kau terlalu keras kepala. Dunia tidak bekerja seperti idealismemu, Brama. Kita harus pragmatis."
    hide BramaK
    show BramaKNetral at rpos
    b "Mungkin aku memang keras kepala, Arya."
    b "Tapi aku tidak akan berpaling dari rakyat Natuna."
    b "Aku tahu ini tidak mudah, tapi mereka pantas untuk diperjuangkan."

    jump pindahidealis

# # ------------------------------------- SCRIPT H -------------------------------------# #
label H:
    play music office_bgm
    scene ruang_kerja_bram_pagi
    show maleGlitch at cpos 
    o "Tujuan yang ingin kamu capai mungkin memang baik, tapi apakah caranya sudah betul, Brama?"
    o "Jikalau cara yang kau gunakan salah, maka akan banyak mendapat penolakan."
    hide maleGlitch
    show BramaKNetral at cpos
    b "Apakah ada cara lain selain cara ini? Ku rasa tidak ada."
    b "Apakah mereka juga memikirkan efek jangka panjangnya jika aku melakukan tindakan yang sebaliknya?"
    b "Ku rasa mereka tidak memikirkan sampai hal itu."
    b "Mereka kalau jadi aku dengan posisi ini pasti akan memiliki pemikiran yang sama."
    hide BramaKNetral
    show maleGlitch at cpos
    o "Terserah kamu lah."
    hide maleGlitch
    "(tok…tok…tok…)"
    show BramaKBingung at cpos
    a "Brama…"
    hide BramaKBingung
    show BramaKLega at cpos
    b "Oh, masuk Arya."
    show AryaYNetral at ayrpos

    a "Bagaimana update dari masyarakat Natuna sana?"
    b "Yaa seperti biasa, mereka menginginkan keadilan."
    b "Jadi, apa yang kau inginkan aku lakukan?"

    a "Lakukan pendekatan diplomatis, setidaknya untuk sementara."
    a "Jangan terburu-buru membuat keputusan yang akan menjadi bumerang."
    a "Biarkan kita menyusun strategi yang tidak hanya mempertahankan prinsipmu, tapi juga menyelamatkan posisi kita."

    b "Diplomasi tidak akan mengubah apa pun. Mereka hanya memanfaatkan kelemahan kita."

    a "Maka buat mereka berpikir kau bukan ancaman. Biarkan mereka lengah."
    a "Waktu akan memberikan kita ruang untuk bertindak lebih cerdas."
    hide BramaKLega
    show BramaKNetral at cpos
    b "Kau pikir ini akan berhasil?"

    a "Aku tidak tahu, Brama. Tapi ini lebih baik daripada menghancurkan segalanya dengan satu keputusan gegabah."

    b "…"
    b "Aku akan mempertimbangkannya, Arya. Tapi ingat, aku tidak akan mengkhianati prinsipku."

    a "Itu cukup untuk saat ini, Brama."
    a "Kita bisa melewati ini bersama, asal kau tetap berpikir jernih."
    a "Kita akan menemukan jalan, Brama. Kita selalu bisa."

    b "Aku rasa kamu benar. Kita harus realistis dalam menghadapi ini."
    hide AryaYNetral
    show AryaYSenyum at ayrpos
    a "Ah Brama, saudaraku."
    a "Aku senang kamu bisa memutuskan yang terbaik."
    a "Kalau begitu mari kita lanjutkan pembahasan dengan Ibu Presiden."

    # [Lanjutkan dengan alur cerita sesuai kebutuhan]
    jump J

# # ------------------------------------- SCRIPT I -------------------------------------# #
# # DEFINE CHARACTERS
define pres = Character("Presiden", color="#ff7c7c")
define kades = Character("Kepala Desa", color="#95ff7d")
define warta = Character("Wartawan", color="#837d77")

# # IMAGE BACKGROUND
image bumnkantor = im.Scale("bg/bumn/kantor.png", 1920, 1080)
image bumnlobi = im.Scale("bg/bumn/lobi.png", 1920, 1080)
image bumnlorong = im.Scale("bg/bumn/lorong.png", 1920, 1080)
image bumnrapat = im.Scale("bg/bumn/rapat.png", 1920, 1080)
image natuna = im.Scale("bg/Natuna.png", 1920, 1080)
image slide_1 = im.Scale("text/I/slide1.png", 1920, 1080)
image slide_2 = im.Scale("text/I/slide2.png", 1920, 1080)
image slide_3 = im.Scale("text/I/slide3.png", 1920, 1080)
image slide_4 = im.Scale("text/I/slide4.png", 1920, 1080)

# # IMAGE CHARA
image Brama_y:
    "chara/bramabumn.png"
    zoom 0.5

image Presiden:
    "chara/presiden.png"
    zoom 0.5

image Pistol Nembak:
    "cutscene/x/pistolnembak.png"
    zoom 1.5
image dentuman = im.Scale("cutscene/x/bg.png", 1920, 1080)

# buat pres
define prcpos = Position(xalign=0.5, yalign=0)
define prrpos = Position(xalign=1.0, yalign=0)
define prlpos = Position(xalign=0,yalign=0)

define pistol = Position(xalign=0.5, yalign=0.4)

label I:
    scene bumnkantor with fade
    show Brama_y at lpos
    show Presiden at prrpos
    play music office_bgm
    b "Yang Mulia Presiden, menteri-menteri terhormat, saya mengajukan kebijakan untuk memprioritaskan kesejahteraan rakyat" 
    b "khususnya di wilayah-wilayah perbatasan seperti Natuna. Sudah terlalu lama mereka menjadi korban dari konflik kepentingan."
    b "Kita harus mengambil tindakan tegas terhadap kapal asing di Natuna."
    pres "Ini langkah yang berani, Menteri Brama. Apakah kau sudah mempertimbangkan seluruh aspeknya?"
    b "Saya sudah mempertimbangkannya, dan ini sangat berdampak baik dan menguntungkan masyarakat Indonesia, Bu. Semuanya akan berjalan lancar."

    #scene natuna with fade
    kades "Terima kasih, Pak Brama. Apa yang Bapak lakukan telah mengubah hidup kami. Kini kami punya sekolah baru dan fasilitas kesehatan yang layak."
    b "…… Ini semua untuk kalian. Negara harus hadir di sini, di mana rakyatnya membutuhkan."
    pres "Baik, apabila meninjau dari dokumen yang sudah kau berikan dan jelaskan, saya setuju dengan keputusanmu. Mari kita laksanakan!"
    play sound trans1
    stop music
    scene black
    show slide_1 with fade
    pause 1
    scene bumnrapat with fade
    show abatik at aycpos
    a "Saya, atas nama integritas dan keadilan, harus mengungkap sebuah fakta."
    a "Menteri Brama telah terlibat dalam penyalahgunaan anggaran beberapa tahun lalu untuk menutupi pembengkakan proyeknya."
    a "Ini adalah pelanggaran hukum yang tidak bisa ditoleransi."

    scene terasrumah_y with fade
    play music crowd
    "(Dengan diketahuinya kasus penyalahgunaan anggaran, Brama ditangkap oleh pihak kepolisian di kediamannya.)"
    "(Beberapa wartawan berkumpul dengan Brama telah diborgol tangannya.)"
    show male at cpos
    warta "Pak Brama, apa benar tuduhan ini? Bagaimana tanggapan Anda?"
    hide male
    show Brama_y at cpos
    b "Saya hanya ingin membantu rakyat. Jika ini harga yang harus saya bayar, saya terima."
    b "Untuk rakyatku, maafkan aku jika langkahku tidak sempurna. Tapi aku tidak pernah menyesal memperjuangkan kalian."
    stop music
    scene black 
    play music "audio/semoga tense.wav"
    show slide_2 with fade
    pause 3
    show slide_3 with fade
    pause 2
    scene dentuman with fade
    show Pistol Nembak at pistol
    pause 1
    show slide_4 with fade
    pause 1.5
    scene black
    play sound dentumanpistol
    stop music
    "DORR!"
    show Arya Serius Glitch at aycpos
    a "Mimpi buruk lagi lu?"

    return
#---------------------------------

# # ------------------------------------- SCRIPT J -------------------------------------# #
# # DEFINE CHARACTERS
define pgw = Character("Pegawai", color="#ffffff")


# # IMAGE CHARA
image kadestv = im.Scale("cutscene/j/kades di tv.png", 1920, 1080)
image endj1 = im.Scale("cutscene/j/ending J.png", 1920, 1080)
image endj2 = im.Scale("cutscene/j/ending j 2.png", 1920, 1080)
image endj3 = im.Scale("cutscene/j/ending j 3.png", 1920, 1080)
image endj4 = im.Scale("cutscene/j/ending j 4.png", 1920, 1080)

image Presiden:
    "chara/presiden.png"
    zoom 0.8

label J:
    "(Beberapa jam setelahnya, diadakan rapat untuk membahas keputusan final geostrategi Indonesia.)"
    scene bumnkantor with fade
    show Brama_y at cpos
    k "Sekretaris, tolong sampaikan kepada seluruh divisi untuk rapat pada sore hari ini. Ada hal penting yang harus diselesaikan sebelum rapat dengan presiden."
    skre "Baik, Pak Brama. Akan segera saya informasikan kepada seluruh divisi untuk menghadiri rapat."

    scene bumnrapat with fade
    show Presiden at prcpos
    pres "Selamat siang, Bapak Ibu sekalian. Saat ini adalah momen krusial kita."
    pres "Melalui rapat ini, kita akan memutuskan aksi kita terhadap China."
    pres "Silakan, Bapak Brama, selaku Menteri Luar Negeri, untuk menyampaikan pendapatnya."
    hide Presiden

    show Brama_y at lpos
    show Presiden at prrpos
    k "Selamat siang, Ibu Presiden yang terhormat, dan yang saya hormati, Bapak Ibu Menteri sekalian."
    k "Di sini izinkan saya untuk menyampaikan solusi yang tepat untuk mengatasi permasalahan Laut Natuna."
    k "Laut Natuna adalah masalah regional yang berlarut-larut dan merugikan negara ini."
    k "Menimbang seluruh pro dan kontra yang ada, maka kebijakan diplomasi menurut saya adalah langkah yang paling ideal."
    k "Oleh karena itu, saya mengajukan untuk kita melalui jalur diplomasi yang lebih kuat agar tidak terjadi ketegangan nasional."
    k "Dengan dilakukannya diplomasi, kita dapat menerima keuntungan dan stabilitas yang lebih baik."
    hide Presiden

    show Arya_y at ayrpos
    r "Setuju dengan apa yang dikatakan oleh Pak Brama."
    hide Arya_y

    show Presiden at prrpos
    pres "Ini langkah yang menguntungkan bagi kita, Pak Brama."
    pres "Apakah Anda sudah mempertimbangkan seluruh aspek dari kebijakan tersebut?"
    k "Sudah, Ibu Presiden. Kami telah mengkaji secara mendalam."
    k "Dengan dilakukannya diplomasi, kita dapat menerima keuntungan lebih untuk membantu meningkatkan perekonomian."
    k "Jika memilih konfrontasi, maka kita akan berada di situasi perang dan akan mengganggu kestabilan negara ini."
    k "Dengan diplomasi, kita dapat meningkatkan kesejahteraan rakyat juga secara tidak langsung."
    pres "Baik, apabila meninjau dari dokumen yang sudah Bapak berikan dan jelaskan, saya setuju dengan keputusan Bapak."
    pres "Mari kita laksanakan!"

    stop music
    "(Satu hari berikutnya..)"
    play music "audio/semoga tense.wav"
    scene  kadestv with fade
    pause 2.0
    
 

    kades "Saya rasa pemerintah tidak peduli terhadap kami, rakyatnya! "
    kades "Para pejabat itu hanya peduli soal kantongnya masing-masing, tidak peduli terhadap kami rakyat kecil di Natuna!"
    kades "Sungguh dzolim, terutama untuk Anda, Pak Menteri Luar Negeri, dan para pejabat negeri ini!"

    scene endj1 with fade
    pause 2.0
    scene endj2 with fade
    pause 2.0
    scene endj3 with fade
    pause 2.0
    scene endj4 with fade
    pause 2.0

    scene black
    
    #scene demo, belum ada
    show Pistol Nembak at pistol with fade
    "(Hukuman mati.)"
    scene black
    play sound dentumanpistol
    stop music
    "DORR!"
    show Arya Serius Glitch at aycpos
    a "Mimpi buruk lagi lu?"

    return



















# GLITCH EFFECT_________________________________________________________________
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
