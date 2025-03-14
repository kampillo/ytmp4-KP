#!/usr/bin/env python3
"""
ytmp4-kp main module - contains the main functionality for downloading YouTube videos.
"""

import argparse
import os
import sys
import subprocess
import platform

from .utils import check_yt_dlp_installed

def download_video(url, output_path=None):
    """
    Download a YouTube video using yt-dlp
    
    Args:
        url (str): The YouTube video URL
        output_path (str, optional): Path where the video will be saved. Defaults to None.
        
    Returns:
        bool: True if download was successful, False otherwise
    """
    if not check_yt_dlp_installed():
        return False
    
    try:
        # If no output path specified, use current directory
        if not output_path:
            output_path = os.getcwd()
        
        # Create directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        # Get video info first
        print(f"Getting video information: {url}")
        info_command = ["yt-dlp", "--dump-json", url]
        result = subprocess.run(info_command, 
                               capture_output=True, 
                               text=True,
                               check=True)
        
        # If we get here, the URL is valid
        print("Video found! Starting download...")
        
        # Build the download command
        output_template = os.path.join(output_path, "%(title)s.%(ext)s")
        command = [
            "yt-dlp",
            "--format", "mp4",    # Format to download
            "--output", output_template,
            "--progress",         # Show progress bar
            url
        ]
        
        # Run the download command
        print(f"Downloading video to: {output_path}")
        subprocess.run(command, check=True)
        
        print(f"Video successfully downloaded to: {output_path}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error downloading the video: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False

def main():
    """
    Main entry point for the ytmp4-kp command.
    Parses command-line arguments and initiates the download.
    """
    parser = argparse.ArgumentParser(description='Download YouTube videos in MP4 format')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('output_path', nargs='?', default=None, help='Path where the video will be saved (optional)')
    parser.add_argument('--version', action='version', version=f'ytmp4-kp {__import__("ytmp4_kp").__version__}')
    
    args = parser.parse_args()
    
    return 0 if download_video(args.url, args.output_path) else 1

if __name__ == "__main__":
    sys.exit(main())
