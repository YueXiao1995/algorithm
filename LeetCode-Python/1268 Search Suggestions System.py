"""
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.

Example 1:
    Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    Output: [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
    ]
    Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
    After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
    After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
    Input: products = ["havana"], searchWord = "havana"
    Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:
    Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
    Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:
    Input: products = ["havana"], searchWord = "tatiana"
    Output: [[],[],[],[],[],[],[]]

Constraints:
    1 <= products.length <= 1000
    1 <= Σ products[i].length <= 2 * 10^4
    All characters of products[i] are lower-case English letters.
    1 <= searchWord.length <= 1000
    All characters of searchWord are lower-case English letters.
"""
def suggestedProducts(products, searchWord):
    searchWord = list(searchWord)
    result = list()
    index = 0
    while index < len(searchWord):
        new_products_list = list()
        target = searchWord[index]
        for product in products:
            product = list(product)
            if len(product) > index:
                if product[index] == target:
                    new_products_list.append(("").join(product))
        result.append(new_products_list)
        products = new_products_list
        index += 1

    for i in range(len(result)):
        result[i] = sorted(result[i])
        if len(result[i]) > 3:
            result[i] = result[i][:3]


    return result

products1 = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord1 = "mouse"
print(suggestedProducts(products1, searchWord1))

products2 = ["havana"]
searchWord2 = "havana"
print(suggestedProducts(products2, searchWord2))

products3 = ["bags","baggage","banner","box","cloths"]
searchWord3 = "bags"
print(suggestedProducts(products3, searchWord3))

products4 = ["havana"]
searchWord4 = "tatiana"
print(suggestedProducts(products4, searchWord4))

