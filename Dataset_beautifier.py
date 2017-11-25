data_set = []

# UNix time stamp
PHASE_1 = 1341214200  # before 02-07-2012 01:00:00 PM
PHASE_2 = 1341253799  # After PHASE_1 till 02-07-2012 11:59:59 PM
PHASE_3 = 1341368999  # After PHASE_2 till 04-07-2012 07:59:59 AM


file1 = 0
file2 = 0
file3 = 0
file4 = 0


def extract_in_list():
    with open("/home/darkmatter/Documents/Network/data/higgs-activity_time.txt") as data_file:
        for text in data_file:
            text = text.strip()
            data_set.append(text)


def create_data_file(value):
    words = value.split()
    global file1
    timestamp = int(float(words[2]))
    if timestamp < PHASE_1:
        file1.write(words[0] + " " + words[1] + " " + words[3] + "\n")

    elif PHASE_1 <= timestamp <= PHASE_2:
        file2.write(words[0] + " " + words[1] + " " + words[3] + "\n")

    elif PHASE_2 < timestamp <= PHASE_3:
        file3.write(words[0] + " " + words[1] + " " + words[3] + "\n")

    elif timestamp > PHASE_3:
        file4.write(words[0] + " " + words[1] + " " + words[3] + "\n")


def main():
    extract_in_list()
    global file1, file2, file3, file4
    file1 = open("/home/darkmatter/Documents/Network/data/data_set_1.txt", "w")
    file2 = open("/home/darkmatter/Documents/Network/data/data_set_2.txt", "w")
    file3 = open("/home/darkmatter/Documents/Network/data/data_set_3.txt", "w")
    file4 = open("/home/darkmatter/Documents/Network/data/data_set_4.txt", "w")

    for value in data_set:
        create_data_file(value)

    file1.close()
    file2.close()
    file3.close()
    file4.close()


if __name__ == '__main__':
    main()
