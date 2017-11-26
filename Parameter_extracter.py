set1 = set()

N = 0
N_phase1 = 1
N_phase2 = 0
N_phase3 = 0
N_phase4 = 0


def main():
    with open("/home/darkmatter/Documents/Rumour_Spreading_Modelling/data/higgs-activity_time.txt", "r") as main_file:
        global N
        for text in main_file:
            text = text.split()
            set1.add(text[0])
            N = len(set1)

    set1.clear()

    with open("data/data_set_1.txt", "r") as main_file:
        global N_phase2
        for text in main_file:
            text = text.split()
            set1.add(text[0])
            N_phase2 = len(set1)


    with open("data/data_set_2.txt", "r") as main_file:
        global N_phase3
        for text in main_file:
            text = text.split()
            set1.add(text[0])
            N_phase3 = len(set1)

    with open("data/data_set_3.txt", "r") as main_file:
        global N_phase4
        for text in main_file:
            text = text.split()
            set1.add(text[0])
            N_phase4 = len(set1)

    set1.clear()

    print (N,N_phase1,N_phase2,N_phase3,N_phase4)


if __name__ == '__main__':
    main()
