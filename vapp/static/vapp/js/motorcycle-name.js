const buttonMotorcycle = document.getElementById('button-motorcycle');

buttonMotorcycle.addEventListener('click', (e) => {
    e.preventDefault()
    const valueInput = document.getElementById('input-motorcycle').value
    fetch(`http://localhost:8000/motorcycle-list-name/?name=${valueInput}`)
    location.assign(`http://localhost:8000/motorcycle-list-name/?name=${valueInput}`)
})