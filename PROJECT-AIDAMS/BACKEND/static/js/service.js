

// Updated PostHandler
async function POSTHandler(data, url, success, fail, msg_show) {
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
  
      if (!response.ok) {
        throw new Error(`${response.status} ${response.statusText}`);
      }
  
      // Check the content type of the response
      const contentType = response.headers.get("content-type");
  
      if (contentType && contentType.includes("application/json")) {
        const JSONdata = await response.json();
        if (msg_show) alert(success);
        return JSONdata;
      } else if (contentType && contentType.includes("application/pdf")) {
        // Assuming it's a PDF file, you can handle it as needed
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        window.open(url, "_blank");
        if (msg_show) alert(success);
        return null; // or whatever makes sense for your use case
      } else {
        // Handle other content types if needed
        if (msg_show) alert(fail);
        return null;
      }
    } catch (error) {
      if (msg_show) alert(fail);
      console.error(error);
      return null;
    }
  }

/*
==============================
    Home Navigation Page
==============================
*/
async function navigateHome() {
    window.location.href = "/";
  }
  

/*
==============================
   Sign In Data Verificaiton
==============================
*/
async function validateUser(){
    const email = document.getElementById("user_email").value;
    const password = document.getElementById("user_password").value;
    if(email.length <= 0 || password.length <= 0)
      {
        alert("Please Fill out the Fields");
      }
    const data = {
        acc_email : email,
        acc_password : password,
    };
    url="/signin";
    success="Sign In Successful!";
    fail="Account does not exist!";

    fetched_data = await POSTHandler(data, url, success, fail, true).then(
        async (fetched_data) => {
          // Code to execute when data is successfully fetched
          if (fetched_data) {
            // Set the session data
            sessionStorage.setItem("acc_data", JSON.stringify(fetched_data));
            console.log(fetched_data);
            // Navigate to the home page
            window.location.href = "/dashboard";
          }
        }
      );
}

/*
==============================
   Sign UP Data Registration
==============================
*/ 
async function registerUser(){
    const f_name = document.getElementById("first_name").value;
    const m_name = document.getElementById("mid_name").value;
    const l_name = document.getElementById("last_name").value;
    const email = document.getElementById("signup_email").value;
    const contact = document.getElementById("signup_contact").value;
    const password = document.getElementById("signup_password").value;
    const conf_password = document.getElementById("confirm_password").value;

    if(password != conf_password){
        alert("Password Does Not Match");
        return;
    }
    if(f_name.length <= 0 || m_name.length <= 0 || l_name.length <= 0 || email.length <= 0 || contact.length <= 0 || password.length <= 0 || conf_password.length <= 0)
    {
      alert("Please Input all the Fields");
    }
    const data = {
        acc_fname : f_name,
        acc_mname : m_name,
        acc_lname : l_name,
        acc_email : email,
        acc_contact : contact,
        acc_password : password,
    };
    url="/signup";
    success="Sign Up Successful Proceed to Verification!";
    fail="Registration Failed!";
    await POSTHandler(data, url, success, fail, true);
   
}

/*
==============================
         Dashboard Search
==============================
*/ 

async function dashboard_lock( dv_status, dv_id){

 data ={
  
 }
  url = "/dashboard_btn/"+dv_id+"/"+dv_status;
  success = "Successfuly Change Door Staus ";
  fail = "Change Failed";
  await POSTHandler(data, url, success, fail, true);
  window.location.href = "/dashboard"
 
}









/*
==============================
         Add Device
==============================
*/ 

async function addDevice(){
    const dev_pass = document.getElementById("inputPassword").value;

    if (password = ""){
        alert ("Please Enter Password");
        return;
    }
    const data = {
        dv_password : dev_pass
    };
    url = "";
    success = "";
    fail = "";
    fetched_data = await POSTHandler(data, url, success, fail, true);
    if (fetched_data){
        sessionStorage.setItem("dev_data",JSON.stringify(fetched_data));
        navigateHome();
    }
}

/*
==============================
  User Account Settings
==============================
*/ 

