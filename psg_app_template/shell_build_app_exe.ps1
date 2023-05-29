# change directory to location of this script
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
Set-Location $dir

# Activate the virtual environment
$venvPath = ".\env-app"
& $venvPath\Scripts\activate

# update version info file
$versionScript = ".\create_version_file.py"
& $venvPath\Scripts\python.exe $versionScript

# Run the pyinstaller command
$pyInstallerExecutable = "pyinstaller"
$specFile = "app.spec"
& $pyInstallerExecutable $specFile