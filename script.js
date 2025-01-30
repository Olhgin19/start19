const container = document.getElementById('container')
const registerBtn = document.getElementById('register')
const loginBtn = document.getElementById('login')

registerBtn.addEventListener('click', () => {
	container.classList.add('active')
})

loginBtn.addEventListener('click', () => {
	container.classList.remove('active')
})

function myFunction() {
	window.location.href = 'gotovo.html'
}

document.addEventListener('DOMContentLoaded', () => {
	const textElement = document.getElementById('animated-text')
	const text = textElement.textContent // Получаем текст "Hello, Friend!"
	textElement.innerHTML = '' // Очищаем текст, чтобы добавить буквы по одной

	// Разбиваем текст на буквы и оборачиваем каждую в <span>
	text.split('').forEach((char, index) => {
		const span = document.createElement('span')
		span.textContent = char // Устанавливаем текст буквы
		textElement.appendChild(span)

		// Добавляем класс с задержкой для каждой буквы
		setTimeout(() => {
			span.classList.add('visible')
		}, index * 100) // Задержка между буквами (100 мс)
	})
})
