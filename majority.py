import pandas as pd
import numpy as np

def dataset():
    train_data = pd.read_csv('train.csv', index_col=None)
    direction_data = train_data['direction']
    sentence_data = train_data['sentence']
    rel_data = train_data['relation']
    term1_data = train_data['term1']
    term2_data = train_data['term2']
    m = []

    fd = pd.read_csv('train.csv', usecols = ['_unit_id'])

    count = 1
    total = 0
    ls = []
    #print(len(sentence_data))

    for i in fd['_unit_id']:
        ls.append(i)

    ls.append(0)        # so that last set of sentences are counted
    j = 0
    i = 0
    for j in range(0, len(ls)-1):
        
        if ls[j] == ls[j+1]:
            count = count + 1
        else:
            dir_data = direction_data.ix[i:i+count-1].sort_values()

            s = set(dir_data)
            a = []
            for x in s:
                a.append(x)
            
            #print(len(a))
            c1 = 0
            c2 = 0
            c3 = 0
            if len(a) != 1:
                for j in dir_data:
                    if a[0] == j:
                        c1+=1
                    elif a[1] == j:
                        c2+=1
                    else:
                        c3+=1
            else:
                c1 = count
                c2 = c3 = 0
            
            if c1 > c2 and c1 > c3:
                m.append([a[0], sentence_data.ix[i], rel_data[i], term1_data[i], term2_data[i]])
            elif c2 > c1 and c2 > c3:
                m.append([a[1], sentence_data.ix[i], rel_data[i], term1_data[i], term2_data[i]])
            elif c3 > c1 and c3 > c2:
                m.append([a[2], sentence_data.ix[i], rel_data[i], term1_data[i], term2_data[i]])
            i += count
            count = 1

    columns= ['direction','sentence', 'relation', 'term1', 'term2']
    data = pd.DataFrame(m, columns=columns)
    return data

