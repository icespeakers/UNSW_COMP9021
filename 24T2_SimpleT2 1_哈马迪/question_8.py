# COMP9021 24T2 - Rachid Hamadi
# Sample Exam Question 8


'''
Will be tested with letters, a string of DISTINCT UPPERCASE letters only.
'''
import itertools
import csv
class dictTries:
    def __init__(self):
        self.nodes = dict()  # 构建字典
        self.is_leaf = False
    def insert(self,letter):
        i=0
        curr=self
        for w in letter:
            if w not in curr.nodes:
                curr.nodes[w]=dictTries()
            
            curr=curr.nodes[w]
        curr.is_leaf=True
    def check(self,letter):
        curr=self
        for w in letter:
            if w not in curr.nodes:
                return False
            else:
                curr=curr.nodes[w]
        return curr.is_leaf



        
def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''
    dictionary = 'dictionary.txt'
    solutions = []
    maxlen=0
    with open(dictionary,'r') as file:
        n=list(csv.reader(file))
        # print(n)
        # for i in n:
        #     maxlen=max(maxlen,len(i))
        # Insert your code here
        solution1=[]
        letter=[]
        target=[]
        for i in letters:
            letter.append(i)
        num=3
        while (num<=len(letters)):
            for i in itertools.permutations(letter,num):
                target.append(''.join(c for c in i))
                # print(i)
            num+=1
        # print(n)
        trie=dictTries()
        for i in n:
            # print(i[0])
            trie.insert(i[0])
        for j in target:
            if(trie.check(j)):
                solution1.append(j)
        for i in itertools.permutations(solution1,2):
                if(len(i[0])+len(i[1])==len(letters)):
                    # print(i)
                    ans=i[0]+i[1]
                    le1=0
                    le2=0
                    le3=0
                    flag=False
                    s=set()
                    while(le1!=len(i[0]) or le2!=len(i[1])):
                        if le1<len(i[0]) and i[0][le1] in letters and i[0][le1] not in s:
                            s.add(i[0][le1])
                            le1+=1
                            le3+=1
                        elif le2<len(i[1])  and i[1][le2] in letters and i[1][le2] not in s:
                            s.add(i[1][le2])
                            le2+=1
                            le3+=1
                        else:
                            flag=True
                            break;
                    # print(le1)
                    # print(flag)
                    if(flag==False):
                        if(i[0][0]<i[1][0]):
                            solutions.append(i)
                # print(len(i[0]))
        # trie.insert('abc')
        # print(trie.check('abc'))
        solutions.sort()
    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')
        for solution in solutions:
            print(solution)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
