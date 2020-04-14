"""
706. Design HashMap
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)
"""
class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_size = 1000
        self.bucket_map = [None] * self.bucket_size



    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        bucket = key % self.bucket_size
        pointer = self.bucket_map[bucket]
        if pointer is not None:
            while pointer.key != key:
                if pointer.next is not None:
                    pointer = pointer.next
                else:
                    break

        else:
            self.bucket_map[bucket] = ListNode(key, value)
            return
        if pointer.key == key:
            pointer.val = value
        else:
            pointer.next = ListNode(key, value)


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket = key % self.bucket_size
        pointer = self.bucket_map[bucket]
        while pointer is not None and pointer.key != key:
            pointer = pointer.next
        if pointer is None:
            return -1
        else:
            return pointer.val



    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        bucket = key % self.bucket_size
        pointer = self.bucket_map[bucket]
        prev_pointer = None
        while (pointer is not None) and pointer.key != key:
            prev_pointer = pointer
            pointer = pointer.next
        if pointer is not None and pointer.key == key:
            if prev_pointer is not None:
                prev_pointer.next = pointer.next
            else:
                self.bucket_map[bucket] = pointer.next

hashmap = MyHashMap()


# action = ["put","remove","get","put","remove","remove","put","put","get","get","put","put","remove","put","put","get","put","put","put","put","remove","put","put","remove","put","remove","get","remove","put","put","put","put","put","remove","put","put","put","put","put","put","put","put","put","remove","put","put","put","remove","put","put","remove","remove","put","remove","put","put","put","remove","put","put","put","get","put","put","put","put","put","remove","put","get","put","get","put","remove","put","put","put","remove","put","remove","put","put","put","get","put","put","put","get","put","put","put","get","put","put","put","remove","remove","remove","put","put","remove","put","put","remove","get","put","put","put","remove","put","remove","put","get","remove","remove","put","put","put","put","put","get","put","put","get","get","put","put","put","remove","put","put","get","put","put","remove","put","put","put","put","put","put","put","put","remove","put","put","put","get","get","get","put","put","get","remove","put","put","get","get","remove","put","put","put","put","put","put","put","get","put","remove","put","remove","put","remove","put","put","put","put","put","put","put","remove","put","put","put","put","remove","get","put","put","put","remove","put","put","put","put","put","put","put","put","put","get","put","put","put","put","put","put","remove","put","get","put","remove","put","put","get","put","get","get","put","remove","put","put","put","put","put","put","put","put","put","get","put","remove","put","remove","remove","put","remove","put","put","put","put","put","put","get","put","put","put","put","put","put","put","put","put","put","put","put","remove","get","put","put","get","get","put","get","get","remove","put","put","put","put","put","put","remove","remove","put","put","put","remove","put","put","put","put","put","put","put","put","put","get","get","put","put","get","put","get","get","put","put","put","put","remove","put","get","get","remove","put","put","remove","put","get","put","put","remove","get","put","put","put","remove","put","put","put","put","put","remove","put","put","put","put","put","put","put","put","put","put","put","get","remove","put","put","remove","put","remove","remove","get","put","put","get","put","put","put","put","put","put","put","put","remove","put","put","remove","put","put","get","put","put","put","put","get","put","remove","put","put","put","remove","remove","remove","remove","get","put","put","put","put","put","put","put","put","put","put","get","put","put","put","put","put","get","put","get","put","put","get","get","remove","get","put","put","put","remove","get","put","get","put","put","get","put","remove","get","put","remove","put","put","put","remove","put","get","put","put","put","put","put","get","put","put","put","get","put","put","put","put","put","remove","put","get","put","put","put","put","put","put","remove","put","get","remove","get","remove","put","put","put","put","remove","put","put","put","put","get","get","get","put","put","put","put","put","put","put","remove","put","put","put","put","put","get","put","put","remove","get","put","put","remove","put","put","put","get","put","put","remove","remove","put","remove","remove","put","put","put","put","put","get","put","remove","put","put","remove","put","put","put","put","get","put","remove","remove","remove","put","get","put","put","remove","put","put","put","put","get","put","put","put","get","put","put","put","put","remove","put","put","put","put","put","get","put","remove","put","put","put","put","put","put","put","put","put","put","remove","put","remove","put","put","put","put","put","put","put","put","put","put","remove","put","remove","put","put","get","put","put","put","put","put","put","put","get","remove","put","get","put","put","put","put","put","put","put","get","remove","put","put","put","put","put","put","put","put","put","put","put","get","put","put","put","put","get","put","put","put","get","remove","get","put","put","put","get","put","remove","get","put","put","remove","put","put","put","put","get","put","put","put","put","put","get","put","put","put","put","put","put","put","put","put","put","put","remove","put","put","put","get","put","put","put","put","get","get","get","put","put","remove","put","put","get","put","get","put","put","put","put","put","put","put","get","put","remove","put","put","put","remove","remove","put","remove","get","put","put","put","put","put","remove","remove","put","put","put","put","get","put","put","put","get","put","put","put","remove","put","remove","get","put","get","remove","put","get","get","get","put","get","put","put","get","put","put","put","put","get","put","put","put","get","put","remove","put","put","put","put","put","remove","get","get","put","put","put","remove","get","put","remove","put","put","put","get","put","put","remove","put","put","put","put","remove","remove","put","get","put","put","put","put","remove","put","put","put","put","put","put","put","put","put","put","put","put","put","put","remove","put","remove","put","remove","put","put","put","remove","get","put","put","put","get","put","put","put","put","remove","put","put","get","put","get","get","put","put","put","put","put","put","put","put","put","get","put","get","put","put","get","remove","remove","put","put","get","get","put","put","put","put","put","put","put","put","put","put","put","put","put","put","put","put","put","put","put","put","put","put","put","remove","put","put","put","put","put","put","put","put","get","remove","put","put","put","put","put","put","get","get","put","put","get","put","get","put","put","put","put","get","put","put","remove","get","get","get","put","remove","get","put","remove","get","put","put","remove","remove","remove","put","remove","put","put","put","put","put","remove","remove","put","remove","get","remove","put","put","put","put","put","put","put","put","put","get","remove","get","put","put","remove","get","put","get","put","put","get","get","get","put","get","remove","get","put","put","remove","put","put","put","get","put","put","remove","put","remove","put","remove","get","remove","put","remove","put","put","get","put","put","put","put","put","put","remove","get","put","put","get","put","put","put","put","put","put","put","put","put","put","get","put","get","put","get","put","get","put","put","put","put","put","put","put","put","put","put","remove","put","put","get","put","put"]
# value = [[504,155],[89],[334],[570,521],[504],[504],[507,661],[175,641],[504],[672],[705,515],[140,609],[309],[588,453],[715,420],[175],[219,179],[267,88],[899,365],[865,707],[184],[214,491],[878,462],[155],[392,988],[932],[504],[797],[495,398],[473,322],[797,365],[673,663],[36,260],[950],[165,645],[537,211],[162,509],[721,166],[614,725],[947,630],[73,570],[317,261],[407,407],[392],[566,440],[153,521],[455,261],[728],[786,278],[964,222],[797],[317],[191,749],[786],[735,561],[148,639],[114,129],[537],[100,452],[845,643],[639,858],[140],[207,929],[691,601],[599,520],[463,611],[662,996],[795],[750,586],[61],[585,883],[73],[270,238],[845],[644,620],[396,225],[605,466],[25],[203,341],[219],[840,931],[967,946],[286,941],[175],[749,711],[449,681],[504,923],[481],[918,89],[875,656],[755,84],[368],[69,553],[650,80],[789,371],[705],[495],[69],[789,974],[444,635],[739],[174,259],[503,976],[691],[79],[157,321],[607,768],[377,600],[793],[611,804],[162],[746,743],[981],[191],[947],[71,587],[200,131],[320,9],[828,249],[94,374],[976],[898,589],[720,557],[407],[100],[118,535],[249,824],[650,854],[918],[562,665],[195,748],[294],[386,593],[721,787],[94],[746,589],[822,358],[587,566],[778,573],[920,290],[801,786],[315,89],[870,33],[660],[435,882],[687,796],[316,699],[642],[149],[504],[633,967],[564,772],[392],[605],[637,992],[665,589],[444],[191],[392],[289,497],[79,352],[962,896],[137,616],[361,929],[976,631],[126,960],[846],[386,65],[661],[210,729],[79],[98,519],[638],[567,947],[179,302],[929,353],[276,100],[116,937],[859,454],[620,801],[567],[854,20],[883,386],[744,482],[331,827],[635],[750],[924,13],[89,120],[374,812],[924],[992,87],[602,78],[610,515],[238,645],[449,440],[624,366],[395,248],[437,2],[183,311],[437],[504,17],[203,112],[981,297],[968,434],[200,39],[643,16],[599],[861,365],[442],[421,837],[55],[808,204],[60,347],[364],[18,361],[260],[264],[963,63],[632],[832,642],[598,326],[42,145],[710,455],[321,142],[847,668],[98,299],[113,342],[273,683],[102],[301,29],[18],[894,627],[351],[286],[558,316],[620],[360,444],[860,742],[855,784],[900,902],[121,851],[391,32],[200],[451,737],[503,337],[955,785],[357,697],[350,885],[620,831],[281,306],[637,948],[111,565],[193,565],[988,489],[920,113],[620],[765],[797,806],[281,34],[396],[479],[221,915],[648],[116],[939],[138,719],[98,532],[715,805],[915,202],[162,184],[307,394],[992],[639],[462,156],[851,10],[911,767],[870],[744,222],[156,803],[289,151],[858,766],[243,127],[83,892],[912,94],[878,179],[203,905],[242],[721],[744,726],[912,988],[345],[903,885],[18],[703],[995,163],[689,400],[883,555],[552,241],[462],[322,638],[200],[607],[98],[179,250],[789,761],[713],[745,965],[978],[84,639],[395,761],[662],[89],[39,421],[86,124],[324,997],[108],[819,421],[410,346],[968,306],[17,41],[562,537],[18],[914,570],[25,463],[791,777],[962,14],[367,208],[519,577],[282,565],[499,939],[804,310],[918,110],[804,585],[435],[614],[615,395],[834,409],[854],[774,236],[503],[207],[71],[593,842],[474,421],[744],[413,293],[623,927],[706,660],[920,237],[286,161],[573,277],[654,905],[323,282],[320],[572,670],[851,47],[25],[31,837],[710,167],[855],[657,382],[939,676],[213,31],[590,666],[930],[1,766],[982],[140,275],[793,471],[769,443],[919],[39],[114],[476],[249],[706,899],[622,986],[254,184],[617,465],[996,822],[506,432],[585,429],[832,256],[179,929],[966,534],[134],[108,437],[849,551],[568,572],[779,859],[548,273],[281],[920,620],[83],[60,597],[115,791],[254],[51],[308],[573],[318,940],[886,329],[916,794],[899],[434],[623,567],[588],[189,566],[770,42],[877],[143,472],[614],[690],[477,716],[326],[501,822],[800,907],[685,884],[614],[614,656],[694],[960,977],[804,360],[212,306],[440,857],[856,93],[435],[986,770],[50,555],[591,159],[590],[820,170],[291,782],[212,298],[5,637],[784,402],[628],[313,58],[130],[367,570],[572,954],[105,544],[458,503],[48,571],[335,973],[344],[169,312],[548],[605],[435],[577],[858,993],[792,315],[478,311],[546,951],[116],[434,156],[331,674],[293,645],[60,206],[671],[939],[650],[994,478],[31,513],[957,25],[795,402],[51,464],[102,876],[698,101],[569],[309,179],[718,712],[984,670],[383,728],[291,299],[746],[584,49],[600,39],[898],[115],[268,779],[477,656],[860],[884,238],[288,479],[990,664],[624],[473,581],[753,443],[650],[421],[996,18],[994],[191],[382,956],[681,570],[982,924],[899,901],[707,635],[275],[793,541],[507],[880,525],[642,998],[449],[661,507],[589,10],[127,58],[226,785],[685],[610,974],[632],[109],[488],[44,298],[258],[734,107],[553,350],[959],[891,680],[27,475],[47,182],[639,310],[644],[624,176],[187,932],[350,477],[572],[563,752],[911,278],[297,281],[417,81],[643],[600,516],[3,95],[181,195],[274,637],[248,392],[89],[200,707],[631],[413,281],[828,846],[242,626],[777,391],[576,137],[902,416],[969,842],[206,131],[366,912],[159,896],[118],[732,45],[620],[24,639],[941,527],[527,631],[501,152],[909,626],[235,433],[865,889],[673,762],[86,429],[111,992],[18],[503,283],[770],[216,440],[526,518],[631],[272,297],[868,627],[907,600],[89,597],[477,894],[820,524],[725,715],[608],[689],[205,365],[50],[72,103],[145,749],[981,662],[339,275],[307,383],[786,667],[770,241],[249],[622],[209,876],[526,679],[945,118],[352,942],[106,95],[666,723],[860,677],[655,315],[675,805],[225,789],[385,873],[439],[103,321],[619,729],[432,285],[630,993],[112],[221,936],[908,166],[326,638],[881],[326],[784],[647,464],[559,192],[940,236],[954],[551,497],[703],[566],[613,683],[0,414],[548],[421,153],[186,907],[435,190],[89,335],[255],[468,585],[821,402],[446,705],[211,520],[671,475],[449],[204,674],[634,370],[560,406],[377,869],[780,656],[915,153],[984,193],[697,173],[571,423],[879,42],[898,744],[410],[469,831],[49,178],[371,182],[623],[636,720],[722,662],[52,548],[485,805],[134],[440],[289],[461,414],[143,881],[289],[881,961],[65,586],[449],[433,846],[778],[370,699],[419,702],[605,993],[360,544],[80,757],[801,371],[39,599],[602],[583,499],[164],[313,829],[34,705],[485,601],[915],[53],[232,560],[265],[572],[406,784],[747,362],[108,25],[648,774],[553,292],[221],[316],[982,650],[762,924],[211,653],[393,962],[977],[121,853],[224,34],[990,992],[309],[870,868],[983,64],[959,200],[377],[787,623],[138],[520],[883,385],[909],[923],[701,741],[190],[382],[361],[673,741],[605],[906,700],[181,547],[949],[160,652],[450,829],[235,740],[455,72],[116],[404,706],[470,291],[885,186],[48],[259,726],[725],[7,332],[68,828],[632,383],[525,955],[622,223],[324],[164],[698],[712,971],[816,546],[911,301],[713],[111],[537,282],[364],[151,597],[343,30],[696,167],[31],[58,738],[461,112],[970],[92,242],[966,608],[43,869],[646,532],[373],[451],[595,492],[393],[224,841],[477,273],[663,328],[455,242],[566],[797,401],[205,841],[166,308],[285,170],[983,16],[592,182],[950,235],[620,429],[941,344],[360,430],[948,715],[868,198],[945,742],[187,391],[153],[327,342],[593],[718,281],[276],[551,14],[673,901],[693,911],[189],[72],[756,314],[769,712],[947,326],[222],[872,174],[97,415],[474,275],[27,426],[238],[910,945],[494,56],[497],[338,413],[998],[203],[427,359],[215,761],[282,150],[523,449],[186,325],[380,427],[196,735],[217,291],[740,657],[711],[695,194],[754],[973,921],[429,597],[58],[300],[50],[815,881],[778,776],[922],[272],[581,125],[856,910],[841,995],[157,11],[223,817],[551,282],[159,324],[832,96],[518,411],[849,245],[253,571],[140,437],[187,640],[788,224],[761,954],[196,510],[361,614],[127,790],[163,804],[735,276],[401,463],[561,230],[800,251],[639],[859,938],[735,12],[953,344],[138,460],[218,54],[632,170],[602,903],[846,642],[831],[871],[94,726],[392,118],[658,154],[706,305],[795,782],[798,248],[964],[165],[286,499],[346,281],[473],[996,151],[475],[688,363],[190,491],[759,350],[918,220],[685],[371,565],[173,151],[683],[253],[891],[326],[534,152],[583],[770],[240,42],[612],[162],[130,364],[458,716],[220],[273],[811],[287,744],[624],[343,858],[198,806],[904,680],[858,686],[680,729],[327],[315],[309,0],[753],[830],[427],[881,440],[281,73],[737,252],[938,831],[815,833],[316,36],[668,763],[433,312],[930,235],[700],[466],[576],[398,157],[314,73],[535],[198],[977,603],[687],[106,978],[948,936],[996],[865],[591],[245,75],[470],[363],[470],[967,403],[841,128],[856],[906,780],[681,22],[278,449],[295],[706,232],[893,912],[936],[755,210],[717],[855,190],[744],[39],[781],[200,137],[634],[957,50],[78,894],[960],[53,825],[781,422],[710,659],[335,495],[303,45],[617,190],[904],[339],[790,178],[723,150],[661],[417,641],[550,894],[656,913],[795,887],[974,226],[750,873],[155,369],[327,87],[899,978],[896,104],[580],[399,207],[851],[72,713],[366],[382,334],[103],[615,835],[826,220],[861,628],[206,421],[496,694],[82,358],[451,609],[89,865],[476,346],[335,928],[387],[529,939],[101,691],[698],[21,493],[565,197]]

action = ["put", "get", "remove", "get"]
value = [[1,100], [1], [1], [1]]

for i in range(len(action)):
    if action[i] == 'put':
        hashmap.put(value[i][0], value[i][1])
    elif action[i] == 'remove':
        hashmap.remove(value[i][0])
    elif action[i] == 'get':
        print(hashmap.get(value[i][0]))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)