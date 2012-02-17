from hashes.bloom import bloomfilter

hash1 = bloomfilter('imastring')
print hash1.hashbits, hash1.num_hashes     # default values (see below)

hash1.add('imastring string')

# print 'test string' in hash1
for word in 'bloom filters are the best'.split():
    hash1.add(word)

if 'machine' in hash1:
    print "machine!"
