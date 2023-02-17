from bs4 import BeautifulSoup
import re

with open('cover_page.html', encoding = 'utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    
result = soup.find_all("a")
for a in result:
	doc = a.get_text()
	newname = input(f"What EXACTLY is the name of your {doc} document?")
	a['href'] = "Documentation/" + newname

result = soup.find_all("p")
for r in result:
	text = r.get_text()
	prompt = re.findall("[^:]+:", text)
	if prompt: 
		if prompt[0] == "Links to:": 
			prompt[0] = prompt[0][:-1] + " product:"
			response = input(prompt[0])
			new_tag = soup.new_tag("a", href="Product/" + response)
			r.string = "Link to product:"
			r.append(new_tag)
			new_tag.string = "Product"
		else:
			response = input(prompt[0])
			r.string = prompt[0] + response
	else:
		prompt = re.findall("_+.+", text)
		if prompt: 
			response = input("WORD COUNT")
			r.string = response
	prompt = None
	
result = soup.find("table")
for r in result.find_all('td'):
	text = r.get_text()
	prompt = re.findall(".*product does not load.*", text)
	if prompt:
		response = input("Directions to access product or any other additional information:")
		r.string = response



f = open("Final_CP.html", "w")
f.write(str(soup))
f.close

