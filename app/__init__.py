# create __init__.py (empty) inside app
New-Item -Path .\app\__init__.py -ItemType File -Force

# confirm
Get-ChildItem .\app -Force
