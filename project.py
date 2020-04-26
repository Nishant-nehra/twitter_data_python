
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s=s.replace(i,'')
    return(s)

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(s):
    count=0
    wds=s.lower().split()
    for i in wds:
        if strip_punctuation(i) in negative_words:
            count+=1
    return count

def get_pos(s):
    count=0
    wds=s.lower().split()
    for i in wds:
        if strip_punctuation(i) in positive_words:
            count+=1
    return count
values=[]

fhand=open('project_twitter_data.csv')
lines=fhand.readlines()
header=lines[0]
field_names=header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals=row.strip().split(',')
    positive=get_pos(vals[0])
    negative=get_neg(vals[0])
    net=positive-negative
    retweet=int(vals[1])
    reply=int(vals[2])
    values.append((retweet,reply,positive,negative,net))
fhand.close()
fhand=open('resulting_data.csv','w')
fhand.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
fhand.write("\n")
print(values)
for value in values:
    row="{},{},{},{},{}".format(value[0],value[1],value[2],value[3],value[4])
    fhand.write(row)
    fhand.write("\n")

fhand.close()
