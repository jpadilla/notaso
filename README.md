# Notaso

Conoce tus profesores antes de llegar al salon.

## Idea

En Puerto Rico hay miles de estudiantes que desean coger sus clases con los profesores que mejor las de. Nos dimos cuenta que no habia una plataforma la cual podias ver la reputacion de un profesor antes de coger la clase. Por lo tanto, desarollamos [Notaso](http://www.notaso.com)

## Reportar errores, sugerencias y otros comentarios

Si tienes una idea de como mejorar esta plataforma o si has encontrado algún error déjanos saber creando un "issue" en el repositorio.

[Issues](https://github.com/SoPR/horas/issues) - para reportar problemas, errores, sugerencias, etc.

### Cómo usar "issues" en GitHub

Aquí un [vídeo](http://www.youtube.com/watch?v=TJlYiMp8FuY) que explica como crear "issues". Recuerda que primero necesitas [crear una cuenta de GitHub](https://github.com/join), es gratis.

## Developers

Este proyecto no sería posible sin la colaboración de otros developers que han donado su tiempo para crear esta aplicación. Si  encuentras un error por favor crea un [issue](https://github.com/jpadilla/notaso/issues) y si puedes arreglarlo te invitamos a hacer y someter un pull request.

### Para correr el proyecto

Debes tener instalado **Python 2.7** en tu máquina. También es recomendado que crees un [virtualenv](http://www.virtualenv.org/) para el proyecto pero no es un requisito.

```bash
$ git clone https://github.com/jpadilla/notaso.git
$ cp .env.example .env
$ pip install -r requirements.txt
$ python manage.py syncdb --migrate
$ python manage.py runserver
```

Abre tu browser en [http://localhost:8000/](http://localhost:8000/). 

Para accesar la sección de administración debes de crear un super usuario.

```bash
$ python manage.py createsuperuser
$ python manage.py runserver
```

Luego ve a [http://localhost:8000/admin/](http://localhost:8000/admin/).

## License

All of "Notaso" is licensed under the MIT license.

Copyright (c) 2010-2014 José Padilla

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Donaciones

100% de las donaciones hechas irán a pagar los gastos de hosting y mantenimiento de la plataforma que en este momento son **$20.00 USD mensual**. Pronosticamos que en poco tiempo este número debe subir así que por eso estamos apuntando a asegurar $40.00 mensual. La idea es que la comunidad que se beneficia del proyecto pueda financiar los gastos recurrentes.

[![Support via Gittip](https://rawgithub.com/twolfson/gittip-badge/0.2.0/dist/gittip.png)](https://www.gittip.com/jpadilla/)

[![Donate Bitcoins](http://i.imgur.com/bMKkFH4.png)](https://coinbase.com/checkouts/171d3ea1bc0e16c33a095dc44b0e15c9)

