function generatePassword() {
    const length = parseInt(document.getElementById('length').value);
    const useSymbols = document.getElementById('useSymbols').checked;

    fetch('/generate_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ length, useSymbols }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('generatedPassword').textContent = data.password;
    })
    .catch(error => console.error('Error:', error));
}
function copyPassword() {
    const password = document.getElementById('generatedPassword').textContent;
    if (!password) {
        alert("No password to copy!");
        return;
    }
    navigator.clipboard.writeText(password)
        .then(() => alert('Password copied to clipboard!'))
        .catch(err => console.error('Error copying password:', err));
}

function clearPassword() {
    document.getElementById('generatedPassword').textContent = '';
}
