from behave import given, when, then


@when("Go to {product_name} details page")
def go_to_product_details_page(context, product_name):
    context.app.acne_products_page.go_to_product_details_page(product_name)

