from setuptools import setup

setup(
    name='iozone-results-comparator',
    version='0.1.2',
    author = "Rovanion Luckey",
    author_email = "rovanion.luckey@gmail.com",
    description = ("Iozone-results-comparator is a Python 3 application for analysing results of the IOzone Filesystem Benchmark."),
    license = "GPL3",
    url = "https://github.com/Rovanion/iozone-results-comparator",
    packages = ['iozone_results_comparator_lib'],
    package_data = {'iozone_results_comparator_lib': ['stylesheet.css', 'arrows.png']},
    include_package_data=True,
    install_requires=['scipy', 'matplotlib'],
    scripts = ['scripts/iozone_results_comparator.py'],
)
