import tensorflow as tf
import torch

def get_best_torch_device():
    """Get the best available PyTorch device.

    Returns:
        torch.device: The best available device (CPU, CUDA, or MPS).
    """
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"Using CUDA: {torch.cuda.get_device_name(device)}")
    elif getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        device = torch.device("mps")
        print("Using Apple MPS (Metal Performance Shaders)")
    else:
        device = torch.device("cpu")
        print("Using CPU")
    return device


def log_available_tf_device():
    """Log the best available TensorFlow device (GPU, MPS, or CPU)."""
    # Get physical devices
    gpus = tf.config.list_physical_devices("GPU")
    all_devices = tf.config.list_physical_devices()
    # Check for CUDA GPU
    if gpus:
        print(f"Using CUDA GPU: {gpus[0].name}")
    # Check for Apple MPS
    elif any("MPS" in dev.device_type for dev in all_devices):
        print("Using Apple MPS (Metal Performance Shaders)")
    else:
        print("Using CPU")
        
        
def print_section(title):
    """Print a section header.

    Args:
        title (str): The title of the section.
    """
    print(f"\n{'#' * 25}\n{title}\n{'#' * 25}\n")
        