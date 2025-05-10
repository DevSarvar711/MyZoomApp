
function togglePassword(fieldId) {
    const passwordField = document.getElementById(fieldId);
    const type = passwordField.type === 'password' ? 'text' : 'password'; // Agar type 'password' bo'lsa, uni 'text' ga o'zgartiramiz
    passwordField.type = type;

    // Ko'z ikonkasi ko'rsatish yoki yashirish
    const icon = document.querySelector(`#${fieldId} + .toggle-password`);
    if (type === 'password') {
        icon.innerHTML = '👁️'; // Agar yashirishni xohlasak
    } else {
        icon.innerHTML = '🙈'; // Agar ko'rsatish uchun o'zgartirsak
    }
}