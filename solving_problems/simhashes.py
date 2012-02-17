from hashes.simhash import simhash

if __name__ == '__main__':
    f = open('flat.txt', 'r')
    data = [line.strip() for line in f.readlines()]
    f.close()

    # print data
    all_hashes = dict([(d, simhash(d)) for d in data])

    for k, h in all_hashes.items():
        print "%s %s" % (k, h)
        print all_hashes['Flatpack Bunny'].similarity(h)

    
