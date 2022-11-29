CHANNEL_NUM = 3
SIZE = 256
CLEAN_DIR = './samples/clean'
NOISY_DIR = './samples/noisy'
DDPM_DENOISED_DIR = 'samples/ddpm-denoised'
MPRNET_DENOISED_DIR = 'samples/mprnet-denoised'
MODEL = 'lsun_church'
DEVICE = 'cuda:0'
SAVE_NOISY = False  # True when saving noisy images, False when denoising
GAUSSIAN_NOISE = True  # True if noises are Gaussian-distributed, False if Poisson-distributed
LEVELS = [.05, .1, .2, .5, .7, .9]