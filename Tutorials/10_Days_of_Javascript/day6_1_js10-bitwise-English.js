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

function getMaxLessThanK(n, k)
{
    // Init max value
    var maxVal = 0;
    // Iterate through each possible a & b < k
    for (let a = 1; a <= n; a++)
    {
        for (let b = a + 1; b <= n; b++)
        {
            var result = a & b;
            // If current result satisfies conditions, set it as new max result
            if (result > maxVal && result < k)
            {
                maxVal = result;
            }
        }
    }
    return maxVal;
}

