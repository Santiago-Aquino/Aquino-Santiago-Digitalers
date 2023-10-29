const buttonCar = document.getElementById('button-car');

buttonCar.addEventListener('click', (e) => {
    e.preventDefault()
    const valueInput = document.getElementById('input-car').value
    fetch(`http://localhost:8000/car-list-name/?name=${valueInput}`)
    location.assign(`http://localhost:8000/car-list-name/?name=${valueInput}`)
})