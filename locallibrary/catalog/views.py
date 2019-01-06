from django.shortcuts import render

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
#@login_required
#def home(request):
#    return render(request, '/home.html')

#@login_required
#def settings(request):
#    user = request.user

#    try:
#        facebook_login = user.social_auth.get(provider='facebook')
#    except UserSocialAuth.DoesNotExist:
#        facebook_login = None

#    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

#    return render(request, 'djauthapp/settings.html', {
        

#        'facebook_login': facebook_login,
#        'can_disconnect': can_disconnect
#    })

#@login_required
#def password(request):
#    if request.user.has_usable_password():
#        PasswordForm = PasswordChangeForm
#    else:
#        PasswordForm = AdminPasswordChangeForm

#    if request.method == 'POST':
#        form = PasswordForm(request.user, request.POST)
#        if form.is_valid():
#            form.save()
#            update_session_auth_hash(request, form.user)
#            messages.success(request, 'Your password was successfully updated!')
#            return redirect('password')
#        else:
#            messages.error(request, 'Please correct the error below.')
#    else:
#        form = PasswordForm(request.user)
