import logging 

try:
    print(10/0)
except Exception:
    print("error")
    logging.exception(Exception)

print("continue")