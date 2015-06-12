from django.shortcuts import render

from zmoc.models import Change
from zmoc.forms import ChangeForm



def zmocindex(request):

    change_list = Change.objects.order_by('uid')
    context_dict = {'changes': change_list}

    return render(request, 'zmoc/mocindex.html', context_dict)

'''
def add_change(request):

    if request.method == 'POST':
        moc_form = ChangeForm(request.POST)

        if moc_form.is_valid():
            moc_form.save(commit=True)

            return zmocindex(request)
        else:
            print moc_form.errors

    else:
        moc_form = ChangeForm()

    return render(request, 'zmoc/add_change.html', {'moc_form': moc_form})
'''