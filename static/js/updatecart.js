

console.log(window.location.origin)


 function getCookie(name) {
     let cookieValue = null;
     if (document.cookie && document.cookie !== '') {
         const cookies = document.cookie.split(';');
         for (let i = 0; i < cookies.length; i++) {
             const cookie = cookies[i].trim();
             // Does this coo/kie string begin with the name we want?
             if (cookie.substring(0, name.length + 1) === (name + '=')) {
                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                 break;
             }
         }
     }
     return cookieValue;
 }
 console.log(document.cookie)
 csrf=getCookie('csrftoken')
 console.log(getCookie('deviceid'))
user=document.getElementById('user').value
console.log(user)


 
 // add to cart product
     $(document).on('click','.cartform',function(e){
         e.preventDefault();
         console.log(e,'e')
         
             var data1= e.currentTarget.id // e.target.id
             console.log(data1)
     $.ajax({
         type:'POST',
         url: window.location.origin+'/updatecart/', //'{% url "cart" %}',
         data:{
             productid:data1,
             user: user,       //device1,
             query:'add',
             csrfmiddlewaretoken: csrf //$('input[name=csrfmiddlewaretoken]').val(),
             
         },
         success:function(json){
            console.log(json)
             console.log(json['items'])
 
             $('#cartvalue')[0].innerText =json['items']
             $('#cartvalue1')[0].innerText =json['items']
             console.log($('#cartvalue')[0].innerText)
           
         },
         error : function(xhr,errmsg,err) {
         console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
     }
     });
 
         
      
     });


     //remove from cart

     $(document).on('click','.remove-product',function(e){
        e.preventDefault();
        console.log(e,'e')
        
            var data1= e.currentTarget.id // e.target.id
            console.log(data1)
    $.ajax({
        type:'POST',
        url: window.location.origin+'/updatecart/', //'{% url "cart" %}',
        data:{
            productid:data1,
            user: user,
            query: 'delete'  ,     //device1,
            csrfmiddlewaretoken: csrf //$('input[name=csrfmiddlewaretoken]').val(),
            
        },
        success:function(json){
           console.log(json)
            console.log(json['items'])

            $('#cartvalue')[0].innerText =json['items']
            $('#cartvalue1')[0].innerText =json['items']
            console.log($('#cartvalue')[0].innerText)
        
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
});
