# miniForum
Um mini-forum/painel de mensagens com membros, discussões e posts em discussões. Código em Inglês, Front-end PT-BR.

Instalação:

- clone o projeto;
- faça um VirtualEnv com os requirements.txt;
- navegue até "forum" (core-application do projeto);
- faça as migrations necessárias (python manage.py migrate, python manage.py makemigrations e python manage.py migrate novamente);
- rode o servidor: python manage.py runserver

PS: gere uma "SECRET KEY" para o projeto funcionar e inclua em "settings.py". Abra um console Python e:
-import random
-result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])
-print(result)
