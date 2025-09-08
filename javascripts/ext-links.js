// extra.js – run after the page has loaded
document.addEventListener('DOMContentLoaded', () => {
  // Find all <a> elements that already have class="blank"
  document.querySelectorAll('a.blank').forEach(link => {
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener noreferrer');
  });
});