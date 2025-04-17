console.log("Hello");
console.log("I like pizza")

//window.alert("This is an alert")
// This is a comments


/* Multiline 
comment*/

// variables: two steps declaration and assignment
//
//var fullName = "Irene Kilgannon";
//var age = 21;
//var isStudent = true;
//
//document.getElementById("p1").textContent= `Your name is ${fullName}`;
//document.getElementById("p2").textContent = `You are ${age} years old.`;
//document.getElementById("p3").textContent = `Enrolled: ${isStudent}`;
//
var username;

document.getElementById("mySubmit").onclick = function(){
    username = document.getElementById("myText").value;
    document.getElementById("myH1").textContent = `Hello ${username}`
}


function happyBirthday(username){
    console.log("Happy Birthday to you")
    console.log("Happy Birthday to you")
    console.log(`Happy Birthday dear ${username}!`)
    console.log("Happy Birthday to you")
}

happyBirthday("Irene");
happyBirthday("Martin");

function add(x, y){
    var result = x + y;
    return result;
}

function subtract(x, y){
    return x-y;
}
let answer = add(2,3);

console.log(answer);

console.log(subtract(5,3));
//
//const username2 = ""
//const welcomeMsg = document.getElementById("welcome-msg");
//welcomeMsg.textContent += username2 === "" ? ` Guest` : username;
//
//
//document.title = "Change title";
//document.body.style.backgroundColor = "pink"

//element selectors
//
//const myHeading = document.getElementById("myH1");
//myHeading.style.backgroundColor = "blue"
//myHeading.style.textAlign = "center";
//
//const h2Elements = document.getElementsByTagName("h2");
//
//Array.from(h2Elements).forEach(h2Element => {
//    h2Element.style.backgroundColor = "green";
//});
//
//const element = document.querySelectorAll("h2");
//element.style.backgroundColor = "yellow";

//const ulElements = document.querySelectorAll("ul");
//
//ulElements.forEach(ulElement => {
//    const firstChild = ulElement.firstElementChild;
//    firstChild.style.backgroundColor = "yellow";
//
//    const lastChild = ulElement.lastElementChild;
//    lastChild.style.backgroundColor = "red";
//})
//
//const element4 = document.getElementById("apple");
//const nextSibling = element4.nextElementSibling;
//nextSibling.style.backgroundColor = "green";
//
// Add and change HTML
// Step 1: Create the Element
//const newH1 = document.createElement("h1");

// Step 2: Add attributes/properties
//newH1.textContent = "I like pizza";
//newH1.id = "myH1";
//newH1.style.color = "tomato";
//newH1.style.textAlign = "center";

// Step 3  Append element to DOM
//document.body.append(newH1);
//document.getElementById("box1").append(newH1);

//const box2 = document.getElementById("box2")
//document.body.insertBefore(newH1, box2);
//
//const boxes = document.querySelectorAll(".box");
//document.body.insertBefore(newH1, boxes[4]);

// remove element
//document.getElementById("box1").removeChild(newH1);

// Add element to fruits list
const newListItem = document.createElement("li")

newListItem.textContent = "coconut";
newListItem.id = "coconut";
newListItem.style.fontWeight = "bold";
newListItem.style.backgroundColor = "lightgreen";

//document.body.append(newListItem);
document.getElementById("fruits").append(newListItem);


// Mouse events
const myBox = document.getElementById("myBox");
const myButton = document.getElementById("myButton")

//function changeColor(event){
//    event.target.style.backgroundColor = "tomato";
//    event.target.textContent = "Ouch"
//}

//myBox.addEventListener("click", event => {
//    event.target.style.backgroundColor = "tomato";
//    event.target.textContent = "Ouch"
//});
//
//
//// Mouse over
//myBox.addEventListener("mouseover", event => {
//    event.target.style.backgroundColor = "yellow";
//    event.target.textContent = "Mouse over"
//})
//
//myBox.addEventListener("mouseout", event => {
//    event.target.style.backgroundColor = "lightgreen";
//    event.target.textContent = "Click me :)";
//})
//
//myButton
myButton.addEventListener("click", event => {
    myBox.style.backgroundColor = "tomato";
    myBox.textContent = "Ouch"
});

// Mouse over
myButton.addEventListener("mouseover", event => {
    myBox.style.backgroundColor = "yellow";
    myBox.textContent = "Mouse over"
})

myButton.addEventListener("mouseout", event => {
    myBox.style.backgroundColor = "lightgreen";
    myBox.textContent = "Click me :)";
})

// Show and hide images
const myHideButton = document.getElementById("hideImageButton");
const myImg = document.getElementById("myImg");

myHideButton.addEventListener("click", event =>{
    if(myImg.style.visibility === "hidden"){
        myImg.style.visibility = "visible";
        myHideButton.textContent = "Hide";
    }
    else{
        myImg.style.visibility = "hidden";
        myHideButton.textContent = "Show";
    }    
})
