
from setuptools import setup, find_packages

setup(
    name='bg_task_queue',
    version='0.4.14',
    packages=find_packages(),
    install_requires=[],
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license='MIT',
    author="jhleee",
    author_email="ng0301@gmail.com",
    description="python simple multi threading task queue",
    url="https://github.com/jhleee/python-bg-task-queue",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
