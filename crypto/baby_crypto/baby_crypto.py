from secret import flag
import random
from Crypto.Util.number import *

pt = int(flag.encode('hex'),16)
p = getPrime(2048)
q = getPrime(2048)
n = p*q
e = 65537
e0 = getPrime(233)
d0 = inverse(e0, (p-1)*(q-1))

assert pt < n

print 'pair:',(e0,d0)
print 'e:',e
print 'n:',n
print 'ct:',pow(pt,e,n)

#pair: (8687691944233534995769428277519740774644964770827863151475439847198691L, 112887984577524392100182952143180904679986378182146203219825450123549142135525185713296432380431460072206536951358771199758582663524595201907308211943493676519071920915863266937757446444946278192672899426518787299549804935906350724074930880934593108044528745161227623447334896788565109083836804664418799332592072793172182157284921700558055026872979883687632935462686857327386240959287282976908174875434748482283508832112086246831132830836492718724877641169737271793146436357839838631644209914745629722691746786497517947292325530748272264737365290758719247715713537012253265653278325111948938829497826412250796692814938694521420537483943174705493337432799970490326879404922287503530196722988496385269093882325702563390771203014373632481146994336435567738429684332666870544593713193133210730772227278308361202577786284884838925922873743858839407656487081202794142570359250112661272352894754440022532582348743756236904280139278009507585353407807076499487891753475552821229597245855120394125237012446911948799216402780665187301771471367741849220817015490912607932490730281589350665104688729464408420530130194681519880355715271584240167534526310083331556730658076144568645035282965817939033437795046888354229764094114528924890530231873171L)
#e: 65537
#n: 472978809784981830708598605480877392667372394603671272484215126525536572558537583995397068665183547100666856095421531598335410738256713171482338777929587987098803027326086098014226265042828066483169664944069896735074107498042462429104227439505281594838858284717461340911154396699315820029271230835576940181105156030931137698300002094132913173501720920515817709413888792685932814254049643727780553532496208058350735675863572201716670409450212022328155864592290304059618049810843075873671774570146389198947022563839723553295406610916879714380353843392067772043013707221089833579898941656582458462304041912513593491819564400471989725743125528396430971675608742185739588433686366526791443411283342989400364738039570167942006406283806881979249342452440658439104450721240892009279786863636024841846314948206570408529538978351297797975488798797302950685952524279971980280638286458750375113812987240422417279832196534728283059669001191359003800512865046835304884245269699069159886922793091361208810324004746956342141500442348932447646067399739439978843634285926396268133651757523619086735227485267995530224057990898601594764246504134503308203719249245132930004166083263842116208656903575459741569036685486274362916006360529237067122459317377
#ct: 265557795262424299583113278894984760665689619767388765852428558128745496396719755732264616032943623406190459966131156434943475805777188973603766481746220557982445847352811106105192080710667261813222899059208889259035651145297143459744612188860113860554852356836959397460940499812884618491829771359289677476399203534490197823769928853573280579246070438100985176646973900066392589448406008332432595280993825059921432295863240480451455146975725548338641381331690817554943445487254828075296564167491715721668763312564052655435580344018585065372484645208731358857886811502045398629536011946050683730535961777542903796113379705283836253934514299246233600065069217609345607894109836494933080483722593537492073695340807394800132306818325938950790504836659678544518310722738349021311453158362980447261677996846390495484071052703363125625252970453497861534080563036404889719936001515231177429010808734120710751229528309108097662209374194750440162243868335790699669161471454273066253011874681074783441599189011332736330016442135955840932222249605747575878213377978358129995256985096455832190615550395530178513748461495253143496566975038618231046364241747810564898916189722187040632378841432623189574976024766637957202837386047136831611203010415
