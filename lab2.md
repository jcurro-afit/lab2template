# Lab 2
# Python Basics 
This lab goes over Python basics and then some keras basics

## Setup
- Make a new repository using the template. You will use this repo to hold the code for the rest of the project. You must have at least 2 commits for this project ie. do not just upload the whole thing in one commit.
- Add a `.gitignore` so files like `.idea`, `.pyc`, '.hf5' etc. do not end up on the repo. You should never upload large data files to the git repo. 
- Make a new PyCharm project and configure the `dockerfile` and `docker-compose.yml` to run your code using the `lab2` service. 
- Make a new python file called `lab2.py` in the `src` folder

## Numpy and Matplotlib basics
This section will go over basic array manipulation in numpy. Complete each task in order as they build on each other. You are not allowed to use python loops.
### Plotting
1. Make an array named `t` which ranges from 0 to 10 in increments of 0.01. (0 should be the first value and the last should be 9.99)
2. Make an array named `x` which is a function of `t` such that  `x=sinc(t)`. Remember that `sinc(0) = 1`
3. Plot `x` vs `t` and label all axes. 
4. Using slicing to clip the `x` values to a max of 0.1 and plot again in a new figure
5. Multiply the last 100 `x` values by 10 and the second to last 100 values times 2 and plot again. 
### Tensor Manipulation
1. Slice out values from indices 500 to 509 (not including 509, this array should have 9 values) of `x` and reshape to be 3 by 3 and call that new variable `X`
2. Slice out the first 3 values of `x` and store that to a variable called `y`
3. Do a matrix multiplication of `X` and `y` and print the result `z`
4. Next do an elementwise multiplication of `X` and `y` and print the result `Z`
5. Concat horizontally `[X|Z]`(should be a `3 x 6` array) and matrix multiply by `y` concatenated to itself `[y|y]` (should be a `6 x 1` array) and print the result `S`.

# Keras Basics

## Hello World Mnist
Start a new python script called `hellomnist.py`
Make the network from 3blue1brown to work with the mnist dataset using the instructions below. Use the keras dataset package to load the mnist dataset as shown in the examples from the Chollet textbook (included in the template code).

### 3blue1brown Network:
- input should be flattened images of size 784 with grayscale values 0 to 1. 
- output labels should be a vector of size 10 with a one in the index of the correct class
- 2 dense layers with 16 nodes each. For these layers use a sigmoid activation
- 1 Output layer with 10 outputs. For this layer use a linear activation
- compile the model with `mean_squared_error` as a loss and use stochastic gradient descent `sgd` as the optimizer
- keep everything else `keras` defaults
- Train for 30 epochs and validation accuracy should be around 75%.

### Your Network
Make your own separate network the beats the 3blue1brown network above. Use any improvement you want as long as your accuracy is higher.

### Dense Data
In order to show that the ANNs in the 3blue1brown (and most likely the one you made) do not think of the data as humans do we will train one last network. 
This network will be exactly the same as the 3blue1brown network but we will change the training data. We are going to reorder the pixels in every image the **exact same way**. For template function see `hellomnist.py`. Using the template function you can mix up the pixels in your training and test set in the **exact same order** for each image in each dataset. 
Make a plot showing the very first image in the normal dataset and the mixed up dataset. Predict the performance you think the ANN will achieve with this new dataset given what you see. Write this in a comment in the python script.

Now retrain the 3blue1brown network using the mixed up data and compare the performance to the first one you trained (with the normal data) in a comment in the python script.

## Git
Remember to submit your code to the git repo and post a link on Canvas.

## Easier to Grade
To grade this lab I will clone your repo and then in the project root run the command
```bash
docker-compose up --build lab2deploy
```
That should be enough to run the entire lab and show me all the output I have asked for. 