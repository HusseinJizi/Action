import xlwings as xw
import yfinance as yf
import smtplib  # Zum Versenden von E-Mails
import time


def get_stock_info(symbol):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        name = info.get("longName", "-")
        price = info.get("regularMarketPrice", "-")
        return (name, price) if name != "-" and price != "-" else (None, None)
    except Exception:
        return None, None


def emailsenden(message):
    try:
        email = "hasunajizi@gmail.com"
        receiver_email = "hasunajizi@gmail.com"
        subject = "Preisalarm: Aktienupdate"

        html_message = f"""
        <html>
        <body style='font-family: Arial, sans-serif; padding: 20px; background-color: #f4f4f4;'>
            <div style='max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);'>
                <h2 style='color: #2C3E50; text-align: center;'>Preisalarm Benachrichtigung</h2>
                <p style='font-size: 16px; color: #333;'>Hier sind die aktuellen Kursbewegungen deiner überwachten Aktien:</p>
                <div style='border-left: 4px solid #3498db; padding: 15px; background-color: #ecf0f1; margin: 10px 0;'>
                    {message.replace("\n\n", "<br><br>")}
                </div>
                <p style='margin-top: 20px; font-size: 14px; color: #555; text-align: center;'>Bleib informiert & viel Erfolg beim Investieren!</p>
                <p style='text-align: center; font-weight: bold; color: #2C3E50;'>Dein Preisalarm-Team</p>
            </div>
        </body>
        </html>
        """

        msg = f"Subject: {subject}\nMIME-Version: 1.0\nContent-Type: text/html\n\n{html_message}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, "ywia fmmm nsmd lswx")
        server.sendmail(email, receiver_email, msg.encode('utf-8'))
        server.quit()
        
    except Exception as e:
        print(f"⚠️ Fehler beim E-Mail-Versand: {e}")


def update_excel():
    wb = xw.Book("ButtonTest.xlsm")
    ws = wb.sheets[0]
    all_messages = []

    last_row = ws.range("A" + str(ws.cells.last_cell.row)).end("up").row

    for row in range(11, last_row + 1):
        symbol = ws.range(f"A{row}").value or ws.range(f"B{row}").value
        if not symbol or symbol == "Egal":
            continue

        name, price = get_stock_info(symbol)
        if name and price:
            ws.range(f"C{row}").value = name
            ws.range(f"D{row}").value = price

    for row in range(11, last_row + 1):
        percentage = ws.range(f"F{row}").value
        if percentage:
            name = ws.range(f"C{row}").value
            price = ws.range(f"D{row}").value
            message = f"<strong>{name}</strong> liegt aktuell bei <strong style='color:#e74c3c;'>{price} USD</strong>, was <strong>{percentage}%</strong> von deinem Preisalarm entfernt ist."
            all_messages.append(message)

    wb.save()  # Speichern der Änderungen ohne die Datei zu schließen
    return all_messages


def check_and_send_email():
    all_messages = update_excel()
    if all_messages:
        emailsenden("<br><br>".join(all_messages))
    else:
        print("ℹ️ Keine relevanten Nachrichten zum Versenden.")


last_email_time = 0
email_interval = 180
last_update_time = 0
update_interval = 120

while True:
    current_time = time.time()

    if current_time - last_update_time >= update_interval:
        update_excel()
        last_update_time = current_time
        print("🔄 Daten aktualisiert.")

    if current_time - last_email_time >= email_interval and last_update_time > 0:
        check_and_send_email()
        last_email_time = current_time
        print("📬 E-Mail gesendet.")

    time.sleep(60)