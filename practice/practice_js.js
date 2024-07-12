document.addEventListener('DOMContentLoaded', function() {
    const labels = document.querySelectorAll('.label');
    labels.forEach(label => {
        label.addEventListener('click', function() {
            labels.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
            // Add your filtering logic here
        });
    });
});
