let score=0;
let time=30;

function update(){
document.getElementById("score").innerText=score;
}

function checkAnswer(a,c){
if(a===c){
score++;
document.getElementById("result").innerText="Correct";
}else{
document.getElementById("result").innerText="Wrong";
}
update();
}

function checkFormula(c){
let v=document.getElementById("answer").value;
if(v===c){
score++;
document.getElementById("result").innerText="Correct";
}else{
document.getElementById("result").innerText="Wrong";
}
update();
}

function checkAB(a){
if(a==="Acid"){
score++;
document.getElementById("result").innerText="Correct";
}else{
document.getElementById("result").innerText="Wrong";
}
update();
}

function startTimer(){
setInterval(()=>{
time--;
let el=document.getElementById("timer");
if(el) el.innerText=time;

if(time<=0){
alert("Time up! Score: "+score);
location.reload();
}
},1000);
}
