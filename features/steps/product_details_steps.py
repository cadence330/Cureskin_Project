from behave import given, when, then


@then("Add {product_name} to cart and verify")
def add_to_cart_and_verify(context, product_name):
    context.app.product_details_page.add_to_cart_and_verify(product_name)


@when("Go to cart page")
def go_to_cart(context):
    context.app.product_details_page.go_to_cart()
