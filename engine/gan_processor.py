import os
from scenarios.configs import GAN_OUTPUTS

def get_gan_output(uploaded_filename):
    name = uploaded_filename.lower().strip()
    return GAN_OUTPUTS.get(name, None)