#encoding=utf-8
import urllib2
import chardet
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')


def web_grap(url):
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read()
    typeEncode = sys.getfilesystemencoding()##系统默认编码
    infoencode = chardet.detect(content).get('encoding','utf-8')##通过第3方模块来自动提取网页的编码
    html = content.decode(infoencode,'ignore').encode(typeEncode)##先转换成unicode编码，然后转换系统编码输出utfile.close()
    return  html

if __name__ == "__main__":
    print grep_web("https://house.chizhouren.com/resoldhome/esf/list")

