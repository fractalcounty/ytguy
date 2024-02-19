from setuptools import setup, find_packages

setup(
    name='YourPackageName',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ytguy=src.main:main',  # Adjust the path and function
        ],
    },
    install_requires=[
        'yt-dlp',
        'ffmpeg-python',
        'textual',
        'rich',
        # Any other dependencies
    ],
)
