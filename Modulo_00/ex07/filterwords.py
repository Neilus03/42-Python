import string
from sys import argv

def filterwords(S: str, N: int) -> list:
    words = S.split(" ")
    out = [w.translate(str.maketrans("", "", string.punctuation)) for w in words]
    out = [w for w in out if len(w) > N]
    return(out)

if len(argv) != 3:
    print("Error, invalid amount of arguments")
else:
    try:
              str(argv[1])
              int(argv[2])
              print(filterwords (str(argv[1]),int(argv[2])))
    except:
        raise AssertionError("Invaid format")
	