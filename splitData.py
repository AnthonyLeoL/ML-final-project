import random
fn = "scaled_whites"
filein = open(fn)
fileoutTrain = open("training_whites", "w")
fileoutTest = open("testing_whites", "w")
random.seed(0)
lines = filein.readlines()
trainCount = 0
testCount = 0
for line in lines:
    if(random.randint(0, 10) < 9):
        fileoutTrain.write(line)
        trainCount += 1
    else:
        testCount += 1
        fileoutTest.write(line)
print("done\n training data = {} test data = {}".format(trainCount, testCount))
