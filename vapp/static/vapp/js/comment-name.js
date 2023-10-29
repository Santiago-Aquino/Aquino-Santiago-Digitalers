const buttonComment = document.getElementById('button-comment');

buttonComment.addEventListener('click', (e) => {
    e.preventDefault()
    const valueInput = document.getElementById('input-comment').value
    fetch(`http://localhost:8000/comment-list-name/?name=${valueInput}`)
    location.assign(`http://localhost:8000/comment-list-name/?name=${valueInput}`)
})