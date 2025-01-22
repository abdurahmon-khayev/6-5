from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, Comment
from django.http import HttpResponse
from django.contrib import messages

# View for product listing
def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context=context)


# View for product detail and placing orders
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        # Process the order
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        quantity = int(request.POST.get('quantity'))
        
        total_price = product.discounted_price * quantity
        order = Order(customer_name=customer_name, customer_phone=customer_phone,
                      product=product, quantity=quantity, total_price=total_price)
        order.save()

        messages.success(request, "Your order has been placed successfully.")
        return redirect('product_detail', pk=product.pk)

    comments = product.comments.all()
    context = {
        'product': product,
        'comments': comments,
    }
    return render(request, 'shop/detail.html', context)


# View for adding a comment to a product
def add_comment(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        author_email = request.POST.get('author_email')
        content = request.POST.get('content')

        comment = Comment(product=product, author_name=author_name, author_email=author_email, content=content)
        comment.save()

        messages.success(request, "Your comment has been posted.")
        return redirect('product_detail', pk=product.pk)

    return HttpResponse("Invalid request method", status=400)
