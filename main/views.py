from django.shortcuts import render


def main(request):
    user = request.user
    return render(request, 'main/index.html', {'user': user})

def listing_found(request):
    return render(request, 'listing/listing_found.html')

def listing_not_found(request):
    return render(request, 'listing/listing_not_found.html')