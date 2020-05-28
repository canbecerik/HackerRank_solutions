from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for i in range(len(attrs)):
                print(f"-> {attrs[i][0]} > {attrs[i][1]}")


html = ""        
        
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

    parser = MyHTMLParser()
parser.feed(html)
parser.close()