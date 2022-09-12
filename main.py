# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    with open("/Users/juliawang/Desktop/Algorithm/10.in") as f:
        n = f.readline()
        shift = []
        for l in f.readlines():
            start, end = l.split()
            shift.append([int(start), int(end)])

        shift.sort(key=lambda start: start[0])
        r = 0

        for i in range(int(n)):
            s = e = -1
            sum = 0
            for j in range(int(n)):
                if i != j:
                    if shift[j][0] <= e: e = max(e, shift[j][1])
                    else:
                        sum += e - s
                        s = shift[j][0]
                        e = shift[j][1]

            sum += e - s
            r = max(r, sum)
        with open('10.out', 'w') as an:
            an.write(str(r))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
