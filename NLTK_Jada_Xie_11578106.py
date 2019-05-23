#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import PlaintextCorpusReader


# In[2]:


raw = open('Trainspotting by Irving Welsh - First 1100 words.txt').read()
i = 0
m = 0 
n = 0 #counters

#trimming and cleaning the text
raw = raw[336:len(raw)-1] #trimming
raw = raw.replace("\\", "")

  
#sentences    
s_tokens = nltk.sent_tokenize(raw)
sentences = [s.lower() for s in s_tokens]

for s in sentences:
    if "fuck" in s:
        i = i + 1
    if "!" in s:
        m = m + 1
    if "?" in s:
        n = n + 1

#words and vocab
w_tokens = nltk.word_tokenize(raw)
words = [word.lower() for word in w_tokens if word.isalpha()]

print("The number of words is:", len(words))

vocab = sorted(set(words))
print("The vocabulary size is:", len(vocab))
print("The number of sentences is:", len(sentences))
print("The number of exclamatory sentences is:", m)
print("The number of interrogative sentences is:", n)

fdist1 = nltk.FreqDist(words)
print("The most frequent 8 words are:", fdist1.most_common(8))

print("Bonus: The number of sentences that contains the word stem fuck is:", i)


# In[3]:


from nltk import CFG
from nltk.grammar import FeatureGrammar
from nltk.parse import RecursiveDescentParser, FeatureEarleyChartParser

def check_sentence(parser, sentence):
    print("--------------------------------------------------")
    print("Checking if provided sentence matches the grammar:")
    print(sentence)
    if isinstance(sentence, str):
        sentence = sentence.split()
    tree_found = False
    results = parser.parse(sentence)
    for tree in results:
        tree_found = True
        print(tree)
    if not tree_found:
        print(sentence, "Does not match the provided grammar.")
    print("--------------------------------------------------")
    return tree_found


# In[4]:


