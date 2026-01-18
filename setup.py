"""
Setup configuration for Ocularis Mose
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mose",
    version="1.1.0",
    description="Eye tracking mouse control system - Control your computer with your eyes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Blackmvmba88",
    url="https://github.com/Blackmvmba88/Mose",
    packages=find_packages(),
    py_modules=["main", "main_modular"],
    entry_points={
        "console_scripts": [
            "mose=main:main",
        ],
    },
    install_requires=[
        "opencv-python==4.8.1.78",
        "mediapipe==0.10.8",
        "pyautogui==0.9.54",
        "numpy==1.24.3",
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0,<10.0.0",
            "pytest-cov>=4.0.0,<7.0.0",
            "pytest-mock>=3.10.0,<4.0.0",
        ]
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video :: Capture",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Human Interface Device (HID)",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords="eye-tracking, accessibility, computer-vision, hands-free, interface",
)
