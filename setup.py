from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ytmp4-kp",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple command-line tool to download YouTube videos in MP4 format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ytmp4-kp",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.6",
    install_requires=[
        "yt-dlp>=2023.3.4",
    ],
    entry_points={
        "console_scripts": [
            "ytmp4-kp=ytmp4_kp.main:main",
        ],
    },
)
