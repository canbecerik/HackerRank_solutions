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

function getGrade(score) {
    var grade = "";
    // Compare against True as switch block enters case only when case_statement == switch_statement
    switch (true)
    {
        default:
            grade = "F";
            break;
        case (score > 25):
            grade = "A";
            break;
        case (score > 20 && score <= 25):
            grade = "B";
            break;
        case (score > 15 && score <= 20):
            grade = "C";
            break;
        case (score > 10 && score <= 15):
            grade = "D";
            break;
        case (score > 5 && score <= 10):
            grade = "E";
            break;
    }
    
    return grade;
}

