"""
Utility functions for the ytmp4-kp package.
"""

import subprocess
import sys

def check_yt_dlp_installed():
    """
    Check if yt-dlp is installed and install it if not.
    
    Returns:
        bool: True if yt-dlp is installed (or was installed successfully), False otherwise
    """
    try:
        # Try to run yt-dlp --version
        subprocess.run(["yt-dlp", "--version"], 
                      stdout=subprocess.PIPE, 
                      stderr=subprocess.PIPE,
                      check=True)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        print("yt-dlp is not installed. Installing now...")
        try:
            # Install yt-dlp using pip
            subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp"], 
                          check=True)
            print("yt-dlp installed successfully!")
            return True
        except subprocess.SubprocessError:
            print("Failed to install yt-dlp automatically.")
            print("\nPlease install it manually:")
            print("pip install yt-dlp")
            print("\nOr visit: https://github.com/yt-dlp/yt-dlp#installation")
            return False
