 $mkvinputdir = "D:\Anime\Vinland Saga\Season 1"
 Set-Location -LiteralPath $mkvinputdir
 
 dir *.mkv | ForEach-Object {
    
     $output = ".\chapters\" + $_.BaseName + ".xml"

     mkvextract.exe $_.Name chapters $output

    }