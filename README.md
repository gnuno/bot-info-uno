# BOT Info-UNO

> [!IMPORTANT]  
> Esta es una re escritura del bot en Rust

Pasos a seguir:

En POSIX:
```
curl -L --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/cargo-bins/cargo-binstall/main/install-from-binstall-release.sh | bash
```

en Windows
```
Set-ExecutionPolicy Unrestricted -Scope Process; iex (iwr "https://raw.githubusercontent.com/cargo-bins/cargo-binstall/main/install-from-binstall-release.ps1").Content
```

Agregar tu Token de [@botfather](https://telegram.me/BotFather) en el `Secrets.dev.toml`

Y luego 

```
cargo binstall cargo-shuttle
cargo shuttle run
```



<table><tr><td>

Un BOT de telegram de uso general para los canales de la Universidad Nacional del Oeste.

La finalidad principal del bot es dar información general y básica sobre la universidad, la cursada y el estado de las plataformas.

</td></tr></table>


## Modo de Uso
Los comandos para interactuar desarrollados hasta ahora son:
* `/help`: Muestra los comandos disponibles.
* `/siu`: Obtiene información del siu para saber el estado del mismo y su latencia.
* `/campus`: Obtiene información del campus virtual para saber el estado del mismo y su latencia.
* `/links`: Te devuelve un listado de links utiles sobre la carrera (grupos, comunidades, etc).
* `/calendar`: Te muestra las fechas importantes del calendario académico de la Universidad.
* `/mails`: Te muestra los mails más importantes de las escuelas, además si especificás la escuela te filtra el resultado.


## Desarrollo
### Setup
Te recomendamos el uso de *pipenv*, con este podras tener todas las dependencias necesarias en un entorno virtual.
```
# Instalar PIPENV
pip install pipenv
```

**A partir de aca los comandos deben correr dentro de la carpeta del proyecto**
```
# Crear entorno virtual 
pipenv install

# Agregar dependencias 
pipenv install {PAQUETE}

# Si agregas nuevas dependencias no te olvides de plasmarlas en el .lock
pipenv lock
pipenv run pip freeze > requirements.txt


# Si queres borrar el entorno virtual
pipenv --rm
```

### Entorno de pruebas
Podes probar las nuevas funcionalidades del bot antes de hacer el PullRequest.
Ejecuta esto y anda a [UNOTestBots_BOT](http://t.me/UNOTestBots_BOT)
```
pipenv run bot.py
```
*NOTA: antes de ejecutar debes cargar el token, el cual es 1761269185:AAHLnECJ30OTXKnR5GkOvQaj6d0PNckoPcI*

### Aportes
Para contribuir con el código o arreglando errores/bugs, lo podés hacer de la siguiente manera:

* Crea un `fork` del repositorio en tu perfil
* Crea una nueva `branch` (`git checkout -b nueva-funcionalidad`)
* Agrega el código necesario
* Commitea los cambios
* Hace un `push` de de la branch a tu repositorio remoto (`git push origin nueva-funcionalidad`)
* Desde tu perfil en Github crea un `pull request` 

### Sugerencias / Problemas
Si querés hacer alguna sugerencia o reportar algún problema, podés [abrir un issue](https://github.com/gnuno/bot-info-uno/issues/new) en este mismo repositorio

## [LICENCIA](https://github.com/gnuno/bot-info-uno/blob/main/LICENSE)