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
        print(shift)
        own_shift = []
        for i in range(int(n)):
            own_shift.append(shift[i][1] - shift[i][0])
        print(own_shift)
        count = []
        for i in range(int(n)-1):
            if shift[i][1] > shift[i+1][0]:
                count.append(shift[i][1] - shift[i+1][0])
                own_shift[i] -= shift[i][1] - shift[i+1][0]
                own_shift[i+1] -= shift[i][1] - shift[i+1][0]

        print(own_shift)
        min_v = min(own_shift)
        min_index = own_shift.index(min_v)
        fire_shift = shift.pop(min_index)
        final_shift = []
        answer = 0
        for i in range(int(n) - 1):
            final_shift.append(shift[i][1] - shift[i][0])
            answer += final_shift[i]
        print(answer)

        with open('10.out', 'w') as an:
            an.write(str(answer))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
