import collections
population_2010 = collections.defaultdict(int)
population_2100 = collections.defaultdict(int)
with open('population.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[6] = int(line[6])
        if line[1] == 'Total National Population':
            population_2010[line[0]] += line[5]
            population_2100[line[0]] += line[6]
for (x,y), (x2,y2) in zip(population_2010.items(), population_2100.items()):
    if x == x2:
        print x
        print "2010 population: "+"{:,}".format(y)
        print "2100 population: "+"{:,}".format(y2)
        change = round(float(y2) / float(y), 4)
        print "Change in population: "+ str((change-1)*100) +"%"