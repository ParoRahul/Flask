'use strict'
const showbtn = document.querySelector('#showbtn');
const upldinput = document.querySelector('#upldimg');
const displayArea = document.querySelector('#displayArea');
const imagetemp = document.getElementsByTagName("template")[0];

showbtn?.addEventListener('click', (event) => {
    event.preventDefault()
    while (displayArea.firstChild) {
        displayArea.removeChild(displayArea.firstChild);
    }
    if (upldinput.classList.contains('invisible')) {
        upldinput.classList.toggle('invisible')
    }
    fetch('/images')
        .then(response => response.json())
        .then(data => {
            //console.log(data[0])
            data.forEach(item => {
                let clon = imagetemp.content.cloneNode(true);
                clon.querySelector('img').src = item.url
                clon.querySelector('.card-title').innerText = item.name;
                displayArea.appendChild(clon)
            });
        })
        .catch(error => {
            console.error(error)
            displayArea.innerHTML = '<div class="error"><h5>No Image Found</h5></div>'

        })

})

upldinput.addEventListener('change', event => {
    const files = event.target.files
    const formData = new FormData()
    formData.append('file', files[0])
    fetch('/images', {
        method: 'POST',
        body: formData
    }).then(() => {
        while (displayArea.firstChild) {
            displayArea.removeChild(displayArea.firstChild);
        }
    }).catch(error => console.error(error));
})