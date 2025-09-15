const PyButton = document.querySelector("div.div.button[id*='Python']")
const JavaButton = document.querySelector("div.div.button[id*='Java']")
const JScriptButton = document.querySelector("div.div.button[id*='Javascript']")
const CsButton = document.querySelector("div.div.button[id*='C#']")
const CppButton = document.querySelector("div.div.button[id*='C++']")
const SqlButton = document.querySelector("div.div.button[id*='SQL']")
const HtmlButton = document.querySelector("div.div.button[id*='Html']")
const CssButton = document.querySelector("div.div.button[id*='Css']")

const Button = document.querySelector("div.div.button")

function createOverlay(buttonClick) {
    alert("a")
    buttonClick.target.h1.id = "a"
}
PyButton.addEventListener("click", buttonClick)

alert("b")