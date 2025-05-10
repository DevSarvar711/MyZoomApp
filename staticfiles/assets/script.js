function showSection(sectionId) {
    // Barcha bo'limlarni yashirish
    var sections = document.querySelectorAll('.content-section');
    sections.forEach(function(section) {
        section.classList.add('hidden');
        section.classList.remove('active');
    });

    // Tanlangan bo'limni ko'rsatish
    var activeSection = document.getElementById(sectionId);
    if (activeSection) {
        activeSection.classList.remove('hidden');
        activeSection.classList.add('active');
    }
}
