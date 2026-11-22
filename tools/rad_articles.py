# Innhold for «Råd og tips». Tekst på bokmål. Ingen oppdiktede tall, kunder eller resultater.

CATEGORIES = {
    'tak': 'Tak og overflater',
    'lys': 'Lys og belysning',
    'bad': 'Bad og våtrom',
    'bolig': 'Kjøp, salg og flytting',
    'strekktak': 'Strekktak forklart',
    'nytt': 'Nytt om oppussing og interiør',
}

# Eldre veiledninger som nå får plass i huben
GUIDES = [
    dict(url='/hva-er-strekktak/', title='Hva er strekktak?', desc='Slik monteres duken, hva den tåler og hvordan den skiller seg fra gips og takplater.', img='/eksempler/stue-lyslinjer.jpg', cat='strekktak'),
    dict(url='/strekktak-pris/', title='Hva koster strekktak?', desc='Priser per kvadratmeter, minste oppdrag og hva som kommer i tillegg.', img='/eksempler/D-lyslinje-spotter.jpg', cat='strekktak'),
    dict(url='/pusse-opp-tak/', title='Pusse opp taket uten sparkling og maling', desc='Når det gamle taket er stygt og du ikke orker støv og tørketid.', img='/eksempler/soverom-lyslinje-skinne.jpg', cat='tak'),
    dict(url='/senke-taket/', title='Senke taket og skjule rør og ledninger', desc='Slik skjuler du rør, kabler og ujevnheter uten å bygge nytt himlingstak.', img='/eksempler/sort-skyggefuge-vindu.jpg', cat='tak'),
    dict(url='/lys-i-taket/', title='Lys i taket: lyslinjer, LED-lister og spotter', desc='Hvilke typer lys som kan bygges inn i taket, og hva som passer hvor.', img='/eksempler/kjokken-oy-lyslinjer.jpg', cat='lys'),
    dict(url='/strekktak-barnerom/', title='Et tak barna gleder seg til å se på', desc='Lys, farger og et glatt tak på barnerommet.', img='/eksempler/lyslinjer-trekant.jpg', cat='lys'),
    dict(url='/strekktak-bad/', title='Strekktak på bad', desc='Et tak som tåler fukt og er ferdig på én dag.', img='/glossy.jpg', cat='bad'),
    dict(url='/oppussing-etter-boligkjop/', title='Nytt tak før du flytter inn', desc='Hvorfor det lønner seg å gjøre taket mens rommene er tomme.', img='/eksempler/kjokken-magnetskinne.jpg', cat='bolig'),
    dict(url='/strekktak-bygard-oslo/', title='Nytt tak i bygårdsleilighet', desc='Høye, skjeve og sprukne tak i gamle bygårder.', img='/eksempler/B-lysramme-lysekrone.jpg', cat='tak'),
    dict(url='/strekktak-kontor/', title='Nytt tak i kontor og butikk', desc='Tak på én dag, uten å stenge i flere uker.', img='/eksempler/A-mansard-lyslinjer.jpg', cat='strekktak'),
]

