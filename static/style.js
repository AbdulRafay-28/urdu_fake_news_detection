// ===============================
// AI Urdu Fake News Detection
// script.js
// ===============================

// Page Fade In
window.addEventListener("load", () => {
    document.body.style.opacity = "1";
});

// Typing Effect
const title = document.querySelector("h1");

if(title){

const text = title.innerText;

title.innerHTML = "";

let i = 0;

function typing(){

    if(i < text.length){

        title.innerHTML += text.charAt(i);

        i++;

        setTimeout(typing,60);

    }

}

typing();

}

// Floating Tilt Card
const card = document.querySelector(".glass");

document.addEventListener("mousemove",(e)=>{

const x = (window.innerWidth/2 - e.pageX)/40;

const y = (window.innerHeight/2 - e.pageY)/40;

card.style.transform =
`rotateY(${-x}deg) rotateX(${y}deg)`;

});

document.addEventListener("mouseleave",()=>{

card.style.transform="rotateX(0) rotateY(0)";

});

// Progress Bar Animation

const progress=document.querySelector(".progress-bar");

if(progress){

const width=progress.style.width;

progress.style.width="0%";

setTimeout(()=>{

progress.style.width=width;

progress.style.transition="2s";

},300);

}

// Button Ripple

const btn=document.querySelector("button");

btn.addEventListener("click",function(e){

let ripple=document.createElement("span");

let x=e.clientX-btn.offsetLeft;

let y=e.clientY-btn.offsetTop;

ripple.style.left=x+"px";

ripple.style.top=y+"px";

ripple.classList.add("ripple");

btn.appendChild(ripple);

setTimeout(()=>{

ripple.remove();

},700);

});

// Random Background Glow

setInterval(()=>{

document.body.style.backgroundPosition=
Math.random()*100+"% "+Math.random()*100+"%";

},4000);

// Result Animation

const result=document.querySelector(".result");

if(result){

result.animate([

{

opacity:0,

transform:"translateY(40px)"

},

{

opacity:1,

transform:"translateY(0)"

}

],{

duration:800,

fill:"forwards"

});

}