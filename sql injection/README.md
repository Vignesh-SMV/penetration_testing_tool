

# Usage

```sh
python3 sqlifinder.py -h
```
This will display help for the tool. Here are all the switches it supports.



# Installation

Sqlifinder requires:
- python3
- huepy
- requests
- tqdm

To install requirements :
 
 pip3 install -r requirements.txt






# Running Sqlifinder

To run the tool on a target, just use the following command.
```sh
▶ python3 sqlifinder.py -d example.com
```


The `-s` command can be used to test sql injection in subdomains of the target.

```sh
▶ python3 sqlifinder -d example.com -s
```


