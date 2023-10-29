const buttonCompany = document.getElementById('button-company');

buttonCompany.addEventListener('click', (e) => {
    e.preventDefault()
    const valueInput = document.getElementById('input-company').value
    fetch(`http://localhost:8000/company-list-name/?name=${valueInput}`)
    location.assign(`http://localhost:8000/company-list-name/?name=${valueInput}`)
})