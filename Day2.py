a=input('Enter a word: ')
for i in set(a):
    a.count(i)
    print(i,'-',a.count(i))