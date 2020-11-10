# Files from yesterday should be copyed to "CopyToPath" and moved to "Backup"


Set-Variable -Name "CopyToPath" -Value "...\Share"
Set-Variable -Name "WorkingPath" -Value "...\Work"
Set-Variable -Name "BackupPath" -Value "...\Backup"
Set-Variable -Name "LogFile" -Value "...\Log.txt"


#Setup Networkdrive for copy
#net use y: \\Server\Path /user:USERNAME password


# get every file in Workingpath if the File includes *.xml
$Files = Get-ChildItem -Path $WorkingPath\* -Include *.xml -File

foreach ($File in $Files)
{
	if ($File.LastWriteTime -gt (get-date).AddDays(-1).ToString("MM/dd/yyyy HH:mm:ss"))
	{
		$md5 = Get-FileHash $File -Algorithm md5
		Copy-Item $File -Destination $CopyToPath
		Move-Item $File -Destination $BackupPath
		Write-Output "Copy/Move for $($File.Name) done / MD5-Hash:$($md5.Hash)" >> $LogFile
	}
	else 
    {
        Write-Output "Not copying $($File.Name)" >> $LogFile
    }
}


#net use y: /delete
#net use \\SERVER\PATH /delete