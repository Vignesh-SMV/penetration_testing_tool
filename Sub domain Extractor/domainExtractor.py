from datetime import date, datetime
import os
import re
import sys
import argparse
import urllib.parse
import logging
import requests
import pyfiglet

def domain():
    
    banner = pyfiglet.figlet_format("domain extractor")

    print("-" * 80)
    print(banner)
    print("-" * 80)

    inputFile = input("Specify the file to extract domains from (comma-separated if multiple): ")
    url = input("Specify the web page to extract domains from (one at a time for now): ")
    target = input("Specify the target top-level domain you'd like to find and extract (e.g., uber.com), or 'all' for all domains: ")
    verbose = input("Enable slightly more verbose console output (True/False): ").lower() == 'true'

    if not inputFile and not url:
        print("You must specify either a file or a URL to extract domains from.")
        return

    # Set up logger
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logfileName = "logs/newdomains.{}.log".format(target)
    logging.basicConfig(filename=logfileName, filemode='a', format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    outputFile = "final.{}.txt".format(target)

    def extractDomains(args, inputFile, rawData):
        domains = []

        if not args:
            print("No target specified, defaulting to finding 'all' domains")

        for i in rawData:
            matches = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', urllib.parse.unquote(urllib.parse.unquote(i)))
            if not args.lower() == 'all':
                for j in matches:

                    if j.find(args.lower()) != -1:
                        domains.append(j)
            else:
                for j in matches:
                    if j.find('.com') != -1:
                        domains.append(j)
                    elif j.find('.net') != -1:
                        domains.append(j)
                    elif j.find('.org') != -1:
                        domains.append(j)
                    elif j.find('.tv') != -1:
                        domains.append(j)
                    elif j.find('.io') != -1:
                        domains.append(j)
        print("File: {} has {} possible domains...".format(inputFile, len(rawData)))

        return domains

    results = []

    # If files are specified, check them
    if inputFile:
        fileList = inputFile.split(',')
        for inputFile in fileList:
            try:
                with open(inputFile, 'r') as f:
                    rawData = f.read().splitlines()
            except UnicodeDecodeError:
                with open(inputFile, 'r', encoding="ISO-8859-1") as f:
                    rawData = f.read().splitlines()

            results += extractDomains(target, inputFile, rawData)

    # If a URL is specified, pull that
    if url:
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}
        rawData = requests.get(url, headers=headers)
        rawData = rawData.text.split('\n')
        results += extractDomains(target, url, rawData)

    # Sort and dedupe results
    finalDomains = sorted(set(results))

    # Read all the domains we already have
    try:
        with open(outputFile, 'r') as out:
            oldDomains = out.read().splitlines()

    # If no final file, create one
    except FileNotFoundError:
        print("Output file not found. Creating one...")

        with open(outputFile, 'w') as out:
            for i in finalDomains:
                out.write("{}\n".format(i))

        print("{} domains written to output file {}".format(len(finalDomains), outputFile))

    # Loop through fresh domains. If we don't already have it, add it to final file, notify us, log it.
    else:
        newDomains = []
        with open(outputFile, 'a') as out:
            for i in finalDomains:
                if i not in oldDomains:
                    newDomains.append(i)
                    out.write("{}\n".format(i))

        if newDomains:
            print("{} new domains were found and added to {}".format(len(newDomains), outputFile))
            for i in newDomains:
                logger.info("New domain found: {}".format(i))

        else:
            print("No new domains found.")


