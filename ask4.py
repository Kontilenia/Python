def one(m=1):
    #elenxo an dothike orisma stin sinartisi
    if isinstance(m, tuple):
        j = m[0]
        k = m[1]
        #an nai tote ektelo tis katalliles prakseis me elenxous
        for i in range(1, 11):
            if k == "plus":
                if j == i:
                    print(i+1)
            if k == "times":
                if j == i:
                    print(i*1)
            if k == "minus":
                if j == i:
                    print(1-i)
    else:
        #allios epistrefo tin time tis sinartisis pou kalesteike
        return m
#akribos me ton idio tropo leitourgoun oi sunartiseis two-nine

def two(m=2):
    if isinstance(m, tuple):
        j = m[0]
        k = m[1]
        for i in range(1, 11):
            if k == "plus":
                if j == i:
                    print(i+2)
            if k == "times":
                if j == i:
                    print(i*2)
            if k == "minus":
                if j == i:
                    print(2-i)
    else:
        return m


def three(m=3):
    if isinstance(m, tuple):
        j = m[0]
        k = m[1]
        for i in range(1, 11):
            if k == "plus":
                if j == i:
                    print(i + 3)
            if k == "times":
                if j == i:
                    print(i * 3)
            if k == "minus":
                if j == i:
                    print(3-i)
    else:
        return m


def four(m=4):
    if isinstance(m, tuple):
        j = m[0]
        k = m[1]
        for i in range(1, 11):
            if k == "plus":
                if j == i:
                    print(i+4)
            if k == "times":
                if j == i:
                    print(i*4)
            if k == "minus":
                if j == i:
                    print(4-i)
    else:
        return m


def five(m=5):
    if isinstance(m, tuple):
        j = m[0]
        k = m[1]
        for i in range(1, 11):
            if k == "plus":
                if j == i:
                    print(i+5)
            if k == "times":
                if j == i:
                    print(i*5)
            if k == "minus":
                if j == i:
                    print(5-i)
    else:
        return m


def six(m=6):
    if isinstance(m, tuple):
        j = m[0]
        k = m[1]
        for i in range(1, 11):
            if k == "plus":
                if j == i:
                    print(i+6)
            if k == "times":
                if j == i:
                    print(i*6)
            if k == "minus":
                if j == i:
                    print(6-i)
    else:
        return m


def seven(m=7):
    if isinstance(m, tuple):
        j = m[0]
        k = m[1]
        for i in range(1, 11):
            if k == "plus":
                if j == i:
                    print(i+7)
            if k == "times":
                if j == i:
                    print(i*7)
            if k == "minus":
                if j == i:
                    print(7-i)
    else:
        return m


def eight(m=8):
    if isinstance(m, tuple):
        j = m[0]
        k = m[1]
        for i in range(1, 11):
            if k == "plus":
                if j == i:
                    print(i+8)
            if k == "times":
                if j == i:
                    print(i*8)
            if k == "minus":
                if j == i:
                    print(8-i)
    else:
        return m


def nine(m=9):
    if isinstance(m, tuple):
        j = m[0]
        k = m[1]
        for i in range(1, 11):
            if k == "plus":
                if j == i:
                    print(9+i)
            if k == "times":
                if j == i:
                    print(i*9)
            if k == "minus":
                if j == i:
                    print(9-i)
    else:
        return m


def zero(m=0):
    if isinstance(m, tuple):
        j = m[0]
        k = m[1]
        for i in range(1, 11):
            if k == "plus":
                if j == i:
                    print(i+0)
            if k == "times":
                if j == i:
                    print(i*0)
            if k == "minus":
                if j == i:
                    print(0-i)
    else:
        return m




#stis sinartiseis ton prakseon epistrefo tin praksi kai to orisma tis

def plus(s=0):
    p = "plus"
    return s, p


def minus(s=0):
    p = "minus"
    return s, p


def times(s=0):
    p = "times"
    return s, p


six(minus(two()))