cfg_1 = CFG.fromstring("""

  S -> NP VP
  S -> VP NP
  S -> NP CP NP
  S -> VP NP VP
  S -> NP VP CP VP
  S -> NP CP NP VP
  S -> CP NP VP NP
  S -> NP CP NP CP NP
  
  S -> ProN
  S -> InterJ
  S -> WH AuxV NP
  S -> PP NP

  Comp -> N N
  
  NP -> Det N
  NP -> Det N Adv
  NP -> Det AdjP N

  AdjP -> Adj Adj
  AdjP -> Adv Adj
  AdjP -> Adj Adj CP Adj
  
  NP -> ProN 
  NP -> AdjP ProN
  NP -> AdjP N
  NP -> AdjP Comp
  NP -> ProN N 
  NP -> ProN VP
 
  NP -> Adv AdjP N
  
  NP -> Adv NP PP

  VP -> CP VP PP 
  VP -> AuxV VP
  VP -> AuxV V
  VP -> AuxV NP
  VP -> AuxV AdjP
  VP -> AuxV AdjP PP
  VP -> AuxV AdjP IP
  
  VP -> V NP
  VP -> V NP VP
  VP -> V NP CP NP
  VP -> V NP PP CP NP
  VP -> V NP CP NP PP
  VP -> AuxV VP PP
  VP -> V NP PP
  VP -> V ProN
  VP -> V ProN Adj
  VP -> V ProN NP
  VP -> V NP Adv
  VP -> AuxV Adv NP
  VP -> V AdjP VP
  
  VP -> V PP 
  VP -> V PP NP
  VP -> V PP VP
  VP -> V Prep CP NP
  VP -> V Prep PP
  VP -> V Adv VP
  VP -> V Adv PP
  VP -> Adv V Prep PP
  VP -> Adv VP
  VP -> V Prep AdjP
  VP -> V CP NP VP
  
  VP -> V IP
  VP -> AuxV IP
  IP -> IPrep VP
  IP -> IPrep V
  IP -> Adv IP
  
  PP -> Prep N
  PP -> Prep NP
  PP -> Adv Prep NP
  PP -> Prep Comp
  PP -> AdjP Adv NP
  PP -> IP CP VP
  
  CP -> CC
  CP -> Adv CC
  CP -> CC CC
  
  
  Det -> "a" | "an" | "any" | "the" | "that" | "one"
  WH -> "what" | "whit" | "whae" | "when"
  Prep -> "wi" | "fir" | "withoot" | "aboot" | "against" | "at" | "before" | "by" | "in" | "fuckin" | "intae" | "later" | "oan" | "ower" | "tae" | "than" | "through" | "up" | "ay"
  IPrep -> "tae"
  AuxV -> "will" | "would" | "have" | "wouldnae" | "wisnae" | "wis" | "wir" | "wid" | "am" | "widae" | "were" | "are" | "be" | "been" | "did" | "didnae" | "dinnae" | "do" | "does" | "hud" | "hudnae" | "huv" | "is" | "has" 
  V ->  "haud" | "gitting" | "supposed" | "opening" | "notice" | "add" | "asks" | "based" | "baws" | "beating" | "breathing" | "bringing" | "building" | "bulging" | "call" | "called" | "came" | "charged" | "comin" | "congregated" | "covered" | "craned" | "done" | "doubt" | "draggin" | "emphasise" | "faster" | "feel" | "fling" | "flings" | "focusing" | "freezing" | "harassing" | "hing" | "introducing" | "knowing" | "lashing" | "looking" | "saying" | "shaking" | "sitting" | "standing" | "sticking" | "straining" | "suffering" | "trembling" | "willing" | "gittin" | "lovin" | "makin" | "pleadin" | "sayin" | "standin" | "sufferin" | "takin" | "tryin" | "walkin" | "wastin" | "fuck" | "gasped" | "gestured" | "gie" | "git" | "go" | "goat" | "happens" | "hit" | "hope" | "keep" | "ken" | "kent" | "leave" | "let" | "live" | "look" | "looked" | "looks" | "meant" | "move" | "moves" | "muttered" | "need" | "piled" | "played" | "pokes" | "preferred" | "protested" | "raises" | "remember" | "rests" | "sais" | "saw" | "scored" | "see" | "seem" | "seemed" | "set" | "shouted" | "shouts" | "smash" | "snapped" | "snarled" | "sped" | "splatterd" | "stares" | "started" | "stoaped" | "switched" | "take" | "think" | "tried" | "turns" | "ur" | "walk" | "want" | "wanted" | "wants" | "watch" | "went" | "involved" 
  Adj -> "some" | "moosey-faced" | "aqua" | "sure" | "aw" | "money-grabbin" | "young" | "advance" | "amused" | "another" | "arrogant" | "auld" | "back" | "better" | "black" | "chuffed" | "crapping" | "crusing" | "dandy" | "dastardly" | "doss" | "dramatic" | "enough" | "every" | "fat" | "feart" | "few" | "fifty" | "first" | "irritating" | "fuckin" | "fucked" | "good" | "here" | "hostile" | "hunted" | "intense" | "irresistible" | "lazy" | "long" | "longer" | "lowest" | "lucky" | "mair" | "measley" | "middle" | "nae" | "next" | "obligatory" | "other" | "petty" | "poignant" | "poxy" | "purple" | "rich" | "right" | "same" | "serious" | "sick" | "side" | "silent" | "smart" | "such" | "supposed" | "this" | "trivial" | "weak" | "wee"
  ProN -> "another" | "what" | "jeanclaude" | "youse" | "yir" | "ye" | "ya" | "white" | "wester" | "ah" | "aye" | "chancey" | "hailes" | "he" | "him" | "his" | "hissel" | "it" | "johnny" | "ma" | "maist" | "mclean" | "mcleans" | "me" | "mines" | "nae" | "oor" | "porty" | "raymie" | "rents" | "ritz" | "seeker" | "si" | "sickboy" | "simon" | "simone" | "mothersuperior" | "swan" | "swanney" | "that" | "them" | "there" | "these" | "they" | "thir" | "thistle" | "um" | "urn" | "us" | "jeanclaudevandamme" | "we"
  N -> "jackjones" | "leithwalk" | "wey" | "windae" | "flat-top" | "shell-suit" | "swedgin" | "opening" | "yards" | "withdrawal" | "way" | "ain" | "animal" | "anxiety" | "anything" | "associates" | "attention" | "august" | "aw" | "back" | "bairn" | "bastard" | "bastards" | "betrayal" | "bomber" | "box" | "boy" | "brar" | "cab" | "case" | "ceiling" | "charges" | "church" | "conviction" | "cunt" | "cunts" | "days" | "dealer" | "deek" | "door" | "driver" | "drivers" | "earth" | "energy" | "eyes" | "feet" | "festival" | "fit" | "nothing" | "vermin" | "villain" | "yin" | "forefinger" | "form" | "friends" | "fucker" | "game" | "gear" | "gob" | "god" | "group" | "guy" | "guys" | "hall" | "hame" | "hand" | "handset" | "hassle" | "heid" | "hundred" | "jaykit" | "jaykits" | "junk" | "last" | "leith" | "lips" | "man" | "mate" | "minute"| "misery" | "mob" | "money" | "movies" | "neck" | "need" | "notice" | "one" | "pence" | "phase" | "picture" | "pish" | "plot" | "point" | "post" | "radge" | "radges" | "rank" | "rhythm" | "ride" | "saps" | "schemes" | "score" | "second" | "seriousness" | "shellsuits" | "shoap" | "show" | "sidekick" | "sighthill" | "sinews" | "size" | "squad" | "square" | "summer" | "sweat" | "taxi" | "taxis" | "telly" | "tension" | "testimonies" | "then" | "thighs" | "time" | "tod" | "tollcross" | "video" | "visage" | "voice" | "Walk" | "waste"
  Adv -> "too" | "ready" | "straight" | "screaming" | "oot" | "sick" | "first" | "not" | "up" | "ay" | "doon" | "thegither" | "yet" | "also" | "back" | "breathlessly" | "deliberately" | "deliriously" | "desperately" | "else" | "even" | "ever" | "eywis" | "fuckin" | "heavily" | "here" | "incrementally" | "jist" | "just" | "nervously" | "never" | "nivir" | "no" | "now" | "oaf" | "off" | "once" | "only" | "probably" | "rather" | "real" | "really" | "sae" | "so" | "sure" | "thair" | "then" | "too" | "truly" | "usually" | "well"
  CC -> "when" | "yet" | "while" | "and" | "as" | "because" | "but" | "fae" | "fi" | "fir" | "if" | "like" | "n" | "or" | "so" | "that" | "thit" | "though"
  InterJ -> "taxi" | "aw" | "aye" | "fuckin" | "hi"
""")

