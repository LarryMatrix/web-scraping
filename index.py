import requests
import bs4

link = 'URL GOES HERE'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text, 'lxml')
select = soup.select('select')
myList = []
myData = select[0].getText()
myList = myData.split('\n')
myNewList = []


file1 = open("myNewList.json", "w")
payload = {
    "states": myList
}
print(payload)
file1.write(str(payload))
file1.close()
