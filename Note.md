# Note
MM:DD::YY

### 06.23.19

* [Difference between batch size and epoch](https://machinelearningmastery.com/difference-between-a-batch-and-an-epoch/)
* [How batch-size affect learning speed](https://machinelearningmastery.com/how-to-control-the-speed-and-stability-of-training-neural-networks-with-gradient-descent-batch-size/)
* Note:
    * Batch size
        1. The batch size is a number of samples processed before the model’s internal parameters are updated.
        2. Type of Batch size:
            * Batch Gradient Descent: Batch Size = Size of Training Set
            * Stochastic Gradient Descent: Batch Size = 1
            * Mini-Batch Gradient Descent: 1 < Batch Size < Size of Training Set
        3. batch size = 32 is a good default value.

    * Epoch
        * The number of epochs is the number of complete passes through the training dataset.
        * The number of times each sample in the training set has an opportunity to update the internal parameters on the neural network.

#### 06.24.19
* [Install CUDA + cuDNN](https://medium.com/@cjanze/how-to-install-tensorflow-with-gpu-support-on-ubuntu-18-04-lts-with-cuda-10-nvidia-gpu-312a693744b5)
* [Install OpenCv 3.4.3](https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/)
* [Install Cafe 1.0.0](https://mc.ai/caffe-installation-on-ubuntu-18-04-lts-python-3-6/)

#### 06.26.19
* [What is lmdb database?](https://chunml.github.io/ChunML.github.io/project/Training-Your-Own-Data-On-Caffe/)

Note:
* “Why LMDB? Why is LMDB converting considered recommended, especially when we are working with large image database? To make it short, because it helps improve the performance of our Network. At present, performance is not all about accuracy anymore, but required to be both fast and accurate. With a same Network and a same dataset, how the data was prepared will decide how fast our Network learns. And LMDB conversion is one way (among many) which helps accomplish that.”

* [How can we create lmdb database?](https://stackoverflow.com/questions/31427094/a-guide-to-convert-imageset-cpp)

#### 07.04.19
* [How To Switch Between Intel and Nvidia Graphics Card on Ubuntu](https://www.linuxbabe.com/desktop-linux/switch-intel-nvidia-graphics-card-ubuntu)
* [How do I access command line arguments in Python? - Stack Overflow](https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python)