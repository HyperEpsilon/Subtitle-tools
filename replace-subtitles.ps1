$dest = 		"C:\Users\Alex\Videos\Anime\Bunny Girl Senpai\Season 1\"
$mkvinputdir = 	"C:\Users\Alex\Downloads\qBittorrent\(Cerberus) Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai  + Movie (BD 1080p HEVC 10-bit OPUS)"

Set-Location -LiteralPath $mkvinputdir

 dir *.mkv | ForEach-Object {
    
    $output = $dest + $_.Name
    $subfile = $mkvinputdir + "\subs\" + $_.BaseName + ".ass"
    
    & mkvmerge.exe -o $output --no-subtitles $_.FullName `
    --default-track 0 --track-name 0:"(vivid)" $subfile

    # -S means no subtitles from the input .mkv
    # --default-track sets so that the subtitle track in track 2 is enabled by default
    }
