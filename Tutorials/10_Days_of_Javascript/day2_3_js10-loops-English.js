'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    // Define vowels string
    const vowels = "aeiou";
    // Flag for vowelness
    let isVowel = 0;
    // Strings to hold 
    let consonantsToPrint = "";
    // For each letter
    for (let i of s)
    {
        // Clear flag
        isVowel = 0;
        // Check against each vowel
        for (let j of vowels)
        {
            // If vowel, print and set flag
            if (i === j)
            {         
                console.log(j);
                isVowel = 1;
                break;                
            }
        }
        // If char is not vowel, store for printing later
        if (isVowel === 0)
        {
            consonantsToPrint += i;
        }
    }
    // Proceed to consonants
    for (let i of consonantsToPrint)
    {
        // Print each consonant
        console.log(i);
    }

    
}

