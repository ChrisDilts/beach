import-csv E:\temp\NameList.csv | ForEach-Object {Get-ADPrincipalGroupMembership -Identity $_.username | Select-Object name | Where-Object {$_.name -match "FIM-LOC*"}} | Out-File -Append E:\Temp\ListOut.csv

$OutArray = New-Object PSObject
import-csv E:\temp\NameList.csv | ForEach-Object {
$user = $_.username
$lob={Get-ADPrincipalGroupMembership -Identity $_.username | Select-Object name | Where-Object {$_.name -match "FIM-LOC*"}}
Add-Member -InputObject $OutArray -MemberType NoteProperty -Name User -Value $user -Force
Add-Member -InputObject $OutArray -MemberType NoteProperty -Name LOB -Value $lob -Force
}
$OutArray | Out-File E:\Temp\ListOut.csv





import-csv E:\temp\NameList.csv
ForEach-Object {
Get-ADPrincipalGroupMembership -Identity $_.username | Select-Object name | Where-Object {$_.name -match "FIM-LOC*"}
}