import httpx
from selectolax.parser import HTMLParser

url = "https://tienda.consum.es/es/s/cerveza?orderById=13&page=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
}


rep = httpx.get(url, headers=headers)
html = HTMLParser(rep.text)

def extract_text(html, sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

prducts = html.css("a.id.grid-widget--descr")

for prduct in prducts:
    item = {
        "name": extract_text(prduct, "u-no-link.ng-tns-c212-5.ng-star-inserted")
    }
    print(item)