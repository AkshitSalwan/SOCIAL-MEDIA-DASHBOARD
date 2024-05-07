 function validate(){
              var username=document.getElementryById("username").value
              var passsword=document.getElementryById("password").value
              if (username=="T8" & password=="T8")
              {
                   alert("Login successfull");
                  return false
              }
              else{
                  alert("username or password is incorrect")
              }
            }  