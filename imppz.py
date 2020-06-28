import models


def read_fl(fname):
    lst = []
    with open(fname, "r") as f:
        for ln in f.readlines():
            dat = ln.split(",")
            v = dat[:-1]
            t = int(dat[-1])
            lst.append(models.Expression(v, t))
    return models.Puzzle(lst)


if __name__ == "__main__":
    samplepz = read_fl("sample.csv")
    print(samplepz)
