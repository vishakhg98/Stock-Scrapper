# importing modules
import tkinter as tk
from tkinter import messagebox 

from bs4 import BeautifulSoup
import requests

class StockWindow:
    def __init__(self, master):
        self.master = master
        # Adding title icon
        master.iconbitmap('./images/stock_titlebar_icon.ico')
        # Adding title name
        master.title("Stock Scrapper")
        # Setting geometry size
        master.geometry('700x500') # Width x Height
        # Disabling resize of window
        master.resizable(0,0)
        
        # Background Main Canvas
        bg_canvas = tk.Canvas(master, width=700, height=500)
        bg_canvas.pack()
        # Canvas / Program background wall
        self.background_image = tk.PhotoImage(file='./images/canvas_background.png')
        background_label = tk.Label(master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        # ============ Search Box and Button ==================================#
        
        # Search Entry and Button
        self.search_box = tk.Entry(background_label, font=("Arial 20"), bd=1,
                                   bg='#fff', fg='#000', width=25,
                                    justify='center')
        self.search_box.place(x=90, y=50)

        self.search_btn_img = tk.PhotoImage(file='./images/search_button.png')
        self.search_btn = tk.Button(background_label, image=self.search_btn_img,
                                 bd=0, bg='#fff', activebackground='#fff',
                                 command=lambda : self.get_stock())
        self.search_btn.place(x=500, y=54)
        

        # # ================ Data Frame =========================================#

        self.dataframe = tk.Frame(background_label, width=600, height=335,
                              highlightthickness=2, bg='#fff')
        self.dataframe.pack(side='bottom', pady=50)
        
        # Stock name label
        self.sname_label = tk.Label(self.dataframe, font='Arial 12 bold', bg='#fff')
        self.sname_label.place(x=30, y=25)

        # Stock Exchange name/ Ticker Symbol label
        self.ticker_symbol_label = tk.Label(self.dataframe, font='Arial 14 bold',
                                             bg='#fff')
        self.ticker_symbol_label.place(x=30, y=60)

        # Stock Value label
        self.svalue_label = tk.Label(self.dataframe, font='Arial 20 bold',
                                     bg='#fff')
        self.svalue_label.place(x=30, y=100)

        # Stock Change/ Fluctuation label
        self.schange_label = tk.Label(self.dataframe, font='Arial 15 bold',
                                     bg='#fff')
        self.schange_label.place(x=310, y=105)

        # Stock Market Closed time
        self.closetime_label = tk.Label(self.dataframe, font='Arial 9 bold',
                                         bg='#fff')
        self.closetime_label.place(x=30, y=145)

        # Additional Informations of stock
        # Additional info includes Headings and its corresponding values
        #Open, High, Low, Mkt-Cap, P/E Ratio, Div yield,
        #Prev-Close, 52k-wk high, 52k-wk low are the additional headings
        # Info 1
        self.headinfo1 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.headinfo1.place(x=30, y=180)
        self.valueinfo1 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.valueinfo1.place(x=150, y=180)

        # Info 2
        self.headinfo2 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.headinfo2.place(x=30, y=210)
        self.valueinfo2 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.valueinfo2.place(x=150, y=210)

        # Info 3
        self.headinfo3 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.headinfo3.place(x=30, y=240)
        self.valueinfo3 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.valueinfo3.place(x=150, y=240)

        # Info 4
        self.headinfo4 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.headinfo4.place(x=30, y=270)
        self.valueinfo4 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.valueinfo4.place(x=150, y=270)

        # Info 5
        self.headinfo5 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.headinfo5.place(x=30, y=300)
        self.valueinfo5 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.valueinfo5.place(x=150, y=300)

        # Info 6
        self.headinfo6 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.headinfo6.place(x=310, y=180)
        self.valueinfo6 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.valueinfo6.place(x=450, y=180)

        # Info 7
        self.headinfo7 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.headinfo7.place(x=310, y=210)
        self.valueinfo7 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.valueinfo7.place(x=450, y=210)
        
        # Info 8
        self.headinfo8 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.headinfo8.place(x=310, y=240)
        self.valueinfo8 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.valueinfo8.place(x=450, y=240)

        # Info 9
        self.headinfo9 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.headinfo9.place(x=310, y=270)
        self.valueinfo9 = tk.Label(self.dataframe, font='arial 10', bg='#fff')
        self.valueinfo9.place(x=450, y=270)



    def get_stock(self):
        # Disabling search button to prevent multiple-clicks when searching
        self.search_btn.config(state='disabled')

        # user agent and language is used as a loophole to fetch data from google
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE

        # Searching in Google
        stock = self.search_box.get()
        url = "https://www.google.com/search?q=Stock+" + stock
        # print(url)

        response = session.get(url)
        # Fetching Values from Google Stock Card
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup)
        try:
            # Fetching subset of entire webpage, Just the google card
            card = soup.find('div', class_='aviV4d')
            # print(card.prettify())

            # Stock name of company
            stock_name = card.find('div', class_='oPhL2e').text
            # Stock exchange name or Ticker Symbol
            ticker_symbol = card.find('div', class_='HfMth').text
            # Current stock amount
            stock_amt = card.find('span', jsname='vWLAgc').text

            try:
                # Currency Denomination ie., USD, INR EUR etc.
                currency_denomination = card.find('span', jsname='T3Us2d').text
                stock_value = stock_amt + currency_denomination
            except:
                stock_value = stock_amt
            
            # Fluctuation/ Change of stock value
            stock_change_amt = card.find('span',{'jsname':'qRSVye'}).text
            stock_change_percent = card.find('span',{'jsname':'rfaVEf'}).text
            stock_change = stock_change_amt + stock_change_percent

            # Market Closed Time
            market_closed = card.find('span', jsname='ihIZgd').text

            # Additional Data of that stock
            # Open, High, Low, Mkt-Cap, P/E ratio, Div Yield,
            #  Prev Close, 52k-wk high, 52-wk low
            table = card.find('div', class_='QhLvnd')
            # All headings in that table container
            theads = table.findAll(class_='JgXcPd')
            # All valuess in that table container
            tvalues = table.findAll(class_='iyjjgb')

            data_table = []
            for i, head in enumerate(theads):
                data_table.append({'headings':head.text, 'values': tvalues[i].text})
            # print(data_table)
            
            #============= Reseting DataFrame label values to blank ===========#
    
            self.closetime_label.config(text='')
    
            # for index in enumerate(data_table, start=1): # index starts from 1
            for index in range(1, 10):
                exec("self.headinfo{}.config(text='')".format(index))
                exec("self.valueinfo{}.config(text='')".format(index))

            #============= Inserting Values to data frame   ===================#

            # Inserting stock name
            self.sname_label.config(text=stock_name)
            
            # Inserting Ticker Symbol
            self.ticker_symbol_label.config(text=ticker_symbol)
            
            # Inserting Stock Value
            self.svalue_label.config(text=stock_value)

            # Inserting Stock Change/ Fluctuation
            if stock_change[0] == '+':  # Raise condition
                self.schange_label.config(text=f'{stock_change} \u2191',
                                         fg='green')  # "\u2191" for up arrow
            else:	# Fall Condition
                self.schange_label.config(text=f'{stock_change} \u2193',
                                        fg='red')  # "\u2193" for down arrow 
            
            # Inserting Stock Market Close time
            self.closetime_label.config(text=f'Closed : {market_closed}')

            # Inserting Additional info/data of stock
            # Open, High, Low, Mkt-Cap, P/E ratio, Div Yield,
            #  Prev Close, 52k-wk high, 52-wk low
            for index, data in enumerate(data_table, start=1): # index starts from 1
                heading = data['headings']
                value = data['values']

                exec("self.headinfo{}.config(text='{}')".format(index, heading))
                exec("self.valueinfo{}.config(text='{}')".format(index, value))


            # # Calling print function
            # self.print_stock(stock_name, ticker_symbol, stock_value,
            #                  stock_change, market_closed, data_table)

            # Enabling search button after search is completed
            self.search_btn.config(state='normal')

        except Exception as e:
            print(e)
            # Showing error message
            messagebox.showerror("showerror",
                             "There was a problem retrieving that information\nRecheck the Stock Name entered or Try a different Stock Name")
            # Deleting Entry of Search-box
            self.search_box.delete(0, 'end')
            # Enabling search button
            self.search_btn.config(state='normal')
    
    def print_stock(self, stock_name, ticker_symbol, stock_value,
                     stock_change, market_closed, data_table):
        print("Stock Name :",stock_name)
        print("Ticker Symbol :",ticker_symbol)
        print("Stock Value :",stock_value)
        
        if stock_change[0] == '+':  # Raise condition
            print("Stock Change :", stock_change, "\u2191") # "\u2191" for up arrow 
        else:	# Fall Condition
            print("Stock Change :", stock_change, "\u2193") # "\u2193" for down arrow 
        
        print("Closed Time :",market_closed)

        for data in data_table:
            print(data['headings'], end=" : ")
            print(data['values'], end="\n")



if __name__ == '__main__':
    # Constant Variables
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    master = tk.Tk()
    app = StockWindow(master)
    master.mainloop()