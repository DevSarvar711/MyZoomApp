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

    // ✅ Yangi parolning mos kelishini tekshirish
    const password1 = document.getElementById("id_new_password1");
    const password2 = document.getElementById("id_new_password2");
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
});