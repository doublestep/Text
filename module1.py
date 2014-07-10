#-*- coding: utf-8 -*-
import math

class CompareDoc:
  def magnitude(self,concordance):
    total = 0
    for word,count in concordance.iteritems():
      total += count ** 2
    return math.sqrt(total)

  def relation(self,concordance1, concordance2):
    relevance = 0
    topvalue = 0
    for word, count in concordance1.iteritems():
      if concordance2.has_key(word):
        topvalue += count * concordance2[word]
    if (self.magnitude(concordance1) * self.magnitude(concordance2)) != 0:
      return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))
    else:
      return 0

  def concordance(self,document):
   if type(document) != str:
    con = {}
    for word in document.split(' '):
      if con.has_key(word):
        con[word] = con[word] + 1
      else:
        con[word] = 1
    return con


v = CompareDoc()

documents = {
  0:u'''Nowa metoda pozwoli częściej ratować życie ofiarom wypadków z silnymi krwawieniami wewnętrznymi. Po raz pierwszy na świecie zastosowało ją lotnicze pogotowie dla Londynu Air Ambulance – pisze „BBCNews”. Silne krwawienia wewnętrzne powstałe na skutek urazów są jedną z głównych przyczyn zgonów, następujących przed dowiezieniem do szpitala ofiar wypadków. Według prof. Karim Brohi z Barts Health NHS Trust, prawie 2,5 mln ludzi na świecie każdego roku wykrwawia się na śmierć przed udzieleniem specjalistycznej pomocy. Często nie ma jak pomóc ludziom z krwawieniami wewnętrznymi, bo nie można zatamować takiego krwawienia przez ucisk z zewnątrz. Pojawiła się jednak nadzieja, że wielu ciężko rannym pomoże użycie cewnika z balonikiem. Przypomina on cewnik wykorzystywany od dawna przez kardiologów interwencyjnych do udrożnienia tętnic wieńcowych mięśnia sercowego. Metoda ta, nazywana balonikowaniem, pozwala ratować życie ludzi w ostrym zawale serca. Nowa technika o nazwie Reboa (resuscitative endovascular balloon occlusion of the aorta) ma teraz ratować życie ofiarom wypadków. Polega ona wprowadzeniu przez małe nacięcie w okolicy pachwiny cewnika z balonikiem do naczynia krwionośnego i wsunięcia jej do aorty, największej tętnicy człowieka. Balonik jest następnie napełniany płynem i po rozprężeniu blokuje przepływ krwi poniżej miejsca gdzie doszło do uszkodzenia tego naczynia.Ratownicy Air Ambulance po raz pierwszy wykorzystali tę metodę do ratowania ofiary wypadku drogowego z urazem miednicy i silnymi krwawienia wewnętrznymi. Twierdzą, że gdyby nie „balonikowanie” prawdopodobnie nie byliby w stanie dowieść go żywego do szpitala. Złamanie miednicy może uszkodzić naczynie i wywołać silne krwawienia. Często dochodzi do niego na skutek przygniecenia ciężkimi przedmiotami, upadku z wysokości lub potrącenia przez samochód.Chirurg z Saint Mary's Hospital w Londynie, David Nott twierdzi, że technika Reboa nie jest łatwa w użyciu i wymaga odpowiedniego przeszkolenia. (PAP)''',
  1:u'''Największe uczelnie w kraju zrezygnowały z pobierania opłat za drugi kierunek studiów w roku akademickim 2014/15. W ten sposób wyprzedziły termin wskazany przez Trybunał Konstytucyjny, który orzekł, że opłaty mogą obowiązywać do września 2015 r.

Obowiązujące przepisy - które weszły w życie w 2011 r. - zakładają, że prawo do bezpłatnych studiów na drugim kierunku mają tylko te osoby, które uzyskają co roku prawo do stypendium rektora (maksymalnie 10 proc. studentów).

5 czerwca Trybunał Konstytucyjny orzekł jednak, że przepisy dotyczące odpłatności za drugi kierunek studiów są niezgodne z konstytucją. Nie wymagał jednak, aby zmiany wprowadzić już od roku akademickiego 2014/15. Czas na zmianę przepisów TK wyznaczył do września 2015 roku, a do tego momentu uczelnie mogłyby pobierać opłaty za drugi kierunek.

Tymczasem wiele uczelni nie czekając na wskazany przez TK termin, już zdecydowała o zniesieniu opłat za studia na drugim kierunku. Jako pierwsze taką decyzję podjęły władze Uniwersytetu Warszawskiego, a zaraz po nich na podobny krok zdecydował się Uniwersytet Szczeciński. W Warszawie z pobierania opłat zrezygnował też Uniwersytet Kardynała Stefana Wyszyńskiego.

Na rezygnację z odpłatności zdecydowały się też krakowskie uczelnie: Uniwersytet Jagielloński, Akademia Górniczo-Hutnicza im. Stanisława Staszica, Uniwersytet Jana Pawła II i Uniwersytet Pedagogiczny. Podobnie postąpiły trzy publiczne uczelnie w Katowicach: Uniwersytet Śląski, Uniwersytet Ekonomiczny i Śląski Uniwersytet Medyczny.

W województwie kujawsko-pomorskim decyzję o niepobieraniu opłat za drugi kierunek studiów w nowym roku akademickim podjęły też cztery spośród pięciu uczelni publicznych: Uniwersytet Mikołaja Kopernika w Toruniu, Uniwersytet Kazimierza Wielkiego w Bydgoszczy, Uniwersytet Technologiczno-Przyrodniczy w Bydgoszczy i Państwowa Wyższa Szkoła Zawodowa we Włocławku. Jedynie Akademia Muzyczna w Bydgoszczy rozważa dopiero wprowadzenie odpowiednich przepisów.

Opłat nie będą pobierać również największe uczelnie wrocławskie: Politechnika Wrocławska i Uniwersytet Wrocławski. Podobnie postąpi Uniwersytet Przyrodniczy we Wrocławiu, który opłat i tak nie pobierał. „Nie pobieraliśmy tych opłat, ponieważ nie mieliśmy studentów spełniających kryteria ich poboru” - powiedziała PAP rzeczniczka uczelni Małgorzata Wanke-Jakubowska.

W Lublinie opłaty zniosły: Uniwersytet Marii Skłodowskiej-Curie, Katolicki Uniwersytet Lubelski, Uniwersytet Przyrodniczy i Politechnika Lubelska. Tak samo postąpiły dwie poznańskie uczelnie: Uniwersytet im. Adama Mickiewicza i Uniwersytet Ekonomiczny.

Do grona uczelni niepobierających opłat dołączyły też: Uniwersytet Rzeszowski i Politechnika Rzeszowska, Politechnika Łódzka Uniwersytet Jana Kochanowskiego w Kielcach, Uniwersytet Warmińsko-Mazurski oraz Uniwersytet Opolski. Decyzji nie podjęła jeszcze Politechnika Opolska, która zrobi to po zapoznaniu się z pisemnym uzasadnieniem wyroku TK.

Z pobierania opłat chce zrezygnować też Uniwersytet Łódzki, ale decyzję władze uczelni podejmą we wrześniu. Wtedy też stanowisko w tej sprawie zajmą senaty Uniwersytetu Rolniczego i Uniwersytetu Ekonomicznego w Krakowie.

Uczelnie z Białegostoku i Gdańska nie podjęły jeszcze decyzji czy drugi kierunek będzie u nich bezpłatny.

Również minister nauki i szkolnictwa wyższego Lena Kolarska-Bobińska chce, aby przepisy dotyczące odpłatności za drugi kierunek już teraz dostosować do wyroku Trybunału Konstytucyjnego. "Chodzi o to, by studenci wraz z nowym rokiem akademickim mieli pewność, jakie są reguły gry" - oceniła w komentarzu dla PAP szefowa resortu nauki.

Zaznaczyła, że teraz wszystko jest teraz w rękach parlamentarzystów. To od nich zależy bowiem, jaki kształt ostatecznie przyjmie nowelizowana ustawa Prawo o szkolnictwie wyższym, nad którą pracuje Sejm. Jej drugie czytanie odbędzie się w środę podczas posiedzenia izby. "Zdecydowanie najlepszym rozwiązaniem będzie wykreślenie przepisów mówiących o odpłatności za drugi i kolejny kierunek" - podkreśliła minister. (PAP)''',
  2:u'''Nowo odkryty gatunek os wykorzystuje szczątki mrówek do budowania swych domów – informują naukowcy na łamach „Public Library of Science ONE”.

Ossuaria (lub ossaria) to budynki lub pomieszczenia, w których gromadzono ludzkie szczątki, układając często czaszki i kości wokół ścian. Powstawały one po bitwach, zarazach lub gdy szczątki ze starego cmentarza poddawano ekshumacji, żeby założyć nowy cmentarz.

Od takich budowli pochodzi nazwa nowego gatunku os, Deuteragenia ossarium. Owady te budują dość niezwykłe domy. Do ich konstrukcji wykorzystują bowiem ciała martwych mrówek.

Gatunek zamieszkuje strefę podzwrotnikową. Zaobserwowano go we wschodnich Chinach w rezerwacie Gutianshan. Osy zakładają gniazda w dziurach, które drążą w klifach lub wykorzystują istniejące wcześniej tunele. Znajdują się tam zwykle komórki, w których lęgną się młode.

Jednak w wielu gniazdach odkryto również dodatkową komorę, wypełnioną martwymi ciałami mrówek. Komora znajdowała się zwykle pomiędzy miejscem, gdzie były złożone jaja, a wejściem, stanowiąc rodzaj barykady. Budowały ją samice już po złożeniu jaj.

Zdaniem naukowców z Uniwersytetu we Fryburgu (Niemcy) osy decydują się na wykorzystanie szczątków mrówek ze względu na ich zapach. Być może działa on jak kamuflaż, który ma zmylić drapieżniki, które kojarzą go z zapachem mrowiska. Potwierdzeniem tej hipotezy jest fakt, że najczęściej służącym za budulec gatunkiem mrówki była agresywna Pachycondyla astuta.(PAP)''',
  3:u'''Przyrodnicy, którzy opiekują się bocianami w Kłopocie (Lubuskie), zaobrączkowali kolejne pokolenie młodych ptaków. W tej niewielkiej wsi znajduje się jedyne w Polsce Muzeum Bociana Białego.

Zaobrączkowano 24 młode bociany z 38 z bocianiej wioski. Dokonano obowiązkowych pomiarów obrączkowanych ptaków, sprawdzono m.in.: długość dzioba, długość skrzydła, ciężar ciała - powiedział PAP Krzysztof Gajda z Muzeum Bociana Białego w Kłopocie.

Dodatkowo pracownicy Uniwersytetu Zielonogórskiego wraz ze studentami dokonywali serii innych badań, w tym np. pobierali krew oraz wymazy z dziobów młodych ptaków, wszystko po to, by sprawdzić kondycję młodych bocianów.

Sprawdzono także bocianie gniazda. W przypadku stwierdzenia w nich sznurków, worków i innych niebezpiecznych materiałów były one usuwane. Te rzeczy znoszą do gniazda dorosłe ptaki, wykorzystując je do wzmocnienia konstrukcji potężnego gniazda, jednak sznurek czy torba foliowa są dużym zagrożeniem dla młodych – ptak może się w nie zaplątać bądź udławić się w przypadku połknięcia.

Przyrodnicy i naukowcy systematycznie monitorują bociany z Kłopotu od 1968 roku. Od 2002 roku zaobrączkowano w tym miejscu 280 tych ptaków.

„Aktualnie młode bociany intensywnie ćwiczą mięśnie, aby niebawem rozpocząć swoje pierwsze próbne loty. Około 10-15 sierpnia tegoroczne młodziaki wystartują w pierwszą podróż do Afryki. Na ich powrót do Polski będziemy musieli poczekać około 3-4 lat” - dodał Gajda.

Kłopot nazywany jest bocianią wioską, gdyż w samej wsi znajduje się 35 bocianich gniazd. To sprzyja badaniom zwyczajów i życia tych ptaków.

Właśnie z tego powodu w 2003 r. z inicjatywy Zarządu Okręgu Ligi Ochrony Przyrody w Zielonej Górze powstało tam Muzeum Bociana Białego.

Kłopot leży w gminie Cybinka na terenie Krzesińskiego Parku Krajobrazowego, obejmującego wilgotne łąki i pastwiska położone w dolinie Odry i Nysy Łużyckiej oraz fragmenty odrzańskich łęgów wierzbowych i wierzbowo-topolowych. Takie warunki to raj dla bocianów, które korzystając z obfitości pokarmu licznie odchowują młode w okolicy Kłopotu. (PAP)''',
  4:u'''Najlepszym rozwiązaniem będzie wykreślenie przepisów mówiących o odpłatności za drugi i kolejny kierunek - oceniła szefowa resortu nauki Lena Kolarska-Bobińska po zapoznaniu się z pisemnym uzasadnieniem czerwcowego orzeczenia Trybunału Konstytucyjnego.

5 czerwca Trybunał Konstytucyjny orzekł, że przepisy dotyczące odpłatności za drugi kierunek studiów są niezgodne z konstytucją. Ministerstwo Nauki i Szkolnictwa Wyższego (MNiSW) zapowiadało, że do orzeczenia będzie się mogło szczegółowo odnieść dopiero wtedy, kiedy zapozna się z pisemnym uzasadnieniem TK dotyczącym orzeczenia. Trybunał takie uzasadnienie opublikował pod koniec ubiegłego tygodnia. Szczegółowo wyliczone są w nim elementy ustawy Prawo o szkolnictwie wyższym, które należy zmienić.

"Zdecydowanie najlepszym rozwiązaniem będzie wykreślenie przepisów mówiących o odpłatności za drugi i kolejny kierunek" - oceniła minister nauki i szkolnictwa wyższego Lena Kolarska-Bobińska, poproszona przez PAP o komentarz po opublikowaniu pisemnego uzasadnienia przez TK.

Projekt nowelizacji Prawa o szkolnictwie wyższym jest w trakcie prac legislacyjnych, drugie czytanie miało się odbyć podczas poprzedniego posiedzenia Sejmu, jednak dyskusję na temat tego projektu przełożono.

"Teraz wszystko w rękach parlamentarzystów. To od nich zależy bowiem, jaki kształt ostatecznie przyjmie nowelizowana ustawa. Mnie zależy jednak bardzo na tym, by przepisy dotyczące odpłatności za drugi kierunek już teraz dostosować do wyroku Trybunału Konstytucyjnego. Chodzi o to, by studenci wraz z nowym rokiem akademickim mieli pewność, jakie są reguły gry" - zaznaczyła szefowa resortu nauki.

Orzeczenie TK nie oznacza, że konieczny będzie powrót do przepisów obowiązujących przed 2011 r. kiedy można było studiować bezpłatnie na dowolnie wielu kierunkach studiów stacjonarnych. TK w swoim uzasadnieniu dopuszcza rozwiązania, które wyeliminowałyby sytuacje "nieodpowiedzialnego korzystania czy też nadużywania prawa do bezpłatnego studiowania". Chodzi np. o sytuację, kiedy student podejmuje studia na wielu kierunkach studiów i studiów tych nie kończy. Zdaniem TK ustawa mogłaby więc np. zawierać zapisy o wyższych wymaganiach wobec studentów, którzy kształcą się na drugim kierunku, a także kierunkach kolejnych. Takie wymagania - zdaniem sędziów TK - nie powinny jednak prowadzić do traktowania studiów na kolejnym kierunku jako nagrody za osiągnięcia.

TK nie wymaga też, by nowe przepisy obowiązywały od nowego roku akademickiego. Obecne przepisy dotyczące opłat (o ile nie zostaną zmienione nową ustawą) mają przestać obowiązywać 30 września 2015 r. W uzasadnieniu TK zaproponowano, by - zanim w życie wejdą nowe przepisy - obowiązująca ustawa interpretowana była "w sposób możliwie najbardziej zbliżony do wymagań stawianych przez ustawę zasadniczą", a więc w znacznej mierze na korzyść studenta.

Obowiązujące aktualnie przepisy zakładają, że prawo do bezpłatnych studiów na drugim kierunku mają tylko te osoby, które uzyskają tam co roku prawo do stypendium rektora (maksymalnie 10 proc. studentów).

Tymczasem po wyroku TK część uczelni – m.in. Uniwersytet Warszawski, Uniwersytet Jagielloński, Uniwersytet Szczeciński czy Uniwersytet Kardynała Stefana Wyszyńskiego w Warszawie - już zdecydowała, że nie będzie pobierać od studentów opłat za drugi kierunek studiów stacjonarnych; część jeszcze się nad takim rozwiązaniem zastanawia.

Ludwika Tomala (PAP)''',
  5:u'''Mleko nie musi być wytwarzane jedynie przez zwierzęta, krowy, kozy czy wielbłądy. Można je wyprodukować w laboratorium, na półkach sklepowych może pojawić się już za trzy lata – zapowiada firma Muufri z San Francisco w wywiadzie dla „Mail Online”.

Biotechnologom z innej amerykańskiej firmy Modern Meadow udało się już wytworzyć, a raczej wydrukować w laboratorium mięso. Posłużyli się drukarką. Pobrali zwierzęce komórki, namnożyli je i wprowadzili do odpowiedniego wkładu drukującego. Powstała w ten sposób sztuczna wołowina. „W przyszłości mięso będzie wytwarzane bez potrzeby hodowania i zabijania zwierząt - zapowiadają przedstawiciele Modern Meadow.

Podobne zamierzenia ma firma Muufri. Zatrudnieni w niej badacze twierdzą, że ustalili już najważniejsze składniki mleka. Zaliczyli do nich sześć białek oraz osiem kwasów tłuszczowych, od których zależą zarówno jego walory odżywcze, jak również smak i zapach.

Specjaliści twierdzą, że te składniki występują we wszystkich odmianach mleka. Są zarówno w mleku krowim, jak i kozim, różne są tylko ich proporcje. Wystarczy zatem odpowiednio je połączyć, żeby uzyskać biały płyn. „Zasady produkcji mleka są takie same jak w przypadku piwa czy leków” – podkreślają przedstawiciele firmy Ryan Pandya, Perumal Gandhi oraz Isha Datar.

Zapewniają oni, że sztuczne mleko będzie się nadawać do produkcji serów, twarogów i innych wyrobów mlecznych. W skali laboratoryjnej będzie wytwarzane już w przyszłym roku. Na półkach sklepowych może się pojawić za trzy lata.

W przyszłości każdy będzie mógł sam wyprodukować mleko. Poza gotowym sztucznym mlekiem w sklepach dostępny będzie zestaw z odpowiednimi składnikami pozwalający wytworzyć mleko w warunkach domowych. Są już jajka i mleko w proszku, niedługo będzie również sztuczne mleko w granulkach. (PAP)''',
  6:u'''Roztwory nikotyny w papierosach elektronicznych podgrzewane do wyższych temperatur dają więcej szkodliwych, rakotwórczych związków – wynika z badań naukowców ze Śląskiego Uniwersytetu Medycznego oraz Instytutu Medycyny Pracy i Zdrowia Środowiskowego.

Chodzi o e-papierosy z możliwością regulacji mocy, w których roztwór nikotyny może być podgrzewany do wyższej temperatury.

Gliceryna i propylen glikolowy to najpowszechniej stosowane w e-papierosach rozpuszczalniki nikotyny. Udowodniono, że wyższe temperatury obu związków powodują ich rozpad do związków karbonylowych, w tym rakotwórczych formaldehydu i acetaldehydu.

Celem badania było ustalenie, jak różne parametry e-papierosów, w tym rodzaj zastosowanego rozpuszczalnika nikotyny i moc baterii, wpływają na poziom związków karbonylowych w aerozolu, wdychanym przez użytkownika e-papierosa.

Badanie objęło 12 związków karbonylowych, mierzonych w aerozolach 10 ogólnie dostępnych roztworów nikotyny i trzech roztworów wzorcowych składających się z czystej gliceryny, czystego propylenu glikolowego oraz mieszaniny obu rozpuszczalników. Moc baterii e-papierosa była stopniowo modyfikowana – od 3,2 wolt do 4,8 wolt.

Obecność formaldehydu i acetaldehydu stwierdzono w 8 z 13 próbek. Najwyższe poziomy związków karbonylowych zaobserwowano w aerozolach na bazie propylenu glikolowego. Podnoszenie mocy baterii od 3,2 V do 4,8 spowodowało od 4- do 200-krotny wzrost poziomów formaldehydu, acetylaldehydu i acetonu w aerozolu wdychanym przez użytkownika e-papierosa.

Choć generalnie były to stężenia niższe niż w dymie z tradycyjnego papierosa, to w jednym przypadku urządzenia o wysokiej mocy poziom formaldehydu był na takim poziomie, jak w przypadku tradycyjnych papierosów.

Badanie potwierdziło, że aerozole z e-papierosów zawierają toksyczne i rakotwórcze związku karbonylowe. Zarówno rodzaj zastosowanego rozpuszczalnika nikotyny, jak i moc baterii znacząco wpływają na zawartość tych związków w aerozolach e-papierosów.

„Ta publikacja odbiła się szerokim echem w środowisku badaczy e-papierosów. To jedna z nielicznych prac wskazujących negatywną stronę papierosów elektronicznych. Wyniki tego badania powinny zwrócić uwagę ich producentów na to, żeby przestali produkować e-papierosy o możliwej regulacji napięcia, a ewentualnych posiadaczy takich urządzeń do tego, żeby nie zwiększali mocy swojego e-papierosa” – powiedział PAP prof. Andrzej Sobczak prowadzący wraz ze współpracownikami badania w Śląskim Uniwersytecie Medycznym w Katowicach oraz w Instytucie Medycyny Pracy i Zdrowia Środowiskowego w Sosnowcu.

Badania przeprowadził międzynarodowy zespół trzech ośrodków – oprócz katowickiego uniwersytetu i sosnowieckiego instytutu uczestniczył w nich także Roswell Park Cancer Institute w Buffalo. (PAP)''',
 7:u'''Pracujący w USA japoński naukowiec potwierdził, że wyhodował w laboratorium wirusa grypy zdolnego uniknąć ataku układu odpornościowego człowieka, co od razu wywołało liczne kontrowersje - informuje AFP.

Eksperyment przeprowadził wirusolog w jednym z ośrodków badawczych University of Wisconsin w Madison. W wypowiedzi dla AFP powiedział on, że udało się tak zmodyfikować jedno z białek wirusa grypy oznaczonego symbolem 2009H1N1, że zarazek ten potrafi oszukać ludzki układ immunologiczny.

Specjalista stwierdził, że w składzie tego drobnoustroju znaleziono miejsca, które na to pozwalają. Jednocześnie skrytykował brytyjski dziennik „Independent”, Yoshihiro Kawaokaktóry wietrzy sensację w jego badaniach. Twierdzi, że ich wymowa została przez to pismo zmanipulowana.

Według Kawaoka głównym celem eksperymentów było jedynie ustalenie, jakim groźnym mutacjom może ulec wirus grypy 2009H1N1, by dzięki temu można było opracować przeciwko temu zarazkowi bardziej skuteczną szczepionkę. Dodał, że wyniki swych badań przedstawił Światowej Organizacji Zdrowia (WHO) i zostały one „dobrze przyjęte”.

Wirus H1N1 błędnie nazywany jest często świńską grypą, tymczasem jest to tylko jedna z jego odmian. Niektóre z nich zaliczane są do tzw. ptasiej grypy.

Kontrowersje wokół tego drobnoustroju są kolejnymi, jakie powstały w ostatnich latach. W 2012 r. pojawiły się podejrzewana, że szczepionka przeciwko szczepowi H1N1 z 2009 r. mogła powodować u dzieci narkolepsję, chorobę powodująca nadmierną senność i napady snu w ciągu dnia.

Prof. Lidia Brydak z Krajowego Ośrodka ds. Grypy powiedziała PAP, że w Polsce nie było tego problemu, ponieważ szczepionka przeciwko grypie z 2009 r. nie była w naszym kraju w ogóle stosowana. Nasze ministerstwo zdrowia nie zdecydowało się wtedy na zakup tego preparatu właśnie z obawy, że nie został on dostatecznie przebadany.

Kontrowersje budzą również prowadzane w laboratorium badaniami nad innymi groźnymi odmianami wirusa grypy. W 2011 r. niezależnie od siebie dwie grupy uczonych holenderskich oraz amerykańsko-japońska oznajmiły, że wyhodowały w laboratorium szczep wirusa H5N1, który może wywołać pandemię grypy.

Mutant ten jest jedną z odmian tzw. ptasiej grypy, którą wcześniej można było się zarazić, ale wyłącznie bezpośrednio od zarażonych ptaków (po głębokim wdechu zawierającym cząsteczki zarazka, które dostały się do płuc). Tymczasem zmodyfikowany szczep H5N1 teoretycznie może się przenosić między ludźmi, co przetestowano na tchórzofretkach (gdy wirus potrafi zaatakować te zwierzęta, to jest duże ryzyko, że może przenosić się również na ludzi – przyp. PAP).

Jesienią 2011 r. Narodowy Naukowy Komitet Doradczy ds. Biobezpieczeństwa (NSABB) w USA sprzeciwiał się publikacji szczegółów badań na ten temat. Obawiano się, że wyniki eksperymentów mogą wykorzystać bioterroryści do własnych prac nad wyhodowaniem groźnego zarazka.

Potem badacze sami ogłosili moratorium na prowadzenie eksperymentów, by zmniejszyć ryzyko ewentualnego wydostania się z laboratoriów groźnego wirusa ptasiej grypy. Jednak w 2012 r. postanowili opublikować wyniki swych badań, po upewnieniu się, że „dane nie dostarczają informacji umożliwiających wykorzystanie ich w złych intencjach (...), co mogłoby narazić na niebezpieczeństwo zdrowie publiczne i bezpieczeństwo narodowe”. (PAP)''',
  8:u'''Sześć młodych sokołów wędrownych zamieszkało w sztucznym gnieździe na terenie nadleśnictwa Żmigród. Dzięki temu jest szansa, że te bardzo rzadkie ptaki zadomowią się w dolnośląskich lasach – powiedział PAP Robert Borkacki z WFOŚiGW we Wrocławiu.

Borkacki dodał, że sokoły przewiezione do nadleśnictwa Żmigród pozostaną zamknięte w gnieździe przez około 10 dni. Służy to przyzwyczajeniu ich do tego miejsca. „Po osiągnięciu dojrzałości, w wieku około 2-3 lat, założą własne gniazda w okolicznych lasach. Uznają je bowiem za teren swojego urodzenia” – wyjaśnił.

W naturze sokoły nie budują samodzielnie gniazd, lecz zajmują siedziby innych dużych ptaków, np. orła albo bociana. Sztuczne gniazda zostaną otwarte, gdy ptaki będą gotowe do pierwszego lotu. Potem jeszcze przez co najmniej miesiąc będą dokarmiane.

Sokół to jeden z najrzadszych gatunków w Polsce. Jego nadrzewna populacja europejska całkowicie wyginęła w latach 60. Przyczyniło się do tego m.in. zatrucie środowiska szkodliwą chemią. Pestycyd DDT wchłaniany do organizmów ptaków wraz z pokarmem powodował, że sokoły zaczęły składać jaja o zbyt cienkiej skorupce. A ta pękała pod ciężarem wysiadującej samicy. Populacja drapieżników w dramatycznym tempie zaczęła spadać.

„W Polsce, dzięki zaangażowaniu sokolników, stwierdzono około 20 gniazd sokoła wędrownego. Na Dolnym Śląsku jest tylko jedna gniazdująca para – w Głogowie” – twierdzi Borkacki.

Ogólnopolskie działania Stowarzyszenia na Rzecz Dzikich Zwierząt "Sokół" są prowadzone na terenie całego kraju i wspierane w ramach Programu Operacyjnego Infrastruktura i Środowisko oraz ze środków Narodowego Funduszu Ochrony Środowiska. Wartość projektu realizowanego na Dolnym Śląsku to ponad 81 tys. zł, z czego dotacja Wojewódzkiego Funduszu Ochrony Środowiska i Gospodarki Wodnej we Wrocławiu to 48 tys. zł. (PAP)''',
  9:u'''Fani muzyki heavymetalowej lubią w rym muzyki „trzepać piórami”, czyli energicznie potrząsać głową, co dla niektórych osób może się skończyć uszkodzeniem mózgu – ostrzega „Lancet”.

Pismo przyznaje, że ryzyko „trzepania piórami” jest małe, ale „metalowcy” powinni zdawać sobie sprawę z zagrożenia. Na koncertach energicznie potrząsają głową rytmicznie odrzucając włosy z góry na dół, na boki lub po okręgu. Już wcześniej sygnalizowano, że może to doprowadzić do urazów karku, wstrząśnienia mózgu albo bólów i zawrotów głowy.

„Lancet” przytacza przykład 50-letniego mężczyzny, którego z silnymi bólami głowy w styczniu 2014 r. przywieziono do szpitala uniwersyteckiego w Hanowerze (Niemcy). Nie miał wcześniej żadnych uszkodzeń mózgu, zapewniał również, że nie nadużywał substancji psychoaktywnych. Przyznał jedynie, że od wielu lat jest fanem muzyki heavymetalowej. Ostatnio z synem był na koncercie brytyjskiego zespołu Motorhead, podczas którego jak zwykle „trzepał piórami”. I to była przyczyna jego nieszczęścia.

Wykonane w szpitalu obrazowanie mózgu wykazało, że powstał w nim krwiak w postaci płynnej. Aby go usunąć, trzeba było przeprowadzić trepanację czaszki polegającą na wykonaniu otworu odsłaniającego opony mózgowo-rdzeniowe oraz mózg. Zabieg się powiódł, a bóle głowy ustąpiły.

Mężczyzna był nadal diagnozowany. Kolejne badania obrazowe ujawniły, że miał w mózgu cystę, która pękła i doszło do krwawienia. Prawdopodobnie zdarzyło się to właśnie wtedy, gdy potrząsał głową na koncercie.

Jeden lekarzy, którzy go leczyli, dr Ariyan Pirayesh Islamian zastrzega się, że nie jest przeciwnikiem rytuału potrząsani głową przez fanów heavy metalu. Ryzyko uszkodzenia mózgu z tego powodu na ogół jest niewielkie. "Gdyby jednak pacjent uczęszczał wyłącznie na koncerty muzyki klasycznej, raczej by do tego nie doszło” – twierdzi niemiecki neurochirurg.

Energiczne potrząsanie głową powoduje, że mózg zostaje wprawiony w ruchu i uderza w otaczające go opony. Mają one chronić go przed uszkodzeniami mechanicznymi, podobnie jak znajdujący się między nimi płyn mózgowo-rdzeniowy ma amortyzować jego ruchy.

Silne potrząsanie głową powoduje jednak, że te zabezpieczenia nie są wystarczające. Mózg może być wtedy narażony na uszkodzenia. Zdarza się to u niektórych sportowców, a szczególnie u bokserów narażonych na silne ciosy w głowę. Urazy mózgu mogą powstać również u małych dzieci, które są potrząsane.

Gwałtowne potrząsania, a tym bardziej uderzanie w głowę niemowlęcia lub małego dziecka, może wywołać tzw. zespół dziecka potrząsanego (SBS). Trzeba uważać, bo nawet podczas zabawy z dzieckiem, polegającej na podrzucania, lub podczas intensywnego kołysania, można nieświadomie wyrządzić mu krzywdę. (PAP)''',
 10:u'''Prezydent Ukrainy Petro Poroszenko powiedział we wtorek, że dobrze by było, gdyby do rozmów na temat uregulowania sytuacji na wschodzie kraju, w których już uczestniczą Francja i Niemcy, przyłączyły się Wielka Brytania i Włochy.

Poroszenko, który tego dnia rozmawiał w Kijowie z szefową włoskiej dyplomacji Federicą Mogherini, wysoko ocenił wysiłki Niemiec i Francji, co - przy udziale Rosji - pozwoliło utworzyć tzw. normandzką czwórkę, i wyraził przekonanie, że międzynarodowe oddziaływanie mogłoby być znacznie silniejsze, gdyby do Niemiec i Francji dołączyły Włochy i Wielka Brytania - powiadomiła prezydencka służba prasowa.

Na początku czerwca w Normandii, na marginesie uroczystości związanych z 70. rocznicą lądowania wojsk alianckich, doszło do szeregu spotkań z udziałem prezydentów Rosji, Francji, Niemiec i Ukrainy, którzy omawiali m.in. sytuację na wschodniej Ukrainie.

Poroszenko omówił z szefową włoskiej dyplomacji perspektywy zagranicznej pomocy, tym Włoch, w odbudowie infrastruktury Donbasu (Donieckiego Zagłębia Węglowego) po uwolnieniu go od rebeliantów.

Minister Mongherini oświadczyła, że rząd Włoch popiera starania władz ukraińskich o uregulowanie kryzysu na wschodzie kraju. "Popieramy pański plan pokojowy" - powiedziała Mogherini.

Szefowa włoskiej dyplomacji zapowiedziała, że podczas wizyty w Moskwie, dokąd wybiera się jeszcze we wtorek, zamierza rozmawiać nie tylko o Ukrainie, lecz i o stosunkach UE z Rosją. Włochy od 1 lipca przewodniczą Radzie UE. (PAP)
 ''',
 11:u'''Siły ukraińskie przystąpiły do blokady Doniecka i Ługańska, zaciskając tam pętlę wokół prorosyjskich separatystów. Wtorkowy "Financial Times" pisze, że korzystają one z pomocy amerykańskiej m.in. w sprawach wywiadowczych.

Według "FT" Stany Zjednoczone dostarczają siłom rządowym Ukrainy pomoc wartą miliony dolarów - racje żywnościowe, noktowizory, kamizelki kuloodporne. Przedstawiciele władz ukraińskich mówią, że USA dostarczają też żywotnie ważnych informacji wywiadowczych i doradzają w sprawach strategii - wskazuje londyński dziennik.

Ukraińskie siły rządowe zajęły w ciągu weekendu kontrolowane od kwietnia przez separatystów miasta w obwodzie donieckim: Słowiańsk, Kramatorsk, Drużkiwkę, Artiomowsk i Konstantynówkę. Po wycofaniu się do Doniecka rebelianci zapowiadają przegrupowanie i dalszy opór. Kijów podkreśla, że blokada ma ich zmusić do złożenia broni.

"FT" odnotowuje, że ofensywę przeciwko separatystom prowadzą teraz żołnierze zreorganizowanych elitarnych jednostek i funkcjonariusze sił bezpieczeństwa wyposażeni w podstawowy sprzęt bojowy.

Gazeta zwraca uwagę na "znaczące czynniki ryzyka" w przypadku blokady Doniecka i Ługańska. Pisze, że taktyka, zastosowana do wyparcia separatystów ze Słowiańska, gdzie odcięto dostawy wody i energii elektrycznej, a mieszkańcy byli narażeni na tygodnie ostrzału artyleryjskiego, byłaby jeszcze bardziej niebezpieczna w większych miastach. Wskazuje, że walki uliczne mogłyby spowodować gwałtowny wzrost liczby ofiar w tym konflikcie, który kosztował już życie setek żołnierzy, rebeliantów i cywilów i zmusił dziesiątki tysięcy ludzi do ucieczki przed walkami.

"FT" pisze też, że wprawdzie Moskwa "pozostaje dziwnie milcząca" w kwestii weekendowych wydarzeń na wschodzie Ukrainy, ale w Kijowie utrzymują się obawy, że rozlew krwi w Doniecku mógłby zostać wykorzystany przez Rosję jako pretekst do wznowienia wsparcia dla rebeliantów, które - jak się wydaje - osłabło w ostatnich tygodniach, albo jako pretekst do bezpośredniej rosyjskiej interwencji wojskowej. (PAP)''',
 12:u'''Były szef dyplomacji Afganistanu Abdullah Abdullah, który ubiegał się o urząd prezydenta, oświadczył we wtorek, przemawiając do tysięcy swoich zwolenników w Kabulu, że to on jest zwycięzcą drugiej tury wyborów prezydenckich.

Dzień wcześniej Niezależna Komisja Wyborcza poinformowała, powołując się na wstępne wyniki, że wybory prezydenckie wygrał były minister finansów Aszraf Ghani. Abdullah natychmiast odrzucił te wyniki; już wcześniej oskarżał komisję o fałszerstwa przy liczeniu głosów.

We wtorek Abdullah ujawnił, że kiedy odmówił zaakceptowania wstępnych wyników, zatelefonowali do niego prezydent USA Barack Obama i szef amerykańskiej dyplomacji John Kerry. Powiedział, że Kerry w najbliższy piątek przyleci do Afganistanu na spotkania, mające zażegnać kryzys.

Przedstawiciele Departamentu Stanu USA, towarzyszący Kerry'emu w Pekinie, odmówili wypowiedzi na ten temat.

Kerry ostrzegł we wtorek, że jakakolwiek próba siłowego przejęcia władzy w Afganistanie, po ogłoszeniu wyników drugiej tury wyborów prezydenckich, spotka się z natychmiastową reakcją Waszyngtonu i cofnięciem poparcia USA.

"Potraktowałem śmiertelnie poważnie informacje o protestach w Afganistanie i o możliwości powstania +władzy równoległej+. (...) Jakiekolwiek działania wykraczające poza prawo, a prowadzące do przejęcia władzy będą kosztować Afgańczyków utratę pomocy finansowej i wsparcia w dziedzinie bezpieczeństwa udzielanego przez Stany Zjednoczone i społeczność międzynarodową" - zapowiedział Kerry w oświadczeniu opublikowanym przez ambasadę USA w Kabulu. (PAP)''',
 13:u'''Obchody 20. rocznicy śmierci założyciela komunistycznej Korei Północnej Kim Ir Sena rozpoczęły się we wtorek od hołdu złożonego mu przez wnuka, obecnego przywódcę Kim Dzong Una. Media zwracają uwagę, że podczas uroczystości 31-letni lider utykał.

Młody przywódca udał się rano do rodzinnego mauzoleum, Pałacu Kumsusan w Pjongjangu, gdzie spoczywa Kim Ir Sen, zwany Wiecznym Prezydentem. Kim Dzong Un złożył też hołd swojemu ojcu, zmarłemu w 2011 roku Kim Dzong Ilowi, którego zabalsamowane ciało znajduje się w pałacu, kilka poziomów pod mumią założyciela Korei Północnej. Następnie przeszedł się po pozostałych salach, w których wyeksponowane są relikwie pozostałych przodków komunistycznej dynastii.

Na zdjęciach telewizyjnych widać, jak Kim Dzong Un, witany oklaskami przez setki wysokich rangą członków Partii Pracy Korei, wchodzi do sali, utykając. Wyemitowanie takich zdjęć jest nietypowe, gdyż reżim ma w zwyczaju ukrywanie wad fizycznych dynastii Kimów i przedstawia liderów jak półbogów - pisze Reuters. Przypomina, że Kim Ir Sen z tyłu szyi miał nieoperacyjną narośl wielkości piłki tenisowej, w związku z czym państwowe media mogły go filmować tylko pod określonym kątem.

Na razie nie ma oficjalnych informacji o tym, że Kim Dzong Il jest w złej formie. Agencja EFE pisze jednak, że w ostatnich miesiącach często spekulowano na temat zdrowia młodego przywódcy, który cierpi na nadwagę i jest nałogowym palaczem.

Nie jest wykluczone, że chodzi o chwilową kontuzję, gdyż Kim w ostatnich tygodniach prowadził ćwiczenia wojskowe na obszarach wiejskich.

Urodzony w 1912 r. Kim Ir Sen założył Koreańską Republikę Ludowo-Demokratyczną w 1948 r. i stał na jej czele do śmierci w 1994 r. 20 lat później w Korei Północnej nadal panuje jego kult. Pomniki Kim Ir Sena znajdują się w całym kraju, a jego nauki są wszechobecne w kontrolowanych przez państwo mediach.

We wszystkich domach i urzędach muszą wisieć obrazy przedstawiające Kim Ir Sena i Kim Dzong Ila. Obywatele noszą też przypinki z ich podobiznami.(PAP)''',
 14:u'''Jednostronnego zawieszenia broni przez ukraińskie oddziały uczestniczące w operacji zbrojnej sił rządowych przeciwko prorosyjskim separatystom więcej nie będzie - zapowiedział cytowany przez Interfax-Ukraina minister obrony Ukrainy Wałerij Hełetej.

"Prezydent Ukrainy powiedział to jednoznacznie. Obecnie wszelkie rozmowy są możliwe wyłącznie po ostatecznym złożeniu broni przez bojowników" - oświadczył dziennikarzom w strefie operacji na wschodzie kraju. Wypowiedź ministra przytoczył jego resort.

Kijów ogłosił zawieszenie broni 20 czerwca, później przedłużył je do 30 czerwca, by dać szanse separatystom na złożenie broni. Rozejm był regularnie naruszany, a rebelianci broni nie złożyli. Prezydent Petro Poroszenko podjął decyzję o wznowieniu operacji przeciw separatystom na wschodzie kraju.

Minister Hełetej powiedział, że wiele dróg w regionie, w tym trasa Słowiańsk-Krematorsk, Słowiańsk-Artiomowsk zostały zaminowane przez nielegalne ugrupowania zbrojne.

"Niemało niewybuchów - min i pocisków - leży po prostu na poboczu i na samej drodze. (...) Podejmujemy wysiłki dla maksymalnego przyspieszenia rozminowania, unieszkodliwiania min i innych ładunków wybuchowych" - powiedział minister obrony.(PAP)''',
 15:u'''Laseczkę wąglika (Bacillus anthracis) stwierdzono w wołowinie w powiecie Heves na wschodzie Węgier. Jedna osoba z objawami choroby została poddana terapii - poinformowała w poniedziałek wieczorem służba weterynaryjna. To kolejny przypadek wąglika w tym kraju.

Tym razem bakterie powodujące tę chorobę znajdowały się w mięsie z uboju gospodarczego. W zeszłym tygodniu laseczkę wąglika stwierdzono w nieprawidłowo zamrożonym mięsie z dwóch krów, nielegalnie ubitych w gospodarstwie w miejscowości Tiszafuered, ok. 160 km na wschód od Budapesztu.

Według służby weterynaryjnej nie ma związku między tymi przypadkami.

Wąglik to groźna, zwykle śmiertelna choroba zakaźna zwierząt domowych. Przenosi się na człowieka i może doprowadzić do zakażeń skóry, przewodu pokarmowego i płuc, a następnie śmierci.

Bakterie wąglika mogą być wykorzystane jako broń biologiczna i są uważane za jedno z najpoważniejszych zagrożeń bioterrorystycznych.(PAP)''',
 16:u'''Barack Obama i Francois Hollande zaapelowali do prezydenta Rosji Władimira Putina, by nakłonił prorosyjskich separatystów do podjęcia dialogu z władzami Ukrainy - poinformował w poniedziałek wieczorem Pałac Elizejski po rozmowie telefonicznej prezydentów USA i Francji.

Prezydenci USA i Francji, jak wynika z komunikatu Pałacu Elizejskiego, chcą, by jak najszybciej doszło do spotkania grupy kontaktowej ds. konfliktu ukraińskiego z przedstawicielami separatystów, którego najważniejszym celem będzie wynegocjowanie trwałego zawieszenia broni na wschodzie Ukrainy.

Grupa składa się z delegacji władz Rosji i Ukrainy oraz mediatorów z OBWE.

Obama i Hollande podkreślili, że "trwałe rozwiązanie kryzysu na Ukrainie może być tylko polityczne". Biały Dom poinformował, że prezydenci USA i Francji byli zgodni, że Rosja powinna zaprzestać "działań destabilizacyjnych" sytuację na wschodzie Ukrainy, w tym umożliwianie przerzutu broni i ludzi przez granicę.

Zagrozili Rosji kolejnymi sankcjami, jeśli Moskwa nie zmieni swej polityki. (PAP)''',
 17:u'''Tajfun Neoguri dotarł do wysp japońskiej prefektury Okinawa na południowym zachodzie kraju zmuszając władze do ewakuacji ponad 500 tys. osób. Służby ostrzegają przed powodziami i porywistym wiatrem, którego prędkość będzie dochodzić do 250 km/h.

Na terenie prefektury Okinawa obowiązują ostrzeżenia przed intensywnymi opadami deszczu i wysokimi falami, które w konsekwencji mogą prowadzić do powodzi. Władze w Tokio apelują do mieszkańców o zachowanie najwyższej ostrożności.

W związku z silnymi wiatrami na Okinawie ponad 50 tysięcy domów zostało pozbawionych energii elektrycznej. Wstrzymano też prace w rafinerii znajdującej się na wyspie. Służby meteorologiczne przewidują, że tajfun będzie przemieszczał się na północ, a następnie skręci na wschód w kierunku Morza Wschodniochińskiego. W czwartek Neoguri ma uderzyć w wybrzeże wyspy Kiusiu, trzeciej pod względem wielkości wyspy Japonii. Znajdują się tam dwie elektrownie nuklearne, które zostały już wyłączone.

Meteorolodzy przewidują, że tajfun może dotrzeć też na największą wyspę Honsiu, gdzie znajduje się Tokio. Jednak do piątku siła wiatru ma zmaleć, dlatego w stolicy spodziewane są tylko intensywne opady deszczu. (PAP)''',
 18:u'''Izraelskie lotnictwo przeprowadziło w nocy z poniedziałku na wtorek dziesiątki ataków na cele w Strefie Gazy, m.in. na domy bojowników Hamasu. Według rzecznika izraelskiej armii to początek operacji wojskowej przeciwko temu radykalnemu ugrupowaniu.

Rzecznik napisał na Twitterze, że celem operacji lotniczej "Protective Edge" jest położenie kresu terrorowi wobec Izraelczyków. W ostatnich dniach Hamas nasilił bowiem ataki rakietowe na Izrael, a w poniedziałek wieczorem wystrzelił około 60 pocisków.

Według źródeł palestyńskich, izraelskie samoloty zaatakowały i zniszczyły m.in. trzy domy bojowników Hamasu w południowej części Strefy Gazy. Wcześniej jednak izraelska armia ostrzegła przed atakami mieszkające tam rodziny.

Przedstawiciel zbrojnego skrzydła Hamasu ostrzegł Izrael przed kolejnymi nalotami na domy bojowników. "Zareagujemy ma nie niespodziewaną eskalacją naszych ataków" - napisał na Twitterze.

Służby medyczne w Strefie Gazy poinformowały, że w atakach izraelskiego lotnictwa przeprowadzonych w nocy z poniedziałku na wtorek rannych zostało 12 Palestyńczyków.

Napięcie między stronami wzrosło od zabicia w Jerozolimie Wschodniej 16-letniego Palestyńczyka w odwecie za śmierć trzech izraelskich nastolatków, o których zamordowanie władze Izraela oskarżyły dwóch członków Hamasu, Palestyńczyków z Hebronu na Zachodnim Brzegu Jordanu. Hamas zaprzeczył, jakoby miał jakikolwiek związek z tą zbrodnią. (PAP)''',
 19:u'''Francja respektuje swe zobowiązania wobec UE dotyczące redukcji deficytu budżetowego, ale ze względu na reformy, które wprowadza, jej deficyt budżetowy powinien być traktowany "elastycznie" przez UE - powiedział w poniedziałek prezydent Francois Hollande.

"W kwestii budżetu każdy kraj, również Francja, muszą respektować swoje zobowiązania" zważywszy jednak na to, że Paryż wdraża już ważne reformy, proces równoważenia budżetu powinien być traktowany z pewną tolerancją - powiedział prezydent w pierwszym dniu dwudniowej konferencji poświęconej konsultacjom społecznym dotyczącym reform rynku pracy.

Wobec planowanych przez rząd reform dwa związki zawodowe: FO i największy francuski związek CGT ogłosiły w poniedziałek, że nie wezmą udziały w drugim dniu konferencji.

Związki zawodowe sprzeciwiają się od początku tzw. paktowi odpowiedzialności, czyli pakietowi reform gospodarczych, które forsuje rząd. Od jego ogłoszenia francuska lewica oskarża Hollande'a o skręt na prawo i forsowanie przez socjalistyczny rząd polityki "socjaldemokratycznej".

Pakt odpowiedzialności zakłada udzielenie przedsiębiorstwom pomocy finansowej rzędu 40 mld euro w zamian za utworzenie przez nie do roku 2017 pół miliona nowych miejsc pracy.

W kwietniu Zgromadzenie Narodowe, izba niższa parlamentu, zatwierdziło program oszczędności w wydatkach publicznych na 50 mld euro. Podczas głosowania ujawniły się głębokie podziały w rządzącej Partii Socjalistycznej.

Przyjęty plan przewiduje, że w latach 2015-2017 państwo zaoszczędzi 18 mld euro, samorządy regionalne - 11 mld euro, a 21 mld euro zostanie zaoszczędzone na osłonach społecznych. Dzięki temu deficyt budżetowy Francji ma zejść do wymaganego w UE poziomu 3 proc. PKB.

Program obejmuje również zamrożenie na rok emerytur i świadczeń socjalnych oraz zamrożenie wynagrodzeń większości pracowników administracji państwowej do 2017 r. Zamrożenie świadczeń socjalnych nie obejmie najbiedniejszych i emerytów o miesięcznych dochodach nieprzekraczających 1200 euro.

Dzięki programowi naprawczemu francuskiej gospodarki Komisja Europejska dała Francji dodatkowe dwa lata na zejście z deficytem do akceptowanego poziomu.(PAP)''',
 20:u'''Selekcjoner piłkarskiej reprezentacji Niemiec Joachim Loew przyznał przed półfinałowym meczem mistrzostw świata z Brazylią w Belo Horizonte, że jego zespół "na pewno nie jest faworytem". Początek wtorkowego spotkania o godz. 22 czasu polskiego.

Trener trzeciej drużyny poprzedniego mundialu podkreślił, że najbliższe starcie z Brazylią będzie jednym z największych wyzwań w karierze jego podopiecznych. Wprawdzie przyznał, iż piłkarze kadry Niemiec mają więcej doświadczenia niż "Canarinhos", ale jak dodał, każde spotkanie jest inne, a starcie z Brazylią to zawsze wielkie wydarzenie.

Loew nie zgadza się z opinią, że jego podopieczni mają największe szanse, aby 13 lipca sięgnąć po końcowe trofeum.

"Na pewno nie jesteśmy faworytami turnieju" - zastrzegł.

Jego zdaniem, absencja w ekipie Brazylii dwóch czołowych piłkarzy nie musi wpłynąć na wynik rywalizacji.

"Brak Neymara i Thiago Silvy (pierwszy leczy kontuzję, drugi pauzuje za kartki - PAP) może teraz daje nam przewagę, ale Brazylijczycy się nie poddadzą. Czasami absencja ważnych zawodników sprawia, że pozostali dają z siebie wszystko co najlepsze i walczą dla zespołu" - podkreślił Loew.

Niemiecki selekcjoner nie ukrywa obaw wynikających z ostrej gry w meczu 1/4 finału Brazylii z Kolumbią (2:1). Jak zaznaczył, walka z obu stron była "brutalna i prawie na granicy". Teraz zaapelował do sędziego, aby we wtorek zwracał na to uwagę.

"Mam nadzieję, że sędzia Marco Rodriguez będzie miał na oko na te sprawy" - podkreślił Loew.

Trener Niemców przyznał, że najbliższe spotkania zapowiadają się bardzo emocjonująco.

"Oba półfinały będą wielkimi wydarzeniami, walką dwóch kontynentów. Dwie drużyny z Europy przeciwko dwóm zespołom z Ameryki Południowej" - zaznaczył.

W środowym półfinale, również o godz. 22 czasu polskiego, Holandia zmierzy się w Sao Paulo z Argentyną. (PAP)''',
 21:u'''Występujący ostatnio w hiszpańskiej Maladze Willy Caballero podpisał trzyletni kontrakt z piłkarskim mistrzem Anglii Manchesterem City. 32-letni Argentyńczyk ma być konkurentem dla bramkarza reprezentacji Anglii Joe'a Harta.

Pozyskanie Caballero związane jest z odejściem do Sunderlandu Rumuna Costela Pantilimona, który pełnił rolę rezerwowego. Nowy zawodnik "The Citizens" nie zamierza jednak pogodzić się z taką rolą.

"Nowa liga jest dla mnie nowym wyzwaniem. W poprzednich latach podejmowałem dobre decyzje i teraz również moim celem jest wzniesienie się na wyższy poziom. Zdaję sobie sprawę, że idę do klubu, gdzie jest znakomity bramkarz. Jednak spróbuję powalczyć z nim o miejsce w podstawowym składzie" - powiedział Argentyńczyk cytowany przez oficjalną stronę klubu.

Szkoleniowiec Manchesteru City Manuel Pellegrini w 2011 roku prowadząc Malagę, pozyskał Caballero z Elche.

"Najpiękniejsze chwile w mojej karierze spędziłem pod opieką Pellegriniego w Maladze, kiedy osiągaliśmy świetne wyniki i wypromowaliśmy klub w całej Europie" - dodał Caballero.

Kwota transferu nie została ujawniona, ale według mediów Argentyńczyk kosztował mistrzów Anglii około sześciu milionów funtów.

Wcześniej Manchester City pozyskał z Arsenalu Londyn francuskiego prawego obrońcę Bacary'ego Sagnę oraz brazylijskiego defensywnego pomocnika FC Porto - Fernando. (PAP)''',
 22:u'''W potencjalnie najmocniejszych składach oraz z nowymi piłkarzami Legia i Zawisza Bydgoszcz w środę (godz. 19) w Warszawie będą walczyły o Superpuchar Polski. Mecz o to trofeum wraca po rocznej przerwie.

Zawisza zdobywając w poprzednim sezonie Puchar Polski odniósł największy sukces w historii klubu. Do tego osiągnięcia zespół poprowadził Ryszard Tarasiewicz, który po zakończeniu sezonu nie doszedł do porozumienia z właścicielem klubu Radosławem Osuchem i nie przedłużył kontraktu.

Dlatego w środę w oficjalnym meczu jako trener Zawiszy zadebiutuje Portugalczyk Jorge Paixao. To nie jedyny debiut w bydgoskim zespole, bo w bramce stanie Grzegorz Sandomierski, który zastąpi kontuzjowanego Wojciecha Kaczmarka. W podstawowym składzie mogą znaleźć się także obrońca, rodak szkoleniowca Joshua Silva oraz Brazylijczycy Wagner i Samuel de Araujo Miranda. Ten ostatni podpisał kontrakt w poniedziałek i jeśli pojawi się na boisku, to raczej jako rezerwowy.

Z kolei dla Legii znacznie ważniejsze spotkanie odbędzie się tydzień później, kiedy rozpocznie zmagania w drugiej rundzie kwalifikacji Ligi Mistrzów. Na własnym stadionie podejmie mistrza Irlandii - St. Patrick's Athletic.

"O Superpuchar zagrają piłkarze pierwszej drużyny. Dla tych młodych będzie to świetna okazja na oswojenie się z meczami o stawkę. Nikt nie powinien mówić, że pierwsza jedenastka Legii jest słabsza niż druga. Przypominam końcówkę ostatniego sezonu, kiedy zupełnie inne jedenastki pokonały najpierw Pogoń, a potem Lecha" - podkreślił trener "Wojskowych" Henning Berg w trakcie poniedziałkowej konferencji prasowej.

Trudno przypuszczać, aby Norweg przeciwko Zawiszy wystawił wszystkich swoich najlepszych graczy. We wtorkowy wieczór stołeczny zespół zagra bowiem sparing z Hapoelem Beer Sheva (godz. 20.45). W sobotę Zawisza przegrał z wicemistrzem Izraela 0:1 w swoim ostatnim sparingu w trakcie letnich przygotowań.

Zarówno we wtorek, jak i środę nie zagra Ondrej Duda. Słowak leczy kontuzję stawu skokowego i do treningów wróci w ciągu tygodnia. Szansę na debiut w drużynie "Wojskowych" prawdopodobnie otrzymają m.in. występujący poprzednio w KGHM Zagłębiu Lubin Arkadiusz Piech i Bartłomiej Kalinkowski, który został przesunięty z drugiej drużyny. Spotkanie może być wyjątkowe natomiast dla obrońcy Igora Lewczuka, który w poprzednim sezonie reprezentował barwy bydgoskiego klubu.

W meczu o Superpuchar rywalizuje mistrz kraju (Legia) i zdobywca Pucharu Polski (Zawisza). Zgodnie z decyzją podjętą przez PZPN na majowym zjeździe, spotkanie to stanowi oficjalną inaugurację sezonu i jest rozgrywane na boisku mistrza Polski. Początek w środę 9 lipca o godz. 19 na stadionie przy ul. Łazienkowskiej. Sędziować będzie Bartosz Frankowski. (PAP)
 ''',
 23:u'''Słynny portugalski trener pracujący obecnie w Chelsea Londyn Jose Mourinho stawia na zwycięstwo Brazylii w piłkarskich mistrzostwach świata. "Gospodarze grają z wielkim zaangażowaniem, walczą +z sercem+ i mają ogromną motywację" - uzasadnił.

51-letni Mourinho uważa, że "Canarinhos" to dobrze zmotywowana drużyna, która gra o zwycięstwo nie tylko dla siebie, ale dla wszystkich mieszkańców Brazylii.

"Siłą Brazylii jest nie tylko gra oparta na umiejętnościach poszczególnych graczy, ale stworzenie zmotywowanego zespołu, który ma przed sobą jeden cel: odniesienie sukcesu jako gospodarz turnieju" - dodał Portugalczyk uznany przez FIFA w 2010 roku najlepszym szkoleniowcem świata.

Jego zdaniem większą stratą dla Brazylijczyków jest nieobecność we wtorkowym półfinale z Niemcami obrońcy i kapitana Thiago Silvy niż napastnika Neymara.

Ten pierwszy będzie pauzował z powodu żółtych kartek; pierwszą został ukarany w meczu z Meksykiem, a drugą w spotkaniu ćwierćfinałowym z Kolumbią. Brazylijska federacja wnioskowała o uchylenie zawieszenia, aby 29-letni obrońca mógł pojawić się na boisku we wtorkowym półfinale z Niemcami. FIFA jednak do prośby się nie przychyliła, argumentując, że nie ma prawnych podstaw. Neymara wykluczyła kontuzja kręgosłupa, której doznał po starciu z Kolumbijczykiem Juanem Camilo Zunigą.

"Thiago Silva jest w tym momencie ważniejszy dla zespołu niż Neymar, więc jego nieobecność to podstawowy problem zespołu, który był do tej pory bardziej zorientowany na grę defensywną niż ofensywną. W obronie to właśnie na Silvie spoczywał największy ciężar, to on miał najwięcej zdań" - ocenił Portugalczyk, który jest nie tylko znakomitym fachowcem, ale i jedną z najbardziej kontrowersyjnych postaci sportu. Często krytykuje pracę sędziów, nie waha się także niepochlebnie wypowiadać o piłkarzach i trenerach rywali.(PAP)
 ''',
 24:u'''Kontuzja gwiazdy Brazylii Neymara, która wyklucza go z udziału w dwóch ostatnich meczach piłkarskiego mundialu, wpłynęła na zmianę notowań u bukmacherów. Obecnie faworytem mistrzostw świata jest Argentyna, a nie jak do tej pory Brazylia.

Najmniej szans na zdobycie pucharu bukmacherzy dają Holendrom, wicemistrzom świata z 2010 roku.

Przy zwycięstwie Argentyny za jedno euro, dolara bądź funta będzie można zarobić od 3,3 do 3,75, zaś w przypadku wygranej "Pomarańczowych" od 4,33 do 4,6.

Tylko jedna firma William Hill, założona w 1934 r., daje równe szanse Argentynie, Brazylii i Niemcom (po 3,5), zaś za najsłabszą ekipę uważa Holandię (4,33), która w pierwszym swoim spotkaniu na mundialu pokonała obrońcę tytułu Hiszpanię 5:1.

W półfinałach spotkają się we wtorek w Belo Horizonte Niemcy z Brazylią i w środę w Sao Paulo Argentyna z Holandią. (PAP)''',
 25:u'''Piłkarze Brazylii i Niemiec zagrają we wtorek o awans do finału mistrzostw świata. Będzie to dopiero ich drugi pojedynek podczas mundialu, choć są to dwie najbardziej utytułowane drużyny. Początek meczu w Belo Horizonte o godz. 22 czasu polskiego.

Brazylijczycy mają w dorobku pięć tytułów, Niemcy - trzy. Pierwsi rozegrali 102 mecze w mistrzostwach świata, drudzy - 104. Do ich jedynego spotkania w najważniejszym turnieju doszło 30 czerwca 2002 roku w Jokohamie. Był to finał MŚ, a zwyciężyli "Canarinhos" 2:0 po dwóch golach Ronaldo.

Po 12 latach od tamtego meczu koszulkę reprezentacyjną wciąż zakłada tylko urodzony w Opolu niemiecki napastnik Miroslav Klose. Jego ówczesny zmiennik Oliver Bierhoff jest obecnie dyrektorem kadry narodowej. Tak jak w Azji, funkcję selekcjonera drużyny narodowej Brazylii pełni Luiz Felipe Scolari, ale wrócił na stanowisko po dłuższej przerwie.

Bilans bezpośrednich meczów jest korzystny dla gospodarzy mundialu: 12 zwycięstw, pięć remisów i cztery porażki. W ostatnim spotkaniu, rozegranym w sierpniu 2011 roku w Stuttgarcie, zwyciężyli jednak Niemcy 3:2.

Przed wtorkowym półfinałem roi się od rozmaitych statystyk. Niemcy po raz siódmy zagrają z gospodarzem MŚ, a do tej pory pokonali czterech. Jeśli strzelą gola, będzie to ich bramka nr 2000 na arenie międzynarodowej (w 890 dotychczasowych meczach stracili ledwie 1058).

Jeśli na listę strzelców wpisze się Klose, to samodzielnie będzie prowadził na liście snajperów MŚ. Do tej pory dzieli pierwsze miejsce z Brazylijczykiem Ronaldo - po 15 goli.

W Belo Horizonte nie zagra najlepszy piłkarz reprezentacji Brazylii - Neymar. W ćwierćfinale z Kolumbią (2:1) doznał urazu kręgosłupa i na tym mundialu już nie wystąpi. W drugiej linii ma go zastąpić Willian, chociaż w mediach pojawiły się informacje, że i on nabawił się kontuzji na treningu. Za żółte kartki będzie musiał pauzować kapitan gospodarzy Thiago Silva.

Niemcy takich problemów personalnych nie mają, a selekcjoner Joachim Loew jest pełen optymizmu.

"W trakcie tego turnieju nabraliśmy pewności siebie, jesteśmy stabilni fizycznie i psychicznie. Na pewno przygotujemy dobry plan na ten mecz, a na boisku nie będzie brakować walki" - powiedział szkoleniowiec.

Ostatnie spotkanie o punkty Niemcy przegrali 28 czerwca 2012 roku w Warszawie - w półfinale ME z Włochami (1:2). Od tego czasu nie schodzili z boiska pokonani w żadnym z dziesięciu spotkań eliminacji mundialu i pięciu w turnieju finałowym.

W drugim półfinale Argentyna zmierzy się z Holandią. Mecz zostanie rozegrany w środę w Sao Paulo.(PAP)''',
 26:u'''Trener Legii Warszawa Henning Berg podczas poniedziałkowej konferencji prasowej zapowiedział, że jego drużyna w środowym meczu o piłkarski Superpuchar Polski z Zawiszą Bydgoszcz nie zagra rezerwowym składem.

"Słyszałem opinie, że z Zawiszą mamy zagrać rezerwowym składem. To nieprawda. Przecież nasze rezerwy grają w III lidze. O Superpuchar zagrają piłkarze pierwszej drużyny. Dla tych młodych będzie to świetna okazja na oswojenie się z meczami o stawkę. Nikt nie powinien mówić, że pierwsza jedenastka Legii jest słabsza niż druga. Przypominam końcówkę ostatniego sezonu, kiedy zupełnie inne jedenastki pokonały najpierw Pogoń, a potem Lecha" - podkreślił Berg.

Walkę o zwycięstwo zapowiedział Arkadiusz Piech, który z mistrzem Polski związał się w czerwcu trzyletnim kontraktem.

"Nastroje są pozytywne. Wyjdziemy na mecz o Superpuchar po to, żeby go wygrać" - zaznaczył 29-letni napastnik.

Dla Legii znacznie ważniejsze spotkanie odbędzie się jednak tydzień później, kiedy rozpocznie zmagania w drugiej rundzie kwalifikacji Ligi Mistrzów. Na własnym stadionie podejmie mistrza Irlandii - St. Patrick's Athletic.

"Chcemy wypaść dobrze w Europie, żeby nie trzeba było wciąż czekać na awans polskiej drużyny do Ligi Mistrzów" - powiedział Berg.

W meczu o Superpuchar rywalizuje mistrz kraju (Legia) i zdobywca Pucharu Polski (Zawisza). Zgodnie z decyzją podjętą przez PZPN na majowym zjeździe, spotkanie to stanowi oficjalną inaugurację sezonu i jest rozgrywane na boisku mistrza Polski. Początek w środę o godz. 19.00. (PAP)''',
 27:u''' Michał Przysiężny przegrał z reprezentantem Izraela Dudim Selą 1:6, 6:7 (2-7) w pierwszej rundzie turnieju tenisowego ATP Tour na kortach trawiastych w amerykańskim Newport (pula nagród 474 005 dolarów).

Polakowi pozostała jeszcze rywalizacja w deblu. W pierwszej rundzie, w parze z Amerykaninem Kevinem Kingiem zmierzy się z duetem amerykańsko-australijskim Austin Krajicek, John-Patrick Smith.

Wynik meczu 1. rundy:

Dudi Sela (Izrael) - Michał Przysiężny (Polska) 6:1, 7:6 (7-2). (PAP)''',
 28:u'''W wieku 88 lat zmarł legendarny piłkarz Realu Madryt Alfredo di Stefano. W 1957 i 1959 roku otrzymał "Złotą Piłkę" magazynu "France Football" - nagrodę dla najlepszego zawodnika grającego w Europie. Ostatnio był honorowym prezesem "Królewskich".

Di Stefano, który 4 lipca obchodził urodziny, następnego dnia miał zawał serca (według portalu abc.es - na ulicy niedaleko stadionu Santiago Bernabeu). Od tej pory przebywał w stanie ciężkim w szpitalu w Madrycie. Zmarł w poniedziałek po godz. 17 w wyniku komplikacji pozawałowych.

Od 2005 roku, po pierwszym ataku serca, miał wszczepiony kardiostymulator i by-pass aorty. Cierpiał także na cukrzycę. W ostatnich latach był kilka razy hospitalizowany w związku ze sprawami kardiologicznymi.

Urodzony w Argentynie Di Stefano, występujący najczęściej na pozycji środkowego napastnika, był jednym z najsłynniejszych piłkarzy świata. W latach 1956-60 z Realem Madryt pięciokrotnie zdobył Puchar Europy, strzelając gole w każdym z meczów finałowych. Z "Królewskimi" ośmiokrotnie wywalczył też mistrzostwo Hiszpanii. W 282 występach ligowych w ich barwach zdobył 216 goli.

W 1957 i 1959 roku otrzymał "Złotą Piłkę" magazynu "France Football" - nagrodę dla najlepszego piłkarza grającego w Europie.

Di Stefano, którego ojciec był Włochem, przygodę z futbolem rozpoczął w River Plate Buenos Aires. W czasie 22-letniej kariery grał w reprezentacjach Argentyny, Kolumbii i Hiszpanii, ale nigdy nie wystąpił w mistrzostwach świata. Karierę zakończył w 1966 roku (w Espanyolu Barcelona) w wieku 40 lat.

Jako trener prowadził m.in. trzykrotnie Valencię (1970-74, 1979-80, 1986-88), dwukrotnie Real Madryt (1982-84, 1990-91), a w Argentynie Boca Juniors i River Plate. W 1980 roku doprowadził Valencię do wywalczenia Pucharu Zdobywców Pucharów.

W 2000 roku został honorowym prezydentem Realu. Sześć lat później nazwano jego imieniem nowy kompleks treningowy klubu, a w 2008 roku postawiono pomnik na jego cześć.

Prezydent Hiszpańskiego Komitetu Olimpijskiego (COE) Alejandro Blanco przyznał, że Di Stefano był "duszą" Realu Madryt. Kondolencje po śmierci wybitnego piłkarza przekazała m.in. Barcelona, a trener reprezentacji Hiszpanii Vicente del Bosque powiedział, że ubolewa nad tą ogromną stratą.

Kondolencje dla rodziny i przyjaciół Di Stefano przekazał także w imieniu władz Realu prezydent "Królewskich" Florentino Perez. (PAP)''',
 29:u''' Niemiec Marcel Kittel z ekipy Giant-Shimano wygrał w Londynie, po finiszu z peletonu, trzeci etap wyścigu kolarskiego Tour de France. Żółtą koszulkę lidera zachował Włoch Vincenzo Nibali (Astana).

Kittel wyprzedził Słowaka Petera Sagana oraz Australijczyka Marka Renshawa (Omega Pharma-Quick Step), którego rozprowadzał Michał Kwiatkowski. Polak minął linię mety na 16. pozycji.

W klasyfikacji generalnej nie zaszły żadne zmiany. Nibali wyprzedza o dwie sekundy Sagana oraz Szwajcara Michaela Albasiniego (Orica GreenEdge). Taką samą stratę ma Kwiatkowski, zajmujący wciąż 20. miejsce.

Kittel odniósł szóste w karierze zwycięstwo etapowe w "Wielkiej Pętli", a drugie w tegorocznej edycji. Wcześniej triumfował na pierwszym odcinku w Harrogate. (PAP)''',
 30:u''' Muzycy brytyjskiej formacji Pink Floyd potwierdzili krążące od paru dni doniesienia o ich nowej, pierwszej od dwudziestu lat płycie. Na krążek „The Endless River” złożą się głównie utwory instrumentalne.

Zamęt wśród wielbicieli Pink Floyd zasiała w miniony weekend żona wokalisty zespołu Davida Gilmoura, Polly Samson, obwieszczając na Twitterze premierę płyty „The Endless River”. Oliwy do ognia natychmiast dolała jedna z chórzystek grupy - Durga McBroom-Hudson, informując o swym udziale w sesjach nagraniowych.

Management zespołu oficjalnie potwierdza sensacyjne doniesienia – nowy album Pink Floyd ukaże się w październiku. Dokładna data premiery wydawnictwa podana zostanie jednak dopiero po wakacjach.

Wedle zapowiedzi na krążku znajdą się głównie instrumentalne kompozycje. Nad całością unosił się będzie duch muzyki ambient – eksperymentalnej odmiany muzyki elektronicznej.

Zalążek każdego z utworów z krążka „The Endless River” powstał na przełomie 1993 i 1994 roku, w trakcie nagrywania przez Pink Floyd ich ostatniej płyty studyjnej „The Division Bell”. Płyty, która podzieliła krytyków, ale spotkała się z entuzjastycznym przyjęciem ze strony słuchaczy.

W Polsce „The Division Bell” znalazł ponad 50 tys. nabywców oraz został nagrodzony Fryderykiem – najwyższym wyróżnieniem rodzimej fonografii - w kategorii najlepszego albumu zagranicznego.

Czas oczekiwania na premierę nowego krążka Pink Floyd umili fanom rozszerzone wydanie „The Division Bell”, które przed kilkoma dniami trafiło do sklepów. W jego skład weszły między innymi trzy kolorowe płyty winylowe, dysk Blu-ray z premierowym klipem do utworu "Marooned", pięć kolekcjonerskich grafik, a także miks albumu w systemie 5.1 audio.

Pink Floyd to brytyjska grupa rockowa założona w Londynie w 1965 roku. Charakterystyczne dla jej działalności są teksty piosenek o zabarwieniu filozoficznym, eksperymenty z dźwiękiem, innowacyjne okładki płyt oraz imponujące rozmachem koncerty.

Wśród najważniejszych dokonań zespołu wymienia się albumy: „The Dark Side of The Moon” (1973), „Wish You Were Here” (1975), „Animals” (1977) i „The Wall” (1979). (PAP Life)''',
 31:u'''Zalety lawendy są nie do przecenienia. Ma właściwości przeciwbakteryjne, pięknie, relaksująco pachnie, znakomicie wygładza skórę. Relaksującą i odświeżającą maseczkę z lawendy można wykonać samemu w domu.

"Gdyby cały świat nagle zwariował (na co się od pewnego czasu zanosi) i gdyby miały zniknąć wszystkie rośliny - najbardziej by mi było brak lawendy" - wyznała kiedyś Magda Umer. Ta niepozorna roślina ma wielu zwolenników ze względu na swój zapach i właściwości.

Do wykonania maseczki lawendowej potrzebujemy: garść suszonych kwiatów lawendy,
odrobinę wrzątku, łyżkę mąki lub glinki kosmetycznej.

Suszone kwiaty lawendy zalewamy niewielką ilością wrzątku i zostawiamy do przestygnięcia. Do mieszanki dobrze jest dodać łyżkę mąki lub glinki kosmetycznej, wtedy uzyskamy gęstszą konsystencję maseczki. Na oczyszczoną skórę twarzy nakładamy maseczkę. Dodatkowo twarz z nałożoną maseczką można przykryć gazą - zapobiegnie to odpadaniu kwiatów. Z nałożona maseczką relaksujemy sie, wdychając upojny zapach... Maseczkę z lawendy zmywamy po ok. 20 minutach letnią wodą.

W łatwiejszej wersji maseczki suszone kwiaty lawendy można zastąpić olejkiem lawendowym.

Maseczka lawendowa działa znakomicie na skórę - jest ona rozjaśniona, a zaczerwienienia po wypryskach są mniejsze. Posiada także właściwości ujędrniające i wygładzające - dając efekt odmładzający. Maseczka z lawendy charakteryzuje się także właściwościami przeciwbakteryjnymi, dzięki czemu nadaje się dla osób cierpiących na trądzik.''',
 32:u''' Znaczek wydany przez Pocztę Polską uznano za najpiękniejszy na świecie spośród wszystkich, jakie wyemitowano w 2013 r. Taki jednogłośny werdykt ogłosiło jury podczas 44. Międzynarodowego Konkursu Sztuki Filatelistycznej w Asiago (Włochy).

Uroczystość wręczenia nagród odbyła się 6 lipca w Asiago na północy Włoch. Nagrodę dla Poczty - Granx Prix – Medal Prezydenta Republiki Włoskiej, który objął konkurs patronatem, odebrała Agnieszka Kłoda-Dębska, zastępca dyrektora Biura Marketingu i Filatelistyki Poczty Polskiej, oraz Zuzanna Schnepf-Kołacz, wicekonsul RP we Włoszech.

Znaczek zaprojektowany przez artystkę plastyk Agnieszkę Sancewicz wydano z okazji 455. rocznicy powstania Poczty Polskiej. Przedstawia on słoje przeciętego pnia dębu symbolizujące wielowiekową tradycję firmy. „Dąb to drzewo królewskie, sadząc dąb możemy być pewni, że jego widokiem będą się cieszyć kolejne pokolenia” - powiedziała autorka projektu.

Tytuł „najpiękniejszego znaczka na świecie” jest kolejnym wyróżnieniem dla Poczty Polskiej w tym konkursie. W ubiegłych latach nagrodzono wydaną w 2012 r. zieloną, pachnącą jałowcem emisję z żubrem. W 2009 r. uznanie zyskała związana z dniem zakochanych emisja „Kocham Cię”; w 2008 r. wyróżniono emisję upamiętniająca zjazd stowarzyszenia PostEurop w Krakowie, w 2007 r. - „Dzień Ziemi w Polsce” , a w 1982 r. znaczek „Piękna jesteś rzeko Wisło”.

Więcej informacji o wydanych znaczkach, historii powstania, jak również planach emisyjnych na kolejne lata na stronie www.poczta-polska.pl. (PAP)''',
}

