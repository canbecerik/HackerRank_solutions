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

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Sort the array as integers, by providing anonymous compare function
    nums = nums.sort(function (a, b) {  return a - b;  });
    // Pop once and store
    const popped_1 = nums.pop();
    var popped_2 = popped_1;
    // In infinite loop, pop until different than first popped value
    // Return the value if different
    while (true)
    {
        popped_2 = nums.pop();
        if (popped_2 !== popped_1)
        {
            return popped_2;
        }
    } 
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}