$dest = 		"C:\Users\Alex\Videos\Anime\Vinland Saga\Season 1\"
$mkvinputdir = 	"C:\Users\Alex\Downloads\qBittorrent\Vinland Saga - Season 1"

$font1 =        "C:\Users\Alex\Downloads\qBittorrent\Vinland Saga - Season 1\attachments\a-otf-musashistd-regular.otf"
$font2 =        "C:\Users\Alex\Downloads\qBittorrent\Vinland Saga - Season 1\attachments\Seagull-Medium-BT.ttf"

Set-Location -LiteralPath $mkvinputdir

 dir *.mkv | ForEach-Object {
    
    $output = $dest + $_.Name
    
    & mkvmerge.exe -o $output -s 2 --default-track 2 --no-attachments $_.FullName `
    --attachment-mime-type "application/x-truetype-font" --attach-file $font1 `
    --attachment-mime-type "application/x-truetype-font" --attach-file $font2
    # Copy and paste the above line for each font, and don't forget the grave (`) at the end of each non-terminus line

    # -s 2 means only grab the second track as a subtitle (usually the first, usually english)
    # --default-track sets so that the subtitle track in track 2 is enabled by default
    }
