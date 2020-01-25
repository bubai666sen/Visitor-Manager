function snackbar(msg,status) {
    let x = document.getElementById("snackbar");
    x.innerHTML = msg;
    x.className = "show";
    $("#snackbar").addClass(status);
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}
function ajaxForMessegeTransfer() {
    let message = $("#message").val();
    let name = $("#name").val();
    let subject= $("#subject").val();
    let email = $("#email").val();
    let flag = false;
    let error = "";
    if(message=='') {
        $("#message").addClass('error');
        flag = true;
        error = "All Fields are required! ";
    } else {
        $("#message").removeClass('error');
    }
    if(name=='') {
        $("#name").addClass('error');
        flag = true;
        error = "All Fields are required! ";
    } else {
        $("#name").removeClass('error');
    }
    if(subject=='') {
        $("#subject").addClass('error');
        flag = true;
        error = "All Fields are required! ";
    } else {
        $("#subject").removeClass('error');
    }
    if(email=='') {
        $("#email").addClass('error');
        flag = true;
        error = "All Fields are required! ";
    } else {
        $("#email").removeClass('error');
        var pattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if(!pattern.test(email)) {
            flag = true;
            error += "Please provide a valid email id!";
            $("#email").addClass('error');
        } else {
            $("#email").removeClass('error');
        }
    }
    if(flag) {
        snackbar(error,'snackbar-error');
        return;
    }
    
    $.ajax({
        headers: {"X-CSRFToken": token },
        type: "POST",
        url: store_message_url,
        data:{
            name: name,
            email: email,
            subject: subject,
            message: message,
            //"X-CSRFToken": token
        },
        success: function(result){
            snackbar("Message sent successfully!",'snackbar-success');
        },
        error: function(result){
            snackbar("Something went wrong!",'snackbar-error');
        }
    });
  }