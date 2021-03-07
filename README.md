# programming-challenges
I made this repo to track all the random coding scraps and challenges I have littered around my hard drive.
Below is a short description of each.

## p
A Hello World Polyglot.
It works on C, C++, Java, JavaScript, TypeScript, and Rust. Running the program outputs "Hello World, " and the name of the language respectively.
I set an additional challenge that each language had to share the "Hello World, " string in the middle of the program.

## q
A 2 language PolyQuine.
For this one I decided to combine the idea of a polyglot with a quine. It works with C and Java. I used a similar technique as [p](#p), making abuse of Java unicode escapes. I was able to golf this one down quite a bit since Java and C syntax is similar and can overlap in certain places.

## r
A 4 language PolyQuine.
Taking the ideas from [p](#p) and [q](#q), I combinied them into this massive beast of a program. It works with Java, C, JavaScript, and Rust. This was quite the puzzle trying to micromanage each language interweaving all over the place. Getting Rust in there was the most difficult, since this is the first program I've written with it. It started out at almost 3000 bytes, but I've managed to golf it down to 1987.
