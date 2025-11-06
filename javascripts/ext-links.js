// extra.js – run after the page has loaded
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a.blank').forEach(link => {
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener noreferrer');
  });
});