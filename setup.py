from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst : List[str]
    try:
        with open('requirements.txt','r')as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement= line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement!=  '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found")
        
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Badashah Kumar",
    author_email="badshahkumar1508@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)