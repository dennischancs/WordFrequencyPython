"""
Python Code to find out most frequent words from famous GRE lists

WordLists ( Courtesy: www.quizlet.com )
1. Barrons 1100 Words
2. Magoosh 1000 Words
3. Majortest Essential 1500 Words
4. Princeton 500 Words
5. Kaplan 500 Words
6. Manhattan Basic+Essential 1000 Words

Above words are stored in different text files along with definations. These text files are combined, parsed and word frequecy is calculated.
Word along with Frequenices is stored in output text file 'output.txt'
"""
from collections import defaultdict, Counter
import json

# Function to calculate word Frequency and store it into Dictionary
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

# Combine all wordslist text files into one and convert to lowercase.
filenames = ['WordLists/其它/公开课.txt','WordLists/其它/英语辅导.txt','WordLists/其它/其他.txt']
with open('CombinedAllWords.txt', 'w', encoding='utf8') as outfile:
    for fname in filenames:
        # with open(fname, encoding="ISO-8859-1") as infile:
        with open(fname, encoding='utf8') as infile:
            for line in infile:
                line = line.lower()
                outfile.write(line)

# Open combined wordlist, remove definations and format words
with open("CombinedAllWords.txt", encoding='utf8') as f:
    items = f.readlines()
    combined_vocab = items
    combined_vocab = list(map(lambda items: items.strip(), combined_vocab))
    for i, w in enumerate(combined_vocab):
        combined_vocab[i]=w.split("@", 1)[0]

# my custom code to create a super dictionary
combined_map = defaultdict(list)
with open("CombinedAllWords.txt", encoding='utf8') as f:
    for line in f:
        line = line.strip()
        splitted =  line.split('@')
        if len(splitted) > 1:
            word, meaning = splitted[0], splitted[1]
            combined_map[word].append(meaning)


#Open file and write sorted dictionary values into text file one by one in decreasing order
with open("output/words.txt","w", encoding='utf8') as f:
# for key, value in sorted(wordListToFreqDict(t).items(), key=lambda k,v: (v,k), reverse =True):
    for key, value in sorted(wordListToFreqDict(combined_vocab).items(), key=lambda x: (x[1], x[0]), reverse =True):
        # l.write(" \n%s: %s" % (key, value))
        word = key
        freq = value
        meaning = combined_map[word]
        f.write("{}[{}]@ {}\n".format(key, value, meaning))

counter = Counter([v for k, v in wordListToFreqDict(combined_vocab).items()])

# dump as json
jsonmap = {}
for word, frequency in sorted(wordListToFreqDict(combined_vocab).items(), key=lambda x: (x[1], x[0]), reverse =True):
    if frequency not in jsonmap:
        jsonmap[frequency] = defaultdict(dict)
    jsonmap[frequency][word] = combined_map[word]

for frequency in jsonmap:
    wordmap = jsonmap[frequency]
    with open("output/{}.json".format(frequency), 'w', encoding='utf8') as f:
        json.dump(wordmap, f, indent=4)


# dump as HTML with some shitty formatting
with open("output/words.html","w", encoding='utf8') as f:
    html = "<!DOCTYPE html>\n<head>{}</head>\n<body>\n{}</body>\n</html>"

    # add a metadata about occurence of each type
    metadata = "<h1>Metadata</h1><ul>"
    for k in range(6, 0, -1):
        metadata += "<li>{} : {}</li>".format(k, counter[k])
    metadata += "</ul>"
    # f.write(metadata)

    # real shit happens now
    content = ""
    count, prev = 0, 6
    for i, (key, value) in enumerate(sorted(wordListToFreqDict(combined_vocab).items(), key=lambda x: (x[1], x[0]), reverse =True)):
        # l.write(" \n%s: %s" % (key, value))
        word = key
        frequency = value
        # reset counter
        if frequency != prev:
            count, prev = 0, frequency
        meaning = "<ul>"
        for m in combined_map[word]:
            meaning += "<li>{}</li>".format(m)
        meaning += "</ul>"
        count += 1
        content += "<h2>{} - {}</h2><h4>frequecy : {}</h4><h4>S.N.: {}/{}</h4>{}<hr/>\n".format(
            i+1, key, frequency, count, counter[frequency], meaning)

        # f.write(content)
    body = "{}\n<hr/><hr/>\n{}".format(metadata, content)
    html = html.format('', body)
    f.write(html)
