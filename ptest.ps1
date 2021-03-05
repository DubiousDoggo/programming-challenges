$file="p"

Write-Output "C, C++, Java, JS, TS Polyglot"

Write-Output "$([char]27)[94m------ C ------$([char]27)[0m"
gcc -x c ".\$file" -o "$file.temp.exe" -std=c11
&".\$file.temp.exe"
Remove-Item "$file.temp.exe"

Write-Output "$([char]27)[94m------ C++ ------$([char]27)[0m"
g++ -x c++ ".\$file" -o "$file.temp.exe"
&".\$file.temp.exe"
Remove-Item "$file.temp.exe"

Write-Output "$([char]27)[94m------ JAVA ------$([char]27)[0m"
Copy-Item "$file" "$file.java"
javac "$file.java"
java "$file"
Remove-Item "$file.java"
Remove-Item "$file.class"

Write-Output "$([char]27)[94m------ JS ------$([char]27)[0m"
node "$file"

Write-Output "$([char]27)[94m------ TS ------$([char]27)[0m"
Copy-Item "$file" "$file.ts"
tsc "$file.ts"
node "$file.js"
Remove-Item "$file.ts"
Remove-Item "$file.js"


Write-Output "$([char]27)[94m------ RUST ------$([char]27)[0m"
rustc ".\$file" -o "$file.temp.exe"
&".\$file.temp.exe"
Remove-Item "$file.temp.exe"

Write-Output "`n$((Get-Item ".\$file").Length) bytes`n"
