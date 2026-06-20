document.getElementById('uploadForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const queryInput = document.getElementById('queryInput');
    const resultDiv = document.getElementById('result');
    const answerText = document.getElementById('answerText');

    if (!fileInput.files.length || !queryInput.value.trim()) {
        alert('Загрузите PDF и введите вопрос.');
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('query', queryInput.value.trim());

    try {
        const response = await fetch('http://localhost:8000/analyze', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.error) {
            alert('Ошибка: ' + data.error);
            return;
        }

        resultDiv.style.display = 'block';
        answerText.textContent = data.answer || 'Нет ответа.';
    } catch (error) {
        alert('Ошибка при обращении к серверу. Убедитесь, что бэкенд запущен.');
        console.error(error);
    }
});