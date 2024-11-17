from django.shortcuts import render


def main(request):
    user = request.user
    return render(request, 'main/index.html', {'user': user})