products5 = ["tkruiswrcbzsbkwbhhvjzzuuiayqzbxjosjssacislcvbtcojpmyatkfgyx","tyqcpfvorznmxxdzsnkjnrkjelwoqorxsnyjqdnxfava","jumcvboxaxjfybdlezcjrarolxjtsuweaigkiudusinfmnczdualqzlpwkm","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnunflh","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckoktdj","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchviotvqi","tyqcpfvorznmxxdzsnkjnrrzpfgkhdwienfhpsqbyrvotbgchkkmvk","hcav","tyqcpfvorznmxxdzsnkjnrrzpfgknjxnepksgdzwxsbziwdzsiiyarxhtpp","ftujoohzvjonlwxwskeydoxpfvbvrdndbhgpuvykif","tyqcpfvorznmxxdzsnkjhvabtzucyooctzzrgehlsuyinrrnzjilfpalvqgwoey","hcvlnbmcrepblcqrvwpfsyevlpyldptubnxkntqhpounxjcw","tyqcpfvoxegnpqesbaugr","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnubpoqoghhgbpew","bteznmwyh","u","tyqcpfvorznmxxdzsnamc","tyqcpfvorznetvhiaobezckojwjbeg","csgadyglxddodloklsegvsbtgtkloklmxkbxxyorcqwybktuzpyeaqasn","mvrrbfbfwyrxooopgcbwmtjfepejyfrqdkyaqencqqlagoilrtdndfyn","tyqcpfvjijiwoup","tyqcpfvorznmxxdzsnkjn","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchviaxsw","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchxeyrnlh","oqojrvinnhlwuqllcsabkpfiusfucpjbsxzzhlgduawaqyp","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqvegfwmtdcrvdb","tyqitegmijccjwxuwvchbvuvllmgsdugzxdkiqvnllhmsjyskxpzzds","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvdertpdpdjsngezrnyjxotgonuigmqkgipgb","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchviof","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnccdnakfkhtg","ziarqmfvzqpqhunfxwfwjtetotozkjaszznbtrvtxarysaxq","tyqcpfvorznmxjnsgyirdtzpwywpnrvgadkmdjghlmerbqysaebyge","yesupowwycvcdbknhrkfyvnpoqtdhcbhybqvhnvgukoohh","tyqcpfvorznpkeynkmbbyptclmhxxlyjzejqbcatgfrmkbbmxs","tyqcpfvorznmxxdzsnkjnrrzpfourbghe","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuze","tyqcpfvorznmxxdzsnkjnrrzpfgknvfnzshqqfpr","zsbcqgctsjdjyfkdvcehawsqzacafwtjmhemfygdahkexvmkqkcehvek","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjghvqg","xusxbbilivpovzsjvfsdnacipk","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqggjwxdvqesbgrqei","ajqpomnpmsayhelmhfehjbvjaeszqigfqyuixbtyjy","etzqiepphjcleaocnwljcdn","tyqcpfzmlffhifutomuvfvwaqatopvur","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwreznx","jndewk","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnudxocavmwpggka","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwcpoxr","tyqcpfvorznmxxdzwilcfwrdlfqppdnuvgltuoooppwyomtvtggmsfxsxievdlsyame","tyqcpfvorznmxxdzsnkjnrrzpewgvvnicz","mzwjshgbgbdogqbrhfgbjkrqogyynbdwwkdclsbpynlrhxeucuuo","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvzquhbkvburnhmerkuabrfcjwanzmfenz","tyqcpfvorznmxxdzsnkjfesxjshxtlinfjltdfl","tyqcpfvorznmxxdzsnkjnrrzpfgknvqqngbpbdtufkgunalbekxbkpajlgbjtqmswh","eiuytvdzhcodcrdgthxynurtpsdyguupijjluucpfinrfnsjkdbbzexfmctejlgvd","tyqcpfvorznmyrzwhjxvhooytltygrakvgkqumrimazzhzoueyqnjz","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdcuudsuqq","tyqcpfvorznmxxdzsnkjnrrzpfgknvqorqffebhoyfvgkspenqpcmvoxpybkjg","tyqcpfvorznmxxdzsnkjnrrzpfgknvnlxdokehsjhiohwdeyikeajzipztzhwmxc","qmgnrjtavzsqtwareroiihendgcvbzbcolvfoanmixxrxdtnmtevvv","tyqcpfvokfxlbmbzmitacnromkoaoxl","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetxpdyhmk","tyqcpfvorznmxfmlzlcuikpxvahtfbfipjcgmeusshufvnirwcopdnvnop","tyqcpfvorznmxxdzsnkjnrfmy","txryxhtutwdrqmpcapbcrlmhzsobueefwfekusmmylr","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvdvagddprewvlgx","rniiqnzbctzeyeeyrxhfzqgbccplsncvtswcrqmevplfzadlulazmpmhdojwaokn","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchviob","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzakckmtmjxx","tyqcpfvorznmxxdzsnkjnrrumaqtylptffsjzygeumkahutdmalkqtrhtgrsrqcyyti","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqandxbuvshebs","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchvioncnr","lhehmbyzcnlwvr","tyqcpfvojuuprlby","tyqcpfvorznmiqmfrhihxsagizcrwyaukrjwbbgrxdzknq","ghhlssixrouzbqcpmxzmsnybaygtb","tyqcpfvorznmxxdzsnkjnrrzpdqanmxattjhgnflnoyynevsxvpbwfmfrnlc","frutebajqddrtrsmabfmdcgipssymldwscxbbrbpb","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbfmryrbgicgzqecje","gpsqlqorcbqffdxlnijgvzvxilnbkynwscuoymqyg","tyqcpfvorznmxxxvjwfgcwegpibuifhfxyomnicutaegshpnschktxknqytritr","pmpoycdxttisazazsgiswnsnhdmejpjbygvtjhwqydeugbouekvornbeiwmpehikbz","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchvie","yaxaddctugikoutgcwqsdekghoemtooljxvysnzqqvgpc","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwoyvqczogovza","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniaymgkdduoabmp","lwaxzivycjkanvikqpbrvdvjkaclyuyfitwfycsnfwjg","tyqcpgwivyfquxqhbkjbioekqbsd","tyqcpfyggtmjahhpjzwhohvchyofsxwkehq","iblyydfzztmtyjmgrxvyjwcobfyxcgyrbtnfhhxswxahze","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckohyof","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejysfrlewzsgukyahggau","yswdsvnzucvsdzrmeghevjrfuhoebfedvyvortaxppwqncmspctdcjlwdxfnc","tyqcpfvorznmbwmhfmudnurhismirfgvojpdmclw","tyqcpfvorznmxxdzkbqgrgeolnwhtvlckmiattpmxwwtmlifnexxbgtpjslwhczrjlhr","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchvqqy","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwghy","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzopnqxxcxshbhdmippldmcuxlvc","gilhnlfkdz","eidradnaqjwmucbrgtp","tyqcqqxonxtwakxlrceyknbockvovdwumbjkfrgmudiafbqlflonfavpsrfq","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqhlqnapfkcqpdb","kjundphljswl","jpfxangixfavlhcssecxljksydrjxmaldhwpftinywtbmffsmtslefcuddk","tyqcpfvorznmxxdzsnkjnrrztrqgpbvvxm","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbzw","bbufxzwpryyakbxuhwwplvdptgybbykqxirsrahsokviihxrawcbgwrktvgacmwtc","vlzfaamutsfqefpafzffwhvpfw","zlovtmburfkd","tyqcpfvorznmxxdzsuyushueegfrnlzbydnefcfagqnxglkulegntoml","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnunl","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbneryahanhrhkal","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetaoqgbczdcemzlmqemy","cxkwvaytkxgafeltbanhsvxlorigkuxnsxlmhvwqm","epbtkgnnupbbdqgheyaks","tyqcpfvorznmxxdzsnkjnrrzpfgkeduq","okoscfpxcndzgbtsozdofgnomtglmoaewgzzjvrxezoq","tyqcplghosxjviooiyddhvzzrhuuwkiosmgafxyajcdyqlmthqkoylxhtxdruw","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchvigzpo","zqrnaierpnsigujuxrftdiauazddadqmrwcimxyztwumwzyjcrqvuexnitdecfgo","tyqcpfvobzfvbiuoktjcqjfx","ybswoottdgryxtupichpvqjmcoytrwnfgzrrnaejojvpzmttlzw","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgcsfjgtwqqubbhjkzmio","zibrwfpwecubjlsjbkrhnvolnnzrqhdynloplzagwnuhpxhbvpxnqaifnln","stcphvgxvcaysehvrfdfllwvxf","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejemb","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnunix","ozmyertmnlwybntwxmpynuynhqdbqhosvjwexzqgvdtnvxexxwwwwhqktmzbfkjfn","rtbpifxevchngjnlumvtqtpebgtoznvvrzfxqzmcktoxydbstbvukrunnyeqwfd","lfjkcljnd","baizdtmgozykukcrkapsnp","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchidnpt","iamtabcpdagicnvdvqcfykonsazrbdivxtczpgqgxjrifukmqjw","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqyalwiaj","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqnzudhzclswotlbgdffwiekw","tyqcpfvrqwrcpusmfyhxaiasfbb","tyqcpqgaus","tyqcpfvacyrjvmadrmntxotgvgivdvcuwygpjfwcuppunolukrum","wds","tyqcpfvorzmjabuccipqln","tyqcpfvorznmxxdzsnkjnrrzpfvfcvufmzzuqrjubsfzp","tyqcpfvorznmxxdzepfxabibcagilwjsqncxnpjqsxjzqqqbae","iddmxxcmwecfutbrbqeihhlnypckofuhkbydmljfemzrvlxsuskxkbgviybzu","tyqcpfvorznigwmavbguxwhunsshdybhzszxvlnpingqgaghkqzeynbbbhgcxeydir","zmmirsxdhyxvmdybjzondyvrkzeafhvualsivfueweuusmsxbttdeofzeripaqv","tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnunqerptgas","tyqcpfudqjrabwwvdvwmsyscnazaxpsjjhetouegipqevvointclztzummwrrbntjlsj"]
searchWord5 = "tyqcpfvorznmxxdzsnkjnrrzpfgknvqvderckuzdqqgaqejetbnuniwwjbdchviotvdticwxwcliylrpvrokbcguhnfvpd"
print(suggestedProducts(products5, searchWord5))
