# Food-delivery-ecommerce-website
  This is food delivery website which is near about complete solution for **Restautent**. 
  Python with Django framework is used in this project.
  
  Deployed on vps server. You can check on [www.dwipal.codevedic.com](https://dwipal.codevedic.com)
  
  
  ## Project look:

  <!-- ![website look](https://github.com/dwipalshrirao/food-delivery-ecommerce-website/blob/main/website_look.gif) -->

  <p align="center" width="100%">
    <img src="https://github.com/dwipalshrirao/food-delivery-ecommerce-website/blob/main/website_look.gif"> 
</p>

  ## Features of project:

  1. **Register user with email verification**. It sends OTP to user's email-id , also it will be expire after 5 minute, if user will have not use this OTP. After expiration of OTP, there is OTP re-genration feature,
  which generate OTP and send again to user's email-id.

  2. **Dine-in feature**. Any user (i.e. Anonymus user) can book a table with email verification.

  3. **Add to cart without reloading page**. User can add item to cart without reloading page(javascript is used for this feature). 
  But if user is not logged in then he will redirect to login page.

  4. **Blogging system**. Admin can make crud operation on posts and any website visitor can see posts.

  5. **FlatePages**. I used Django's flat pages feature for about us page.


  In future update I will add some feature like,
  * Anonymus user can add items to cart without login.
  * Payment gateway.
  
  
  I am not very good at desing UI so i got some HTMl and css code from [codersgyan github account](https://github.com/codersgyan/Responsive-restaurant-website)

  ## Technology Used:

  #### Backend

  * Python, Django
  * MySQL
  #### Frontend
  * HTML
  * CSS
  * JAVASCRIPT
  * AJAX
  * JQUERY

  ### Run the following commands to get started your project:

  1. download project

  ```
  git clone https://github.com/dwipalshrirao/food-delivery-ecommerce-website.git

  cd food-delivery-ecommerce-website
  ```

  2. Add your email-id and password to settings.py file which will be useful for sending otp to user's email-id. But make sure that 2 step verification is turned off and Access to less secure apps is turned on of your Gmail account otherwise it will show error while sending OTP.

  ![add email and password](https://github.com/dwipalshrirao/food-delivery-ecommerce-website/blob/main/Screenshot1.png)


  3. run command below

  ```python
  python3 manage.py makemigrations

  python3 manage.py migrate

  python3 manage.py runserver
  ```

  if you are using windows then:
  
  ```python
  python manage.py makemigrations

  python manage.py migrate

  python manage.py runserver
```

  if this is helpful please give star to repo. 
  thank you.


Join me on: 

<!-- display the social media buttons in your README -->

![alt text](https://github.com/dwipalshrirao/food-delivery-ecommerce-website/blob/main/instagram.svg  =100x100  )(http://www.instagram.com/2palshrirao)
[![alt text][2.1]][2]



<!-- links to social media icons -->
<!-- no need to change these -->

<!-- icons with padding -->

[1.1]: https://github.com/dwipalshrirao/food-delivery-ecommerce-website/blob/main/instagram.svg 
[2.1]: https://github.com/dwipalshrirao/food-delivery-ecommerce-website/blob/main/LinkedIn-logo-vector.svg  (Join on linkedin)





<!-- links to your social media accounts -->
<!-- update these accordingly -->

[1]: http://www.instagram.com/2palshrirao
[2]: https://www.linkedin.com/in/dwipal-shrirao/



  
