// docs/js/animations.js
document.addEventListener('DOMContentLoaded', () => {
    const isEnabled = localStorage.getItem('animationsEnabled') === 'true';
    applyAnimationState(isEnabled);
});

function toggleAnimations() {
    const isEnabled = localStorage.getItem('animationsEnabled') === 'true';
    const newState = !isEnabled;
    localStorage.setItem('animationsEnabled', newState);
    applyAnimationState(newState);
}

function applyAnimationState(enable) {
    document.querySelectorAll('.icon-def-0').forEach(el => {
        el.classList.toggle('icon-anim-0', enable);
    });
    document.querySelectorAll('.icon-def-1').forEach(el => {
        el.classList.toggle('icon-anim-1', enable);
    });
    document.querySelectorAll('.icon-def-2').forEach(el => {
        el.classList.toggle('icon-anim-0', enable);
    });

    if (enable) {
        document.body.classList.add('animations-enabled');
    } else {
        document.body.classList.remove('animations-enabled');
    }
}
