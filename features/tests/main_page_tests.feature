Feature: Verify Product Page


 Scenario: User can see product details on product page
   Given Open main page
   When Go to acne products page
   And Go to Sensitive Pro Cleanser details page
   Then Add Sensitive Pro Cleanser to cart and verify
   When Go to cart page
   Then Verify user is taken to the cart page

 Scenario:
   Given
   When
   Then
