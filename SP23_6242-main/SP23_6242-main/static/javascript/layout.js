const toggleSwitch = document.getElementById("darkModeSlider");
const currentTheme = localStorage.getItem('theme');

if (currentTheme) {
    document.body.setAttribute('data-theme', currentTheme);
    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
    }
}

function switchTheme(a) {
    if (a.target.checked) {
        document.body.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
    else {  
        document.body.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    }    
    
}

toggleSwitch.addEventListener('change', switchTheme, false);