index = {
0:v.concordance(documents[0].lower()),
1:v.concordance(documents[1].lower()),
2:v.concordance(documents[2].lower()),
3:v.concordance(documents[3].lower()),
4:v.concordance(documents[4].lower()),
5:v.concordance(documents[5].lower()),
6:v.concordance(documents[6].lower()),
7:v.concordance(documents[7].lower()),
8:v.concordance(documents[8].lower()),
9:v.concordance(documents[9].lower()),
10:v.concordance(documents[10].lower()),
11:v.concordance(documents[11].lower()),
12:v.concordance(documents[12].lower()),
13:v.concordance(documents[13].lower()),
14:v.concordance(documents[14].lower()),
15:v.concordance(documents[15].lower()),
16:v.concordance(documents[16].lower()),
17:v.concordance(documents[17].lower()),
18:v.concordance(documents[18].lower()),
19:v.concordance(documents[19].lower()),
20:v.concordance(documents[20].lower()),
21:v.concordance(documents[21].lower()),
22:v.concordance(documents[22].lower()),
23:v.concordance(documents[23].lower()),
24:v.concordance(documents[24].lower()),
25:v.concordance(documents[25].lower()),
26:v.concordance(documents[26].lower()),
27:v.concordance(documents[27].lower()),
28:v.concordance(documents[28].lower()),
29:v.concordance(documents[29].lower()),
30:v.concordance(documents[30].lower()),
31:v.concordance(documents[31].lower()),
32:v.concordance(documents[32].lower()),
}


searchterm = raw_input(u'Wprowadż szukany tekst: ')


matches = []

for i in range(len(index)):
  relation = v.relation(v.concordance(searchterm.lower()),index[i])
  if relation != 0:
    matches.append((relation,documents [i][:100]))

matches.sort(reverse=True)

for i in matches:
  print u"Podobieństwo do tekstu:"
  print i[1]
  print "Wynosi:"
  print  i[0], "%"











