function togglePassword(fieldId) {
    let field = document.getElementById(fieldId);
    let icon = field.nextElementSibling;

    if (field.type === "password") {
        field.type = "text";
        icon.textContent = "🙈";
    } else {
        field.type = "password";
        icon.textContent = "👁️";
    }
}