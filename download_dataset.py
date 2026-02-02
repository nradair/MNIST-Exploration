# Download and prepare dataset

from torchvision.datasets import QMNIST
QMNIST(root='./data', what='train', compat=True, train=True, download=True)
QMNIST(root='./data', what='test', compat=True, train=False, download=True)
