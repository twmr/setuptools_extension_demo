import setuptools

demo_cxx = setuptools.Extension(
    "demo._cxx", sources=[], libraries=["z"], language="c++"
)

setuptools.setup(
    name="demo",
    packages=["demo"],
    ext_modules=[demo_cxx],
)
