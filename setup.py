from setuptools import setup, find_packages

REQUIRED_PACKAGES = [
    "pycuda",
    "numpy",
]

def main():
    setup(
        name="yolo_trt",
        version="1.0",
        description="TensorRT for YOLO Series",
        long_description=open("README.md", "r", encoding="utf-8").read(),
        classifiers=[
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
        ],
        install_requires=REQUIRED_PACKAGES,
        packages=find_packages(),
    )

if __name__ == '__main__':
    main()