cfg_1_parser = nltk.RecursiveDescentParser(cfg_1)
#"yir" in "yir no feart ay they wee fuckin saps ur ye?"  --> "you are feart ay they wee fuckin saps ur ye?"
  #"yuv" See whit yuv done now, ya big-moothed cunt. --> See whit you have done nnow, ya big-moothed cunt. 
    #"oafay" (off of) in the original text is re-written as "oaf" (Adv) and "ay" (Prep). Compounds are broken up to simplify part-of-speech tagging.
    
#check_sentence(cfg_1_parser, 'the sweat wis lashing oaf ay sickboy')
#"sick boy" and further pronouns composed with two words are simplifed by eliminating the space between the words. This is done to reduce ambiguity (since Welsh nicknames his character with names highly similar to NPs.)
#check_sentence(cfg_1_parser, 'he wis trembling')
#the semicolon has been replaced with a dot before "he wis trembling" to simplify the usage of semicolons. 
#check_sentence(cfg_1_parser, 'ah wis jist sitting thair focusing oan the telly tryin no tae notice the cunt')
#commas in a long sentence are eliminated for the parser. 
#check_sentence(cfg_1_parser, 'he wis bringing me doon')
#check_sentence(cfg_1_parser, 'ah tried tae keep ma attention oan the jeanclaudevandamme video')
#check_sentence(cfg_1_parser, 'they started oaf wi an obligatory dramatic opening as happens in such movies')
check_sentence(cfg_1_parser, 'then the next phase ay the picture involved building up the tension through introducing the dastardly villain and sticking the weak plot thegither')
#check_sentence(cfg_1_parser, 'any minute now though auld jeanclaude is ready tae git doon tae some serious swedgin') #eliminated ready for now
#((any minute) now). NP -> Det N Adv
#the apostrophy s is modifed to be xx is. For the sake of simplicity.
#check_sentence(cfg_1_parser, 'rents')
#check_sentence(cfg_1_parser, 'ah have goat tae see mothersuperior')
#ah've -> ah have. 
#ah have goat tae see mothersuperior, sickboy gasped, shaking his heid. Example of sentence broken up
#check_sentence(cfg_1_parser, 'sickboy gasped shaking his heid')
#check_sentence(cfg_1_parser, 'aw') #sentence broken up
#check_sentence(cfg_1_parser, 'ah sais') 
#ah wanted the radge tae jist fuck off ootay ma visage, tae go oan his ain n jist leave us wi jeanclaude

