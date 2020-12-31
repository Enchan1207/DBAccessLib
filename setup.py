#
# pipが読んでライブラリの諸々を設定するためのファイル
#
import glob
import setuptools, os

setuptools.setup(
    name="DBAccessLib",
    version="0.2.5",
    license="MIT Licence",
    description="Database access interface library",
    author="Enchan1207",
    url="https://github.com/Enchan1207/DBAccessLib",
    packages=setuptools.find_packages("src"),
    install_requires=["mysql-connector-python"],
    package_dir={"": "src"},
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob.glob('src/*.py')],
    include_package_data=True,
    zip_safe=False
)
