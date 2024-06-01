from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "tgaimage",
        ["bindings.cpp", "tgaimage.cpp"],
    ),
]

setup(
    name="tgaimage",
    version="0.0.1",
    description="tgaimage support from tinyrenderer starter code",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
