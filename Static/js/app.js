let PyButton, JavaButton, JScriptButton, CsButton, CppButton, SqlButton, HtmlButton, CssButton, Shadow, Overlay, Exit

window.onload = function() {
    Shadow = document.getElementById("shadow");
    Overlay = document.getElementById("overlayed");
    Exit = document.getElementById("exited");


    PyButton = document.getElementById("Python");
    JavaButton = document.getElementById("Java");
    JScriptButton = document.getElementById("Javascript");
    CsButton = document.getElementById("C#");
    CppButton = document.getElementById("C++");
    SqlButton = document.getElementById("SQL");
    HtmlButton = document.getElementById("Html");
    CssButton = document.getElementById("Css");
    // alert(PyButton);
    PyButton.addEventListener("click", createOverlay);
    JavaButton.addEventListener("click", createOverlay);
    JScriptButton.addEventListener("click", createOverlay);
    CsButton.addEventListener("click", createOverlay);
    CppButton.addEventListener("click", createOverlay);
    SqlButton.addEventListener("click", createOverlay);
    HtmlButton.addEventListener("click", createOverlay);
    CssButton.addEventListener("click", createOverlay);
}


function createOverlay() {
    Shadow.id = "shadow2";
    Overlay.id = "overlayed2";
    Overlay.children[3].innerHTML = this.id;
    Exit.children[0].id = "exit2";
    Exit.addEventListener("click", leaveOverlay);
    // if (this.id === "Python") {
    //     Shadow.id = "shadow2";
    //     Overlay.id = "overlayed2";
    //     Overlay.children[3].innerHTML = "Python";
    //     Exit.children[0].id = "exit2";
    //     Exit.addEventListener("click", leaveOverlay);
    // }
    // if (this.id === "Java") {
    //     Shadow.id = "shadow2";
    //     Overlay.id = "overlayed2";
    //     Overlay.children[3].innerHTML = "Java";
    //     Exit.children[0].id = "exit2";
    // }
}

function leaveOverlay() {
    Shadow.id = "shadow";
    Overlay.id = "overlayed";
    Overlay.children[3].innerHTML = "";
    Exit.children[0].id = "exit";
}


// alert("Help!");

