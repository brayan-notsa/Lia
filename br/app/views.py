from django.shortcuts import render


def compter(request):

    if request.method == 'POST':

        text = request.POST['texttocount']

        if text != '':

            word = len(text.split())

            i =True

            return render(request, 'compter.html',
                          {'word':word, 'text': text, 'i': i, 'on':'active'}
                          )
        else:
            return render(request, 'compter.html', {'on':'active'})
    
    else: 
        return render(request, 'compter.html', {'on':'active'})