async function updateUser(){
    const first_name = document.getElementById("user_fname").value;
    const mid_name = document.getElementById("user_mname").value;
    const last_name = document.getElementById("user_lname").value;
    const current_pass = document.getElementById("old_password").value;
    const new_pass = document.getElementById("new_password").value;
    const confirm_pass = document.getElementById("confirm_new_password").value;
    const contact= document.getElementById("user_number").value;
    const email = document.getElementById("user_email").value;


    if(new_pass != confirm_pass){
        alert("Please Check Your Password!");
        return;
    }
    const data ={
        acc_fname : first_name,
        acc_mname : mid_name,
        acc_lname : last_name,
        acc_password : current_pass,
        acc_password : new_pass,
        acc_contact : contact,
        acc_email : email,
    };
    url = "";
    success = "";
    fail = "";
    fetched_data = await POSTHandler(data, url, success, fail, true);
    if (fetched_data){
        sessionStorage.setItem("acc_data",JSON.stringify(fetched_data));
        navigateHome();
    }

}

/*
==============================
  User Accoutn Settings Photo update
==============================
*/ 

 
async function updateUserphoto(){
    const user_image = document.getElementById("display_image").value;
    const name = document.getElementById("display_name").value;
    const email = document.getElementById("display_email").value;

    const data ={
        acc_profile : user_image,
        acc_fname, acc_mname, acc_lname : name,
        acc_email : email,
    };
    url = "";
    success = "";
    fail = "";
    fetched_data = await POSTHandler(data, url, success, fail, true);
    if (fetched_data){
        sessionStorage.setItem("acc_data",JSON.stringify(fetched_data));
        navigateHome();
    }
}

/*
==============================
  // Admin Device Edit
==============================
*/ 

async function editAdmindevice(){
    const dev_id = document.getElementById("device_id").value;
    const dev_name = document.getElementById("device_name").value;
    const dev_key = document.getElementById("device_key").value;

    const data = {
        dv_id : dev_id,
        dv_name : dev_name,
        dv_key : dev_key,

    };
    url = "";
    success = "";
    fail = "";
    fetched_data = await POSTHandler(data, url, success, fail, true);
    if (fetched_data){
        sessionStorage.setItem("dev_data",JSON.stringify(fetched_data));
        navigateHome();
    }
}

/*
==============================
  // Admin User Edit
==============================
*/ 

async function  editAdminusers(){
    const user_id = document.getElementById("user_id").value;
    const fname = docuement.getElementById("ad_user_fname").value;
    const mname = docuement.getElementById("ad_user_mname").value;
    const lname = docuement.getElementById("ad_user_lname").value;
    const password = docuement.getElementById("ad_user_password").value;
    const contact = docuement.getElementById("ad_user_contact").value;
    const email = docuement.getElementById("ad_user_email").value;

    const data = {
        acc_id : user_id,
        acc_fname : fname,
        acc_mname : mname,
        acc_lname : lname,
        acc_password : password,
        acc_contact : contact,
        acc_email : email,
       
    };
    url = "";
    success = "";
    fail = "";
    fetched_data = await POSTHandler(data, url, success, fail, true);
    if (fetched_data){
        sessionStorage.setItem("admin_user_data",JSON.stringify(fetched_data));
        navigateHome();
    }

}

async function editAdminusersphoto(){
    const image = document.getElementById("admin_display_name").src;
    const name = document.getElementById("admin_display_name").innerHTML;
    const email = document.getElementById("admin_display_email").innerHTML;

    const data = {   
        acc_fname, acc_mname, acc_lname : name,
        acc_email : email,
        acc_profile : image,
    };
    url = "";
    success = "";
    fail = "";
    fetched_data = await POSTHandler(data, url, success, fail, true);
    if (fetched_data){
        sessionStorage.setItem("",JSON.stringify(fetched_data));
        navigateHome();
    }
}

/*
==============================
  // Admin settings
==============================
*/ 

async function adminSettings(){
    const ad_fname = document.getElementById("admin_fname").value;
    const ad_mname = document.getElementById("admin_mname").value;
    const ad_lname = document.getElementById("admin_lname").value;
    const ad_newpass = document.getElementById("admin_new_pass").value;
    const ad_con_pass = document.getElementById("admin_conf_pass").value;

    if(ad_newpass != ad_con_pass){
        alert("Password Does Not Match");
        return;
    }

    const data ={
        acc_fname : ad_fname,
        acc_mname : ad_mname,
        acc_lname : ad_lname,
        acc_password : ad_newpass,
    };
    url = "";
    success = "";
    fail = "";
    fetched_data = await POSTHandler(data, url, success, fail, true);
    if (fetched_data){
        sessionStorage.setItem("",JSON.stringify(fetched_data));
        navigateHome();
    }
}

