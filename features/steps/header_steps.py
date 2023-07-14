from behave import given, when, then


@when('Go to acne products page')
def go_to_acne_products(context):
    context.app.header.go_to_acne_products()
