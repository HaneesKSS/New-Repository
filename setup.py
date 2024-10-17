from setuptools import find_packages,setup
setup(
    name='mcqgenerator',
    version="0.0.1",
    author='haneeshkss',
    author_email='sanjaysanju1214@gmail.com',
    install_requires=["openai","langchain"],
    packages=find_packages()

)