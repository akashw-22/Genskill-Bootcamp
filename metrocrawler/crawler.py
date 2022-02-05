import requests
import bs4

def get_links(url):
	
	ret = []
	resp = requests.get(url)
	soup = bs4.BeautifulSoup(resp.content, features = "html.parser")
	links = soup.find_all("a", attrs = {"class" : "title hasvidtable"})

	for i in links:
		ret.append(i['href'])
		
	return ret

def get_lyrics(url):
	
	lyrics = []
	resp = requests.get(url)
	soup = bs4.BeautifulSoup(resp.content, features = "html.parser")
	title = soup.find_all("h1")
	print("Copying: ", title[0].get_text(), "....")
	lyrics.append('\t'+title[0].get_text()+'\n')
	verse = soup.find_all("p", attrs = {"class" : "verse"})
		
	for i in verse:
		lyrics.append(i.get_text())
		lyrics.append("\n")
		
	return "\n".join(lyrics)

def get_fname(url):
	return url.split("/")[-1].replace(".html", ".txt")
	
		
def main():
	
	links = get_links("https://www.metrolyrics.com/drake-lyrics.html")
	
	for i in links:
		#print(get_lyrics(i))
		
		fname = get_fname(i)
		f = open(fname, "w")
		f.write(get_lyrics(i))
		#break

if __name__ == "__main__":
	main()
else:
	print("imported")
	
