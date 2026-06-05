import streamlit as st
import os

# 1. Sayfa Ayarları (Ferah ve geniş görünüm için layout="wide" yapıldı)
st.set_page_config(
    page_title="Türk Havacılık Tarihi Dijital Kitaplığı",
    page_icon="✈️",
    layout="wide"
)

# 2. Tam ve Eksiksiz Veri Tabanı (Sözlük Yapısı - 50 Kronolojik Sayfa + Ana Sayfa)
havacilik_tarihi_db = {
    "🏠 Ana Sayfa - Karşılama Ekranı": {
        "metin": (
            "Türk Havacılık Tarihi Dijital Kitaplığı'na Hoş Geldiniz! Bu web sitesi, Türk milletinin gökyüzündeki "
            "ve uzaydaki bağımsızlık mücadelesini, tarihi belgeler ve teknik analizler ışığında kronolojik olarak "
            "sunmak amacıyla tasarlanmış dijital bir kültür ve teknoloji arşividir. Sol tarafta yer alan menüyü "
            "kullanarak, 1000'li yıllarda İmam Cevheri'nin Nişabur semalarında gerçekleştirdiği ilk aralıksız uçuş ve "
            "fedakarlık girişiminden başlayıp, 21. Yüzyılda Türk Havacılık ve Uzay Sanayisinin (TUSAŞ) Küresel Jeopolitik "
            "Konumu ve 2026 Vizyonu'na kadar uzanan tam 50 sayfalık muazzam bir tarihi yolculuğa çıkabilirsiniz. "
            "Her sayfada dönemin mühendislik zorluklarını, vizyoner liderlerin stratejik adımlarını ve yerli teknoloji "
            "hamlelerimizin gelişim süreçlerini en az 7-8 satırlık detaylı ve derinlemesine metinlerle inceleyebilirsiniz. "
            "Göklerine sahip çıkamayan milletlerin yarınlarından emin olamayacağı bilinciyle hazırlanan bu projede, "
            "keyifli ve ilham dolu okumalar dileriz."
        ),
        "resim": "images/ana_sayfa_karsilama.jpg"
    },
    "01. 1002: İmam Cevheri'nin İlk Uçuş Denemesi": {
        "metin": (
            "Türk-İslam bilim dünyasının en önemli öncülerinden biri olan İmam Cevheri, 1002 yılında Nişabur'da "
            "havacılık tarihinin en cesur adımlarından birini atmıştır. Kendi geliştirdiği ahşap kanat düzeneklerini "
            "kollarına bağlayarak bir cami minaresinden kendini boşluğa bırakan Cevheri, aerodinamik kuvvetlerin "
            "insan bedenini taşımadaki etkisini uygulamalı olarak test etmiştir. Belirli bir mesafe havada süzülmeyi "
            "başarmış olsa da dönemin malzeme yetersizliği, kaldırma kuvveti (lift) hesaplarındaki eksiklikler ve "
            "dengeleme (stabilite) mekanizmasının bulunmaması nedeniyle sert bir iniş yapmış ve şehit olmuştur. "
            "Onun bu fedakar girişimi, Türk dünyasının gökyüzüne olan tutkunun ilk somut adımı ve havacılık mekaniği "
            "üzerine yapılmış ilk deneysel çalışmalardan biri olarak kabul edilir."
        ),
        "resim": "images/01_imam_cevheri.jpg"
    },
    "02. 1150: Siraceddin El-Cevheri ve Havacılık Çalışmaları": {
        "metin": (
            "12. yüzyılın ortalarında İslam dünyasında aerodinamik ve mekanik üzerine teorik çalışmalar yürüten "
            "Siraceddin El-Cevheri, uçuş fiziğinin temellerini inceleyen önemli bir bilim insanıdır. İmam Cevheri'nin "
            "deneysel çalışmalarını teorik bir çerçeveye oturtmaya çalışan Siraceddin, kuşların kanat yapısı ve hava "
            "akımlarının katı cisimler üzerindeki kaldırma etkisini formüle etmeye çalışmıştır. Dönemin kısıtlı bilimsel "
            "imkanlarına rağmen, geometrik hesaplamalarla kanat alanının vücut ağırlığına oranını analiz eden yazılar "
            "kaleme almıştır. Onun bu çalışmaları, doğu bilim dünyasında planör benzeri düzeneklerin matematiksel "
            "altyapısının oluşmasına büyük katkı sağlamış ve havacılığın sadece bir cesaret işi değil, aynı zamanda "
            "bir mühendislik disiplini olduğunu gösteren ilk erken dönem kanıtlardan biri olmuştur."
        ),
        "resim": "images/02_siraceddin_cevheri.jpg"
    },
    "03. 1632: Hezarfen Ahmed Çelebi ve Galata Uçuşu": {
        "metin": (
            "17. Yüzyıl Osmanlı dünyasında yaşayan üstün zeka Hezarfen Ahmed Çelebi, kuşların uçuş anatomisini, "
            "kanat çırpış mekanizmalarını ve rüzgar akımlarını yıllarca inceleyerek kendi yapay kanatlarını tasarlamıştır. "
            "1632 yılında, lodos rüzgarının en elverişli olduğu anda Galata Kulesi'nden kendini boşluğa bırakmış, "
            "İstanbul Boğazı'nı yerçekimine meydan okuyarak aşmayı başarmıştır. Süzülme mekaniği ve aerodinamik "
            "süzülme oranlarını (glide ratio) doğru hesaplayarak yaklaşık 3.358 metrelik bu uçuşun ardından Üsküdar "
            "Doğancılar Meydanı'na güvenli bir iniş gerçekleştirmiştir. Evliya Çelebi'nin seyahatnamesinde geniş yer "
            "bulan bu olay, dünya havacılık tarihinde planörle yapılan ilk başarılı kıtalararası uçuş denemelerinden biri "
            "olarak bilim ve teknoloji tarihine altın harflerle kazınmıştır."
        ),
        "resim": "images/03_hezarfen_celebi.jpg"
    },
    "04. 1633: Lagari Hasan Çelebi'nin Roket Uçuşu": {
        "metin": (
            "Hezarfen'in uçuşundan sadece bir yıl sonra, bu kez kardeşi Lagari Hasan Çelebi dünya havacılık ve uzay "
            "tarihine geçecek benzersiz bir çılgınlığa imza atmıştır. Yaklaşık 50 okka barut içeren, yedi kollu ve "
            "tamamen kendi tasarımı olan konik gövdeli bir rokete binerek dikey fırlatılış gerçekleştirmiştir. "
            "IV. Murad'ın huzurunda yapılan bu denemede, barutun sağladığı yüksek itki (thrust) kuvvetiyle yaklaşık "
            "300 metre yüksekliğe kadar dikey olarak tırmanmayı başarmıştır. Barutun tükenme noktasına geldiği tepe "
            "noktasında (apoje) ise hazırladığı kartal kanadı şeklindeki ilkel paraşüt/süzülme sistemini açarak "
            "Sarayburnu açıklarında denize yumuşak bir iniş yapmıştır. Lagari, insanlı roket uçuşunun ve kademeli "
            "itki mantığının dünyadaki ilk öncüsü olarak kabul edilmektedir."
        ),
        "resim": "images/04_lagari_hasan.jpg"
    },
    "05. 1783: Osmanlı'da İlk Balon Uçuşu Denemeleri": {
        "metin": (
            "Avrupa'da Montgolfier Kardeşlerin sıcak hava balonuyla uçuş gerçekleştirmesinden kısa bir süre sonra, "
            "bu teknolojik gelişme Osmanlı İmparatorluğu'nda da büyük bir yankı uyandırmıştır. 1783 yılının sonlarında "
            "İstanbul'da yabancı seyyahlar ve Osmanlı zanaatkarlarının ortak girişimiyle ilk sıcak hava balonu denemeleri "
            "gerçekleştirilmiştir. Saray çevresinde ve halkın yoğun katılımı eşliğinde yapılan bu fırlatmalarda, gazların "
            "genleşme prensibi ve kaldırma kuvveti uygulamalı olarak sergilenmiştir. Havadan hafif araçların askeri "
            "gözlem ve istihbarat alanında kullanılabileceğine dair ilk fikirler bu dönemde devlet ricali arasında "
            "tartışılmaya başlanmıştır. This denemeler, Osmanlı bilim dünyasının batıdaki havacılık devrimini eş zamanlı "
            "olarak takip ettiğini ve teknolojik yeniliklere açık olduğunu gösteren önemli bir kronolojik adımdır."
        ),
        "resim": "images/05_osmanli_balon.jpg"
    },
    "06. 1909: Osmanlı Havacılık Komisyonu'nun Kurulması": {
        "metin": (
            "20. yüzyılın başında Wright Kardeşlerin uçuşuyla havacılığın askeri bir stratejiye dönüşmesi, Osmanlı "
            "İmparatorluğu'nu harekete geçirmiştir. 1909 yılında Harbiye Nezareti bünyesinde askeri havacılığın "
            "temellerini atmak amacıyla resmi bir Havacılık Komisyonu kurulmuştur. Bu komisyonun temel görevi, "
            "Avrupa'daki havacılık okullarını incelemek, orduya uçak satın almak ve pilot yetiştirilmesini organize "
            "etmekti. Dönemin Harbiye Nazırı Mahmut Şevket Paşa'nın vizyoner liderliğinde yürütülen bu süreç, "
            "Türk askeri havacılığının kurumsal kimlik kazandığı ilk resmi adımdır. Komisyon, ordunun modernizasyonu "
            "için gökyüzünün mutlak bir zorunluluk olduğunu raporlamış ve gelecekte kurulacak olan Türk Hava "
            "Kuvvetleri'nin ilk yasal ve idari altyapısını oluşturmuştur."
        ),
        "resim": "images/06_havacilik_komisyonu.jpg"
    },
    "07. 1912: Yeşilköy Tayyare Mektebi'nin Açılışı": {
        "metin": (
            "Osmanlı İmparatorluğu, havacılığın askeri operasyonlardaki stratejik önemini hızla kavrayarak 1912 yılında "
            "Yeşilköy Tayyare Mektebi'ni kurmuştur. Mahmut Şevket Paşa'nın vizyoner girişimleriyle açılan bu okul, "
            "Türk askeri havacılığının pilot, rasıt ve teknisyen yetiştiren ilk resmi ve kurumsal altyapısı olmuştur. "
            "Dönemin kısıtlı imkanlarına ve Balkan Savaşları'nın getirdiği büyük lojistik zorluklara rağmen, Fransa ve "
            "Almanya'dan getirilen uçaklar üzerinde teorik ve pratik uçuş mekaniği eğitimleri verilmiştir. Yeşilköy "
            "Tayyare Mektebi, sadece Osmanlı'nın son dönemindeki hava harekatlarına pilot yetiştirmekle kalmamış, "
            "aynı zamanda Cumhuriyet dönemi Türk Hava Kuvvetleri'nin ve yerli havacılık sanayisinin kurulmasında rol "
            "oynayacak yetişmiş insan kaynağının ana yuvası olmuştur."
        ),
        "resim": "images/07_yesilkoy_tayyare_mektebi.jpg"
    },
    "08. 1914: İstanbul-Kahire Seferi ve Hava Şehitleri": {
        "metin": (
            "1914 yılında Osmanlı Devleti, hem havacılığın ulaştığı seviyeyi göstermek hem de imparatorluk topraklarındaki "
            "bağları güçlendirmek amacıyla İstanbul'dan Kahire'ye uzanan tarihi bir hava seferi düzenlemiştir. Fethi Bey, "
            "Sadık Bey, Nuri Bey ve İsmail Hakkı Bey gibi dönemin en seçkin pilotlarının katıldığı bu sefer, binlerce "
            "kilometrelik zorlu bir rotayı kapsamaktaydı. Ancak o dönem uçaklarındaki teknik yetersizlikler ve şiddetli "
            "hava muhalefeti nedeniyle uçaklar Taberiye Gölü yakınlarında ve Toros dağlarında kaza kırıma uğramıştır. "
            "Bu kazalarda Fethi, Sadık ve Nuri Beyler şehit düşerek Türk havacılık tarihinin ilk hava şehitleri olarak "
            "tarihe geçmişlerdir. Bu trajik ama kahramanca sefer, Türk havacılarının uzak mesafeli stratejik uçuş yeteneğini "
            "gösterme yolundaki ilk büyük fedakarlığıdır."
        ),
        "resim": "images/08_istanbul_kahire_seferi.jpg"
    },
    "09. 1915: Birinci Dünya Savaşı ve Çanakkale Hava Savaşları": {
        "metin": (
            "Birinci Dünya Savaşı'nın patlak vermesiyle birlikte, Osmanlı Hava Bölükleri Çanakkale Cephesi'nde hayati "
            "bir rol üstlenmiştir. İngiliz ve Fransız donanmalarının hareketliliğini havadan izleyen Türk pilotları, "
            "müttefik gemilerinin konumlarını ve kara çıkartması planlarını anlık olarak ordu komutanlığına bildirmişlerdir. "
            "Kısıtlı sayıdaki Albatros ve Fokker tipi uçaklarla düşmanın modern hava filosuna karşı kahramanca bir mücadele "
            "verilmiştir. Çanakkale semalarında gerçekleşen hava çarpışmalarında Türk havacıları ilk hava zaferlerini kazanmış, "
            "düşman uçaklarını düşürmeyi başarmışlardır. Bu savaşlar, havadan keşif ve gözetlemenin kara savaşlarının "
            "kaderini nasıl doğrudan değiştirebileceğini kanıtlayan, askeri havacılık taktiklerimizin olgunlaştığı en çetin "
            "dönemlerden biridir."
        ),
        "resim": "images/09_canakkale_hava_savaslari.jpg"
    },
    "10. 1917: Kafkas Cephesi ve Yeşilköy Tayyare Fabrikası": {
        "metin": (
            "1917 yılına gelindiğinde Birinci Dünya Savaşı'nın geniş cephelerinde uçak ihtiyacı had safhaya ulaşmıştır. "
            "Özellikle Kafkas Cephesi'nde Rus ordusuna karşı yürütülen operasyonlarda hava desteği sağlamak amacıyla büyük "
            "lojistik hatlar kurulmuştur. İstanbul'daki Yeşilköy Tayyare Mektebi bünyesinde kurulan tamir atölyeleri "
            "genişletilerek bir nevi Tayyare Fabrikası işlevi görmeye başlamıştır. Burada cepheden dönen hasarlı uçakların "
            "motor revizyonları yapılmış, kanat bezleri yenilenmiş ve yerli imkanlarla yedek parça üretimi denenmiştir. "
            "Zorlu kış şartlarında Kafkasya semalarında uçan Türk pilotları, bu atölyelerden gelen teknik destek sayesinde "
            "uçuşlarını sürdürebilmişlerdir. Bu süreç, Türk havacılığında bakım-onarım ve lojistik mühendisliğinin ilk "
            "kurumsal deneyimlerini oluşturmuştur."
        ),
        "resim": "images/10_kafkas_cephesi_tamir.jpg"
    },
    "11. 1918: Osmanlı Hava Kuvvetleri Müfettişliği": {
        "metin": (
            "Birinci Dünya Savaşı'nın son yılı olan 1918'de, havacılık faaliyetlerinin tek bir elden ve daha profesyonel "
            "yönetilmesi amacıyla Umur-u Havacılık Müfettişliği (Osmanlı Hava Kuvvetleri Müfettişliği) kurulmuştur. "
            "Bu idari yapılanma, havacılığın ordunun yardımcı bir unsuru olmaktan çıkıp bağımsız bir kuvvet komutanlığına "
            "dönüşmesinin ilk sinyallerini taşımaktaydı. Savaşın getirdiği büyük yıkıma ve malzeme sıkıntısına rağmen, "
            "müfettişlik tüm cephelerdeki hava bölüklerini koordine etmeye çalışmıştır. Mondros Mütarekesi'nin imzalanmasıyla "
            "birlikte işgal güçleri bu yapıya el koymaya çalışsa da, müfettişlik bünyesindeki vatansever subaylar gizli "
            "planlar yaparak uçakları ve teknik malzemeleri Anadolu'ya kaçırmanın hazırlıklarını başlatmışlerdir."
        ),
        "resim": "images/11_havacilik_mufettisligi.jpg"
    },
    "12. 1919: Kurtuluş Savaşı'nda İlk Hava Faaliyetleri": {
        "metin": (
            "1919 yılında Anadolu'nun işgal edilmeye başlanmasıyla birlikte, Türk havacıları Mustafa Kemal Atatürk'ün "
            "başlattığı Milli Mücadele'ye katılmak üzere gizlice Anadolu'ya geçmeye başlamışlardır. İşgal altındaki "
            "İstanbul'dan kaçırılan uçak parçaları, motorlar ve teknik aletler binbir zorlukla İnebolu üzerinden iç "
            "kısımlara taşınmıştır. Anadolu'da neredeyse hiç uçak bulunmazken, havacı subaylar Konya ve Eskişehir'deki eski "
            "hangarlarda terk edilmiş, parçalanmış uçakları bir araya getirerek ilk direniş hava birimlerini kurmuşlardır. "
            "Bu erken dönem faaliyetleri, imkansızlıklar içinde bir halkın gökyüzünde nasıl yeniden doğabileceğinin, "
            "inanç ve azimle örülmüş ilk teknik direniş hamlelerinin başlangıcıdır."
        ),
        "resim": "images/12_kurtulus_savasi_ilk_hava.jpg"
    },
    "13. 1920: Kuva-yi Milliye Dönemi Erzurum ve Akşehir Tayyare Bölükleri": {
        "metin": (
            "1920 yılında Ankara'da TBMM'nin açılmasıyla birlikte havacılık faaliyetleri resmi bir boyut kazanmış ve "
            "Harbiye Nezareti yerine kurulan Milli Müdafaa Vekaleti bünyesinde Hava Kuva-yi Müdiriyeti oluşturulmuştur. "
            "Erzurum ve Akşehir gibi stratejik merkezlerde ilk Tayyare Bölükleri kurulmuştur. Ellerinde sadece birkaç adet "
            "uçabilir durumda olan eski keşif uçağı bulunan bu bölükler, düşman hareketliliğini izlemek ve Anadolu "
            "halkına moral aşılamak amacıyla uçuşlar yapmışlardır. Teknik personel, uçakların kanatlarını evlerde dokunan "
            "bezlerle kaplamış, motor yağları yerine patates ve bezir yağı karışımları kullanarak uçakları havada tutmayı "
            "başarmışlardır. Kuva-yi Milliye havacılığı, tamamen bir halkın özverisiyle ayakta kalan bir mühendislik direnişidir."
        ),
        "resim": "images/13_kuvayimilliye_tayyare.jpg"
    },
    "14. 1921: İnönü Savaşları ve Keşif Uçuşlarının Rolü": {
        "metin": (
            "1921 yılındaki Birinci ve İkinci İnönü Savaşları, düzenli Türk ordusunun Yunan ilerleyişine karşı verdiği "
            "ilk büyük sınavlardır. Bu savaşlarda Türk pilotları, altlarındaki tek tük uçakla sürekli olarak düşman "
            "hatlarının gerisine sızarak keşif uçuşları gerçekleştirmişlerdir. Yunan ordusunun taarruz yönlerini, lojistik "
            "yığınak noktalarını ve asker sayısını tam isabetle belirleyen havacılarımız, bu hayati istihbarat bilgilerini "
            "Batı Cephesi Komutanlığı'na ileterek savaş taktiklerinin başarıyla uygulanmasını sağlamışlardır. Düşmanın sayıca "
            "çok üstün hava filosuna karşı gökyüzünde adeta köşe kapmaca oynayan Türk havacılığı, İnönü zaferlerinin "
            "kazanılmasında görünmeyen ama çok kritik bir kaldıraç görevi üstlenmiştir."
        ),
        "resim": "images/14_inonu_savaslari_hava.jpg"
    },
    "15. 1922: Sakarya Meydan Muharebesi Hava Harekatı": {
        "metin": (
            "Türk milletinin dönüm noktası olan 1922 Sakarya Meydan Muharebesi'nde, cephe hattının genişliği ve savaşın "
            "şiddeti hava unsurlarının önemini en üst düzeye çıkarmıştır. Türk havacıları, uçağın düşmesi durumunda "
            "yerine yenisini koyamayacaklarını bildikleri halde günde bazen 3-4 sorti yaparak düşman mevzilerini bombalamış "
            "ve keşif yapmışlardır. Savaş boyunca havada sağlanan istihbarat üstünlüğü, Mustafa Kemal Paşa'nın 'Hatt-ı "
            "müdafaa yoktur, sath-ı müdafaa vardır' stratejisinin sahada kusursuz uygulanmasına destek vermiştir. "
            "Uçakların mekanik bakımları gece yarıları gaz lambası ışığında, siperlerin hemen arkasında yapılmıştır. "
            "Sakarya semalarındaki bu destansı mücadele, havacılarımızın teknik dehası ve vatan sevgisiyle kazanılmıştır.Cephenin Kaderini Değiştiren Keşif: 22 gün 22 gece süren bu amansız savaşta, Türk pilotları her gün düzenli olarak havalandı. Yunan ordusunun Ankara'ya doğru ilerlerken yaptığı kuşatma manevraları, özellikle Haymana ve Polatlı yönündeki büyük güç kaydırmaları bu iki uçakla havadan tespit edildi."
        ),
        "resim": "images/15_sakarya_hava_harekati.jpg"
    },
    "16. 1922: Büyük Taarruz'da Türk Havacılarının Rolü": {
        "metin": (
            "26 Ağustos 1922'de başlayan Büyük Taarruz'da Türk havacılığı, tarihinin en organize hava harekatını "
            "gerçekleştirmiştir. Savaşın ilk saatlerinden itibaren Yunan hava birimlerinin keşif yapması tamamen "
            "engellenmiş, böylece Türk ordusunun gizli intikal ve taarruz planları gizli kalmıştır. Türk pilotları, "
            "düşman hatlarının üzerine pike yaparak makineli tüfeklerle saldırmış ve geri çekilen Yunan kollarını havadan "
            "baskı altında almışlerdir. Bu harekatta havacılarımız sadece keşif değil, aktif birer yakın hava destek "
            "unsuru olarak ordunun ilerleyişini hızlandırmışlardır. Büyük Taarruz, Türk Hava Kuvvetleri'nin askeri "
            "doktrin açısından olgunlaştığını ve tam bir zafer unsuru haline geldiğini kanıtlamıştır."
        ),
        "resim": "images/16_buyuk_taarruz_hava.jpg"
    },
    "17. 1922: Vecihi Hürkuş'un İlk Hava Zaferleri": {
        "metin": (
            "Milli Mücadele'nin efsanevi pilotu Vecihi Hürkuş, savaş boyunca gökyüzünde gösterdiği olağanüstü başarılarla "
            "düşman pilotlarının korkulu rüyası haline gelmiştir. Rus ve Yunan uçaklarına karşı giriştiği hava it dalaşlarında "
            "(dogfight) üstün uçuş tekniği ve cesareti sayesinde ilk yerli hava zaferlerini kazanmıştır. Bir uçuşunda düşman "
            "uçağını vurarak indirmeyi başarmış ve bu başarısıyla Kurtuluş Savaşı'nda düşman uçağı düşüren ilk Türk pilot "
            "unvanını almıştır. Sadece iyi bir pilot olmakla kalmayan Vecihi Bey, vurduğu uçakların mekanik aksamlarını "
            "inceleyerek uçuş mekaniği konusundaki bilgilerini derinleştirmiş ve gelecekte yapacağı yerli uçak tasarımlarının "
            "fikri temellerini bu savaş meydanlarında atmıştır."
        ),
        "resim": "images/17_vecihi_ilk_zaferler.jpg"
    },
    "18. 1922: Vecihi Hürkuş ve Akşehir Ganimet Uçağı": {
        "metin": (
            "Kurtuluş Savaşı'nın en çetin günlerinde Garp Cephesi Tayyare Bölüğü'nde görev yapan Vecihi Hürkuş, "
            "Akşehir'deki imkansızlıklar içinde adeta bir mühendislik mucizesi yaratmıştır. Yunan ordusundan zorunlu "
            "iniş yaptığı için ele geçirilen veya cephede bırakılan hasarlı De Havilland DH.9 tipi keşif uçağını ele "
            "alan Hürkuş, ellerindeki diğer hurda ve parçalanmış uçakların sağlam kısımlarını sökerek bu uçağa entegre "
            "etmiştir. Teknik literatüre 'Ganimet' ya da 'Ganimet No:1' olarak geçen bu uçak, Büyük Taarruz'un hemen "
            "öncesinde ve sırasında cephe gerisindeki düşman hareketliliğini gözlemlemek amacıyla çok kritik keşif "
            "ve bombardıman uçuşlarında kullanılmıştır. Kısıtlı malzeme ve aletlerle uçak gövdesi tamiri, kanat "
            "gerdirme ve motor optimizasyonu yapan Vecihi Bey, zaferin gökyüzündeki mimarlarından biri olmuştur."
        ),
        "resim": "images/18_vecihi_akşehir_ganimet.jpg"
    },
    "19. 1923: Cumhuriyetin İlanı ve Hava Kuvvetleri Yeniden Yapılanması": {
        "metin": (
            "29 Ekim 1923'te Cumhuriyetin ilan edilmesiyle birlikte, savaştan galip ama yorgun çıkan Türkiye, askeri "
            "havacılığını modern dünyayla uyumlu hale getirmek için büyük bir yeniden yapılanma süreci başlatmıştır. "
            "İzmir, Eskişehir ve Konya'daki hava birimleri birleştirilerek modern bir komuta zinciri oluşturulmuştur. "
            "Mustafa Kemal Atatürk, 'İstikbal göklerdedir' vizyonunu devlet politikası haline getirerek ordunun hava "
            "gücünün tamamen yerli ve bağımsız bir yapıya kavuşturulmasını emretmiştir. Bu dönemde Avrupa'daki teknolojik "
            "gelişmeler yakından izlenmeye başlanmış, hava subaylarının eğitimi için yeni modern müfredatlar hazırlanmış "
            "ve genç Türkiye Cumhuriyeti'nin gökyüzündeki egemenlik hakları yasal olarak perçinlenmiştir."
        ),
        "resim": "images/19_cumhuriyet_hava_kuvvetleri.jpg"
    },
    "20. 1925: Türk Tayyare Cemiyeti'nin (TTC) Kurulması": {
        "metin": (
            "16 Şubat 1925 tarihinde, bizzat Mustafa Kemal Atatürk'ün direktifleriyle halkta havacılık bilincini "
            "geliştirmek ve yerli uçak sanayisine finansal kaynak sağlamak amacıyla Türk Tayyare Cemiyeti (daha sonra "
            "Türk Hava Kurumu - THK) kurulmuştur. Cemiyet, kısa sürede tüm yurtta büyük bir bağış kampanyası başlatmış, "
            "halkın fitre, zekat ve kurban derisi bağışlarıyla milyonlarca lira kaynak toplanmıştır. Toplanan bu paralarla "
            "yurt dışından uçaklar satın alınarak orduya bağışlanmış, aynı zamanda yerli uçak fabrikalarının kurulması "
            "için gerekli sermaye biriktirilmiştir. TTC, Türk milletinin havacılığı toplumsal bir dava olarak benimsemesini "
            "sağlayan, sivil ve askeri havacılığın gelişimindeki en büyük finansal ve kültürel motordur."
        ),
        "resim": "images/20_turk_tayyare_cemiyeti.jpg"
    },
    "21. 1925: Kayseri TOMTAŞ Fabrk.": {
        "metin": (
            "Cumhuriyetin ilanından hemen sonra, tam bağımsız bir savunma sanayisi inşa etmek amacıyla 6 Ekim 1925 "
            "yılında Kayseri'de Tayyare ve Motor Türk Anonim Şirketi (TOMTAŞ) kurulmuştur. Alman Junkers firması "
            "ortaklığıyla hayata geçirilen bu vizyoner fabrika, dönemin dünyadaki en modern ve ileri teknoloji uçak "
            "üretim tesislerinden biri olarak tasarlanmıştır. Fabrikada yüzlerce Türk mühendis, teknisyen ve kalifiye "
            "işçi eğitilmiş, Junkers A-20 ve F-13 gibi metal gövdeli ileri teknoloji uçaklarının montajı, bakımı ve "
            "üretimi başarıyla gerçekleştirilmiştir. TOMTAŞ, Kayseri'nin stratejik konumunu havacılık merkezine "
            "dönüştürürken, Türk milletinin kendi kanatlarını kendi topraklarında üretebileceğini tüm dünyaya gösteren "
            "tarihi bir sanayi kalesi olmuştur."
        ),
        "resim": "images/21_kayseri_tomtas.jpg"
    },
    "22. 1926: Eskişehir Tayyare Tamir Fabrikasının Faaliyete Geçmesi": {
        "metin": (
            "1926 yılında askeri uçakların bakım, onarım ve parça yenileme ihtiyaçlarını karşılamak üzere Eskişehir'de "
            "Tayyare Tamir Fabrikası (bugünkü 1. HİBM) kurulmuştur. Bu tesis, Türk Hava Kuvvetleri'nin envanterindeki "
            "farklı ülkelerden alınan uçakların motor revizyonlarını yapabilecek, gövde çatlaklarını onarabilecek ve "
            "pervanelerini kalibre edebilecek teknik donanıma sahipti. Fabrika bünyesinde kurulan metalurji ve döküm "
            "atölyeleri sayesinde, dışa bağımlılık önemli ölçüde azaltılmıştır. Eskişehir'deki bu teknik altyapı, "
            "Türk mühendislerinin ve teknisyenlerinin uçak mekaniği üzerinde uzmanlaşmasını sağlayarak gelecekteki "
            "yerli üretim hamlelerine muazzam bir pratik iş gücü desteği sunmuştur."
        ),
        "resim": "images/22_eskisehir_tamir_fabrikasi.jpg"
    },
    "23. 1928: TOMTAŞ'ın Kapatılması ve Kayseri Tayyare Fabrikası (KTF)": {
        "metin": (
            "1928 yılına gelindiğinde, Alman Junkers firmasının yaşadığı ekonomik krizler ve ortaklık sözleşmesindeki "
            "bazı bürokratik anlaşmazlıklar nedeniyle TOMTAŞ ortaklığı sona ermiş ve fabrika kapatılmıştır. Ancak "
            "Türk devleti bu stratejik yatırımdan vazgeçmemiş, hisseleri tamamen devralarak tesisi Kayseri Tayyare "
            "Fabrikası (KTF) adıyla yeniden faaliyete geçirmiştir. Tamamen milli sermaye ve yönetimle yoluna devam "
            "eden fabrika, Amerikan Curtiss-Wright ve Polonya PZL firmalarıyla yeni lisans anlaşmaları imzalayarak "
            "avcı ve keşif uçaklarının üretimine odaklanmıştır. Bu dönüşüm, dış ortaklar gitse bile yerli üretim "
            "iradesinin devlet eliyle kararlılıkla sürdürüldüğünün tarihi bir kanıtıdır."
        ),
        "resim": "images/23_kayseri_tayyare_fabrikasi.jpg"
    },
    "24. 1930: Türk Kuşu'nun Temelleri ve Havacılık Eğitimleri": {
        "metin": (
            "1930'lu yılların başında Türkiye, sivil havacılığı yaygınlaştırmak ve genç nesillere uçuş disiplinini "
            "aşılamak amacıyla sivil havacılık eğitimlerine hız vermiştir. Türk Tayyare Cemiyeti bünyesinde planörlük, "
            "paraşütçülük ve sivil pilotluk kurslarının altyapısı planlanmaya başlanmıştır. Mustafa Kemal Atatürk'ün "
            "yakından takip ettiği bu süreçte, gençlerin havacılık kulüplerine katılması teşvik edilmiş, yurt dışından "
            "uzman eğitmenler getirilmiştir. Sivil havacılığın gelişmesi, sadece hobi veya spor amaçlı değil, olası bir "
            "savaş durumunda orduya hazır yedek pilot havuzu oluşturmak açısından da stratejik bir öneme sahipti. Bu "
            "dönem, Türk sivil havacılığının kurumsal altın çağının habercisidir."
        ),
        "resim": "images/24_turkkusu_temelleri.jpg"
    },
    "25. 1930: Kayseri Fabrikasında İlk Montaj Üretimleri": {
        "metin": (
            "1930 yılından itibaren Kayseri Tayyare Fabrikası, uluslararası standartlarda seri montaj ve parça üretimi "
            "yeteneneğini en üst seviyeye çıkarmıştır. Polonya ile yapılan anlaşma çerçevesinde PZL-24 avcı uçaklarının "
            "parçaları Kayseri'ye getirilmiş ve burada Türk işçilerinin emeğiyle montajlanarak gökyüzüyle buluşturulmuştur. "
            "Fabrikada üretilen uçaklar, dönemin en hızlı ve en gelişmiş avcı uçakları arasında yer almaktaydı. İşçiler "
            "ve mühendisler sac şekillendirme, perçinleme ve motor montajı konusunda mükemmel bir hassasiyet kazanmışlardır. "
            "Kayseri'de üretilen bu uçaklar Türk Hava Kuvvetleri filosunun bel kemiğini oluşturmuş ve fabrikada üretilen "
            "uçakların kalitesi yabancı heyetler tarafından takdirle karşılanmıştır."
        ),
        "resim": "images/25_kayseri_pzl_uretimi.jpg"
    },
    "26. 1930: Vecihi V-XIV İlk Türk Sivil Eğitim Uçağı": {
        "metin": (
            "Havacılık dehamız Vecihi Hürkuş, 1930 yılında Kadıköy'de kiraladığı bir keresteci dükkanında, tamamen "
            "kendi tasarımı ve mühendislik hesaplarıyla ilk sivil Türk uçağı olan Vecihi V-XIV'ü inşa etmiştir. "
            "İki kişilik, tek motorlu ve parasol kanat yapısına sahip bu uçak, dönemin aerodinamik standartlarını "
            "başarıyla karşılayan muazzam bir tasarım örneğidir. Uçağı tamamladıktan sonra uçuş müsaadesi almak "
            "isteyen Hürkuş, dönemin bürokratik yetersizlikleri nedeniyle Türkiye'de sertifika alamamış, bunun üzerine "
            "uçağı sökerek trenle Çekoslovakya'ya götürmüştür. Prag'da yapılan uluslararası teknik testlerde uçağın "
            "mükemmel uçuş dinamiklerine ve mukavemete sahip olduğu kanıtlanarak tam uçuş sertifikası alınmış, Vecihi Bey "
            "bu uçakla Avrupa semalarından uçarak yurda geri dönmüştür."
        ),
        "resim": "images/26_vecihi_v14.jpg"
    },
    "27. 1932: Vecihi Sivil Tayyare Mektebi'nin Kurulması": {
        "metin": (
            "Avrupa'dan uçuş sertifikasıyla dönen Vecihi Hürkuş, Türkiye'nin ilk sivil havacılık okulu olan Vecihi Sivil "
            "Tayyare Mektebi'ni 1932 yılında İstanbul Kadıköy'de kurmuştur. Okulun temel amacı, Türk gençlerine havacılığı "
            "sevdirmek ve tamamen yerli imkanlarla sivil pilotlar yetiştirmekti. Aralarında Bedriye Tahir Gökmen'in de "
            "bulunduğu ilk Türk kadın sivil pilotlar bu okulda eğitim görmüşlerdir. Vecihi Bey, kendi ürettiği uçakları "
            "eğitimlerde kullanmış, öğrencilerine hem teorik aerodinamik hem de pratik uçuş mekaniği dersleri vermiştir. "
            "Devletten yeterli maddi destek alamamasına rağmen büyük bir fedakarlıkla okulu açık tutan Hürkuş, sivil "
            "havacılığımızın kurumsallaşması yolunda tek başına bir akademi gibi çalışmıştır."
        ),
        "resim": "images/27_vecihi_sivil_mektep.jpg"
    },
    "28. 1936: Nuri Demirağ ve Yerli Havacılık Vizyonu": {
        "metin": (
            "Cumhuriyet döneminin en büyük vizyoner girişimcilerinden biri olan Nuri Demirağ, 'Avrupa'dan uçak satın "
            "almakla bu milletin gökleri korunamaz, kendi fabrikamızı kurmalıyız' diyerek 1936 yılında büyük bir "
            "havacılık hamlesi başlatmıştır. İstanbul Beşiktaş'ta dönemin en modern uçak tasarım atölyesini kuran "
            "Demirağ, Yeşilköy'de ise gök okulu, teknik hangarlar ve bugün Atatürk Havalimanı olan geniş bir uçuş pisti "
            "inşa etmiştir. Türk mühendis ve teknisyenlerine güvenerek tam finansal destek sağlayan Nuri Demirağ, "
            "yerli uçak tasarımı, rüzgar tüneli testleri ve malzeme metalurjisi konularında Türkiye'de ilk kez kurumsal "
            "Ar-Ge faaliyetlerini fonlayan lider olmuştur. Onun bu bütüncül ve bağımsız havacılık vizyonu, Türk savunma "
            "sanayisinin proto-endüstriyel dönemdeki en parlak sayfasını temsil eder."
        ),
        "resim": "images/28_nuri_demirag_vizyon.jpg"
    },
    "29. 1935: Türkkuşu Havacılık Okulu'nun Resmi Açılışı": {
        "metin": (
            "3 Mayıs 1935 tarihinde Mustafa Kemal Atatürk'ün emirleriyle kurulan Türkkuşu, sivil havacılık eğitimlerini "
            "devlet çatısı altında kurumsallaştıran devasa bir adımdır. Ankara Güvercinlik'te açılan okulun ilk müdürlüğüne "
            "Abdurrahman Türkkuşu getirilmiş, Rusya'dan getirilen uzmanlarla birlikte planör ve paraşüt eğitimleri hızla "
            "başlatılmıştır. Atatürk, havacılığın Türk gençliğinin karakterinin bir parçası olması gerektiğine inanmaktaydı. "
            "Türkkuşu kısa sürede binlerce gence ücretsiz uçuş eğitimi vermiş, Anadolu'nun dört bir yanından gelen yetenekli "
            "çocukları birer gökyüzü kahramanına dönüştürmüştür. Bu okul, modern sivil havacılığımızın ve Hava Kuvvetlerimizin "
            "en önemli insan kaynağı tedarik merkezi haline gelmiştir."
        ),
        "resim": "images/29_turkkusu_acilis.jpg"
    },
    "30. 1936: Nu.D-36 İlk Türk Eğitim Uçağı": {
        "metin": (
            "Nuri Demirağ'ın Beşiktaş'taki uçak fabrikasında, Başmühendis Selahattin Alan'ın tasarım liderliğinde "
            "geliştirilen Nu.D-36, Türkiye'nin ilk yerli üretim eğitim ve yakın keşif uçağıdır. Çift kanatlı (biplane), "
            "iki kokpitli ve dönemin eğitim gereksinimlerine uygun olarak yüksek manevra kabiliyetine sahip olan bu "
            "uçak, gövde mukavemeti ve aerodinamik dengesiyle öne çıkmıştır. Türk Hava Kurumu (THK) tarafından verilen "
            "siparişler doğrultusunda seri üretimi yapılan Nu.D-36 uçakları, Yeşilköy Gök Okulu'nda onlarca genç Türk "
            "pilot adayının ilk uçuş deneyimlerini emniyetle gerçekleştirmesini sağlamıştır. Tamamen yerli iş gücü, "
            "yerli ahşap ve bez kaplama teknolojileri ile üretilen bu model, yapısal hafifliği ve stabil uçuş "
            "karakteristiği ile Türk mühendisliğinin rüştünü ispat ettiği bir tasarımdır."
        ),
        "resim": "images/30_nud36_egitim.jpg"
    },
    "31. 1938: Sabiha Gökçen ve İlk Kadın Savaş Pilotu Dönemi": {
        "metin": (
            "Mustafa Kemal Atatürk'ün manevi kızı Sabiha Gökçen, 1935 yılında Türkkuşu'nda başladığı havacılık eğitimlerini "
            "başarıyla tamamlayarak askeri havacılık alanına yönelmiştir. Eskişehir Hava Okulu'nda özel askeri uçuş eğitimi "
            "alan Gökçen, 1937-1938 yıllarında gerçekleştirilen askeri harekatlara bizzat katılarak dünya tarihinin ilk "
            "kadın savaş pilotu unvanını kazanmıştır. Breguet ve Vultee tipi bombardıman uçaklarıyla zorlu operasyonel "
            "görevleri başarıyla icra eden Sabiha Gökçen, Türk kadınının fırsat verildiğinde en ileri teknoloji askeri "
            "platformları bile ne kadar mükemmel kullanabileceğini tüm dünyaya kanıtlamıştır. Onun bu başarısı, küresel "
            "havacılık tarihine kadın hakları ve askeri tarih açısından altın harflerle geçmiştir."
        ),
        "resim": "images/31_sabiha_gokcen.jpg"
    },
    "32. 1938: Nu.D-38 İlk Türk Yolcu Uçağı Tasarımı": {
        "metin": (
            "Nu.D-36'nın başarısının ardından Nuri Demirağ ve ekibi, çok daha büyük ve stratejik bir projeye imza atarak "
            "Türkiye'nin ilk yerli yolcu uçağı olan Nu.D-38'i tasarlamışlardır. Çift motorlu, tamamen metal gövdeli ve 6 "
            "yolcu kapasiteli bu uçak, dönemin Avrupa ve Amerika standartlarındaki yolcu uçaklarıyla yarışabilecek teknik "
            "özelliklere sahipti. Saatte 325 km hıza ulaşabilen ve binlerce kilometre menzili olan Nu.D-38, İstanbul-Ankara "
            "arasında başarılı deneme uçuşları gerçekleştirmiştir. Tamamen Türk mühendislerinin aerodinamik ve mukavemet "
            "hesaplarıyla üretilen bu uçak, ticari havacılıkta kendi kendine yeten bir Türkiye vizyonunun en somut ve "
            "en ileri seviyedeki mühendislik ürünüdür."
        ),
        "resim": "images/32_nud38_yolcu_ucagi.jpg"
    },
    "33. 1941: THK Etimesgut Uçak Fabikasının Açılması": {
        "metin": (
            "İkinci Dünya Savaşı'nın tüm dünyayı kavurduğu 1941 yılında, Türkiye dışarıdan uçak alımının tamamen "
            "duracağını öngörerek Ankara Etimesgut'ta devasa bir yerli uçak fabrikası kurmuştur. Türk Hava Kurumu bünyesinde "
            "işletilen Etimesgut Uçak Fabrikası, dönemin en iyi yetişmiş Türk mühendislerini, rüzgar tüneli uzmanlarını "
            "ve ahşap-metal ustalarını bir araya getirmiştir. İngiltere ve Fransa'dan dönen yüksek mühendislerin de "
            "katılımıyla fabrikada geniş bir Ar-Ge laboratuvarı oluşturulmuştur. Savaş yıllarının getirdiği hammadde "
            "ambargolarına rağmen, yerli kereste, özel kumaşlar ve ithal motorlar birleştirilerek özgün tasarımlar "
            "geliştirilmiş, fabrika adeta bir ulusal teknoloji enstitüsü gibi çalışmıştır."
        ),
        "resim": "images/33_etimesgut_uçak_fabrikası.jpg"
    },
    "34. 1944: THK-2 Özgün Eğitim Uçağı Projesi": {
        "metin": (
            "THK Etimesgut Fabrikası'nda üretilen en başarılı ve tamamen özgün projelerden biri THK-2 akrobasi ve eğitim "
            "uçağıdır. Tek motorlu, alçak kanatlı ve tamamen ahşap monokok gövde yapısına sahip olan bu uçak, olağanüstü "
            "bir manevra kabiliyetine ve aerodinamik zarafete sahipti. Dönemin Türk Hava Kuvvetleri pilotlarının ileri "
            "düzey uçuş ve akrobasi eğitimleri için tasarlanmış olup, seri üretimi başarıyla gerçekleştirilmiştir. "
            "THK-2, Türk tasarımcıların akışkanlar mekaniği ve ağırlık-denge (weight and balance) optimizasyonunda ne kadar "
            "usta olduğunu gösteren, yabancı lisanslara ihtiyaç duymadan da sıfırdan mükemmel bir uçak gövdesi inşa "
            "edebileceğimizin en net kanıtıdır."
        ),
        "resim": "images/34_thk2_egitim_ucagi.jpg"
    },
    "35. 1948: THK-13 Uçan Kanat Projesi": {
        "metin": (
            "İkinci Dünya Savaşı sonrasında Türk Hava Kurumu (THK) Etimesgut Uçak Fabrikası'nda görev yapan Türk "
            "mühendisler, havacılık dünyasında fütüristik bir konsept olan 'Uçan Kanat' (Flying Wing) tasarımı üzerinde "
            "çalışmaya başlamışlardır. 1948 yılında prototipi üretilen THK-13, geleneksel bir gövde ve kuyruk yapısı "
            "barındırmayan, tüm uçağın tek bir kanat profilinden (airfoil) oluştuğu son derece ileri düzey bir aerodinamik "
            "projedir. Tasarımındaki ana amaç, parazit sürüklemeyi (drag) minimuma indirerek maksimum kaldırma kuvveti "
            "ve yakıt verimliliği elde etmekti. İlk olarak planör versiyonu üretilen ve başarılı süzülme testleri "
            "gerçekleştiren THK-13, dönemin havacılık devleriyle aynı anda bu karmaşık teknolojiyi çözen Türk "
            "mühendislerinin aerodinamik ve akışkanlar mekaniği konusundaki yüksek seviyesini kanıtlamaktadır."
        ),
        "resim": "images/35_thk13_ucan_kanat.jpg"
    },
    "36. 1945: Ankara Rüzgar Tüneli (ART) İnşası": {
        "metin": (
            "Uçak tasarımlarının aerodinamik testlerini yerli imkanlarla yapabilmek amacıyla 1945 yılında Ankara'da "
            "büyük bir rüzgar tüneli (ART) inşası başlatılmıştır. Dönemin Başbakanlık ve THK bütçesiyle fonlanan bu "
            "proje, Türkiye'nin havacılıkta bilimsel Ar-Ge altyapısına verdiği önemi gösteren en büyük anıttır. Ses "
            "altı (subsonic) hızlarda hava akımları üretebilen bu tünel, uçak modellerinin üzerindeki sürükleme ve kaldırma "
            "kuvvetlerini hassas mekanik terazilerle ölçebilecek kapasitedeydi. İnşası tamamlandıktan sonra dönemin "
            "siyasi çalkantıları nedeniyle uzun süre atıl kalsa da, Ankara Rüzgar Tüneli, Türk havacılık biliminin deneysel "
            "altyapı konusundaki en vizyoner ve en stratejik yatırımlarından biri olarak tarihteki yerini almıştır."
        ),
        "resim": "images/36_ankara_ruzgar_tuneli.jpg"
    },
    "37. 1950: Gazi Uçak Motoru Fabrikası ve Kapatılma Süreci": {
        "metin": (
            "Türkiye sadece uçak gövdesi değil, havacılığın en zor kısmı olan motor teknolojisinde de bağımsız olmak "
            "amacıyla 1948'de Ankara Gazi Çiftliği'nde THK Uçak Motoru Fabrikası'nı kurmuş ve 1950'de tam üretime geçirmiştir. "
            "İngiliz Gipsy Major motorlarının lisanslı üretimi ve revizyonu amacıyla kurulan bu modern tesiste, silindir "
            "blokları dökülmüş ve hassas krank milleri işlenmiştir. Ancak 1950'lerin başında başlayan Marshall Yardımları "
            "ve ABD'nin ucuz, hibe uçak ve motor politikası, fabrikanın sipariş almasını engellemiştir. Siyasi iradenin "
            "yerli üretime olan desteğini çekmesiyle birlikte bu muazzam motor fabrikası önce traktör fabrikasına "
            "dönüştürülmüş, ardından tamamen kapatılarak Türk motor sanayisine vurulan en büyük darbelerden biri olmuştur."
        ),
        "resim": "images/37_gazi_motor_fabrikasi.jpg"
    },
    "38. 1952: Türkiye'nin NATO'ya Girişi ve Havacılıkta Jet Çağı": {
        "metin": (
            "1952 yılında Türkiye'nin Kuzey Atlantik Antlaşması Örgütü'ne (NATO) üye olmasıyla birlikte, Türk Hava "
            "Kuvvetleri'nde lojistik ve teknolojik açıdan köklü bir değişim yaşanmıştır. Pistonlu ve pervaneli uçakların "
            "yerini hızla F-84G Thunderjet ve F-86 Sabre gibi modern jet savaş uçakları almaya başlamıştır. Bu süreç "
            "Türk pilotlarının jet hızlarında uçuş mekaniği, yüksek G kuvveti yönetimi ve modern hava taktikleri konusunda "
            "uzmanlaşmasını sağlamıştır. Ancak bu teknolojik sıçrama, askeri sistemlerin tamamen ABD ve NATO "
            "standartlarına bağımlı hale gelmesiyle sonuçlanmış, yerli uçak tasarımı ve üretimi felsefesi uzun bir "
            "süreliğine askeri doktrinden tamamen silinmiştir."
        ),
        "resim": "images/38_nato_jet_cagi.jpg"
    },
    "39. 1954: THK Fabrikalarının MKEK'e Devredilmesi": {
        "metin": (
            "1954 yılı, Türk yerli havacılık sanayisinin kurumsal olarak tasfiye edildiği kara bir kronolojik dönüm "
            "noktasıdır. Finansal zorluklar ve devlet desteğinin tamamen kesilmesi nedeniyle THK Etimesgut Uçak Fabrikası "
            "ve Gazi Motor Fabrikası, Makine ve Kimya Endüstrisi Kurumu'na (MKEK) devredilmiştir. MKEK bünyesinde bir "
            "süre daha MKEK-4 Uğur gibi eğitim uçakları üretilmiş olsa da, yurt dışından bedelsiz gelen Amerikan "
            "uçaklarının cazibesi ve savunma politikasındaki vizyonsuzluk nedeniyle üretim hatları tamamen durdurulmuştur. "
            "Fabrikalar tekstil ambarlarına veya makine parçası üreten atölyelere dönüştürülerek, onlarca yıllık yetişmiş "
            "mühendislik birikimi ve yerli havacılık rüyası askıya alınmıştır."
        ),
        "resim": "images/39_thk_mkek_devri.jpg"
    },
    "40. 1964: Kıbrıs Uyarı Uçuşları ve Cengiz Topel'in Şehadeti": {
        "metin": (
            "1964 yılında Kıbrıs'ta Türk halkına yönelik başlayan katliamlar ve baskılar karşısında, Türk Hava Kuvvetleri "
            "jetleri Kıbrıs semalarında tarihi uyarı uçuşları gerçekleştirmiştir. Erenköy direnişine destek vermek amacıyla "
            "Eskişehir'den kalkan F-100 Super Sabre jetlerimizin liderliğini yapan Yüzbaşı Cengiz Topel'in uçağı, "
            "uçaksavar ateşiyle vurulmuştur. Paraşütle atlayarak Rum bölgesine inen ve esir alınan Topel, işkenceyle "
            "şehit edilerek modern Türk jet havacılığının ilk cumhuriyet dönemi şehidi olmuştur. Bu olay, Türkiye'ye "
            "dışarıdan müdahale edilmek istendiğinde yerli ve bağımsız bir hava gücünün, ambargolara boyun eğmeyen bir "
            "askeri endüstrinin ne kadar hayati olduğunu tüm topluma ve devlet ricaline sert bir şekilde hatırlatmıştır."
        ),
        "resim": "images/40_cengiz_topel_kibris.jpg"
    },
    "41. 1970: Hava Kuvvetlerini Güçlendirme Vakfı'nın Kurulması": {
        "metin": (
            "Kıbrıs gerginliği ve ardından gelen uluslararası siyasi baskılar, Türk milletinde 'Kendi uçağını kendin yap' "
            "ruhunu yeniden ateşlemiştir. 1970 yılında, halkın doğrudan desteğiyle Türk Hava Kuvvetlerini Güçlendirme "
            "Vakfı kurulmuştur. Tıpkı 1925'teki Türk Tayyare Cemiyeti gibi, Türk halkı yine büyük bir fedakarlıkla vakfa "
            "bağışlar yağdırmıştır. Vakfın biriken sermayesi, tamamen yerli savunma sanayii şirketlerinin kurulması amacıyla "
            "bir Ar-Ge ve endüstri fonuna dönüştürülmüştür. Bu vakıf modeli, bugünkü ASELSAN, TUSAŞ ve HAVELSAN gibi "
            "dünya devi yerli şirketlerimizin kurulmasını sağlayan finansal ve fikri kuluçka merkezi olmuş, bağımsızlık "
            "iradesini kurumsallaştırmıştır."
        ),
        "resim": "images/41_hava_kuvvetleri_vakfi.jpg"
    },
    "42. 1973: TUSAŞ'ın (Türk Havacılık ve Uzay Sanayii) İlk Kuruluşu": {
        "metin": (
            "28 Haziran 1973 tarihinde, Türkiye'nin uçak sanayisini sıfırdan ve devlet eliyle yeniden ayağa kaldırmak "
            "amacıyla Türk Havacılık ve Uzay Sanayii A.Ş. (TUSAŞ) resmen kurulmuştur. 1950'lerde kesintiye uğrayan yerli "
            "uçak üretimi rüyası, bu kuruluşla birlikte yasal ve kurumsal bir devlet politikasına dönüşmüştür. TUSAŞ'ın "
            "ilk misyonu, Türk Hava Kuvvetleri'nin modern savaş uçağı ihtiyacını karşılayacak küresel ortaklıklar kurmak "
            "ve bu süreçte teknoloji transferi sağlayarak yerli mühendislik kadrolarını yetiştirmekti. Bu tarihi hamle, "
            "bugünkü KAAN, HÜRKUŞ ve ANKA gibi devasa projelerin doğmasını sağlayan ana kurumsal kökün toprağa atılmasıdır."
        ),
        "resim": "images/42_tusas_ilk_kurulus.jpg"
    },
    "43. 1975: ASELSAN'ın Kurulması ve Avyonik Teknolojilerin Temeli": {
        "metin": (
            "1974 Kıbrıs Barış Harekâtı sırasında müttefiklerin telsiz ve muhabere sistemlerini karartması ve ardından "
            "gelen ağır ABD ambargosu, askeri elektroniğin önemini ortaya çıkarmıştır. 1975 yılında Türk Silahlı Kuvvetlerini "
            "Güçlendirme Vakfı öncülüğünde Askeri Elektronik Sanayii (ASELSAN) kurulmuştur. İlk olarak askeri telsiz "
            "üretimiyle işe başlayan ASELSAN, kısa sürede uçakların, helikopterlerin ve İHA'ların beynini oluşturan aviyonik "
            "(aviation electronics) sistemler, radarlar, hedefleme podları ve uçuş bilgisayarları geliştiren küresel "
            "bir teknoloji devine dönüşmüştür. Tam bağımsız havacılık için uçak gövdesi kadar, o gövdeyi yönetecek "
            "elektronik sistemlerin de yerli olması gerektiği gerçeği ASELSAN ile hayat bulmuştur."
        ),
        "resim": "images/43_aselsan_kurulus.jpg"
    },
    "44. 1987: TAI Mürted Tesisleri ve F-16 Üretimi": {
        "metin": (
            "1974 Kıbrıs Barış Harekâtı sonrası uygulanan ambargoların ardından kendi uçağını kendin yap iradesi "
            "yeniden canlanmış ve 1984 yılında TUSAŞ Havacılık ve Uzay Sanayii (TAI) kurulmuştur. 1987 yılında Ankara "
            "Mürted'de (Akıncı) kurulan devasa tesislerde, Türk Hava Kuvvetleri'nin ana vurucu gücünü oluşturacak F-16 "
            "Fighting Falcon savaş uçaklarının ortak üretimi ve montajı başlatılmıştır. Bu proje kapsamında sadece montaj "
            "yapılmamış; uçak gövdesi (fuselage) imalatı, kanat yapımı, kompozit malzeme işleme ve aviyonik entegrasyon "
            "teknolojileri Türkiye'ye kazandırılmıştır. Yüksek kalite standartlarında üretilen Türk F-16'ları, TAI "
            "tesislerinin küresel havacılık devleri tarafından tanınan bir üretim üssü olmasını sağlamış ve modern "
            "askeri havacılık ekosistemimizin temel taşını oluşturmuştur."
        ),
        "resim": "images/44_tai_f16_murted.jpg"
    },
    "45. 1988: TEI ve İlk Jet Motoru Parça Üretimi": {
        "metin": (
            "Uçak gövdesi ve elektroniğindeki gelişmelerin yanı sıra, en kritik teknoloji olan motor alanında yetkinlik "
            "kazanmak amacıyla 1985'te kurulan TUSAŞ Motor Sanayii (TEI), 1988 yılında Eskişehir'de üretime başlamıştır. "
            "F-16'larda kullanılan General Electric F110 jet motorlarının montajı ve kritik parçalarının üretimiyle faaliyete "
            "geçen TEI, havacılık metalurjisi, hassas döküm ve yüksek teknolojili talaşlı imalat konularında Türkiye'de "
            "çığır açmıştır. Dünyadaki binlerce uçak motoruna parça tedarik eden küresel bir lider haline gelen TEI, "
            "kazandığı bu derin mühendislik birikimiyle günümüzde tamamen yerli ve milli helikopter, İHA ve jet motorlarını "
            "tasarlayıp çalıştıran bir teknoloji kalesi olmuştur."
        ),
        "resim": "images/45_tei_eskisehir.jpg"
    },
    "46. 2013: TUSAŞ HÜRKUŞ'un İlk Uçuşu": {
        "metin": (
            "Türk Havacılık ve Uzay Sanayii (TUSAŞ) tarafından tamamen özgün olarak tasarlanan ve adını havacılık "
            "dehamız Vecihi Hürkuş'tan alan yeni nesil temel eğitim ve yakın hava destek uçağı HÜRKUŞ, ilk uçuşunu "
            "29 Ağustos 2013 tarihinde başarıyla gerçekleştirmiştir. Tamamen Türk mühendislerince geliştirilen ve "
            "uluslararası sivil havacılık otoritesinden (EASA) CS-23 standartlarında tip sertifikası almayı başaran ilk "
            "Türk uçağı olan HÜRKUŞ, tandem iki koltuklu, alçak kanatlı ve tek motorlu güçlü bir turboprop motor yapısına "
            "sahiptir. Gelişmiş aviyonik sistemleri, fırlatma koltukları ve zorlu manevra kabiliyeti ile modern jet "
            "pilotu eğitim ihtiyaçlarını en üst düzeyde karşılayan HÜRKUŞ, askeri ve sivil havacılığımızın gurur kaynağıdır."
        ),
        "resim": "images/46_tusas_hurkus.jpg"
    },
    "47. 2014: Bayraktar TB2 ve İHA Devrimi": {
        "metin": (
            "Baykar Teknoloji tarafından tamamen özgün tasarım, yazılım ve aviyonik mimariyle geliştirilen Taktik Sınıfı "
            "İnsansız Hava Aracı Bayraktar TB2, 2014 yılında ilk uçuşunu ve kabul testlerini tamamlayarak Türk Silahlı "
            "Kuvvetleri envanterine girmiştir. Üç yedekli uçuş kontrol sistemi, otonom taksi, kalkış, seyir ve iniş "
            "kabiliyetleri ile donatılan TB2, dünyada askeri doktrinleri değiştiren bir İHA devrimine imza atmıştır. "
            "Akıllı mühimmat entegrasyonu (MAM-L/MAM-C) ve yüksek faydalı yük (payload) kapasitesiyle terörle mücadelede, "
            "sınır ötesi harekatlarda ve küresel çatışma bölgelerinde gösterdiği üstün operasyonel başarı, onu dünyanın en "
            "çok ihraç edilen insansız hava aracı konumuna getirmiştir. TB2, Türk mühendisliğinin yazılım ve robotik "
            "alanındaki küresel liderliğinin somut bir kanıtıdır."
        ),
        "resim": "images/47_bayraktar_tb2.jpg"
    },
    "48. 2023: KIZILELMA ve ANKA-3 İnsansız Jet Çağı": {
        "metin": (
            "Cumhuriyetimizin 100. yılı olan 2023, Türk havacılık sanayisinin insansız savaş jeti çağına adım attığı "
            "tarihi bir dönüm noktası olmuştur. Baykar tarafından geliştirilen Bayraktar KIZILELMA MİUS (Milli İnsansız "
            "Uçak Sistemi) ve TUSAŞ tarafından geliştirilen ANKA-3 Delta Kanat İnsansız Savaş Uçağı ardı ardına başarılı "
            "ilk uçuşlarını gerçekleştirmişlerdir. Turbojet/Turbofan motor sistemleriyle donatılan, düşük radar kesit alanı "
            "(stealth) teknolojisine sahip olan bu platformlar, hava-hava ve hava-yer görevlerini otonom olarak icra "
            "edebilmektedir. Agresif manevra kabiliyetleri, yapay zeka destekli uçuş bilgisayarları ve insanlı savaş "
            "uçaklarıyla müşterek harekat icra etme yetenekleri ile KIZILELMA ve ANKA-3, Türk mühendisliğinin havacılığın "
            "geleceğini şekillendirdiğinin en açık ilanıdır."
        ),
        "resim": "images/48_kizilelma_anka3.jpg"
    },
    "49. 2024: TUSAŞ KAAN Beşinci Nesil Savaş Uçağının İlk Uçuşu": {
        "metin": (
            "21 Şubat 2024 tarihinde, Türk havacılık tarihinin en büyük ve en görkemli mühendislik başarısı gerçekleşmiş "
            "ve TUSAŞ tarafından geliştirilen 5. Nesil Milli Muharip Uçak KAAN, ilk uçuşunu başarıyla tamamlamıştır. "
            "Çift jet motorlu, düşük radar görünürlüğü (stealth), dahili silah istasyonları ve yapay zeka destekli akıllı "
            "sensör füzyonuna sahip olan KAAN, Türkiye'yi dünyada bu seviyede bir uçak üretebilen topu topu 4-5 ülkeden "
            "biri konumuna yükseltmiştir. Gökyüzünde süper-seyir (supercruise) yapabilen, elektronik harp korumalı aviyonikleri "
            "ve yerli füzeleriyle tam bir egemenlik silahı olan KAAN, Türk mühendislerinin, teknisyenlerinin ve havacılık "
            "sanayimizin yüzyıllık bağımsızlık yürüyüşünün ulaştığı nihai zirvedir."
        ),
        "resim": "images/49_tusas_kaan_ilk_ucus.jpg"
    },
    "50. 2026 Vizyonu: Küresel Jeopolitik Konum ve Uzay Sanayii": {
        "metin": (
            "2026 yılı itibarıyla Türkiye, havacılıkta kazandığı bu muazzam teknolojik ivmeyi uzay sanayii ve küresel "
            "jeopolitik stratejilerle taçlandırmaktadır. TUSAŞ, Baykar, ASELSAN, TEI ve ROKETSAN gibi kuruluşların "
            "kurduğu entegre ekosistem, sadece yerli ihtiyaçları karşılamakla kalmayıp dünyaya milyarlarca dolarlık "
            "ileri teknoloji ihraç etmektedir. 2026 vizyonu doğrultusunda, yerli motor projelerinin olgunlaşması, KAAN'ın "
            "seri üretim hazırlıkları, alçak yörünge uydu takımları ve mikro fırlatma sistemleri (MFS) ile gökyüzündeki "
            "bağımsızlık uzayın derinliklerine taşınmaktadır. Türk milleti, köklü tarihi mirasından aldığı ilham ve "
            "sarsılmaz milli teknoloji hamlesi iradesiyle, geleceğin dünyasında ve uzay jeopolitiğinde kendi oyununu "
            "kuran küresel bir aktör haline gelmiştir."
        ),
        "resim": "images/50_2026_vizyonu_kaan.jpg"
    }
}

