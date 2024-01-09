# Script Name:                  			Lab 01
# Author:                       			Matthew Earles
# Date of latest revision:      		  01/08/2024
# Purpose:                      			powershell script that automates windows updates

# Main

# PowerShell script to enable Automatic OS updates

# Define the registry path for Windows Update settings
$registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update"

# Define the registry values to enable automatic updates
$registryValues = @{

# Set AUOptions to 4 for automatic updates
"AUOptions" = 4

# Set ScheduledInstallDay to 0 for every day
"ScheduledInstallDay" = 0  

# Set ScheduledInstallTime to 3 for 3:00 AM
"ScheduledInstallTime" = 3 }

# Set the registry values to enable automatic updates
foreach ($key in $registryValues.Keys) {
    Set-ItemProperty -Path $registryPath -Name $key -Value $registryValues[$key]
}

Write-Host "Automatic OS updates have been enabled."

# End
