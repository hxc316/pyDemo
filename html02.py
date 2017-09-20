from html.parser import HTMLParser
page ='''''<sada>啊啊啊</sada>
<a href="http://click.union.360buy.com/JdClick/?unionId=75" class="f1"  style="padding-left:13px; padding-right:14px">京东商城</a>
<a href="http://www.baidu.com">百度</a>
</td>'''

class hp(HTMLParser):
    a_text = False

    def handle_starttag(self,tag,attr):
        if tag == 'a':
            self.a_text = True
            #print (dict(attr))

    def handle_endtag(self,tag):
        if tag == 'a':
            self.a_text = False

    def handle_data(self,data):
        if self.a_text:
            print (data)

yk = hp()
yk.feed(page)
yk.close()