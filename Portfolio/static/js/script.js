function toggleExperienceDetails(index) {
    var details = document.getElementById('experience-details-' + index);
    var icon = document.getElementById('folder-icon-' + index);
    if (details && icon) {
        if (details.style.display === 'none' || details.style.display === '') {
            details.style.display = 'block';
            icon.classList.remove('fa-folder');
            icon.classList.add('fa-folder-open');
        } else {
            details.style.display = 'none';
            icon.classList.remove('fa-folder-open');
            icon.classList.add('fa-folder');
        }
    } else {
        console.error('Element with id experience-details-' + index + ' or folder-icon-' + index + ' not found.');
    }
}
