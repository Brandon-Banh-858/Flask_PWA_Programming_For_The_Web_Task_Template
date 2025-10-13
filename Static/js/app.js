let PyButton, JavaButton, JScriptButton, CsButton, CppButton, SqlButton, HtmlButton, CssButton, Shadow, Overlay, Exit

window.onload = function() {
    if (document.getElementById("shadow")) {
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

        UserName = document.getElementById("TrueUsernamed");
        if (UserName.textContent != "") {

            document.getElementById("PythonQs").addEventListener("click", detect);
            document.getElementById("PythonAs").addEventListener("click", detect);

            this.document.getElementById("menu_text4").children.item(0).textContent = UserName.textContent + "'s Profile";
            this.document.getElementById("bottom_menu_text4").children.item(0).textContent = UserName.textContent + "'s Profile";
            this.document.getElementById("menu_text4").children.item(0).setAttribute('href', '');
            this.document.getElementById("bottom_menu_text4").children.item(0).setAttribute('href', '');

            this.document.getElementById("menu_text4").children.item(0).addEventListener("click", LoginOverlay);
            this.document.getElementById("bottom_menu_text4").children.item(0).addEventListener("click", LoginOverlay);

            if (document.getElementById("Success").textContent != "") {
                LoginOverlay2();
            }
        }
    }

    if (document.getElementById("username")) {
        InputUsername = document.getElementById("username");
        InputPassword = document.getElementById("password");

        SendToSign = document.getElementById("LoginIn");
        SendToSign2 = document.getElementById("LoginIn2");
        SendToSign2.addEventListener("click", SendSign);
        SendToSign.addEventListener("click", SendSign2);

        if (document.getElementById("PassData").textContent == "Valid") {
                document.getElementById("ErrorMes").classList.remove("invisible");
                document.getElementById("ErrorMes").classList.add("visible");
            }
        else if (document.getElementById("PassData").textContent == "Invalid") {
                document.getElementById("ErrorMes").classList.remove("visible");
                document.getElementById("ErrorMes").classList.add("invisible");
            }
        else if (document.getElementById("PassData").textContent == "Change") {
                document.location.href = "homepage.html"
            }

        UserName = document.getElementById("TrueUsernamed");
        if (UserName.textContent != "") {
            this.document.getElementById("menu_text4").children.item(0).textContent = UserName.textContent + "'s Profile";
            this.document.getElementById("bottom_menu_text4").children.item(0).textContent = UserName.textContent + "'s Profile";
            this.document.getElementById("menu_text4").children.item(0).setAttribute('href', '')
            this.document.getElementById("bottom_menu_text4").children.item(0).setAttribute('href', '')

            this.document.getElementById("menu_text4").children.item(0).addEventListener("click", LoginOverlay);
            this.document.getElementById("bottom_menu_text4").children.item(0).addEventListener("click", LoginOverlay);

            if (document.getElementById("Success").textContent != "") {
                LoginOverlay2();
            }
        }   
    }

    if (document.getElementById("homepage_text")) {
        UserName = document.getElementById("TrueUsernamed");
        if (UserName.textContent != "") {
            this.document.getElementById("menu_text4").children.item(0).textContent = UserName.textContent + "'s Profile";
            this.document.getElementById("bottom_menu_text4").children.item(0).textContent = UserName.textContent + "'s Profile";
            this.document.getElementById("menu_text4").children.item(0).setAttribute('href', '');
            this.document.getElementById("bottom_menu_text4").children.item(0).setAttribute('href', '');

            this.document.getElementById("menu_text4").children.item(0).addEventListener("click", LoginOverlay);
            this.document.getElementById("bottom_menu_text4").children.item(0).addEventListener("click", LoginOverlay);

            if (document.getElementById("Success").textContent != "") {
                LoginOverlay2();
            }
        }
    }

    if (document.getElementById("MessageSend")) {

        this.document.getElementById("GoBackLeave").addEventListener("click", Leave);
        this.document.getElementById("SubmitOrLeave").addEventListener("click", Leave2);

        // this.document.querySelectorAll('.Deletion')
        deletionlist = this.document.querySelectorAll('.Deletion');
        for (let num = 0; num < deletionlist.length; num++) {
            deletionlist[num].addEventListener("click", destroy);
        }

        UserName = document.getElementById("TrueUsernamed");
        if (UserName.textContent != "") {
            this.document.getElementById("menu_text4").children.item(0).textContent = UserName.textContent + "'s Profile";
            this.document.getElementById("bottom_menu_text4").children.item(0).textContent = UserName.textContent + "'s Profile";
            this.document.getElementById("menu_text4").children.item(0).setAttribute('href', '');
            this.document.getElementById("bottom_menu_text4").children.item(0).setAttribute('href', '');

            this.document.getElementById("menu_text4").children.item(0).addEventListener("click", LoginOverlay);
            this.document.getElementById("bottom_menu_text4").children.item(0).addEventListener("click", LoginOverlay);

            if (document.getElementById("Success").textContent != "") {
                LoginOverlay2();
            }
        }
        else {
            if (this.document.location.href == "http://192.168.1.122:5000/messages.html") {
                document.location.href = "ask_and_answer.html";
            }
        }
    }
}

function createOverlay(ev) {
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

function SendSign() {
    document.forms["SignInForm"].submit();
    // document.location.href = "homepage.html";
}

function SendSign2() {
    document.getElementById("Type").value = "Login"
    document.forms["SignInForm"].submit();
    // document.location.href = "homepage.html";
}

function LoginOverlay(ev) {
    document.getElementById("LoginOverlay").style.visibility = "visible";
    document.getElementById("LoginShadow").style.visibility = "visible";
    document.getElementById("exitLogin").style.visibility = "visible";
    document.getElementById("exitLogin").addEventListener("click", LoginOverlay0);
    ev.preventDefault();
}

function LoginOverlay2() {
    document.getElementById("LoginOverlay").style.visibility = "visible";
    document.getElementById("LoginShadow").style.visibility = "visible";
    document.getElementById("exitLogin").style.visibility = "visible";
    document.getElementById("exitLogin").addEventListener("click", LoginOverlay0);
}

function LoginOverlay0() {
    document.getElementById("LoginOverlay").style.visibility = "hidden";
    document.getElementById("LoginShadow").style.visibility = "hidden";
    document.getElementById("exitLogin").style.visibility = "hidden";
    document.getElementById("Success").textContent = "";
}


function Leave() {
    document.location.href = "ask_and_answer.html";
}

function Leave2() {
    document.location.href = "question.html";
}

function destroy(ev) {
    document.getElementById("whatToDelete").value = ev.target.id;
    document.forms["DeleteSystem"].submit();
}

function detect(ev) {
    document.getElementById("ChangeLang").value = Overlay.children[3].textContent;
    document.forms["ChangingProgram"].submit();
}

function detect2(ev) {
    
}

// alert("Help!");

