
let middle=document.querySelector(".middle")
let middle2=document.querySelector(".middle2")
let m1=document.querySelector(".m1")
let m2=document.querySelector(".m2")
let m3=document.querySelector(".m3")
let m4=document.querySelector(".m4")
let btn=document.querySelector("#btnn")
let butt=document.querySelector(".butt")

let current=0
let count=4
let load=document.querySelector("#load")

    document.addEventListener("DOMContentLoaded", function(){
    setTimeout(function() {
       load.style.display = "none";
        butt.style.display="flex"
      }, 200);});
    
    btn.addEventListener('click', function() {
    let content = document.querySelector(".m" + (current+1));
  
    if (content) {
        content.style.display = "flex";
    }
    if (current==count-1) {
        btn.style.display = "none"; 
      } 
    current +=1; 
    });

    
 
    url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
    fetch(url).then(function(reponse){
        return reponse.json()
    }).then(function(data){
  
        
    
    list=data["result"]['results']
    
    for(let i=0;i<list.length;i++){
    file=(list[i]["file"].toLowerCase().split("jpg"))[0]+"jpg"
    text=list[i]["stitle"]
    let picc = document.createElement("img");
    picc.src = file;

    let t = document.createElement("P");
    t.textContent = text;

    let pic1 = document.createElement("div");
    pic1.classList.add("pic"); 
    let t1 = document.createElement("div");
    t1.classList.add("t1"); 
    
    let pic2 = document.createElement("div");
    pic2.classList.add("pic2");
    let t2 = document.createElement("div");
    t2.classList.add("tt1"); 
       
    if (i < 3) {
        pic1.appendChild(picc)
        t1.appendChild(t)   
        let square = document.createElement("div");
        square.classList.add("square" + (i + 1));
        square.appendChild(pic1);
        square.appendChild(t1);
        middle.appendChild(square);
       
    } else if (i < 15) {
         
        
        pic2.appendChild(picc)
        t2.appendChild(t)
        let s = document.createElement("div");
            s.classList.add("s" + (i -2));
            s.appendChild(pic2);
            s.appendChild(t2);
            middle2.appendChild(s)
    } else if (i < 27) {
        
        pic2.appendChild(picc)
        t2.appendChild(t)
        let s = document.createElement("div");
        s.classList.add("s" + (i -14));
        s.appendChild(pic2);
        s.appendChild(t2);
        m1.appendChild(s)
    } else if (i < 39) {
       
        pic2.appendChild(picc)
        t2.appendChild(t)
        let s = document.createElement("div");
        s.classList.add("s" + (i -26));
        s.appendChild(pic2);
        s.appendChild(t2);
        m2.appendChild(s)
    } else if (i < 51) {
      
        pic2.appendChild(picc)
        t2.appendChild(t)
        let s = document.createElement("div");
        s.classList.add("s" + (i -38));
        s.appendChild(pic2);
        s.appendChild(t2);
        m3.appendChild(s)
    } else if (i < 58) {
       
        pic2.appendChild(picc)
        t2.appendChild(t)
        let s = document.createElement("div");
        s.classList.add("s" + (i -50));
        s.appendChild(pic2);
        s.appendChild(t2);
        m4.appendChild(s)
    }

   
}})

    
