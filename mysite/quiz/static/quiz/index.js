console.log("js file loaded");

document.addEventListener("DOMContentLoaded", function() {
    const radios = document.querySelectorAll('input[name="choice"]');
    const submitBtn = document.getElementById('submit-btn');

    if (!radios.length || !submitBtn) return;

    radios.forEach(radio => {
        radio.addEventListener('change', () => {
            submitBtn.disabled = false;
        });
    });
});

console.log('document.head');
console.log(document.head);

console.log('document.body');
console.log(document.body);

console.log('document.forms');
console.log(document.forms);

console.log('document.getElementById("submit-btn")');
console.log(document.getElementById('submit-btn'));