## food-delivery-ecommerce-website
  this is food delivery website which is near about complete solution for hotel ,in next update i will add dine-in feature to project. 
  Python with Django framework is used in this project. Here are some feature of it:
  1. user can add item to cart without reloading page(javascript is used for this feature). 
  But if user is not logged in then he will redirect to login page.
  2. Register user with email verification. it sends OTP to user's email-id , also it will be expire after 5 minute,
  if user will have not use this OTP. After expiration of OTP, there is OTP re-genration feature,
  which generate OTP and send again to user's email-id.
  3. Blogging system. admin can make crud operation on posts. Any website visitor can see posts.

  in future update I will add some feature like,
  * Dine-in, website visitor can book a table.
  * anonymus user can add items to cart without login.
  
  
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




  
