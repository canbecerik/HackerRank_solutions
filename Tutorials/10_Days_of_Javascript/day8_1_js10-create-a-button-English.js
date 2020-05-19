var clickMeButton = document.createElement('button');
clickMeButton.id = 'btn';
clickMeButton.innerHTML = '0';
clickMeButton.className = 'myStyleClass';
document.body.appendChild(clickMeButton);
clickMeButton.onclick = function()
{
    clickMeButton.innerHTML++;
}