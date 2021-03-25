$mkvinputdir = 	"C:\Users\Alex\Downloads\qBittorrent\AoT"
$dest = 		"C:\Users\Alex\Videos\Anime\Attack on Titan\Season 4" + "\"

Set-Location -LiteralPath $mkvinputdir

 dir *.mkv | ForEach-Object {
    
    $output = $dest + $_.Name
    
    & mkvmerge.exe -o $output -s 2 --default-track 2 $_.FullName
    # -s 2 means only grab the second track as a subtitle (usually the first, usually english)
    # --default-track sets so that the subtitle track in track 2 is enabled by default
    }
