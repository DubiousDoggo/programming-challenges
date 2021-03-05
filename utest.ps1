$file="u"

Write-Output "C, Java, JS Polyquine"

Write-Output "$([char]27)[94m------ C ------$([char]27)[0m"
gcc -x c ".\$file" -o "$file.temp.exe" -std=c11
&".\$file.temp.exe" | out-file "$file.temp.c" -encoding ascii
fc.exe "$file" "$file.temp.c"
Remove-Item "$file.temp.exe"
Remove-Item "$file.temp.c"

Write-Output "$([char]27)[94m------ JAVA ------$([char]27)[0m"
Copy-Item "$file" "$file.java"
javac "$file.java"
java "$file" | out-file "$file.temp.java" -encoding ascii
fc.exe "$file" "$file.temp.java"
Remove-Item "$file.java"
Remove-Item "$file.class"
Remove-Item "$file.temp.java"

Write-Output "$([char]27)[94m------ JS ------$([char]27)[0m"
node "$file" | out-file "$file.temp.js" -encoding ascii
fc.exe "$file" "$file.temp.js"
Remove-Item "$file.temp.js"

Write-Output "$((Get-Item ".\$file").Length) bytes`n"
