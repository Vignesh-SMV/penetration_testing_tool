# domainExtractor
Extract domains/subdomains/FQDNs from files and URLs 



```bash
python3 domainExtractor.py
usage: domainExtractor.py [-h] [-f INPUTFILE] [-u URL] [-t TARGET] [-v]

This script will extract domains from the file you specify and add it to a final file

optional arguments:
  -h, --help            show this help message and exit
  -f INPUTFILE, --file INPUTFILE
                        Specify the file to extract domains from
  -u URL, --url URL     Specify the web page to extract domains from. One at a time for now
  -t TARGET, --target TARGET
                        Specify the target top-level domain you'd like to find and extract e.g. uber.com
  -v, --verbose         Enable slightly more verbose console output

```


```bash
python3 domainExtractor.py -f ~/Desktop/yahoo/test/test.html -t yahoo.com

python3 domainExtractor.py -f amass.playstation.net.txt,subfinder.playstation.net.txt --target playstation.net
```


```bash
python3 domainExtractor.py -u "https://yahoo.com" -t yahoo.com
```


```bash
# pulling from a file, extract all domains
python3 domainExtractor.py -f test.html --target all

# pull from yahoo.com home page, extract all domains. No target specified defaults to 'all'
python3 domainExtractor.py -u "https://yahoo.com"
```



