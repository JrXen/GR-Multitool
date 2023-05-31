import PyInstaller.__main__

# Path to your Python script
script_path = 'main.py'

# PyInstaller command to create the executable
PyInstaller.__main__.run([
    '--onefile',
    '--console',  # Use '--console' instead of '--windowed' for a console application
    script_path
])

