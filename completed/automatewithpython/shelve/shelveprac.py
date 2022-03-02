import shelve

shelffile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelffile['cats'] = cats
shelffile.close()

