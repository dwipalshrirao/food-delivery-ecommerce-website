## Food-delivery-ecommerce-website
  This is food delivery website which is near about complete solution for **Restautent**. 
  Python with Django framework is used in this project.

  ### Project look:
  ![website look](https://github.com/dwipalshrirao/food-delivery-ecommerce-website/blob/master/website_look.gif)

  ### Features of project:

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
  ##### Run the following commands to get started your project:

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




  
