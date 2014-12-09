import urllib
import json

def main(api_key, category, label):
    
    content = []
    for i in range(0,5):
        # print "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:('%s')&api-key=%s&page=%s" % (category, api_key, i)
        h = urllib.urlopen("http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:(\"%s\")&api-key=%s&page=%s" % (category, api_key, i))
        print h
        try:
            result = json.loads(h.read())
            content.append(result)
        except ValueError:
            print "Malformed JSON: " + data
            continue #In the rare cases that JSON refuses to parse

    f = open(label, 'w')
    for line in content:
        try:
            f.write('%s\n' % line)
        except UnicodeEncodeError:
            pass
            
    f.close()

if __name__ == '__main__':
    main("f7b4a1749764aec0364b215c354e3a0f:18:25759498", "Arts","arts")
    main("f7b4a1749764aec0364b215c354e3a0f:18:25759498", "Sports","sports")

