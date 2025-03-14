#!/usr/bin/env python3
import argparse
import os
import sys
import subprocess
import platform
import shutil

def check_yt_dlp_installed():
    """Check if yt-dlp is installed and install it if not"""
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

def download_video(url, output_path=None):
    """Download a YouTube video using yt-dlp"""
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
    parser = argparse.ArgumentParser(description='Download YouTube videos in MP4 format')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('output_path', nargs='?', default=None, help='Path where the video will be saved (optional)')
    
    args = parser.parse_args()
    
    download_video(args.url, args.output_path)

if __name__ == "__main__":
    main()
