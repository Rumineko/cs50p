def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        userdate = input("Date: ").strip()
        try:
            if "/" in userdate:
                M, D, Y = userdate.split("/")
                M = int(M)
                D = int(D)
                Y = int(Y)
                if D <= 31 and M <= 12:
                    print(f"{Y}-{M:02}-{D:02}")
                    break
                else:
                    pass
            else:
                if ","in userdate:
                    userdate = userdate.replace(",", "")
                    M, D, Y = userdate.split(" ")
                    D = int(D)
                    M = M.title()
                    if M in months:
                        month = months.index(M)+1
                        if D <= 31 and month <= 12:
                            print(f"{Y}-{(months.index(M)+1):02}-{D:02}")
                            break
                        else:
                            pass
                    else:
                        pass
        except ValueError:
            pass


main()