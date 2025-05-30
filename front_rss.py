from tkinter import Button, Entry, IntVar, Label, StringVar, Tk, filedialog, messagebox, ttk
from tkinter.ttk import Style
import rss_generate


def upload_file(max_urls, anchor_text):
    filename = filedialog.askopenfilename()
    with open(filename, 'r') as f:
        messagebox.showinfo("Start processing", "Start processing")
        i = 1
        for line in f:
            data = line.splitlines()
            for link in data:
                feed = rss_generate.rss_read(link)
                rss_generate.rss_to_excel(feed, max_urls, i, anchor_text)
                i = i + 1
    messagebox.showinfo("Success", "RSS feed generated successfully")


root = Tk()
root.title("RSS Reader")
root.geometry("400x400")
root.config(bg="white")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
# style
s = Style()
s.configure('My.TFrame')
frm = ttk.Frame(root, style='My.TFrame')
frm.grid(column=0, row=0)
# label anchor text
lbl_anchor_text = Label(frm, text="Anchor Text:", fg='#FF4000',
                        font=('helvetica', 12, 'bold'))
lbl_anchor_text.grid(column=1, row=0)
# entry anchor text
anchor_text = StringVar()
entry_anchor_text = Entry(frm, textvariable=anchor_text, width=10)
entry_anchor_text.grid(column=1, row=1)
# label Number max urls
lbl_max_urls = Label(frm, text="Number of URLs to generate:", fg='#FF4000',
                     font=('helvetica', 12, 'bold'))
lbl_max_urls.grid(column=1, row=2)
# entry Number max urls
max_urls = IntVar()
entry_max_urls = Entry(frm, textvariable=max_urls, width=10)
entry_max_urls.grid(column=1, row=3)
# label upload file
label_rss_url = Label(
    frm, text="Upload File:", fg='#FF4000',
    font=('helvetica', 12, 'bold'))
label_rss_url.grid(column=1, row=4)
# upload text file
upload_buttom = Button(
    frm, text="Upload", command=lambda: upload_file(max_urls.get(), anchor_text.get()), bg="#50B2C0", fg="white", width=41, height=4)
upload_buttom.grid(column=1, row=5)

root.mainloop()
