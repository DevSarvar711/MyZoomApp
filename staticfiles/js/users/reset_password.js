document.addEventListener("DOMContentLoaded", function () {
    // 🔐 Parolni ko‘rsatish/yashirish funksiyasi
    function togglePasswordVisibility(inputId) {
        const inputField = document.getElementById(inputId);
        if (inputField) {
            inputField.type = inputField.type === "password" ? "text" : "password";
        }
    }

    // 👁️ Parolni yashirish/ko‘rsatish tugmalariga event qo‘shish
    const toggleIcons = document.querySelectorAll(".toggle-password");
    toggleIcons.forEach(icon => {
        icon.addEventListener("click", function () {
            const inputId = this.previousElementSibling.id;
            togglePasswordVisibility(inputId);
        });
    });

    // 📧 Emailni tekshirish va xato chiqarsa ko‘rsatish
    const emailField = document.getElementById("email");
    const emailError = document.getElementById("email-error");
    if (emailField && emailError) {
        emailField.addEventListener("input", function () {
            const emailValue = emailField.value.trim();
            if (!emailValue.includes("@") || !emailValue.includes(".")) {
                emailError.textContent = "⚠️ Iltimos, to‘g‘ri email kiriting!";
            } else {
                emailError.textContent = "";
            }
        });
    }

    // ✅ Parollarni mos kelishini tekshirish
    const password1 = document.getElementById("id_password1");
    const password2 = document.getElementById("id_password2");
    const passwordError = document.getElementById("password-error");

    if (password1 && password2 && passwordError) {
        password2.addEventListener("input", function () {
            if (password1.value !== password2.value) {
                passwordError.textContent = "⚠️ Parollar mos kelmayapti!";
            } else {
                passwordError.textContent = "";
            }
        });
    }

    // ⏳ Form submit bo‘lganda tugmani disable qilish
    const resetForm = document.getElementById("password-reset-form");
    const resetButton = document.querySelector(".reset-btn");

    if (resetForm && resetButton) {
        resetForm.addEventListener("submit", function () {
            resetButton.disabled = true;
            resetButton.textContent = "⏳ Iltimos, kuting...";
        });
    }
});