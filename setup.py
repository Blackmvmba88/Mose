"""
Setup configuration for Ocularis Mose
"""
from setuptools import setup, find_packages

setup(
    name="ocularis-mose",
    version="1.0.0",
    description="Eye tracking mouse control system",
    author="Blackmvmba88",
    py_modules=["main"],
    install_requires=[
        "opencv-python",
        "mediapipe",
        "pyautogui",
        "numpy",
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0,<10.0.0",
            "pytest-cov>=4.0.0,<7.0.0",
            "pytest-mock>=3.10.0,<4.0.0",
        ]
    },
    python_requires=">=3.9",
)
