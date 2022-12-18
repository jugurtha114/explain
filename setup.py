import sys
from setuptools import setup

if sys.version_info[:3] < (3, 0, 0):
    print("Requires Python 3 to run.")
    sys.exit(1)

setup(
    name="explain",
    version="1.0.0",
    description="Command-line tool that automatically explains your error message using ChatGPT",
    url="https://github.com/jugurtha114/explain",
    author="jugurtha114",
    author_email="jugurthagreen@gmail.com",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Software Development :: Debuggers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    keywords="chatgpt cli humain conversastion error_message gpt commandline error message stack trace explain explanation python",
    include_package_data=True,
    packages=["explain", "explain.utilities"],
    entry_points={"console_scripts": ["explain = explain.explain:main"]},
    install_requires=["revChatGPT", "pygments"],
    requires=["revChatGPT", "pygments"],
    python_requires=">=3",
    license="MIT"
)
