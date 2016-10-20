from django.shortcuts import render


def default_view(request):
    # Return the React view
    context = {}
    return render(request, 'react_loader.html', context)
