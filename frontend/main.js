let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')

let token = localStorage.getItem('token')

if (token){
    loginBtn.remove()
}else{
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = 'file:///home/grzegorz-oledzki/Downloads/theme/Django-2021-master/New%20front/login.html'

})

let playersUrl = "http://127.0.0.1:8000/api/players/"

let getPlayers = () => {
    fetch(playersUrl)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        buildPlayers(data)
        })
}

let buildPlayers = (players) => {
    let playersWrapper = document.getElementById('projects-wrapper')
       playersWrapper.innerHTML = ''
    for (let i = 0; players.length > i; i++){
        let player = players[i]
        let playerCard = `
            <div class='player--card'>
                <img src='http://127.0.0.1:8000${player.featured_image}'>

                <div>
                    <div class='card--header'>
                        <h3>${player.title} </h3>
                        <strong class='vote--option' data-vote='up' data-player='${player.id}'>&#43;</strong>
                        <strong class='vote--option' data-vote='down' data-player='${player.id}'>&#8722;</strong>
                    </div>
                    <i>${player.vote_ratio}% Positive feedback</i>
                    <p>${player.description.substring(0,150)}<p>
                </div>
            </div>
        `
        playersWrapper.innerHTML += playerCard
    }

    addVoteEvents()
    //Add an listener
}

let addVoteEvents = () => {
    let voteBtns = document.getElementsByClassName('vote--option')
    for (let i =0; voteBtns.length > i; i++) {
        voteBtns[i].addEventListener('click', (e) =>{
            let token = localStorage.getItem('token')
            let vote = e.target.dataset.vote
            let player = e.target.dataset.player
                fetch(`http://127.0.0.1:8000/api/player/${player}/vote/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({ 'value': vote })
            })
            .then(response => response.json())
            .then(data => {
                console.log('sukces', data)})
                getPlayers()
        })
    }
}

getPlayers()