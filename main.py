import os
import random
import socket
from pprint import pp

import numpy as np
import tomli
import torch

import src.utils as utils

##########################################
# Main Program for MoriaTestRun
# - Self identifies Local/Moriah
# - Sets configuration according to config
# - Idetifies best Torch device (CPU/GPU)
# - Logs the available TensorFlow devices
##########################################


## Configuration
utils.print_section("Setting up configuration and paths.")

# Get computer name
computer_name = socket.gethostname()
print(f"\nComputer/node Name: {computer_name}\n")

# Load configuration file
config_file_path = "config.toml"
with open(config_file_path, "rb") as f:
    config = tomli.load(f)

# Set data and output paths based on computer name (Local vs Moriah)
if computer_name in config["local"]["local_computer_name"]:
    config["data_path"] = config["local"]["data_path"]
    config["output_path"] = os.path.join(config["local"]["output_path"])
elif any(
    item in computer_name for item in config["moriah"]["moriah_node_types"]
):  # computer_name in config["moriah"]["moriah_node_types):
    config["data_path"] = config["moriah"]["data_path"]
    config["output_path"] = os.path.join(config["moriah"]["output_path"])

pp(config)

# Ensure reproducibility
random.seed(config["seed"])  # Setting random seed for reproducibility
np.random.seed(config["seed"])


## FINDING BEST TORCH/TF DEVICE
utils.print_section("See available devices and select best Torch device.")

# Get best Torch device:
device_torch = utils.get_best_torch_device()

# Log the TF device being used:
# utils.log_available_tf_device()

## Exit
utils.print_section("Done with program, exiting")
