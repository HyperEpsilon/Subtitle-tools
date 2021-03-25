 $mkvinputdir = "D:\Anime\Vinland Saga\Season 1"
 Set-Location -LiteralPath $mkvinputdir
 
 dir *.mkv | ForEach-Object {
    
     $output = ".\subs\" + $_.BaseName + ".ass"

     mkvextract.exe $_.Name tracks 2:$output

    }