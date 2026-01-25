fname = input("File Name: ").lower()
if ".gif" in fname:
    print("image/gif")
elif ".jpg" in fname:
    print("image/jpeg")
elif ".jpeg" in fname:
    print("image/jpeg")
elif ".png" in fname:
    print("image/png")
elif ".pdf" in fname:
    print("application/pdf")
elif ".zip" in fname:
    print("application/zip")
elif ".txt" in fname:
    print("text/plain")
else:
    print("application/octet-stream")

