from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for i in range(len(attrs)):
                print(f"-> {attrs[i][0]} > {attrs[i][1]}")

    def handle_endtag(self, tag):
        print("End   :", tag)
   
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for i in range(len(attrs)):
                print(f"-> {attrs[i][0]} > {attrs[i][1]}")
        
N = int(input())
parser = MyHTMLParser()

for _ in range(N):
    parser.feed(input())
