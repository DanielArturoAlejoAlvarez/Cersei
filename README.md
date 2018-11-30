# Cersei
## Description

This repository is a Software of Application REST API with Python.

## Installation
Using Django 2.0 preferably.

## Apps
Using Postman, RestEasy preferably.

## Usage
```html
$ git clone https://github.com/DanielArturoAlejoAlvarez/Cersei.git [NAME APP] 

$ npm start
```
Follow the following steps and you're good to go! Important:


![alt text](https://media.giphy.com/media/xTiTnu2pGg9hz5stUI/giphy.gif)


## Coding

### Model 

```python
...
class Code(models.Model):
    language=models.CharField(max_length=100)
    paradigm=models.CharField(max_length=100)
    designer=models.CharField(max_length=50)
    first_appeared = models.DateField("Date", default=datetime.date.today)

    def __str__(self):
        return '%s %s' % (self.language, '('+self.designer+')')
...
```

### Urls

```python
...
from rest_framework import routers

router=routers.DefaultRouter()
router.register('codes', views.CodeView)

urlpatterns = [
    path('', include(router.urls))
]
...
```

### Views

```python
...
from rest_framework import viewsets
from .models import Code
from .serializers import CodeSerializer

class CodeView(viewsets.ModelViewSet):
    queryset=Code.objects.all()
    serializer_class=CodeSerializer
...
```

### Serializer

```python
...
from rest_framework import serializers 
from .models import Code

class CodeSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    class Meta:
        model=Code
        fields=('url','language','paradigm','designer','first_appeared')
...
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/DanielArturoAlejoAlvarez/Cersei. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).