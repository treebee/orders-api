from setuptools import find_packages, setup

install_requires = ["fastapi", "uvicorn"]

setup(
    name="orders_api",
    install_requires=install_requires,
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
)
