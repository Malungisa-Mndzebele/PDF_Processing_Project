// The Birthday Book - Interactive JavaScript

// Global variables
let confettiActive = false;
let darkMode = false;
let currentTheme = 'birthday';

// Theme configurations
const themes = {
    birthday: {
        name: 'Birthday Party',
        colors: ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4'],
        emojis: ['🎂', '🎉', '🎊', '🎈', '🎁', '✨']
    },
    halloween: {
        name: 'Spooky PDF',
        colors: ['#8B4513', '#FF4500', '#2F4F4F', '#800080'],
        emojis: ['🎃', '👻', '🦇', '🕷️', '💀', '⚡']
    },
    christmas: {
        name: 'Holiday PDF',
        colors: ['#228B22', '#DC143C', '#FFD700', '#FFFFFF'],
        emojis: ['🎄', '🎅', '❄️', '🎁', '🔔', '⭐']
    },
    valentine: {
        name: 'Love Letter PDF',
        colors: ['#FF69B4', '#FF1493', '#FFB6C1', '#FFC0CB'],
        emojis: ['💕', '💖', '💗', '💘', '💝', '💞']
    }
};

// Initialize the website
document.addEventListener('DOMContentLoaded', function() {
    initializeWebsite();
    setupEventListeners();
    startBackgroundAnimations();
    addKeyboardShortcuts();
});

function initializeWebsite() {
    console.log('🎂 The Birthday Book is loading...');
    
    // Add loading animation
    showLoadingAnimation();
    
    // Initialize theme
    applyTheme(currentTheme);
    
    // Add welcome message
    setTimeout(() => {
        showWelcomeMessage();
    }, 1000);
}

function setupEventListeners() {
    // Add click effects to all interactive elements
    const interactiveElements = document.querySelectorAll('.fun-button, .stat-card');
    interactiveElements.forEach(element => {
        element.addEventListener('click', function() {
            addClickEffect(this);
        });
    });

    // Add hover effects
    const cards = document.querySelectorAll('.stat-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.05)';
            addSparkleEffect(this);
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });
}

function startBackgroundAnimations() {
    // Create floating elements
    setInterval(createFloatingElement, 3000);
    
    // Add random sparkles
    setInterval(addRandomSparkle, 2000);
    
    // Animate progress bar
    animateProgressBar();
}

function createFloatingElement() {
    const emojis = themes[currentTheme].emojis;
    const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)];
    
    const element = document.createElement('div');
    element.className = 'floating-element';
    element.textContent = randomEmoji;
    element.style.top = Math.random() * 100 + '%';
    element.style.left = Math.random() * 100 + '%';
    element.style.animationDuration = (Math.random() * 3 + 3) + 's';
    element.style.fontSize = (Math.random() * 1 + 1.5) + 'rem';
    
    document.querySelector('.floating-elements').appendChild(element);
    
    setTimeout(() => {
        element.remove();
    }, 6000);
}

function addRandomSparkle() {
    const sparkle = document.createElement('div');
    sparkle.innerHTML = '✨';
    sparkle.style.position = 'fixed';
    sparkle.style.top = Math.random() * window.innerHeight + 'px';
    sparkle.style.left = Math.random() * window.innerWidth + 'px';
    sparkle.style.fontSize = '1.5rem';
    sparkle.style.pointerEvents = 'none';
    sparkle.style.zIndex = '1000';
    sparkle.style.animation = 'sparkle 2s ease-out forwards';
    
    document.body.appendChild(sparkle);
    
    setTimeout(() => {
        sparkle.remove();
    }, 2000);
}

function animateProgressBar() {
    const progressFill = document.querySelector('.progress-fill');
    let width = 0;
    
    const interval = setInterval(() => {
        width += 2;
        progressFill.style.width = width + '%';
        
        if (width >= 100) {
            clearInterval(interval);
            showCompletionCelebration();
        }
    }, 50);
}

function showCompletionCelebration() {
    setTimeout(() => {
        createConfetti();
        showCelebration();
    }, 500);
}

