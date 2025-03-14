# ytmp4-kp

> A simple command-line tool to download YouTube videos in MP4 format.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- Download YouTube videos in high-quality MP4 format
- Simple command-line interface
- Real-time download progress
- Automatic dependency installation
- Cross-platform (Windows, macOS, Linux)
- Custom download location support

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Method 1: From PyPI (Recommended)

```bash
pip install ytmp4-kp
```

### Method 2: From Source

```bash
# Clone the repository
git clone https://github.com/yourusername/ytmp4-kp.git
cd ytmp4-kp

# Install the dependencies
pip install -r requirements.txt

# Make the script executable (Linux/macOS only)
chmod +x ytmp4-kp.py
```

## Usage

### Basic Usage

```bash
ytmp4-kp [URL]
```

This will download the video to the current directory.

### Specify Download Location

```bash
ytmp4-kp [URL] [OUTPUT_PATH]
```

For example:

```bash
ytmp4-kp https://www.youtube.com/watch?v=example ~/Downloads/Videos
```

### Global Installation (Optional)

To make `ytmp4-kp` available as a global command:

#### On Linux/macOS:

```bash
# Create a symbolic link
sudo ln -s /full/path/to/ytmp4-kp.py /usr/local/bin/ytmp4-kp

# Or install as a package
pip install -e .
```

#### On Windows:

Create a batch file named `ytmp4-kp.bat` with the following content:

```batch
@echo off
python C:\full\path\to\ytmp4-kp.py %*
```

Place this file in a directory included in your PATH.

## How It Works

`ytmp4-kp` is built on top of [yt-dlp](https://github.com/yt-dlp/yt-dlp), a powerful YouTube downloader that is actively maintained. The script:

1. Checks if yt-dlp is installed and installs it if necessary
2. Processes the command-line arguments
3. Fetches information about the video
4. Downloads the video in MP4 format
5. Displays download progress in real-time

## Configuration Options

The default behavior can be modified by editing the script. Future versions will include a configuration file.

## Dependencies

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Core functionality for downloading videos

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful downloader that makes this tool possible
- Everyone who has contributed to the YouTube downloading open-source community

## Disclaimer

This tool is for educational purposes only. Please respect YouTube's terms of service and copyright laws when using this tool. Only download content you have the right to access.
