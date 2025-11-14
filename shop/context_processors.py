def cart_count(request):
    """Context processor to make cart count available in all templates"""
    from .models import Cart
    
    cart_item_count = 0
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_item_count = sum(item.quantity for item in cart.items.all())
        except Cart.DoesNotExist:
            pass
    else:
        session_id = request.session.session_key
        if session_id:
            try:
                cart = Cart.objects.get(session_id=session_id)
                cart_item_count = sum(item.quantity for item in cart.items.all())
            except Cart.DoesNotExist:
                pass
    
    return {'cart_item_count': cart_item_count}