ARTICLES = [
# ---------------------------------------------------------------- 1
dict(
slug='sprekker-i-taket', cat='tak', image='/eksempler/soverom-lyslinje-skinne.jpg',
alt='Glatt, hvitt tak uten sprekker i et soverom',
title='Sprekker i taket: når er det farlig, og hvordan fikser du det? | TakNova',
desc='Sprekker i taket er som regel kosmetiske, men ikke alltid. Slik ser du forskjellen, slik reparerer du dem selv, og dette gjør du når de kommer tilbake.',
h1='Sprekker i taket: når er det farlig, og hvordan fikser du dem?',
card='Sprekker i taket', teaser='Når sprekker er ufarlige, når du bør få noen til å se på dem, og hvorfor de kommer tilbake etter maling.',
form_hint='For eksempel: sprekker i stuetaket, ca. 25 m²',
related=['/pusse-opp-tak/', '/strekktak-bygard-oslo/', '/rad/mugg-i-taket-bad/', '/hva-er-strekktak/'],
lead='Nesten alle som bor i et hus eller en leilighet noen år, får sprekker i taket. De fleste er ufarlige og handler om at materialene beveger seg. Noen få er tegn på noe du bør ta på alvor. Her er hvordan du skiller dem, og hva du kan gjøre selv.',
short='<ul><li>Hårfine sprekker i maling og sprekker langs gipsskjøter er som regel kosmetiske.</li><li>Få noen til å se på taket hvis sprekken vokser, går på skrå ut i veggen, eller kommer sammen med gule flekker, fukt eller dører som plutselig går tregt.</li><li>Sprekker i hjørner kommer ofte tilbake etter maling. Der må du bruke en fuge som tåler bevegelse.</li><li>Er hele taket fullt av sprekker, er det ofte enklere å dekke det enn å reparere sprekk for sprekk.</li></ul>',
body='''<h2>Hvorfor får man sprekker i taket?</h2>
<p>Et tak står aldri helt stille. Trevirke krymper og sveller med årstidene, særlig i norske hus der lufta er tørr om vinteren og fuktigere om sommeren. Gipsplater er skrudd fast i bjelker som beveger seg litt, og skjøtene mellom platene er det svakeste punktet. I nye hus og nye påbygg setter konstruksjonen seg de første årene. I eldre bygårder med pusset tak kan pussen slippe underlaget etter mange tiår.</p>
<p>Det betyr at en sprekk i seg selv ikke er et tegn på at noe er galt. Det viktige er hvor den går, hvordan den ser ut og om den endrer seg.</p>
<h2>Vanlige typer sprekker, og hva de betyr</h2>
<p><strong>Hårfine sprekker i malingen.</strong> Et nett av tynne sprekker, ofte i eldre tak med mange lag maling. Det er malingen som sprekker, ikke taket. Ufarlig, men vanskelig å få pent uten å slipe ned.</p>
<p><strong>Rette sprekker langs en linje.</strong> Går sprekken rett over taket i jevn avstand fra veggen, følger den nesten alltid en skjøt mellom to gipsplater. Sparkelen har sluppet fordi platene beveger seg. Vanlig og som regel ufarlig.</p>
<p><strong>Sprekk i hjørnet mellom tak og vegg.</strong> Her møtes to flater som beveger seg ulikt. Den kommer gjerne tilbake hvert år, særlig om vinteren. Ufarlig, men irriterende.</p>
<p><strong>Sprekker i pusset tak i murgård.</strong> Pussen kan bli løs fra underlaget. Bank lett rundt sprekken. Høres det hult ut over et større område, bør pussen sjekkes før noen maler eller henger noe tungt i taket.</p>
<p><strong>Sprekker med gule eller brune kanter.</strong> Misfarging betyr nesten alltid at vann har vært der. Da er sprekken et symptom, og du må finne lekkasjen først.</p>
<h2>Når bør du få en fagperson til å se på det?</h2>
<p>Kontakt en takstmann eller en bygningsingeniør hvis du ser ett eller flere av disse tegnene:</p>
<ul><li>sprekken blir bredere eller lengre over noen uker eller måneder</li><li>den går på skrå, eller fortsetter fra taket og ned i veggen</li><li>dører og vinduer i samme område har begynt å gå tregt</li><li>taket har begynt å bule eller henge</li><li>du ser fukt, misfarging eller kjenner muggslukt</li></ul>
<p>Et enkelt triks: sett en tynn blyantstrek ved hver ende av sprekken og skriv datoen. Da ser du om den vokser.</p>
<h2>Slik reparerer du sprekker selv</h2>
<p>For en vanlig sprekk i et gipstak:</p>
<ol><li>Skrap bort løs maling og sparkel langs sprekken. Åpne den litt med en sparkelspade, så den nye sparkelen får tak.</li><li>Er det en skjøt som har sprukket, legg på ny papir- eller glassfiberremse før du sparkler.</li><li>Sparkle i to til tre tynne lag, med tørketid imellom. Slip lett mellom lagene.</li><li>Grunn det reparerte feltet. Ellers ser du flekken gjennom malingen.</li><li>Mal hele taket, ikke bare sprekken. Ny maling ved siden av gammel nesten alltid synes, særlig i sidelys.</li></ol>
<p>I hjørnet mellom tak og vegg hjelper sparkel lite, fordi den sprekker igjen når flatene beveger seg. Bruk heller en malbar akrylfuge som er laget for bevegelse, og trekk den pent ut med en fuktig finger.</p>
<h2>Hvorfor kommer sprekken tilbake?</h2>
<p>Fordi årsaken fortsatt er der. Sparkel er hard, og treverket bak beveger seg. Det er derfor de samme sprekkene ofte dukker opp igjen hver vinter. En skjøt med ny remse holder bedre enn en skjøt som bare er sparklet over, og en elastisk fuge holder bedre i hjørner enn sparkel. Men helt sikker blir du aldri med maling og sparkel på et tak som beveger seg.</p>
<h2>Når taket har for mange sprekker</h2>
<p>Noen ganger er det ikke én sprekk, men et helt tak med skjøter som har sluppet, hårfine sprekker og gamle reparasjoner som skinner gjennom. Da blir det mye arbeid: sparkling av hele flaten, sliping med mye støv, grunning, to strøk maling og tørketid imellom. Og sprekkene kan komme tilbake.</p>
<p>Alternativet er å dekke taket. Det kan gjøres med nye gipsplater, takplater eller et strekktak. Et strekktak er en duk som spennes mellom profiler på veggene, noen centimeter under det gamle taket. Duken henger fritt, så bevegelser i det gamle taket synes ikke. Det blir ingen sparkling, ingen sliping og ingen maling, og et vanlig rom er som regel ferdig på én dag. Les mer i <a href="/pusse-opp-tak/">Pusse opp taket uten sparkling og maling</a>.</p>
<p>Én viktig ting: et nytt tak løser ikke årsaken til en sprekk. Skyldes sprekken fukt, en lekkasje eller at konstruksjonen har satt seg mer enn normalt, må det fikses først. Det sier vi også på befaringen hvis vi ser det.</p>''',
faq=[
('Er sprekker i taket farlig?', 'Som regel ikke. De fleste sprekker skyldes at gips, tre og maling beveger seg med temperatur og fukt. Få en fagperson til å se på det hvis sprekken vokser, går på skrå ned i veggen, eller kommer sammen med fukt, misfarging eller et tak som buler.'),
('Hvorfor sprekker taket om vinteren?', 'Lufta inne blir tørr når vi fyrer, og treverket krymper. Da beveger gipsplatene seg litt, og sparkelen i skjøtene og hjørnene sprekker. Mange ser de samme sprekkene komme tilbake hver vinter.'),
('Hva bruker jeg i sprekken mellom tak og vegg?', 'En malbar akrylfuge som tåler bevegelse. Sparkel er for hard og sprekker igjen.'),
('Kan man legge strekktak over et tak med sprekker?', 'Ja. Duken festes i profiler på veggene og henger fritt under det gamle taket, så sprekkene blir skjult og bevegelser synes ikke. Er det fukt eller lekkasje i taket, må det utbedres før montering.'),
]),
# ---------------------------------------------------------------- 2
dict(
slug='belysning-stue', cat='lys', image='/eksempler/stue-lyslinjer.jpg',
alt='Stue med lyslinjer i et hvitt tak',
title='Belysning i stua: slik får du nok lys i mørketiden | TakNova',
desc='Én taklampe midt i rommet gir sjelden godt lys. Slik planlegger du lys i lag, velger riktig fargetemperatur og bruker taket til spotter, lyslinjer og skjult LED.',
h1='Belysning i stua: slik får du nok lys i mørketiden',
card='Belysning i stua', teaser='Lys i lag, riktig fargetemperatur og hvordan taket kan gjøre stua lysere fra november til februar.',
form_hint='For eksempel: vil ha lyslinjer i stua, ca. 30 m²',
related=['/lys-i-taket/', '/strekktak-barnerom/', '/rad/sprekker-i-taket/', '/hva-er-strekktak/'],
lead='Fra november til februar er stua rommet der vi tilbringer de mørke timene. Likevel er den ofte lyssatt med én lampe midt i taket og et par lamper i hjørnene. Resultatet er et rom som føles mørkt i kantene og hardt i midten. Det finnes enkle grep som hjelper.',
short='<ul><li>Lys stua i tre lag: grunnlys, arbeidslys der du leser eller jobber, og stemningslys.</li><li>Lys på veggene og i taket får rommet til å virke større og lysere enn én sterk lampe midt i rommet.</li><li>Velg varmt lys rundt 2700 K i stua, og ha alt på dimmer.</li><li>Fast lys i taket må kobles av en registrert elektroinstallatør. Planlegg det før du pusser opp taket.</li></ul>',
body='''<h2>Hvorfor føles stua mørk selv med mange lamper?</h2>
<p>Øyet opplever et rom som lyst når veggene og taket er lyse, ikke bare når lampen er sterk. En taklampe midt i rommet lyser opp gulvet og bordet under seg, mens veggene og hjørnene blir liggende i skygge. Da føles rommet mindre og mørkere. Det hjelper lite å skru opp watten. Det som hjelper, er å spre lyset.</p>
<h2>Tenk i tre lag</h2>
<p><strong>Grunnlys</strong> er det jevne lyset som gjør at du finner fram og ser hele rommet. Det kan komme fra spotter, lyslinjer eller skjult LED langs veggene.</p>
<p><strong>Arbeidslys</strong> er lyset der du gjør noe: en leselampe ved lenestolen, lys over spisebordet, lys der barna gjør lekser.</p>
<p><strong>Stemningslys</strong> er lyset du har på om kvelden: bordlamper, lys i hyller, dimmet lys i taket.</p>
<p>En stue med alle tre lagene kan brukes til alt, fra lørdagsrydding til filmkveld, bare ved å skru av og på.</p>
<h2>Fargetemperatur: hvorfor lyset føles kaldt eller varmt</h2>
<p>Lyspærer og LED er merket med Kelvin (K). Jo lavere tall, jo varmere og gulere lys.</p>
<ul><li>2700 K er varmt, nær det gamle glødelyset. Passer i stue og soverom.</li><li>3000 K er litt friskere og passer der du både koser deg og jobber, for eksempel ved spisebordet eller på kjøkkenet.</li><li>4000 K og høyere er kjølig hvitt. Det passer på et verksted, sjelden i en stue.</li></ul>
<p>Bland ikke for mange fargetemperaturer i samme rom. Det ser urolig ut, særlig om kvelden. Se også etter fargegjengivelse (Ra eller CRI). Jo høyere tall, jo mer naturlige ser farger og hud ut. Ra 90 eller høyere er et godt valg i stua.</p>
<h2>Bruk taket</h2>
<p>Taket er den største ledige flaten i rommet, og det er der du kan plassere grunnlyset uten at det tar plass.</p>
<p><strong>Spotter</strong> gir punktvis lys. Plasser dem i forhold til det du vil lyse opp, for eksempel langs veggen der bildene henger eller over sofabordet, og ikke rett over der du sitter. Spotter rett over sofaen blender når du lener deg tilbake.</p>
<p><strong>Lyslinjer</strong> er smale LED-linjer som felles inn i taket. De gir et jevnt lys og blir samtidig en del av designet.</p>
<p><strong>Skjult LED langs veggene</strong> lyser opp tak og vegg indirekte. Det gir et mykt lys uten blending, og det er dette som får rommet til å virke høyere og større.</p>
<p><strong>Skinner</strong>, gjerne magnetskinner, gir deg frihet til å flytte og bytte spotter senere.</p>
<p>Les mer om de ulike løsningene i <a href="/lys-i-taket/">Lys i taket: lyslinjer, LED-lister og spotter</a>.</p>
<h2>Elektrikeren må med</h2>
<p>All fast elektrisk installasjon i Norge skal gjøres av en registrert elektroinstallatør, og du skal få en samsvarserklæring når jobben er ferdig. Det gjelder også nye spotter og lyslinjer i taket. Snakk med elektrikeren tidlig, før taket lukkes.</p>
<h2>Hvis du likevel skal gjøre noe med taket</h2>
<p>Et betongtak er vanskelig å bygge lys inn i. Gips krever hulltaking, sparkling og maling etterpå. Med et strekktak monteres duken noen centimeter under det gamle taket, og ledningene legges i mellomrommet. Spotter, lyslinjer og skjult LED felles rett inn i duken. Lyset planlegges på befaringen, og tilkoblingen gjør et registrert elektroforetak vi samarbeider med.</p>
<p>Har du allerede et fint tak og vil bare ha bedre lys, trenger du ikke strekktak. Da holder det med bedre plassering av lamper og en elektriker.</p>''',
faq=[
('Hvor mange spotter trenger jeg i stua?', 'Det avhenger av takhøyden, hvor bredt lys spottene gir og hva du skal lyse opp. Start med det du vil se, som veggene, sofabordet og bildene, og plasser spottene ut fra det. På befaringen tegner vi forslag ut fra rommet ditt.'),
('Hvilken fargetemperatur er best i stua?', 'Rundt 2700 K gir et varmt og rolig lys. 3000 K passer der du også jobber, som ved spisebordet. Hold deg til én eller to fargetemperaturer i samme rom.'),
('Kan jeg montere spotter i taket selv?', 'Nei. Fast elektrisk installasjon skal gjøres av en registrert elektroinstallatør, og du skal få en samsvarserklæring.'),
('Hvordan får jeg stua til å føles lysere uten nye vinduer?', 'Lys opp vegger og tak i stedet for bare gulvet. Skjult LED langs veggene, lyslinjer i taket og lyse flater gjør at rommet oppleves lysere og større.'),
]),
# ---------------------------------------------------------------- 3
dict(
slug='pusse-opp-for-salg', cat='bolig', image='/eksempler/kjokken-oy-lyslinjer.jpg',
alt='Lyst kjøkken med lyslinjer i taket',
title='Pusse opp før salg: dette lønner seg, og dette kan du droppe | TakNova',
desc='Lønner det seg å pusse opp før du selger boligen? Hva meglere vanligvis anbefaler, hva som synes på bildene, og hvorfor du aldri skal skjule feil.',
h1='Pusse opp før salg: dette lønner seg, og dette kan du droppe',
card='Pusse opp før salg', teaser='Hva som synes på salgsbildene, hva du kan droppe, og hvorfor du aldri skal skjule feil før salg.',
form_hint='For eksempel: skal selge i februar, stygt tak i stue og gang',
related=['/oppussing-etter-boligkjop/', '/rad/sprekker-i-taket/', '/pusse-opp-tak/', '/strekktak-pris/'],
lead='Når boligen skal selges, kommer spørsmålet: skal vi pusse opp først? Svaret er sjelden et nytt kjøkken eller et nytt bad rett før salg. Det som oftest gir mest, er små ting som gjør at boligen ser ren, lys og vedlikeholdt ut på bildene og på visning.',
short='<ul><li>Store oppussinger rett før salg betaler seg ofte ikke. Kjøperen vil gjerne velge kjøkken og bad selv.</li><li>Rydding, vask, små reparasjoner, lyse flater og godt lys er det meglere oftest anbefaler.</li><li>Taket synes på nesten alle salgsbilder. Sprekker, flekker og gamle takplater trekker ned.</li><li>Skjul aldri feil. Fukt og lekkasjer skal utbedres og opplyses om, ikke dekkes over.</li></ul>',
body='''<h2>Lønner det seg å pusse opp før salg?</h2>
<p>Ingen kan love at en oppussing gir mer tilbake enn den koster. Det avhenger av boligen, området og markedet akkurat da. Spør megleren din før du setter i gang. Megleren kjenner kjøperne i ditt område og vet hva som trekker ned i prisen der.</p>
<p>Det de fleste meglere sier, er at store prosjekter sjelden lønner seg rett før salg. Et nytt kjøkken er en smakssak, og mange kjøpere planlegger uansett å gjøre om. Små tiltak som får boligen til å se vedlikeholdt ut, er en annen sak.</p>
<h2>Dette synes på bildene</h2>
<p>De fleste kjøpere ser boligen først på FINN. Det er bildene som avgjør om de kommer på visning. På bildene synes dette godt:</p>
<ul><li><strong>Lys.</strong> Mørke rom ser mindre ut. Ekstra lamper, lyse flater og rene vinduer gjør stor forskjell.</li><li><strong>Vegger.</strong> Merker, hull og sterke farger. Ett strøk i en lys, nøytral farge er ofte det enkleste grepet.</li><li><strong>Tak.</strong> Fotografen bruker vidvinkel, og da kommer taket med på nesten alle bilder. Sprekker, vannflekker, gulnede takplater og synlige skjøter trekker blikket.</li><li><strong>Rot og personlige ting.</strong> Kjøperen skal kunne se for seg sine egne ting i rommet.</li></ul>
<h2>Dette kan du ofte droppe</h2>
<ul><li>nytt kjøkken eller bad, med mindre det er direkte i dårlig stand</li><li>dyre gulv i rom der det gamle gulvet bare trenger en vask og litt olje</li><li>personlige valg som sterke farger, tapet og spesielle fliser</li></ul>
<h2>Skjul aldri feil</h2>
<p>Dette er det viktigste rådet i hele artikkelen. Har det vært lekkasje, fukt eller muggskader, skal årsaken utbedres og opplyses om. Å male over en vannflekk eller dekke et fuktig tak rett før salg kan bli en dyr reklamasjonssak etterpå. Ta vare på kvitteringer og dokumentasjon på det du har fått gjort, og gi det til megleren og takstmannen.</p>
<p>Det gjelder også oss. Ser vi tegn på fukt eller lekkasje på befaringen, monterer vi ikke før det er sjekket og utbedret.</p>
<h2>Når taket er det som trekker ned</h2>
<p>Har boligen et tak med sprekker, gamle takplater eller flekker etter en lekkasje som for lengst er utbedret, er det ofte et av de rimeligste grepene som synes på bildene. Problemet er tiden. Sparkling og maling av et tak med mange sprekker tar flere dager med støv og tørketid, og det passer dårlig når boligen samtidig skal vaskes og styles.</p>
<p>Et strekktak monteres under det gamle taket. Det blir ingen sparkling, ingen sliping og nesten ikke noe støv, og et vanlig rom er som regel ferdig på én dag. Duken lages etter mål, så ta kontakt i god tid før fotograferingen. På befaringen får du vite når vi kan montere.</p>
<p>Selger du ikke, men har kjøpt? Les <a href="/oppussing-etter-boligkjop/">Nytt tak før du flytter inn</a>.</p>''',
faq=[
('Lønner det seg å pusse opp før salg?', 'Store prosjekter som nytt kjøkken eller bad lønner seg sjelden rett før salg. Små grep som rydding, vask, reparasjoner, lyse flater og godt lys er det meglere oftest anbefaler. Spør megleren din, som kjenner kjøperne i området.'),
('Bør jeg male taket før salg?', 'Har taket flekker eller sprekker, synes det på salgsbildene. Maling er greit hvis taket er i god stand. Har det mange sprekker, kan sparkling og maling ta flere dager. Da kan et nytt tak være raskere.'),
('Kan jeg dekke over en vannskade før salg?', 'Nei. Årsaken skal utbedres, og skaden skal opplyses om til megleren og kjøperen. Å skjule feil kan føre til en reklamasjonssak etter salget.'),
('Hvor lang tid tar det å få nytt tak før salg?', 'Selve monteringen tar som regel én dag per rom. Duken lages etter mål, så ta kontakt i god tid før fotograferingen.'),
]),
# ---------------------------------------------------------------- 4
dict(
slug='mugg-i-taket-bad', cat='bad', image='/glossy.jpg',
alt='Blankt, glatt tak på bad',
title='Mugg og flassende maling i taket på badet: årsak og løsning | TakNova',
desc='Svarte prikker og maling som flasser i baderomstaket skyldes nesten alltid fukt som ikke kommer ut. Slik finner du årsaken, vasker bort mugg og hindrer at det kommer igjen.',
h1='Mugg og flassende maling i taket på badet: årsak og løsning',
card='Mugg i taket på badet', teaser='Hvorfor det blir svarte prikker og flassende maling i baderomstaket, og hvordan du får det bort for godt.',
form_hint='For eksempel: maling flasser i badetaket, ca. 5 m²',
related=['/strekktak-bad/', '/rad/sprekker-i-taket/', '/hva-er-strekktak/', '/senke-taket/'],
lead='Svarte prikker i hjørnet over dusjen, maling som bobler og flasser, og en lukt som ikke vil gå bort. Det er et av de vanligste problemene i norske bad. Det kommer nesten alltid av det samme: fuktig luft som ikke kommer ut fort nok.',
short='<ul><li>Mugg og flassende maling i badetaket skyldes nesten alltid for dårlig ventilasjon.</li><li>Sjekk at viften faktisk trekker, at ventilen ikke er tett, og at det kommer luft inn under døra.</li><li>La viften gå etter dusjing, og vask bort mugg med et middel laget for det.</li><li>Nytt tak eller ny maling hjelper lite hvis fukten ikke kommer ut.</li></ul>',
body='''<h2>Hvorfor blir det mugg i taket?</h2>
<p>En dusj sender mye vanndamp opp mot taket. Taket er ofte den kaldeste flaten i rommet, særlig ved yttervegg eller under et kaldt loft. Der kondenserer dampen, og flaten blir fuktig. Skjer det hver dag, og fukten ikke rekker å tørke, får mugg gode vekstvilkår. Maling som stadig blir fuktig, mister heften og begynner å boble og flasse.</p>
<h2>Sjekk ventilasjonen først</h2>
<p>Dette kan du sjekke selv på noen minutter:</p>
<ol><li><strong>Trekker viften?</strong> Hold et ark mot ventilen mens viften går. Suges arket fast, trekker den. Faller det ned, gjør den lite.</li><li><strong>Er ventilen ren?</strong> Støv og lo kan tette den nesten helt. Ta av ventilen og vask den.</li><li><strong>Kommer det luft inn?</strong> Viften kan bare trekke ut luft hvis ny luft kommer inn. Det skal være en spalte under døra eller en ventil i døra.</li><li><strong>Hvor lenge går den?</strong> La viften gå til speilet er tørt og en stund etter. Mange slår den av for tidlig.</li></ol>
<p>Er viften gammel eller svak, er det en jobb for elektriker eller ventilasjonsfirma å bytte den. Bor du i borettslag eller sameie med felles ventilasjon, kontakt styret.</p>
<h2>Slik vasker du bort mugg</h2>
<p>Bruk et muggfjerningsmiddel fra byggvarehandelen og følg bruksanvisningen. Bruk hansker og luft godt ut. Ikke bland ulike rengjøringsmidler. Vask hele flaten, ikke bare prikkene du ser, og la det tørke helt. Kommer muggen tilbake på samme sted etter kort tid, er fukten fortsatt der.</p>
<h2>Maling som flasser</h2>
<p>Skrap bort all løs maling. Vask og la taket tørke godt. Grunn og mal med en maling som er laget for våtrom. Maler du over løs maling eller en fuktig flate, flasser det igjen.</p>
<h2>Når bør du få noen til å se på det?</h2>
<p>Hvis muggen er stor eller kommer tilbake raskt, hvis taket er mykt eller buler, eller hvis du ser brune ringer og misfarging, kan det være fukt i konstruksjonen eller en lekkasje fra etasjen over. Da trenger du en fagperson som kan måle fukt og finne årsaken. Det må utbedres før du gjør noe med overflaten.</p>
<h2>Et tak som tåler fuktig luft</h2>
<p>Når ventilasjonen er i orden og taket er tørt, er det fortsatt mange som er lei av å male badetaket med noen års mellomrom. Et strekktak av PVC-duk tar ikke opp fukt, og den glatte flaten kan tørkes av. Den skal aldri males. Ventil, vifte og spotter monteres i duken.</p>
<p>Vi sier det like tydelig på befaringen som her: et strekktak erstatter ikke ventilasjonen. Kommer ikke fukten ut av rommet, legger den seg på andre kalde flater i stedet. Les mer om <a href="/strekktak-bad/">strekktak på bad</a>.</p>''',
faq=[
('Hvorfor flasser malingen i taket på badet?', 'Fordi taket blir fuktig hver gang noen dusjer, og fukten ikke rekker å tørke. Malingen mister heften og bobler eller flasser. Sjekk ventilasjonen før du maler på nytt.'),
('Hvordan sjekker jeg om baderomsviften trekker?', 'Hold et papirark mot ventilen mens viften går. Suges arket fast, trekker den. Faller det ned, bør ventilen rengjøres eller viften sjekkes av en fagperson.'),
('Er mugg i taket på badet farlig?', 'Mugg kan gi plager, særlig for folk med astma og allergi. Vask det bort, finn årsaken og få en fagperson til å se på det hvis det kommer tilbake eller dekker et stort område.'),
('Hjelper strekktak mot mugg på badet?', 'Duken tar ikke opp fukt og kan tørkes av, og den skal aldri males. Men den erstatter ikke ventilasjonen. Fukten må fortsatt ut av rommet.'),
]),
]

from rad_articles_extra import EXTRA
ARTICLES = ARTICLES + EXTRA
