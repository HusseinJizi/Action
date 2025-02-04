import main

import yfinance as yf

ticker = yf.Ticker("^NDX")
data = ticker.history(period="1d")  # Tagesdaten abrufen

open_kurs = data["Open"][0]
aktueller_kurs = data["Close"][0]
differenz = aktueller_kurs - open_kurs
prozent = (differenz / open_kurs) * 100

nachricht =(f"NASDAQ-100: {aktueller_kurs} USD\n"
      f"Eröffnungskurs: {open_kurs} USD\n"
      f"Veränderung: {differenz:.2f} USD ({prozent:.2f}%)")

main.emailsenden(f'"{nachricht}"')
print("NASDAQ-Bericht gesendet!")


