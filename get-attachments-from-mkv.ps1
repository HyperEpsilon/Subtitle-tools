$dest = 		"C:\Users\Alex\Videos\Anime\Vinland Saga\Season 1\"
$mkvinputfile = "D:\_temp\vinland" +"\"+ "[Judas] Vinland Saga S1 - 14.mkv"
# Remove the double back ticks from the file names, it breaks it

$path = Split-Path -Path $mkvinputfile
$newpath = $path + "\attachments"
If(!(test-path $newpath))
{
      New-Item -ItemType Directory -Force -Path $newpath
}
Set-Location -LiteralPath $newpath

& mkvextract.exe $mkvinputfile attachments $(foreach ($num in 1..50) {$num})