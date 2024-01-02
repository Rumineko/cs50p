def file(type):
    if type.endswith(".gif") == True:
        print("image/gif")
    elif type.endswith(".jpg") == True:
        print("image/jpeg")
    elif type.endswith(".jpeg") == True:
        print("image/jpeg")
    elif type.endswith(".png") == True:
        print ("image/png")
    elif type.endswith(".pdf") == True:
        print ("application/pdf")
    elif type.endswith(".txt") == True:
        print ("text/plain")
    elif type.endswith(".zip") == True:
        print ("application/zip")
    else:
        print ("application/octet-stream")

def main():
    extension = input("File name: ").strip().lower()
    file(extension)

main()