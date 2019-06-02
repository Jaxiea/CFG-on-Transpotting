#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = ['fling', 'flings', 'focusing', 'forefinger', 'form', 'freezing', 'friends', 'fuck', 'fucked', 'fucker', 'fuckin', 'game', 'gasped', 'gear', 'gestured', 'gie', 'git', 'gittin', 'gitting', 'go', 'goat', 'gob', 'god', 'good', 'group', 'guy', 'guys', 'hailes', 'hall', 'hame', 'hand', 'handset', 'happens', 'harassing', 'has', 'hassle', 'haud', 'he', 'heavily', 'heid', 'here', 'hi', 'him', 'hing', 'his', 'hissel', 'hit', 'hope', 'hostile', 'hud', 'hudnae', 'hundred', 'hunted', 'huv', 'if', 'in', 'incrementally', 'intae', 'intense', 'introducing', 'involved', 'irresistible', 'irritating', 'is', 'it', 'jack', 'jaykit', 'jaykits', 'jist', 'johnny', 'jones', 'junk', 'just', 'keep', 'ken', 'kent', 'knowing', 'lashing', 'last', 'later', 'lazy', 'leave', 'leith', 'let', 'like', 'lips', 'live', 'long', 'longer', 'look', 'looked', 'looking', 'looks', 'lovin', 'lowest', 'lucky', 'ma', 'mair', 'maist', 'makin', 'man', 'mate', 'mclean', 'mcleans', 'me', 'meant', 'measley', 'middle', 'mines', 'minute', 'misery', 'mob', 'money', 'mother', 'move', 'moves', 'movies', 'muttered', 'n', 'nae', 'neck', 'need', 'nervously', 'never', 'next', 'nivir', 'no', 'nothing', 'notice', 'now', 'oaf', 'oafay', 'oan', 'obligatory', 'off', 'once', 'one', 'only', 'oor', 'oot', 'ootay', 'opening', 'or', 'other', 'ower', 'pence', 'petty', 'phase', 'picture', 'piled', 'pish', 'played', 'pleadin', 'plot', 'poignant', 'point', 'pokes', 'porty', 'post', 'poxy', 'preferred', 'probably', 'protested', 'purple', 'radge', 'radges', 'raises', 'rank', 'rather', 'raymie', 'ready', 'real', 'really', 'remember', 'rents', 'rests', 'rhythm', 'rich', 'ride', 'right', 'ritz', 'sae', 'sais', 'same', 'saps', 'saw', 'sayin', 'saying', 'schemes', 'score', 'scored', 'screaming', 'second', 'see', 'seeker', 'seem', 'seemed', 'serious', 'seriousness', 'set', 'shaking', 'shellsuits', 'shoap', 'shouted', 'shouts', 'show', 'si', 'sick', 'side', 'sidekick', 'sighthill', 'silent', 'simon', 'simone', 'sinews', 'sitting', 'size', 'smart', 'smash', 'snapped', 'snarled', 'so', 'some', 'sped', 'splattered', 'squad', 'square', 'standin', 'standing', 'stares', 'started', 'sticking', 'stoaped', 'straight', 'straining', 'such', 'sufferin', 'suffering', 'summer', 'superior', 'supposed', 'sure', 'swan', 'swanney', 'sweat', 'swedgin', 'switched', 'tae', 'take', 'takin', 'taxi', 'taxis', 'telly', 'tension', 'testimonies', 'thair', 'than', 'that', 'the', 'thegither', 'them', 'then', 'there', 'these', 'they', 'thighs', 'think', 'thir', 'this', 'thistle', 'thit', 'though', 'through', 'time', 'tod', 'tollcross', 'too', 'trembling', 'tried', 'trivial', 'truly', 'tryin', 'turns', 'um', 'up', 'ur', 'urn', 'us', 'usually', 'van', 'vermin', 'video', 'villain', 'visage', 'voice', 'walk', 'walkin', 'want', 'wanted', 'wants', 'waste', 'wastin', 'watch', 'we', 'weak', 'wee', 'well', 'went', 'were', 'wester', 'wey', 'whae', 'what', 'when', 'while', 'whit', 'white', 'wi', 'wid', 'willing', 'windae', 'wir', 'wis', 'wisnae', 'withdrawal', 'withoot', 'wouldnae', 'ya', 'yards', 'ye', 'yet', 'yin', 'yir', 'young', 'youse', 'yuv']
v = []
p = []

#For all words that end in "ing"

for i in s:
    if "ing" in i and i[-2] == "n":
        v.append(i)
#print(len(s))
#print (set(s) - set(v))
#print (len(set(s) - set(v)))

#For all words that end in "in"
for m in s:
    if "in" in m and m[-1] == "n":
        p.append(m)
#print(p)
print(sorted(set(s) - set(v) - set(p)))
#print(len(set(s) - set(v) - set(p)))

b = set(s) - set(v) - set(p)

print(len(b))
print(len(s) - len(b))
        


# In[ ]:




