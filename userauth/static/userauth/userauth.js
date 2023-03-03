"use strict"
/**
 * @description
 * Basic listener event set up
 */

// eye-icon
document.getElementsByClassName("fa-eye-slash")[0].addEventListener("click", switchPasswdType);

// close login
document.getElementsByClassName("embed-close-icon")[0].addEventListener("click", closeTab);

// sign_in and sign_up
document.getElementsByClassName("btn-login")[0].addEventListener("click", login);
document.getElementsByClassName("btn-register")[0].addEventListener("click", register);

/**
 * @description
 * Web view change functions
 */

/**
 * @name functionSwitch
 * @description 
 * Swith from signin and signup
 * @author YaoMang
 * @lastedit 2023/1/27
 */
function functionSwitch()
{
    //console.log("Being called")

    let element_signin = document.getElementById("sign_in");
    let element_signup = document.getElementById("sign_up");

    if(element_signin.hidden){
        element_signin.removeAttribute("hidden");
        element_signup.hidden = "hidden";
    }
    else{
        element_signin.hidden = "hidden";
        element_signup.removeAttribute("hidden");
    }
}

/**
 * @name switchPasswdType
 * @description 
 * Show and hide password in input element
 * @author YaoMang
 * @lastedit 2023/1/29
 */
function switchPasswdType()
{
    let element_i = document.getElementsByClassName("fa");
    for(let i = 0; i < element_i.length; ++i){
        if(element_i[i].hasAttribute("data-icon-eye")){
            element_i = element_i[i];
        }
    }

    const eye_open = "fa-eye";
    const eye_close = "fa-eye-slash"; 

    let element_input = document.getElementsByTagName("input");
    let target_element;
    for(let i = 0; i < element_input.length; ++i){
        if(element_input[i].hasAttribute("data-passwd")){
            target_element = element_input[i];
            break;
        }
    }

    if(element_i.classList.contains(eye_close)){
        element_i.classList.remove(eye_close);
        element_i.classList.add(eye_open);
        target_element.type = "text";
    }
    else{
        element_i.classList.remove(eye_open);
        element_i.classList.add(eye_close);
        target_element.type = "password";
    }
    return;
}

/**
 * @name pop_info
 * @description
 * Display message with a pop window
 * @author YaoMang
 * @lastedit 2023/1/31
 */
class popInfo{
    constructor(info, during){
        this.info = info;
        this.during = during;

        let pop_container = document.getElementsByClassName("pop_container");
        let container = pop_container[0];
        if(!container){
            container = document.createElement("div");
            container.classList.add("pop_container");
            let parent_element = document.getElementsByTagName("body")[0];
            parent_element.appendChild(container, parent_element);
        }
    }
    
    mask() {
        let docList = document.getElementsByClassName("pop_mask_container");
        let container = docList[0];
        if(!container){
            container = document.createElement("div");
            container.classList.add("pop_mask_container");
            let pop_container = document.getElementsByClassName("pop_container");
            pop_container[0].appendChild(container, pop_container);
        }
        let element_info = document.createElement("div");
        element_info.classList.add("pop_info-mask");
        element_info.innerText = this.info;
        container.appendChild(element_info, container);

        setTimeout(function(elementX){elementX.remove()}, this.during, element_info);
    }
}

/**
 * @name closeTab
 * @description
 * close embed login page
 * @author YaoMang
 * @lastedit 2023/1/29
 */
function closeTab()
{
    let x = document.getElementsByClassName("embed-mask");
    x[0].remove();
}

/**
 * @name login
 * @description
 * Prototype of login
 * @author YaoMang
 * @lastedit 2023/1/29
 */
function login()
{
    let element_login_info = document.getElementById("sign_in_info");
    let login_info = element_login_info.href;
    submitUserInfo(login_info);
}

/**
 * @name register
 * @description
 * Prototype of register
 * @author YaoMang
 * @lastedit 2023/1/29
 */
function register()
{
    let element_register_info = document.getElementById("sign_up_info");
    let register_info = element_register_info.href;
    submitUserInfo(register_info);
}

/**
 * @name submitUserInfo
 * 
 * @param {*} req_url 
 * @returns serverInfo
 * 
 * @description
 * Core function of userauth
 * @author YaoMang
 * @lastedit 2023/1/29
 */
function submitUserInfo(req_url)
{
    let xhr_userinfo = new XMLHttpRequest();
    let inputs = document.getElementsByTagName("input");

    let submitContent = new FormData;
    
    let headArray = [inputs[0].name,"username", "password"];

    for(let i = 0; i < headArray.length; ++i){
        submitContent.append(headArray[i], inputs[i].value);
    }

    xhr_userinfo.open("POST", req_url, true);
    xhr_userinfo.send(submitContent);

    xhr_userinfo.onreadystatechange=function()
    {
        if(xhr_userinfo.readyState==4 && xhr_userinfo.status==200)
        {
            new popInfo(xhr_userinfo.responseText, 1000).mask();
        }
        else if(xhr_userinfo.readyState==4 && xhr_userinfo.status!=200){
            new popInfo(xhr_userinfo.responseText, 1000).mask();
        }
    }
    

    return xhr_userinfo.status;
}