# 3. Sayfa Listesini Çıkarma ve Hafıza Yönetimi (Session State)
sayfalar = list(havacilik_tarihi_db.keys())

if "sayfa_index" not in st.session_state:
    st.session_state.sayfa_index = 0

# 4. Yan Menü (Sidebar) Alanı
st.sidebar.title("Türk Havacılık Tarihi")

# Menüyü hafızadaki index ile senkronize oluşturuyoruz
secilen_sayfa = st.sidebar.selectbox(
    "Görüntülemek İstediğiniz Sayfayı Seçiniz:",
    sayfalar,
    index=st.session_state.sayfa_index
)

# Eğer kullanıcı sol menüden el ile başka bir sayfaya tıklarsa hafızayı güncelle
yeni_index = sayfalar.index(secilen_sayfa)
if yeni_index != st.session_state.sayfa_index:
    st.session_state.sayfa_index = yeni_index
    st.rerun()

# Sol menü altındaki takım bilgi kutusu
st.sidebar.write("")
st.sidebar.info("🛸 ALBAYRAK Teknoloji Takımı -\nDijital Havacılık Kitaplığı\nProjesi © 2026")

# 5. Ana İçerik Ekranı (layout="wide" sayesinde ekranın tamamına yayılır)
st.title(secilen_sayfa)

# Aktif sayfanın verilerini çekiyoruz
aktif_icerik = havacilik_tarihi_db[secilen_sayfa]

# Metin Gösterimi
st.write(aktif_icerik["metin"])

# Görsel Kontrolü ve Gösterimi
resim_yolu = aktif_icerik["resim"]
if resim_yolu:
    if os.path.exists(resim_yolu):
        st.image(resim_yolu, use_container_width=True)
    else:
        st.warning(f"⚠️ Görsel bulunamadı! Lütfen '{resim_yolu}' adıyla klasöre ekleyin.")

# 6. Akıllı Navigasyon Butonları (En Alt Kısım)
st.write("---")
col1, col2 = st.columns(2)

with col1:
    # İlk sayfada değilsek ÖNCEKİ butonunu göster
    if st.session_state.sayfa_index > 0:
        if st.button("⬅️ Önceki Sayfa", use_container_width=True):
            st.session_state.sayfa_index -= 1
            st.rerun()

with col2:
    # Son sayfada değilsek SONRAKİ butonunu göster
    if st.session_state.sayfa_index < len(sayfalar) - 1:
        if st.button("Sonraki Sayfa ➡️", use_container_width=True):
            st.session_state.sayfa_index += 1
            st.rerun()