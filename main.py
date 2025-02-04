import smtplib



def emailsenden(message):
    email ="hasunajizi@gmail.com"
    receiver_email="hasunajizi@gmail.com"
    

    subject="Python"
   

    text=f"Subject: {subject}\n\n{message}"
    server= smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, "ywia fmmm nsmd lswx")
    server.sendmail(email, receiver_email, text.encode('utf-8'))


    print("gesendet")


if __name__ == "__main__":
    emailsenden("test")