########

#check_sentence(cfg_1_parser, 'ah wanted the radge oot ay ma visage tae go oan his ain n jist leave us wi jeanclaude') #example of sentence combined. Getting rid of "tae jist fuck off"
   ##check_sentence(cfg_1_parser, 'oan the other hand ah would be gitting sick tae')  #at the moment, the before long at the end of the sentence is ignored. 
   ##check_sentence(cfg_1_parser, 'and if that cunt went n scored he would haud oot oan us')

   ##check_sentence(cfg_1_parser, 'they call um sickboy no because he is eywis sick wi junk withdrawal but because he is just one sick cunt')
   ##check_sentence(cfg_1_parser, 'let us fuckin go') #sentence split
   ##check_sentence(cfg_1_parser, 'he snapped desperately')
   ##check_sentence(cfg_1_parser, 'haud oan a second')
   ##check_sentence(cfg_1_parser, 'ah wanted tae see jeanclaude smash up this arrogant fucker')
#check_sentence(cfg_1_parser, 'ah wouldnae git tae watch it') 

#check_sentence(cfg_1_parser, 'ah would be too fucked by the time we goat back')
#check_sentence(cfg_1_parser, 'and in any case it wid probably be a few days later')
#check_sentence(cfg_1_parser, 'that meant ah wouldd git hit fir fuckin back charges fi the shoap oan a video ah hudnae even goat a deek at')
  ##check_sentence(cfg_1_parser, 'ah have goat tae fuckin move') #eliminated "man" in the end to reduce ambig
  ##check_sentence(cfg_1_parser, 'he shouts standing up')
#check_sentence(cfg_1_parser, 'he moves ower tae the windae and rests against it breathing heavily looking like a hunted animal')
  ##check_sentence(cfg_1_parser, 'there is nothing in his eyes but need')
  ##check_sentence(cfg_1_parser, 'ah switched the box oaf at the handset')
  ##check_sentence(cfg_1_parser, 'fuckin waste')
#check_sentence(cfg_1_parser, 'that is aw it is')  #sentence split
  ##check_sentence(cfg_1_parser, ' a fuckin waste')
  ##check_sentence(cfg_1_parser, 'ah snarled at the cunt the fuckin irritating bastard')
  ##check_sentence(cfg_1_parser, 'he flings back his heid n raises his eyes tae the ceiling')
  ##check_sentence(cfg_1_parser, 'ah will gie ye the money tae git it oot') #deleted back from back oot

#check_sentence(cfg_1_parser, 'is that aw yir sae fuckin moosey-faced aboot')
  ##check_sentence(cfg_1_parser, 'fifty measley fuckin pence oot ay ritz')
