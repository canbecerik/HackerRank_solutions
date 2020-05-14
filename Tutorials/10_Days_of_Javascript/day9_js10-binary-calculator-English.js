  function onButton(e) {
    // Get current button, current action from button text, and what is on result (res)
    var btn = e.target || e.srcElement;
    var action = document.getElementById(btn.id).innerHTML;
    var res = document.getElementById('res');
      
    // State machine acting depending on which button is pressed,
    // Add to screen for buttons 0, 1, +, -, *, /
    
    switch(action) {
        case '0':
        case '1':
        case '+':
        case '-':
        case '*':
        case '/':
            res.innerHTML += action;
            break;
        // Clear screen for C
        case 'C':
            res.innerHTML = '';
            break;
        // Perform operation as depicted on res
        case '=':
            // Store operation
            var expr = res.innerHTML;
            // Regex to extract all digits
            var nums = /(\d+)/g;
            // Replace all base 2 nums with base 10 equivs
            expr = expr.replace(nums, function(match) {
                return parseInt(match, 2);
            })
            // eval in base 10 and convert to base 2
            res.innerHTML = eval(expr).toString(2);
            break;
        default:
            console.error('should not be executed');
            break;
    }
}
// Get all buttons into an array
var buttons = document.getElementsByTagName('button');

// Iterate each button, call onButton() when a button is clicked
for (let button of buttons) {
    button.onclick = onButton;
}