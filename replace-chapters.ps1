$dest = 		"D:\Anime\Vinland Saga\Season 1\New" + "\"
$mkvinputdir = 	"D:\Anime\Vinland Saga\Season 1"

Set-Location -LiteralPath $mkvinputdir

 dir *.mkv | ForEach-Object {
    
    $output = $dest + $_.Name
    $chapfile = $mkvinputdir + "\chapters\new_chapters\" + $_.BaseName + ".xml"
    
    & mkvmerge.exe -o $output --no-chapters $_.FullName `
    --chapter-language eng --chapters $chapfile

    # -S means no subtitles from the input .mkv
    # --default-track sets so that the subtitle track in track 2 is enabled by default
    }