function createConfetti() {
    if (confettiActive) return;
    
    confettiActive = true;
    const colors = themes[currentTheme].colors;
    
    for (let i = 0; i < 100; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.left = Math.random() * 100 + '%';
        confetti.style.animationDelay = Math.random() * 3 + 's';
        confetti.style.animationDuration = (Math.random() * 2 + 2) + 's';
        
        document.body.appendChild(confetti);
        
        setTimeout(() => {
            confetti.remove();
        }, 5000);
    }
    
    setTimeout(() => {
        confettiActive = false;
    }, 5000);
}

function showCelebration() {
    const celebration = document.getElementById('celebration');
    celebration.classList.add('show');
    
    // Add multiple celebration emojis
    const emojis = ['🎉', '🎊', '🎂', '🎈', '🎁', '✨'];
    celebration.innerHTML = emojis.join(' ');
    
    setTimeout(() => {
        celebration.classList.remove('show');
    }, 3000);
}

function addClickEffect(element) {
    element.style.transform = 'scale(0.95)';
    element.style.transition = 'transform 0.1s ease';
    
    setTimeout(() => {
        element.style.transform = '';
    }, 100);
    
    // Add ripple effect
    createRippleEffect(element);
}

function createRippleEffect(element) {
    const ripple = document.createElement('div');
    ripple.style.position = 'absolute';
    ripple.style.borderRadius = '50%';
    ripple.style.background = 'rgba(255, 255, 255, 0.6)';
    ripple.style.transform = 'scale(0)';
    ripple.style.animation = 'ripple 0.6s linear';
    ripple.style.left = '50%';
    ripple.style.top = '50%';
    ripple.style.width = '20px';
    ripple.style.height = '20px';
    ripple.style.marginLeft = '-10px';
    ripple.style.marginTop = '-10px';
    ripple.style.pointerEvents = 'none';
    
    element.style.position = 'relative';
    element.appendChild(ripple);
    
    setTimeout(() => {
        ripple.remove();
    }, 600);
}

function addSparkleEffect(element) {
    for (let i = 0; i < 5; i++) {
        const sparkle = document.createElement('div');
        sparkle.innerHTML = '✨';
        sparkle.style.position = 'absolute';
        sparkle.style.top = Math.random() * element.offsetHeight + 'px';
        sparkle.style.left = Math.random() * element.offsetWidth + 'px';
        sparkle.style.fontSize = '1rem';
        sparkle.style.pointerEvents = 'none';
        sparkle.style.animation = 'sparkle 1s ease-out forwards';
        sparkle.style.zIndex = '10';
        
        element.appendChild(sparkle);
        
        setTimeout(() => {
            sparkle.remove();
        }, 1000);
    }
}

function showLoadingAnimation() {
    const loading = document.createElement('div');
    loading.id = 'loading';
    loading.innerHTML = '🎂 Loading The Birthday Book... 🎂';
    loading.style.position = 'fixed';
    loading.style.top = '50%';
    loading.style.left = '50%';
    loading.style.transform = 'translate(-50%, -50%)';
    loading.style.fontSize = '2rem';
    loading.style.color = 'white';
    loading.style.textShadow = '2px 2px 4px rgba(0,0,0,0.5)';
    loading.style.zIndex = '2000';
    loading.style.animation = 'pulse 1s ease-in-out infinite';
    
    document.body.appendChild(loading);
    
    setTimeout(() => {
        loading.remove();
    }, 2000);
}

function showWelcomeMessage() {
    const welcome = document.createElement('div');
    welcome.innerHTML = '🎉 Welcome to The Birthday Book! 🎉';
    welcome.style.position = 'fixed';
    welcome.style.top = '20px';
    welcome.style.left = '50%';
    welcome.style.transform = 'translateX(-50%)';
    welcome.style.fontSize = '1.5rem';
    welcome.style.color = 'white';
    welcome.style.textShadow = '2px 2px 4px rgba(0,0,0,0.5)';
    welcome.style.zIndex = '1000';
    welcome.style.animation = 'slideInDown 1s ease-out';
    
    document.body.appendChild(welcome);
    
    setTimeout(() => {
        welcome.style.animation = 'slideOutUp 1s ease-in forwards';
        setTimeout(() => {
            welcome.remove();
        }, 1000);
    }, 3000);
}

function addKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        switch(e.key.toLowerCase()) {
            case 'c':
                showCelebration();
                break;
            case 'd':
                toggleDarkMode();
                break;
            case 't':
                cycleTheme();
                break;
            case 'h':
                showHelp();
                break;
            case 'r':
                location.reload();
                break;
        }
    });
}

