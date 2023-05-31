const my = document.querySelector('.myJs')

function StartLove() {
    my.addEventListener('click',()=>{
        console.log('worked');
        
        my.style.color='red'
        
    })
}

StartLove()