#check_sentence(cfg_1_parser, 'this cunt has a wey ay makin ye feel a real petty trivial bastard')
#check_sentence(cfg_1_parser, 'that is no the fuckin point')  #sentence split
  ##check_sentence(cfg_1_parser, 'ah sais withoot conviction') #deleted but from but withoot conviction
  ##check_sentence(cfg_1_parser, 'aye')
#check_sentence(cfg_1_parser, 'The point is ah'm really fuckin sufferin here, n ma so-called mate's draggin his feet deliberately, lovin every fuckin minute ay it')
#check_sentence(cfg_1_parser, 'His eyes seem the size ay fitba's n look hostile, yet pleadin at the same time')
  ##check_sentence(cfg_1_parser, 'poignant testimonies tae ma supposed betrayal')
#check_sentence(cfg_1_parser, 'If ah ever live long enough tae huv a bairn, ah hope it never looks at us like Sick Boy does')#check_sentence(cfg_1_parser, 'The cunt is irresistible oan this form')
  ##check_sentence(cfg_1_parser, 'ah wis not')  #wisnae -> wis nae -> wis not. Not added to vocab
  ##check_sentence(cfg_1_parser, 'ah protested')
#check_sentence(cfg_1_parser, 'fling yir fuckin jaykit oan well')
#check_sentence(cfg_1_parser, 'at the fit ay the Walk thir wir nae taxis')
  ##check_sentence(cfg_1_parser, 'they only congregated here when ye didnae need them')
#check_sentence(cfg_1_parser, 'supposed tae be August, but ah'm fuckin freezing ma baws oaf here')
#check_sentence(cfg_1_parser, 'ah am no sick yet but it is in the fuckin post')
#check_sentence(cfg_1_parser, 'that is fir sure')
   ##check_sentence(cfg_1_parser, 'supposed tae be a rank')
   ##check_sentence(cfg_1_parser, 'supposed tae be a fuckin taxi rank')   
   ##check_sentence(cfg_1_parser, 'nivir fuckin git one in the summer')
#check_sentence(cfg_1_parser, 'up cruising fat rich festival cunts too fuckin lazy tae walk a hundred fuckin yards fae one poxy church hall tae another fir thir fuckin show')
  ##check_sentence(cfg_1_parser, 'taxi drivers')
  ##check_sentence(cfg_1_parser, 'money-grabbin bastards')
#check_sentence(cfg_1_parser, 'sickboy muttered deliriously and breathlessly tae hissel, eyes bulging and sinews in his neck straining as his heid craned up leithwalk ')
  ##check_sentence(cfg_1_parser, 'at last one came')
#check_sentence(cfg_1_parser, 'there were a group ay young guys in shellsuits n bomber jaykits whae had been standin thair longer than us')
  ##check_sentence(cfg_1_parser, 'ah doubt if sickboy even saw them')

  ##check_sentence(cfg_1_parser, 'he charged screaming intae the middle ay the Walk') #moved the adverb screaming behind the verb, to accomedate for the the VP -> Adv VP (not VP -> VP Adv). Deleted "oot".    #straight intae the middle ay the walk causes a few too many trees. 
  #first time i specifed capital letters, to reduce ambiguity of Walk (street) and walk. 

  ##check_sentence(cfg_1_parser, 'taxi')
  ##check_sentence(cfg_1_parser, 'hi ')
  ##check_sentence(cfg_1_parser, 'whit is the score')
#check_sentence(cfg_1_parser, 'one guy asks in a black purple and aqua shell-suit wi a flat-top') 
  ##check_sentence(cfg_1_parser, 'git tae fuck') 
  ##check_sentence(cfg_1_parser, 'we wir here first')
  ##check_sentence(cfg_1_parser, 'sickboy sais opening the taxi door')
#check_sentence(cfg_1_parser, 'Thir's another yin comin'）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）
#check_sentence(cfg_1_parser, ''）


# In[ ]:





# In[ ]:





# In[7]:


from nltk.parse.generate import generate, demo_grammar
for sentence in generate(cfg_1, depth=4, n=50):
     print(' '.join(sentence))


# In[ ]:





# In[ ]:




