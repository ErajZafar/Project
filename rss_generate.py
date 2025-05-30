import feedparser
import xlsxwriter
import os
import requests


def rss_read(url):
    """
    Generate RSS feed from URL
    """
    feed = feedparser.parse(url)

    return feed

# generate excel from rss feed


def rss_to_excel(feed, max_urls, ni, anchor_text):
    """
    Generate excel from RSS feed
    """
    # get current directory
    current_directory = os.getcwd()
    # create excel file
    workbook = xlsxwriter.Workbook(
        current_directory + "/rss_urls" + str(ni) + ".xlsx")
    # create worksheet
    worksheet = workbook.add_worksheet()
    worksheet.set_default_row(20, 100)
    # get urls from feed
    urls = feed.entries
    # get the number of urls
    urls_number = len(urls)
    # get the number of urls to be generated
    urls_to_generate = min(urls_number, max_urls)
    # write urls to excel
    for i in range(urls_to_generate):
        # get url
        url = urls[i].link
        title = urls[i].title
        # write url
        worksheet.write_row('A'+str(i + 1), [title])
        worksheet.write_row('B'+str(i + 1), [url])
        # anchor text
        worksheet.write_url('C'+str(i + 1), url, string=anchor_text)
        # generate qr code
        qr_url = generate_qr(url)
        # write qr code in ecxel
        worksheet.write_row('D'+str(i + 1), [qr_url])

    # close excel file
    workbook.close()


# generate qr code from url usign google char api
def generate_qr(url):
    qr_url = "https://chart.googleapis.com/chart?cht=qr&chs=300x300&chl=" + url
    return qr_url
