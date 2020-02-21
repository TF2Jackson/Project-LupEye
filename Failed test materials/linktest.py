{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter start date (Y/M/D -> XXXX/XX/XX) 20180101\n",
      "Enter end date (Y/M/D -> XXXX/XX/XX) 20190101\n",
      "Enter query term impeachment\n"
     ]
    },
    {
     "ename": "NoSuchWindowException",
     "evalue": "Message: no such window: window was already closed\n  (Session info: chrome=78.0.3904.108)\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNoSuchWindowException\u001b[0m                     Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-48-ea1bb4a7a991>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     37\u001b[0m \u001b[0mz\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     38\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0mz\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;36m150\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 39\u001b[0;31m     \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element_by_xpath\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbutton\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     40\u001b[0m     \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     41\u001b[0m     \u001b[0mz\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m//anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mfind_element_by_xpath\u001b[0;34m(self, xpath)\u001b[0m\n\u001b[1;32m    392\u001b[0m             \u001b[0melement\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element_by_xpath\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'//div/td[1]'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    393\u001b[0m         \"\"\"\n\u001b[0;32m--> 394\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mby\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mXPATH\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mxpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    395\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    396\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mfind_elements_by_xpath\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mxpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m//anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mfind_element\u001b[0;34m(self, by, value)\u001b[0m\n\u001b[1;32m    976\u001b[0m         return self.execute(Command.FIND_ELEMENT, {\n\u001b[1;32m    977\u001b[0m             \u001b[0;34m'using'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 978\u001b[0;31m             'value': value})['value']\n\u001b[0m\u001b[1;32m    979\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    980\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mfind_elements\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mID\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m//anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    320\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 321\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[1;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[0;32m//anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'alert'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    241\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 242\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    243\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    244\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNoSuchWindowException\u001b[0m: Message: no such window: window was already closed\n  (Session info: chrome=78.0.3904.108)\n"
     ]
    }
   ],
   "source": [
    "#This program scrapes all of the links of a given website.\n",
    "\n",
    "from bs4 import BeautifulSoup\n",
    "from pprint import pprint\n",
    "import requests\n",
    "import re\n",
    "import sys\n",
    "import time\n",
    "from requests_html import HTMLSession\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "\n",
    "# Using inputs, create a custom link (urlmaster) that searches the NYT archive for a...\n",
    "# ... certain query term between a start and end date\n",
    "sd = input(\"Enter start date (Y/M/D -> XXXX/XX/XX)\")\n",
    "ed = input(\"Enter end date (Y/M/D -> XXXX/XX/XX)\")\n",
    "query = input(\"Enter query term\")\n",
    "\n",
    "# Set parts of URL that do not change depending on inputs\n",
    "url1 = 'https://www.nytimes.com/search?dropmab=true&endDate= +'\n",
    "url2 = '&query='\n",
    "url3 = '&sort=newest&startDate='\n",
    "url4 = 'types=article'\n",
    "\n",
    "# Concectenate variables to make the url we will scrape for the rest of the code\n",
    "urlmaster = url1 + ed + url2 + query + url3 + sd + url4\n",
    "\n",
    "# This variable will tell our code how to find the 'show more' button as we move through the results\n",
    "button = \"//button[contains(text(),'Show More')]\"\n",
    "\n",
    "\n",
    "# Bring in chromedriver to be able to access the urlmaster in our code, and then open the webpage\n",
    "driver = webdriver.Chrome(executable_path=r\"/Users/drewmedway/Downloads/chromedriver\")\n",
    "driver.get(urlmaster)\n",
    "\n",
    "# Use a while loop to repeatedly click the 'show more' button in order to have access to all the results\n",
    "z = 0\n",
    "while z < 100:\n",
    "    driver.find_element_by_xpath(button).click()\n",
    "    time.sleep(4)\n",
    "    z += 1\n",
    "\n",
    "# Create a new variable with the content of our updated page, and then bring in BeautifulSoup\n",
    "raw_html = driver.page_source\n",
    "html = BeautifulSoup(raw_html, 'html.parser')\n",
    "\n",
    "# Create an empty list, and fill it with all links we can find on our page\n",
    "links = []\n",
    "for link in html.find_all('a'):\n",
    "    links.append(link.get('href'))\n",
    "\n",
    "print(\"complete\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "110\n"
     ]
    }
   ],
   "source": [
    "# Our code above collected ALL links from the page, not just the ones relevant to our inquiry. \n",
    "# However, all the relevant ones share a term that we can filter by using our variable below.\n",
    "\n",
    "searcher = 'searchResultPosition'\n",
    "base = 'https://www.nytimes.com'\n",
    "\n",
    "linksTemp = []\n",
    "masterLinks = []\n",
    "\n",
    "# We filter the old list and take relevant links into our new list\n",
    "for i in links:\n",
    "    if searcher in i:\n",
    "        linksTemp.append(i)\n",
    "        \n",
    "# This ensures the relative links we collected previously can be found on an absolute basis...\n",
    "# ...in the next steps of our program\n",
    "        \n",
    "for i in linksTemp:\n",
    "    if i.startswith('/'):\n",
    "        masterLinks.append(base + i)\n",
    "        \n",
    "for i in linksTemp:\n",
    "    if i.startswith('https'):\n",
    "        masterLinks.append(i)\n",
    "        \n",
    "print(len(masterLinks))   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2929\n"
     ]
    }
   ],
   "source": [
    "# Now, we use another for loop to scrape the text from individual articles and put it into an empty list\n",
    "\n",
    "linkText = []\n",
    "\n",
    "for i in masterLinks:\n",
    "    response = requests.get(i)\n",
    "    soup = BeautifulSoup(response.text, 'html.parser')\n",
    "    for item in soup.select('p'):\n",
    "        linkText.append(item.get_text())\n",
    "        \n",
    "print(len(linkText))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'linkText' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-e3848acb83de>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0msb\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"Supported by\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mlinkText\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mads\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m         \u001b[0;32mpass\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'linkText' is not defined"
     ]
    }
   ],
   "source": [
    "# This for loop removes the strings listed under ads and sb from the text we've scraped\n",
    "\n",
    "linkTextClean = []\n",
    "\n",
    "ads = \"Advertisement\"\n",
    "sb = \"Supported by\"\n",
    "\n",
    "for i in linkText:\n",
    "    if ads in i:\n",
    "        pass\n",
    "    elif sb in i:\n",
    "        pass\n",
    "    else:\n",
    "        linkTextClean.append(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "complete\n"
     ]
    }
   ],
   "source": [
    "# Finally, we move all the text into a txt file so LIWC can analyze it\n",
    "\n",
    "with open('impeachment2000.txt', 'w') as filehandle:\n",
    "    for listitem in linkTextClean:\n",
    "        filehandle.write('%s\\n' % listitem)\n",
    "        \n",
    "print(\"complete\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
