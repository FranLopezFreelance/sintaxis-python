# CREAR UN ARCHIVO setup.py con este código:
    # from setuptools import setup

    # setup(
    #     name="modulos",
    #     version="1.0.0",
    #     description="Prueba de Módulos",
    #     author="FJL",
    #     author_email="franlopez.freelance@gmail.com",
    #     packages=["modulos", "modulos.sub_modulos"]
    # )
# CORRER EL COMANDO: python setup.py sdist
# CORRER EL COMANDO pip3 install nombre_del_archivo.tar.gz para instalar el paquete 
#   (parado en su carpeta, o haciendo referencia a la rut correcta)
# CORRER EL COMANDO pip3 uninstall nombre_del_archivo para desintalar