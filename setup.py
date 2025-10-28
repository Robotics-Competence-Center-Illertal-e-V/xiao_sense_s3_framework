from cx_Freeze import setup


# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["PySide6", "numpy"],
}

setup(
    name="raw_image_viewer",
    version="0.1",
    description="Display Raw Images",
    options={"build_exe": build_exe_options},
    executables=[{"script": "raw_image_viewer/raw_image_viewer.py", "base": "gui"}],
)