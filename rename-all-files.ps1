$path = "C:\Users\Alex\Videos\Anime\Bunny Girl Senpai\Season 1"

Set-Location -LiteralPath $path

#Get-ChildItem *.mkv | Rename-Item -NewName { [string]($_.Name).Substring(8)}
#Get-ChildItem *.mkv | Rename-Item -NewName { $_.Name -replace 'Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai', 'Rascal Does Not Dream of Bunny Girl Senpai'}
Get-ChildItem *.mkv | Rename-Item -NewName { $_.Name -replace ' (\d)x', ' - S01E'}