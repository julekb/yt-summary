import pytest

from clients.clients import YoutubeClientImplementation, YoutubeTranscriptClientImpl
from clients.openai_client import OpenAIClientImplementation, OpenAIModels
from config import get_config

video_id = "dDYE0GPDV84"
channel_id = "UCX92mVE0rfBDSyRticjqzIA"
video_id_2 = "eA3gqNqRC1g"


config = get_config()


class TestYoutubeClient:
    @pytest.fixture
    def youtube_client(self):
        return YoutubeClientImplementation(service=YoutubeClientImplementation.build_resource(config.GOOGLE_API_KEY))

    def test_get_latest_video_for_channel(self, youtube_client):
        out = youtube_client.get_latest_videos_for_channel(channel_id, 2)
        assert len(out) == 2

    def test_get_videos_details(self, youtube_client):
        out = youtube_client.get_videos_details([video_id, video_id_2])
        assert len(out) == 2


class TestTranscriptClient:
    @pytest.fixture
    def transcript_client(self):
        return YoutubeTranscriptClientImpl()

    def test_get_transcript(self, transcript_client):
        captions = transcript_client.get_captions_for_video(video_id)
        assert isinstance(captions, str)


class TestOpenAIClient:
    @pytest.fixture
    def openai_service(self):
        return OpenAIClientImplementation(
            api_key=config.OPENAI_API_KEY,
            model=OpenAIModels.GPT_3_5_TURBO,
        )

    def test_get_summary(self, openai_service):
        input_text = """
        Dzień dobry witam w kolejnym filmie
        dzisiaj czas na odpowiedzi na wasze
        pytania łącznie ponad 180 pytań na
        YouTubie i na Instagramie ten film
        będzie jak zwykle przy takich okazjach
        bardzo długi więc tradycyjnie podzielę
        go na rozdziały także nie musicie całego
        długiego materiału słuchać jak
        klikniecie sobie opis filmu to w opisie
        znajdziecie rozdział odpowiedzi na
        konkretne pytania ze znacznikami
        czasowymi także od razu będziecie mogli
        przeskoczyć do tej treści która was
        interesuje A jak już jesteśmy przy
        opisie filmu to w opisie do tego filmu
        znajdziecie też kod rabatowy od
        Revolution Race od stałego partnera
        mojego kanału kod rabatowy który mam dla
        was działa cały czas bezterminowo Także
        ja was Zachęcam do tego żeby przed
        jesiennymi wędrówkami zaopatrzyć się w
        odpowiednie ciuchy kod rabatowy i link
        do strony w opisie do tego filmu teraz
        nie przedłużając startujemy od razu z
        waszymi pytaniami No oczywiście tych
        pytań jest tak dużo że na wszystkie nie
        uda się odpowiedzieć ale postaram się
        wybrać te najważniejsze pierwsze pytanie
        po nocy w namiocie gdy jest wilgotny
        tropik czekasz aż wynie czy też pakujesz
        mokry i suszysz później No to wszystko
        zależy od warunków wędrówki to znaczy
        zależy to od tego czy mi się śpieszy
        rano czy nie Jeśli mi się nie śpieszy A
        jest sucho świeci słońce wieje wiatr no
        to wszystkie czynności obozowe wykonuje
        zostawiając tropik namiot czy tarp
        rozłożony i daje mu po prostu czas na
        wyschnięcie więc jest to ostatnia rzecz
        którą składam na takim biwaku jeśli mi
        się nie śpieszy jeśli mi się śpieszy No
        to czasem trzeba Schronienie złożyć
        złożyć mokre No prostym sposobem który
        trochę pozwala tego problemu uniknąć
        jest zabieranie niewielkiej ściereczki z
        mikrofibry taka ściereczka waży tam 10
        15 g i możemy rano sobie przetrzeć
        schronienie
        i od zewnątrz i od wewnątrz wykręcić
        ściereczkę także na pewno tej wilgoci
        będzie będzie mniej w taki jeśli
        zastosujemy ten sposób no i pozwoli to
        trochę czasu zaoszczędzić jeśli wtedy
        kiedy nam się śpieszy Jeśli jest taka
        sytuacja że ten namiot trzeba spakować
        mokry czy czy tarpa trzeba spakować
        mokrego No to oczywiście staram się go
        spakować gdzieś na zewnątrz plecaka do
        kieszeni siatkowej żeby był łatwo
        dostępny i jeśli warunki się zmienią w
        trakcie wędrówki wyjdzie słońce zrobi
        się sucho to gdzieś na na postoju przy
        okazji jakiegoś postoju wyciągam
        wyciągam namiot wyciągam tarpa i go
        suszę w takim w tym czasie nawet takie
        15 minut przerwy jak słońce mocno
        wyjdzie albo wiaterek fajny się zerwie
        to nawet takie 15 minut może dużo
        podsuszyć nie kolejne pytanie od tego
        samego autora czy Doczekamy się twojej
        książki z poradami rowerowo bushcraftowy
        na ten moment mogę tylko obiecać że tak
        doczeka się ale więcej szczegółów nie
        mogę nie mogę jeszcze zdradzić Jak sobie
        radzisz z zapachem ogniska na ubraniach
        i sprzęcie czy w ogóle ci to nie
        przeszkadza nie nie przeszkadza mi to
        ubrania i sprzęt biwakowy żyje sobie w
        swoich przestrzeniach domowych że tak
        powiem nie wchodzi na salony Więc jak
        jest gdzieś tam rzucony w odpowiednim
        miejscu to nikomu to nie przeszkadza a w
        tym sezonie powiedzmy to ogniskowym No
        bo nie ma co ukrywać że te lata w Polsce
        też powoli stają się takie
        że No że to nie jest sezon na ogniska
        Moim zdaniem więc od jesieni do do
        wiosny w tym sezonie ogniskowym kiedy
        biwaku dosyć często No to też
        Najzwyczajniej nie byłoby sensu żeby za
        każdym razem te ubrania prać wietrzyć No
        bo za kilka dni jest kolejny biwak więc
        rzeczy wracają do do stanu pierwotnego
        czyli do stanu
        zakopcony się tym nie stanowi to dla
        mnie problemu kolejne pytanie czy
        myślisz o jakiejś serii filmów zimowych
        gdzie pokazujesz dłuższe biwaki nie
        tylko jednodniowe Och o czym to Ja nie
        myślę ja myślę o wielu rzeczach ale to
        się wszystko rozbija o logistykę w
        przypadku biwaków zimowych No to przede
        wszystkim dotyczy też elektroniki ilości
        baterii powerbanków które trzeba byłoby
        zabrać żeby żeby taki wielodniowy biwak
        nagrać no i do tego dochodzą takie
        kwestie dla was pewnie mniej
        interesujące a dla mnie dosyć istotne
        Czyli po prostu kwestie rodzinne No i to
        ile mam czasu na to żeby żeby wyjeżdżać
        na dłużej co myślisz o wprowadzeniu na
        kanał elementów biwaku nie tylko w lesie
        nie tylko na łonie natury ale na
        przykład też przetrwania w
        mieście Myślę że to się nie wydarzy bo
        to jest coś co mnie po prostu nie
        interesuje interesuje mnie głównie
        Przyroda natura no ja mam ochotę
        wyjeżdżać i nagrywać takie biwaki które
        odbywają się w miejscach które mi też
        sprawiają przyjemność biwakowanie w
        mieście raczej by mi przyjemności nie
        sprawiało A może wyprawa zimą na NC
        wprawa zimą na Nord Cup to chyba tylko
        za karę rejon w którym zimą panuje noc
        polarna więc no raczej Byłaby to wyprawa
        polegająca na cierpieniu niż na
        jakiejkolwiek przyjemności latem w
        czasie dnia polarnego No to już inny
        temat gdybyś mógł zmienić jeden przepis
        prawny dotyczący biwakowania to co można
        byłoby poprawić Gdybym mógł zmienić
        jeden przepis prawny to wprowadziłbym w
        Polsce unormowania podobne do tych które
        mamy na północy czyli w zasadzie prawo
        do swobodnego biwakowania no z
        wyłączeniem dotyczącym oczywiście
        terenów terenów prywatnych parków
        narodowych
        rezerwatów także doprowadziłby do tego
        że to biwakowanie w Polsce byłoby bardzo
        podobne do tego co można robić na
        północy w krajach
        skandynawskich natomiast no też musimy
        mieć świadomość że na tle państw
        europejskich czy tutaj państw starej
        Europy bardzo
        takiej mocno regulowanej z inflacją
        prw to te nasze uwarunkowania odkąd
        pojawił się program zanu w lesie nie są
        nie są złe jesteśmy w całkiem niezłej
        niezłej sytuacji kolejne pytanie Bardzo
        mi się podobały twoje wypady
        minimalistyczne które opisywał na blogu
        czyli są tu jeszcze ludzie którzy bloga
        pamiętają to ciekawe czy są szanse że
        coś podobnego nagrasz Pewnie tak pewnie
        jak przyjdzie jesień przyjdzie zima
        pojawią się niższe
        temperatury townie jakieś bardziej
        minimalistyczny
        pojawią tak no ale to pogoda musi temu
        sprzyjać bo w takich warunkach jak teraz
        no to wiecie co to za co to za biwak
        minimalistyczny siadasz pod drzewem i
        sobie biwaku jesz nie Ile godzin
        tygodniowo pracujesz w porównaniu do
        normalnego
        etatu nie wiem jest to trudne do
        policzenia bo jest to bardzo
        nieregularny tryb pracy moja żona
        twierdzi że pracuje cały czas
        i No pewnie coś w tym jest bo to chyba
        potwierdzą
        żeś jest na swoim prowadzi własną
        działalność to w jakiś tam sposób czy to
        mentalnie Czy fizycznie najczęściej
        mentalnie cały czas w tej pracy jest no
        ale jak to przeliczyć na godzinę No jak
        jadę nagrywać
        biwak i z dojazdem w terenie jestem Nie
        wiem 30 godzin i potem trzeba to
        zmontować i montaż zajmuje 10 12
        godzin no to tak nawę już się robi
        tygodniówka już robi taki tygodniowy
        wym wymiar pracy No wy w efekcie
        widzicie 15 20 25 minut filmu nie jakim
        sprzętem nagrywasz Ile minut godzin
        materiału wychodzi z jednego biwakowania
        ile materiału trafia do kosza w tej
        chwili mam cztery kamery Jeśli dobrze
        pamiętam Lumix G7 To jest cały czas no
        leciwa kamera ale cały czas cały czas
        jej używam kolejna kamera to jest DJ
        Osmo Pocket 3 dalej mam kamerę sportową
        DJ Osmo Action 4 która całkowicie
        wyparła użycie GoPro bo wcześniej
        korzystałem z GoPro teraz to jest Action
        4 No mam dwa drony z których od dawna
        dawna już nie korzystam więc tak to
        wygląda jeśli chodzi o o sprzęt do
        nagrywania Ile minut godzin materiału
        wychodzi bardzo różnie ale jeśli to jest
        biwak stacjonarny bo to trudno porównać
        do jakiegoś filmowania wyjazdu tak no bo
        naturalnie zupełnie inna ilość
        materiałów wyjdzie z biwaku
        stacjonarnego nagrywanego gdzieś w miarę
        lokalnie a zupełnie inne to będą ilości
        przy takim wyjeździe Jak na przykład
        miało miejsce w Jordanii więc łatwiej mi
        powiedzieć w przypadku takich biwaków
        stacjonarnych to jest zawsze gdzieś
        około dwóch godzin surowego materiału i
        z tych dwóch godzin surowego materiału
        wy widzicie właśnie około tych 20 20
        paru minut natomiast to co jest wycinane
        to najczęściej są po prostu sekundy
        przed i pod danym fragmentem który
        wchodzi do filmu mam bardzo bardzo mało
        takich ujęć które w całości idą do kosza
        czy nakrył Cię ktoś kiedyś na biwaku
        straż leśna leśniczy myśliwy lub po
        prostu jacyś przypadkowi
        ludzie zdarzyli się tylko przypadkowi
        ludzie jeśli chodzi o to czym ktoś
        nakrył na biwaku kiedyś dawno dawno temu
        spotkaliśmy się ze strażą Graniczną
        która
        patrolowa gdzieś w okolicach Pogórza
        przemyskiego
        tereny to tylko wtedy kiedy to znaczy
        Zdarzyło się to tylko wtedy kiedy
        pokonywał jakiś konkretny szlak No i
        czasem się układa tak sytuacja że trzeba
        biwakować w
        miejscu No w którym się człowiek po
        prostu gdzieś tam znajduje nie wieczorem
        to nie jest do końca takie idealnie
        wytypowane
        miejsce bo po prostu zapada Zapada zmrok
        i trzeba gdzieś się rozbić No to
        zdarzało się że rano gdzieś tam w
        pobliżu biwaku ktoś tam pieska
        wyprowadzał na
        spacer czy ktoś przyjechał grzybów
        poszukać ale to nigdy nie były negatywne
        negatywne spotkania po prostu po prostu
        zwykłe spotkania jak dbasz o odzież
        outdoorowa jakich środków do prania i do
        impregnacji używasz
        To jest bardzo trudne pytanie bo żeby
        tutaj coś konkretnego polecić to by
        trzeba było wykonać serię testów użyć 10
        impregnatów Potem porównać ich działanie
        w tych samych warunkach No w praktyce
        tak się nie da Ja nie jestem testerem
        sprzętu w takim rozumieniu tak bo
        musiałbym mieć 10 tych samych kurtek
        równocześnie
        impregnować 10 różnymi środkami i
        wychodzić w nich na deszcz w tych samych
        warunkach tak i sprawdzać który
        impregnat będzie bardziej trwały który
        mniej trwał jeśli impregnuje kurtkę dwa
        razy w
        roku No to też ocenienie trwałości
        impregnatu jest trudne bo można
        zaimpregnować krótk dwa razy w roku i
        wyjść na pięć deszczowych biwaków można
        zaimpregnować dwa razy w roku i wyjść na
        15 deszczowych biwaków nie więc no
        próbuję
        [Muzyka]
        impr
        ale ale żaden z tych impregnatów nigdy
        nie dał olśniewających rezultatów także
        niczego w tym temacie nie będę nie będę
        polecał czy myślisz może nad biwakiem
        post Apo w scenariuszu surwiwalowy No i
        znowu tutaj nie nie myślę bo to jest coś
        co mnie interesuje
        interesu owym stylu w kontekście walki z
        jakimś zagrożeniem uciekaniem przed
        jakąś zagładą przed wojną Staram się
        unikać w życiu wszystkiego Co generuje
        strach
        i po prostu nie nakręcają mnie takie
        tematy ja jadę na biwak w naturę w
        przyrodę w ciszę w spokój po to żeby się
        zrelaksować No czasem żeby się zmęczyć
        ale tu chodzi o takie zmęczenie fizyczne
        nie kolejne pytanie tutaj bezpośrednie
        nawiązanie do jednego z filmów który
        pojawiał się na kanale mikro przygody
        kask full face czy ostatnie bliskie
        spotkanie twarzą z kamieniem nie
        przekonało cię do zakupu i testów
        takiego sprzętu wydaje się to być fajnym
        pomysłem na film nie wiem czy testowanie
        kasku full face to jest fajny pomysł na
        film bo to by pewnie uwzględniał
        upadanie na twarz a tego wolałbym
        uniknąć natomiast no tak no to spotkanie
        twarzą z kamieniem nie tyle pokazało mi
        to że używanie kasku full face byłoby
        dobrym pomysłem bo w tej sytuacji Pewnie
        były
        nawet dla dla amatorów albo nawet Im
        bardziej jesteś amatorem
        tym tym pewnie bardziej sensowne
        używanie byłoby takiego kasku natomiast
        to spotkanie z kamieniem pokazało mi to
        że to chyba mimo wszystko jednak nie
        jest aktywność dla mnie Ja i tak nigdy
        po takich singlach kamienistych dużo nie
        jeździłem to zawsze był tam jeden wypad
        w roku dwa wypady w roku i jest to fajne
        ale nie jest to na tyle fajne żeby
        ryzykować połamanie szczęki albo
        albo ryzykować innym poważnym urazem tym
        bardziej Kiedy ciało jest ci trochę
        potrzebne do pracy w mojej pracy ciało
        trochę trochę potrzebne jest i fajnie
        jakby było sprawne więc u mnie to raczej
        nie pójdzie w stronę zakupu kasku full
        face a bardziej pójdzie w stronę
        dziadowanie
        buan i odpuszczania nie nie jeżdżenia po
        po takich trasach Gdzie można upaść po
        prostu twarzą na nał
        Przynajmniej tak mówię teraz no a w
        praktyce zobaczymy Cześć czy w ramach
        twojej działalności organizujesz wypady
        szkoleniowe z podstaw bushcraftu
        obozowania tak to pytanie tylko pokazuje
        że jestem słabiutki w marketingu bo
        kursy prowadzę od wielu lat i
        najwyraźniej nie wszyscy widzowie o tym
        wiedzą
        więc więc nadrabiam moją ułomność
        marketingową i Ogłaszam wszem iow tak
        prowadzimy kursy przetrwania w polskich
        warunkach wszystkie informacje na ten
        temat na stronie sklepu bushcraftowy.pl
        można znaleźć po całym dniu wędrówki
        jazdy rowerem nie zawsze jest gdzie się
        opłukać Czy zakładanie świeżej bielizny
        do spania po takim aktywnym dniu jest
        mocno niekomfortowe Czy w zasadzie jest
        do zniesienia Czy masz może jakieś swoje
        patenty które neutralizują ewentualny
        dyskomfort No na pewno jest to
        niekomfortowe Jeśli nie ma totalnie
        żadnej opcji żeby się umyć No to wolę
        założyć tą bieliznę do spania na nawet
        na brudne ciało żeby prostu nie brudzić
        żeby nie brudzić piora to Wszystko się
        sprowadza do Planowania biwaku na etapie
        planowania biwaku Staram się zawsze tak
        tak to zaplanować Żeby jakiś dostęp do
        wody Był wtedy problem jest rozwiązany
        można się wykąpać Jeśli na samym miejscu
        biwaku dostępu do wody nie ma no to
        Staram się nabrać chociażby trochę wody
        do butelki do bidonu
        żeby żeby przed przed położeniem się do
        śpiwora trochę się umyć nawet taki bidon
        półlitrowy i niewielka szmatka potrafi
        potrafi całkiem dużo zdziałać jeśli się
        nabierze trochę wprawy więc to jest
        druga opcja żeby sobie faktycznie tej
        trochę wody z wyprzedzeniem nabrać
        trzecia opcja bardzo często używana to
        są oczywiście mokre nawilżane chusteczki
        Są też takie chusteczki ze środkiem
        dezynfekującym więc to jest jakieś tam
        rozwiązanie nie tak dobre oczywiście jak
        używanie wody no i w zasadzie do tego to
        się sprowadza podstawa to jest dobry
        dobry wybór miejsca na żeby żeby była
        woda a jak nie ma no to to o czym
        powiedziałem jak wygląda teraz sprawa z
        twoim EDC czy dalej używasz takiego
        zestawu jeśli tak to jak się zmienił na
        przestrzeni czasu Gdy twoje
        zainteresowania poszły w stronę rowerową
        No tak sprawa mojego EDC niestety jest
        dosyć nudna bo ja nie noszę zestawu
        EDC jak wychodzę z domu to zabieram ze
        sobą telefon portfel i klucze i
        Nie wiem nie chcę mówić że wyrosłem
        zestawu EDC bo to nie jest tak że ja nie
        wierzę w to że on się może nie przydać
        bo pewnie są sytuacje w których może się
        przydać ale to pewnie wynika trochę z
        mojego trybu życia funkcjonowania i
        pracy Ja po prostu nie wychodzę do pracy
        jak Nazwijmy to normalny
        człowiek moje moje wyjście do pracy to
        jest wyjście z całym plecakiem pełnym
        ekwipunku a pozostałą część pracy
        wykonuje w domu w biurze No więc znowu
        też jestem otoczony
        jak gdzieś wyjeżdżam No to zawsze
        wyjeżdżam z jakimś tam ekwipunkiem
        takich moich wyjść typowych codziennych
        jest niewiele i to są wyjścia po
        przysłowiowe bułki do sklepu albo gdzieś
        tam właśnie jakieś wyjścia treningowe na
        rower pod domem nawet jak wychodzę na
        rower pod domem pojeździć godzinę to nie
        zabieram ze sobą
        Niczego poza telefonem poza kluczami do
        domu bo jestem w takiej odległości od
        domu że nawet jak jakaś usterka się
        przytrafi to po prostu z buta albo
        wykonuje telefon do przyjaciela w
        postaci mojej
        żony No po prostu to nie mówię że
        Zachęcam do takiego postępowania i że że
        trzeba że nie warto nosić zestawu EDC
        Każdy ma inne warunki pracy inny tryb
        codzienny Iną inną codzienną rutynę moja
        rutyna Codzienna jest taka że zestaw EDC
        No nie mam gdzie go nosić O tak tak to
        powiedzmy nie bo jak już wychodzę w
        teren To i tak wychodzę z plecakiem
        pełnym ekwipunku w sezonie od wczesnej
        wiosny do późnej jesieni jakiego rodzaju
        buty do bushcraftu i wędrówek polecasz
        buty membranowe czy nie jaki konkretny
        model lub Marka którą jesteś w stanie
        zarekomendować na ten temat można by
        książki pisać tu jest pytanie jakie buty
        do bushcraftu do wędrówek Moim zdaniem
        buty do bushcraftu i do wędrówek to są
        dwa różne rodzaje butów Dlatego że w
        bushcrafcie będę chciał tradycyjnie
        rozumiane buty trackingowe wysokie
        solidne z wysoką cholewką ciężkie buty
        tak które dadzą ochronę mechaniczną
        stopie w czasie zbierania opału w czasie
        wędrowania poza szlakiem
        tak buty odporne na bliskość ogniska na
        iskry więc to będą zupełnie inne buty
        które zabrałbym na klasyczną wędrówkę po
        szlaku na przykład w Beskidach tak bo
        latem wiosną w Beskidach na szlak
        zabrałbym pewnie lekkie buty biegowe
        trailowe będą to buty najwygodniejsze
        najlżejsze najprzyjemniejsze do
        wędrowania ale znowu takie buty moim
        zdaniem bardzo słabo się sprawdzą
        na na biwaku bushcraftowy stacjonarnym
        No może nie tyle słabo się sprawdzą co
        po prostu Będą łatwe do uszkodzenia będą
        łatwe do uszkodzenia i na pewno nie
        dadzą takiej ochrony mechanicznej jak
        solidny solidny pełny wysoki but na
        temat butów zrobiliśmy z Łukaszem super
        gunem bardzo obszerny odcinek ja nie
        będę polecał Żadnej konkretnej marki No
        bo tu znowu trzeba byłoby przetestować
        20 par butów żeby się na ten temat na
        ten temat wypowiedzieć więc nie będę
        polecał Żadnej konkretnej marki odsyłam
        do filmu z Łukaszem super ganem
        znajdziecie ten film na playliście
        szkoła biwakowania i tam naprawdę sporo
        o tych butach sobie porozmawialiśmy czy
        zobaczymy jakieś starty na rowerze w
        twoim wykonaniu Czy w tym roku odpuścił
        wyścigi No tak temat rowerowych Ultra to
        temat bardzo dynamiczny w naszym kraju
        jeszcze parę lat temu to tych wyścigów
        było tyle że to na palcach jednej ręki
        moż było policzyć i były one nastawione
        bardzo mocno na jazdę
        przygodową startowały osoby które chyba
        bardzo rozumiały formułę
        samowystarczalności i w moich oczach ten
        świat się bardzo rozwod rozmył i popsuł
        w ostatnich latach z wyścigów z
        ultramaratonów przygodowych robi nam się
        taki Gravel Gravel Racing Czyli po
        prostu kolejne wyścigi rowerowe tak były
        wyścigi szosowe były wyścigi MTB teraz
        zrobiły się kolejne wyścigi
        gravelowe gdzie ten aspekt przygodowy
        zszedł bardzo bardzo gdzieś tam daleko
        na dalszy plan i no nie wiem no moje
        zainteresowanie tym tematem
        trochę trochę upadło Trochę
        ochłonąłem więc w tym roku na pewno nie
        będzie żadnych startów w ultramaratonach
        No były takie plany ale ale sprawy
        osobiste zdrowotne je
        pokrzyżowały więc w tym roku już nie
        będzie nie będzie takich startów
        natomiast to nie zmienia faktu że pewnie
        chciałbym jeździć jakieś ultramaratony
        na własnych warunkach na po własnych
        trasach i w
        przyszłości Nadal chciałbym jeździć
        ultramaratony ale tylko te w których ten
        element przygody jest zachowany jest
        gdzieś tam postawione bardzo wysoko i
        tylko te które poważnie traktują regułę
        samowystarczalności to jeździmy w moich
        oczach po to jeździmy ultramaratony żeby
        robić coś trudnego i żeby sobie stawiać
        wyzwania a nie żeby oczekiwać od
        organizatora że wszystkie przepisy będą
        łagodzacy jak najwięcej osób się na
        wyścig zapisało kolejne pytanie czy
        wypady jeszcze dają ci satysfakcję czy
        wkradła się już zawodowa rutyna jak to
        bywa nawet podczas najfajniejszych zadań
        wykonywanych rutynowo i
        zarobkowo oczywiście oczywiście
        wypady dalej dają mi dużą satysfakcję
        ale oczywiście są momenty gdzie jakieś
        tam wypalenie i Zawodowa rutyna się
        wkrada to tego się nie da uniknąć ja już
        chyba 10 10 rok nagrywam filmy i to cały
        czas są te same filmy nie cały czas
        jeżdżę I śpię w lesie cały czas
        biwaku Więc siłą rzeczy jakaś rutyna się
        wkrada są jakieś tam mniejsze czy
        większe kryzysy teraz też jestem w
        pewnym sensie w punkcie zwrotnym pewne z
        pojawią się w mojej działalności
        youtubowe ale to to pewnie Ogłoszę
        gdzieś tam na
        jesień będzie to dla mnie to będzie duża
        zmiana Ale najważniejsze dla mnie jest
        to że tak nadal mi to daje bardzo dużą
        satysfakcję Nadal są takie szlaki które
        bardzo mnie pociągają chcę je przejść
        przejechać pokazać też
        wam dalej przebywanie w naturze daje mi
        daje mi dużo frajdy
        bardzo specyficzne dotyczące konkretnego
        roweru marin Bob Marine Bobcat Trail 4
        Jak zrobić z niego wyprawowy rower jaki
        bagażnik sakwy I
        nóżka tak z głowy nie pamiętam
        specyfikacji ale wydaje mi się że ten
        rower ma w ramie otwory montażowe na
        bagażnik więc w zasadzie tutaj nie
        trzeba niczego robić żeby robić zrobić z
        tego roweru Rower wyprawowy wystarczy
        dokupić bagażnik saky ja mogę śmiało
        polecić i sakwy extra Wheel i sakwy
        crosso polskich producentów którzy robią
        Naprawdę fajne fajne
        produkty nóżki nigdy nie potrzebowałem w
        rowerze wyprawowy więc nie widzę takiej
        potrzeby bagażnik sakwy najprostsza
        metoda przewożenia bagażu na rowerze
        żadnej filozofii a ten rower jeśli ma
        otwory montażowe na bagażnik A chyba ma
        jest w zasadzie do tego przygotowany
        kolejne pytanie co z komarami pomijam
        moskitiery w namiocie w obecnej chwili w
        lesie wytrzymać wieczorem 5 minut to
        wyzwanie No tak tutaj można znowu kilka
        metod zastosować żeby się chronić przed
        przed komarami
        Ja staram się nie używać chemii używam
        chemii w ostateczności kiedy już
        faktycznie owady są tak uciążliwe że że
        nie ma innego sposobu na przykład jak
        jechaliśmy z Krzesimir niedawno
        centralny szlak roztocza no to wtedy nam
        doskwierał głównie muchy Końskie gzy i
        tym podobne no i tak no i wtedy już
        sięgnęliśmy po chemi po
        repelenty Staram się unikać tego po
        prostu nie lubię Nie lubię się
        spryskiwać tymi chemicznymi środkami one
        pozostawiają taki nieprzyjemny film na
        na skórze więc ja przede wszystkim
        chronię się
        odzieżą No dzisiaj akurat to jest
        zaprzeczenie tego o czym będę mówił ale
        w teren w zasadzie na biwak prawie
        zawsze wychodzę w pełnych butach
        wysokich skarpetach w spodniach z długim
        z długimi nogawkami i w koszulkach z
        długim rękawem Czy w koszulach w
        koszulkach z długim rękawem
        do tego jakieś nakrycie głowy więc
        niewiele zostaje tych tych obszarów
        ciała odsłoniętych na na
        ugryzienia jeśli komary bardzo
        doskwierają No to jakieś odmianie
        ogniska może pomóc No jak jest susza No
        to ognisko odpada nie ale jak nie ma
        Suszy to to możemy rozpalić ogień możemy
        zrobić takie pochodnie z Pruchna
        pochodnie To wygląda jak pochodnie ale
        chodzi o to żeby nabić fragmenty Pruchna
        na kawa drewna podp one się żarzą i
        dymią można je rozstawić w kilku
        punktach obozu i
        one no zadymia dosyć dosyć spory obszar
        wtedy i to też trochę pomaga a co do
        spania na takim biwaku No to w okresie
        kiedy kiedy owady są bardzo aktywne No
        to po prostu korzystam z moskitiery ze
        schronienia z moskitierą to nie ma innej
        metody nie ma co kombinować albo namiot
        albo b z
        moskitierą tak żeby się przed tymi
        insektami
        ochronić spotkania ze zwierzętami w
        lesie na co zwracać szczególną uwagę
        zwracać uwagę przede wszystkim na to
        żeby zwierzętom nie przeszkadzać
        zwierzęta w lesie nie są w polskim lesie
        nie są szczególnym
        zagrożeniem jeśli będziemy tylko troszkę
        hałasu robić w lesie to zwierzęta na
        pewno nas z wyprzedzeniem usłyszą i i
        nie będą stanowiły problemu Chyba że to
        są jakieś latające muchy oczywiście
        często mi się zdarza spotykać sarny
        jelenie to chyba na chyba najczęściej
        sarne jelenie rzadziej dziki raz mi się
        udało spotkać niedźwiedzia ale
        Nigdy nie miałem żadnego problemu z tego
        z tego tytułu po prostu trochę hałasu
        wystarczy kolejne pytanie dotyczące
        filtra do wody zastanawiam się nad
        zakupem filtra raczej skłaniam się ku
        filtrom oczyszczającym z wszystkich
        trzech typów zanieczyszczeń ale może
        masz jakieś Argumenty za tym że filtr
        zanieczyszczeń tylko biologicznych i
        mechanicznych mi wystarczy czy są jakieś
        inne opcje poza filtrem msr tring które
        to robią tak oprócz filtra msr tring
        jest Jest kilka takich filtrów na ryku
        między
        firma Care Plus robi taki filtr który ma
        wkład i Hollow Fiber i wkład węglowy
        Czyli usuwa i zanieczyszczenia chemiczne
        i biologiczne i mechaniczne czy filtr
        oczyszczający wodę tylko biologicznie i
        mechanicznie wystarczy w moim uznaniu
        jeśli wędrujemy głównie w terenach
        dzikich poza cywilizacją to wystarczy
        jeśli szukamy filtra który ma nam
        oczyścić wodę w górach gdzieś ponad
        osadami ludzkimi czy w jakimś dzikim
        terenie to moim zdaniem można sobie ten
        wkład węglowy odpuścić tak bo bo w
        takich naturalnych terenach głównie nas
        będą interesowały właśnie
        zanieczyszczenia mechaniczne i
        biologiczne jakimś argumentem za tym
        jest też to że te wkłady węglowe zawsze
        mają mniejszą żywotność krótszą
        żywotność niż
        wkłady wkłady ceramiczne no Natomiast w
        przypadku takiego filtra jak na przykład
        ten filtr k plus o którym mówię on się
        nazywa bodajże Evo plus to te wkłady są
        wymienne więc zużywając to filtr węglowy
        czy czy ceramiczny możemy sobie sam
        wkład wymienić i filtra używać dalej tak
        więc tutaj wybór bym uzależnił przede
        wszystkim od tego w jakich Z jakich
        terenów chcemy wodę pozyskiwać jeśli w
        grę wchodzą jakieś no jeziora na
        nizinach jakieś cieki wodne które mogą
        gdzieś tam zahaczać o jakieś pola
        uprawne no to wtedy Fajnie byłoby mieć
        też ten wkład węglowy kolejne pytanie
        Jakich map używasz Planując biwaki czy
        wyprawy prawie zawsze to są mapy cz to
        jest wersja na komputer
        z portalu mapy cz Jest tam bardzo dużo
        informacji szczegółowych oczywiście
        wspieram się do tego jakimiś obrazami
        satelitarnymi czasem mapa turystyczna pl
        ale
        99,9 mojego planowania To są mapy cz Jak
        wygląda twój trening przygotowania do
        Maratonów rowerowych trenujesz zimą na
        rowerkach stacjonarnych czy zaczynasz od
        wiosny Tak chciałbym żeby mój trening
        wyglądał bardzo regularnie i żeby miał
        jakąś
        taką fajną strukturę ale tak nie
        jest najwięcej oczywiście czasu spędzam
        na rowerze i to są jakieś takie godzinne
        wypady na na intensywną przejażdżkę bo
        jak tego czasu mam mało mam godzinę no
        to Staram się żeby to była faktycznie
        godzina intensywnej jazdy praktycznie w
        ogóle nie wychodzę na rower po to żeby
        się tak wozić nie więc nie nie ma u mnie
        takich wycieczek rowerowych że ja sobie
        idę na rower i sobie gdzieś tam jadę 10
        15 na godzinę i i podziwiam sobie
        kwiatki i i wiewiórki chociaż chciałbym
        i też chciałbym trochę zmienić to swoje
        funkcjonowanie tak żeby na co dzień też
        sobie dać trochę takiego takiego resetu
        właśnie ale na ten moment tak nie jest
        każde wyjście na rower to jest w
        zasadzie takie piłowanie nie to godzina
        intensywnej jazdy czy po lesie C czy po
        drogach ale tak żeby żeby to była jakaś
        Wysoka intensywność No i staram się to
        uzupełniać siłownią no z tym też jest
        bardzo różnie ostatnio ostatnio było
        trochę gorzej ale jak zawsze plany są
        takie żeby żeby tego
        wrócić no i też chciałbym trochę
        regularniej trochę regularniej biegać na
        razie jakieś takie nieśmiałe próby
        nieśmiałe próby z bieganiem wprowadzam
        ale temu wszystkiemu daleko do
        regularności zdecydowanie największą
        regularność udaje mi się utrzymać z
        rowerem i to jest to jest jedyna
        aktywność taka którą faktycznie udają
        się regularnie
        uprawiać jeździć na ten moment przy
        wszystkich
        ROD dwój dzieci staram się celować
        godzin treningu tygodniowo staram się
        celować godzin treningu tygodniowo i
        jestem zadowolony kiedy mi się to uda
        nie zawsze uda się te 6 godzin
        utrzymać ale Taki jest plan kolejne
        pytanie techniczne dotyczące filmowania
        na filmach masz super przebitki kupę
        zdjęć ile
        obróbka ile samo nagrywanie powroty po
        kamery i tak dalej no to już na to
        odpowiedziałem że to wychodzi mniej
        więcej dwi godziny surowego materiału No
        czyli siłą rzeczy przez dwie godziny
        kamera nagrywa No ja pewnie do tego
        jeszcze muszę dołożyć Nie wiem może
        drugie tyle na ustawianie kamery na na
        wracanie po kamerę no i obróbka to
        bardzo zależy od od filmów najdłuższe
        filmy najbardziej skomplikowane filmy No
        to to jest kilkanaście godzin obrabiania
        Czy masz może w planach zrob jakieś
        konstrukcji w lesie lub czegoś w tym
        stylu jeśli pytasz o takie stałe
        konstrukcje typu jakieś ziemianki stałe
        szałasy chaty to nie to nie mam takich
        planów uważam że to jest niezgodne z
        zasadą le not Race nie pozostawiania po
        sobie po sobie śladów nie widzę też
        żadnej potrzeby żeby takich konstrukcje
        budować bo nie interesuje mnie
        przesiadywanie w jednym miejscu przez
        jakiś dłuższy czas Nie interesują mnie
        biwaki stacjonarne w tym rozumieniu że
        Buduję sobie ziemiankę i siedzę tam
        tydzień nie to to nie jest coś co mnie
        interesuje interesuje mnie jakaś
        wędrówka w terenie mi nieznanym albo
        biwak stacjonarny który ma być jakimś
        takim zresetowaniem się i i nie musi
        trwać nie wiadomo ile nie myślę że na
        takim biwaku stacjonarnym w tym samym
        miejscu bym się po prostu wynudziłem
        wszystkim plecak do 30 40 lit dla mnie
        nie jest idealny dla mnie idealny plecak
        to jest plecak o pojemności około 50 l
        """
        output = openai_service.summarize_text(input_text, max_length=1000)
        assert output
