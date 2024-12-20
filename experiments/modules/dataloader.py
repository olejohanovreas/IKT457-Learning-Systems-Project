import numpy as np

def load_data(filepath, ratio):
    boards = []
    labels = []

    with open(filepath, "r") as file:
        lines = file.readlines()

    #skip the first line
    data_lines = lines[1:]

    #split lines into boards and labels
    for line in data_lines:
        splitted = line.split(',')
        board = splitted[0]
        label = splitted[1]
        boards.append(board)
        labels.append(label)

    #convert the labels to a numpy array
    labels = np.array(labels, dtype=np.uint32)

    print("Number of boards:", len(boards))
    print("First board:", boards[0])
    print("First label:", labels[0])

    #splitting dataset

    split_point = int(len(labels) * ratio)

    #slice dataset
    boards_train = boards[:split_point]
    boards_test = boards[split_point:]
    labels_train = labels[:split_point]
    labels_test = labels[split_point:]

    print("Training samples: ", len(boards_train))
    print("Test samples: ", len(boards_test))
    print("First training board: ", boards_train[0])
    print("First training label: ", labels_train[0])
    print("First test board: ", boards_test[0])
    print("First test label: ", labels_test[0])

    return boards_train, labels_train, boards_test, labels_test