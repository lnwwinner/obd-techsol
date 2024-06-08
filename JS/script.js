let menu= document.querySelector('#bars-icon');
let navbar= document.querySelector('.navbar');

menu.onclick= () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}
window.onscroll = ()=>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
  }
  document.querySelector('#learn-more').onclick = () =>{ 
    document.querySelector('.popup-image').style.display = 'block';
    }

document.querySelector('.popup-image span').onclick = () =>{
    document.querySelector('.popup-image').style.display = 'none';
}

/*  scroll reveal */
ScrollReveal({
    distance: '80px',
    duration: 1500,
    delay:100,
});

ScrollReveal().reveal('.main, heading',{origin: 'top'});
ScrollReveal().reveal('.services',{origin: 'bottom'});
ScrollReveal().reveal('.contact',{origin: 'bottom'});

// send email from Form
const btn = document.getElementById('btn-email');

document.getElementById('form')
.addEventListener('submit', function(event) {
    event.preventDefault();
 
    btn.value = 'Sending...';
 
    const serviceID = 'default_service';
    const templateID = 'template_iz8zmzq';
 
    emailjs.sendForm(serviceID, templateID, this)
     .then(() => {
       btn.value = 'Send Email';
       alert('Sent!');
     }, (err) => {
       btn.value = 'Send Email';
       alert(JSON.stringify(err));
     });
 });