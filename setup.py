from setuptools import setup, find_packages

setup(
    name='pyqt-foldable-toolbar',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_foldable_toolbar.ico': ['fold.svg', 'unfold.svg']},
    description='PyQt foldable toolbar',
    url='https://github.com/yjg30737/pyqt-foldable-toolbar.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main'
    ]
)