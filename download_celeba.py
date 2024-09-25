from torchvision.datasets.celeba import CelebA
PATH_DATASETS = 'Data/'

# Needs gdown package!!!
# > pip install gdown
celeba = CelebA(PATH_DATASETS, split='all', download=True)