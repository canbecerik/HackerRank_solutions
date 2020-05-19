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
function factorial(n)
{
    // Initialize result
    var result = 1;
    // Iterate through each integer value between 1..n
    for (let i = 1; i <= n; i++)
    {
        result *= i; 
    }
    return result;
}

