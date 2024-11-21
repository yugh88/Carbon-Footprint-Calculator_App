from setuptools import setup, find_packages

setup(
    name='carbon-footprint-calculator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'pandas>=1.4.2,<2.0.0',
        'numpy>=1.22.3,<2.0.0',
        'scikit-learn>=1.0.2,<2.0.0',
        'pillow',
        'matplotlib',
        'joblib'
    ],
    python_requires='>=3.8,<3.13'
)