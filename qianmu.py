import threading
from queue import Queue
import requests
import lxml.etree
import time

start_url = 'http://140.143.192.76:8002/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D'
link_queue =Queue()
threads_num =10
threads =[]
download_pages =0

def fetch(url):
    global download_pages
    response = requests.get(url)
    if response.status_code == 200:
        download_pages += 1
        print('%s:%s'%(url,response.reason))
    return response.text.replace('\t','')


def parse(html):

    # print(response)
    # print(response.text)
    dom = lxml.etree.HTML(html)
    return dom.xpath('//*[@id="content"]/table//tr/td[2]/a/@href')


def details_parse(html):
    dom2 = lxml.etree.HTML(html)
    wiki = dom2.xpath('//div[@id="wikiContent"]')[0]
    name =wiki.xpath('./h1[@class="wikiTitle"]/text()')[0]
    print(name)
    keys = wiki.xpath('./div[@class="infobox"]/table/tbody/tr/td[1]/p/text()')
    cols =wiki.xpath('./div[@class="infobox"]/table/tbody/tr/td[2]')
    values = [','.join(col.xpath('.//text()'))for col in cols]
    info =dict(zip(keys,values))
    info ={name:info}
    print(info)


def downloader():
    while True:
        link = link_queue.get()
        if link is None:
            break
        details_parse(fetch(link))
        link_queue.task_done()
        print('remaining queue: %s' % link_queue.qsize())

if __name__ == "__main__":
    start_time = time.time()
    links = parse(fetch(start_url))
    for link in links:
        link_queue.put(link)

    link_queue.join()

    for i in range(threads_num):
         link_queue.put(None)

    for t in threads:

        t.join()

    cost_seconds = time.time() - start_time
    print('dowmload %s pages in %.2f seconds' % (download_pages,cost_seconds))