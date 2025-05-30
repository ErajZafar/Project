from tkinter import Button, Entry, IntVar, Label, StringVar, Tk, filedialog, messagebox, ttk
from tkinter.constants import CENTER, HORIZONTAL
from tkinter.ttk import Style
import generate_urls


root = Tk()
root.title("RSS Reader")
root.geometry("400x400")
root.config(bg="white")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
# style
s = Style()
s.configure('My.TFrame')
s.configure('blue.TSeparator', background='blue')
s.configure('red.TSeparator', background='red')
frm = ttk.Frame(root, style='My.TFrame')
frm.grid(column=0, row=0)
# label Enter your centroid
lbl_centroid = Label(frm, text="Enter your centroid:", fg='#FF4000',
                     font=('helvetica', 12, 'bold'))
lbl_centroid.grid(column=1, row=0)
# entry centroid
centroid = StringVar()
entry_centroid = Entry(frm, textvariable=centroid, width=10)
entry_centroid.grid(column=1, row=1)
# label Max urls
lbl_max_urls = Label(frm, text="Number of URLs to generate:", fg='#FF4000',
                     font=('helvetica', 12, 'bold'))
lbl_max_urls.grid(column=1, row=2)
# entry max urls
max_urls = IntVar()
entry_max_urls = Entry(frm, textvariable=max_urls, width=10)
entry_max_urls.grid(column=1, row=3)
# label Ratio
lbl_ratio = Label(frm, text="Ratio:", fg='#FF4000',
                  font=('helvetica', 12, 'bold'))
lbl_ratio.grid(column=1, row=4)
# entry ratio
ratio = IntVar()
entry_ratio = Entry(frm, textvariable=ratio, width=10)
entry_ratio.grid(column=1, row=5)

# label gbm name
lbl_gbm_name = Label(frm, text="Anchor Text:", fg='#FF4000',
                     font=('helvetica', 12, 'bold'))
lbl_gbm_name.grid(column=1, row=6)
# entry gbm name
gbm_name = StringVar()
entry_gbm_name = Entry(frm, textvariable=gbm_name, width=10)
entry_gbm_name.grid(column=1, row=7)

# entre data link
lbl_data_link = Label(frm, text="Data link:", fg='#FF4000',
                      font=('helvetica', 12, 'bold'))
lbl_data_link.grid(column=1, row=8)
# entry data link
data_link = StringVar()
entry_data_link = Entry(frm, textvariable=data_link, width=10)
entry_data_link.grid(column=1, row=9)

# label buttom process
label_Buttom = Label(frm, text="Process", fg='#FF4000',
                     font=('helvetica', 12, 'bold'))
label_Buttom.grid(column=1, row=10)
# buttom process
buttom = Button(frm, text="Process", command=lambda: generate_urls.generate_urls(centroid.get(
), max_urls.get(), ratio.get(), gbm_name.get(), data_link.get()), bg="#50B2C0", fg="white", width=41, height=4)
buttom.grid(column=1, row=11)

root.mainloop()