function toggleDarkMode() {
    darkMode = !darkMode;
    document.body.classList.toggle('dark-mode', darkMode);
    
    const message = darkMode ? '🌙 Dark mode activated!' : '☀️ Light mode activated!';
    showNotification(message);
}

function cycleTheme() {
    const themeNames = Object.keys(themes);
    const currentIndex = themeNames.indexOf(currentTheme);
    const nextIndex = (currentIndex + 1) % themeNames.length;
    currentTheme = themeNames[nextIndex];
    
    applyTheme(currentTheme);
    showNotification(`🎨 Theme changed to: ${themes[currentTheme].name}`);
}

function applyTheme(themeName) {
    const theme = themes[themeName];
    const root = document.documentElement;
    
    // Update CSS custom properties
    root.style.setProperty('--primary-color', theme.colors[0]);
    root.style.setProperty('--secondary-color', theme.colors[1]);
    root.style.setProperty('--accent-color', theme.colors[2]);
    root.style.setProperty('--highlight-color', theme.colors[3]);
    
    // Update floating elements
    const floatingElements = document.querySelectorAll('.floating-element');
    floatingElements.forEach(element => {
        element.textContent = theme.emojis[Math.floor(Math.random() * theme.emojis.length)];
    });
}

function showNotification(message) {
    const notification = document.createElement('div');
    notification.innerHTML = message;
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.background = 'rgba(0, 0, 0, 0.8)';
    notification.style.color = 'white';
    notification.style.padding = '15px 20px';
    notification.style.borderRadius = '10px';
    notification.style.fontSize = '1rem';
    notification.style.zIndex = '2000';
    notification.style.animation = 'slideInRight 0.5s ease-out';
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.5s ease-in forwards';
        setTimeout(() => {
            notification.remove();
        }, 500);
    }, 3000);
}

function showHelp() {
    const help = document.createElement('div');
    help.innerHTML = `
        <h3>🎮 Keyboard Shortcuts</h3>
        <p><strong>C</strong> - Show celebration</p>
        <p><strong>D</strong> - Toggle dark mode</p>
        <p><strong>T</strong> - Cycle themes</p>
        <p><strong>H</strong> - Show this help</p>
        <p><strong>R</strong> - Reload page</p>
    `;
    help.style.position = 'fixed';
    help.style.top = '50%';
    help.style.left = '50%';
    help.style.transform = 'translate(-50%, -50%)';
    help.style.background = 'rgba(0, 0, 0, 0.9)';
    help.style.color = 'white';
    help.style.padding = '30px';
    help.style.borderRadius = '15px';
    help.style.zIndex = '2000';
    help.style.maxWidth = '400px';
    help.style.animation = 'fadeIn 0.5s ease-out';
    
    document.body.appendChild(help);
    
    setTimeout(() => {
        help.style.animation = 'fadeOut 0.5s ease-in forwards';
        setTimeout(() => {
            help.remove();
        }, 500);
    }, 5000);
}

// Add CSS animations dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes sparkle {
        0% { opacity: 1; transform: scale(0) rotate(0deg); }
        50% { opacity: 1; transform: scale(1) rotate(180deg); }
        100% { opacity: 0; transform: scale(0) rotate(360deg); }
    }
    
    @keyframes ripple {
        to { transform: scale(4); opacity: 0; }
    }
    
    @keyframes pulse {
        0%, 100% { transform: translate(-50%, -50%) scale(1); }
        50% { transform: translate(-50%, -50%) scale(1.1); }
    }
    
    @keyframes slideInDown {
        from { transform: translateX(-50%) translateY(-100%); opacity: 0; }
        to { transform: translateX(-50%) translateY(0); opacity: 1; }
    }
    
    @keyframes slideOutUp {
        from { transform: translateX(-50%) translateY(0); opacity: 1; }
        to { transform: translateX(-50%) translateY(-100%); opacity: 0; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOutRight {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes fadeOut {
        from { opacity: 1; }
        to { opacity: 0; }
    }
`;
document.head.appendChild(style);

// Export functions for global access
window.showContent = showContent;
window.showCelebration = showCelebration;
window.toggleDarkMode = toggleDarkMode;
window.cycleTheme = cycleTheme;
window.showHelp = showHelp;
