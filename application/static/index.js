'use strict'
const showbtn = document.querySelector('#showbtn');
const upldbtn = document.querySelector('#upldbtn');
const displayArea = document.querySelector('#displayArea');
const imagetemp = document.getElementsByTagName("template")[0];

showbtn?.addEventListener('click', (event) => {
    event.preventDefault()
    while (displayArea.firstChild) {
        displayArea.removeChild(displayArea.firstChild);
    }
    if (upldbtn.classList.contains('invisible')) {
        upldbtn.classList.toggle('invisible')
    }
    fetch('/images')
        .then(response => response.json())
        .then(data => {
            //console.log(data[0])
            data.forEach(item => {
                let clon = imagetemp.content.cloneNode(true);
                clon.querySelector('img').src = 'static/image/1234567.jpeg'
                clon.querySelector('.card-title').innerText = item.name;
                displayArea.appendChild(clon)
            });
        })
        .catch(error => {
            console.error(error)
            displayArea.innerHTML = 'No Images Found'
        })

})