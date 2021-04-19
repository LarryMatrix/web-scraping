import requests
import bs4

link = 'https://www.lotteryusa.com/'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text, 'lxml')
select = soup.select('select')
myList = []
myData = select[0].getText()
myList = myData.split('\n')
myNewList = []

# for i in range(0, len(myList)):
#     if 1 < i < 50:
#         myNewList.append(myList[i])
#     else:
#         print('skipped:: ', myList[i])

file1 = open("myNewList.json", "w")
payload = {
    "states": myList
}
print(payload)
file1.write(str(payload))
file1.close()
