import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from react.render import render_component


# Create your views here.
@login_required
def home(request):
    # return render(request, 'registration_system/index.html')
    rendered = render_component(
        os.path.join(os.getcwd(), 'registration_system', 'static', 'js', 'Test.jsx'),
        {
            'test': 'full test',
        },
        to_static_markup=False,
    )

    print(rendered)
    return render(request, 'registration_system/index.html', {'rendered': rendered})
