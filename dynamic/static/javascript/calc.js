document.addEventListener('DOMContentLoaded', () => {
    document.addEventListener('keydown', handleKeyPress);
    document.addEventListener('keyup', handleKeyRelease);
});

function appendToDisplay(value) {
    const display = document.getElementById('display');
    if (display.innerText === '0') {
        display.innerText = value;
    } else {
        display.innerText += value;
    }
}

function clearDisplay() {
    document.getElementById('display').innerText = '0';
}

function calculate() {
    const display = document.getElementById('display');
    try {
        display.innerText = eval(display.innerText);
    } catch (e) {
        display.innerText = 'Error';
    }
}

function handleKeyPress(event) {
    const key = event.key;
    if (key >= '0' && key <= '9') {
        appendToDisplay(key);
        addHoverEffect(key);
    } else if (key === 'Enter') {
        calculate();
        addHoverEffect('=');
    } else if (key === 'Backspace') {
        const display = document.getElementById('display');
        display.innerText = display.innerText.slice(0, -1) || '0';
    } else if (key === 'Escape') {
        clearDisplay();
    } else if (['+', '-', '*', '/', '(', ')', '.'].includes(key)) {
        appendToDisplay(key);
        addHoverEffect(key);
    }
}

function handleKeyRelease(event) {
    const key = event.key;
    if (key >= '0' && key <= '9') {
        removeHoverEffect(key);
    } else if (key === 'Enter') {
        removeHoverEffect('=');
    } else if (['+', '-', '*', '/', '(', ')', '.'].includes(key)) {
        removeHoverEffect(key);
    }
}

function addHoverEffect(key) {
    const button = document.getElementById(key);
    if (button) {
        button.classList.add('hover');
    }
}

function removeHoverEffect(key) {
    const button = document.getElementById(key);
    if (button) {
        button.classList.remove('hover');
    }
}
