from ayoomoney import auth
import click


def check_redirect_uri(address: str):
    if not address.startswith("https"):
        print(f"Параметр redirect_url требует использовать https протокол, не http.")
        print(f"Замените: [{address}] на [{address.replace('http', 'https', 1)}]")
        exit(1)


@click.group()
def main():
    pass


@main.command()
@click.argument("client_id")
@click.argument("redirect_url")
@click.option("--scope", default="", help="Список разрешений/scope, по умолчанию включены все разрешения")
def simple(client_id: str, redirect_url: str, scope: str):
    check_redirect_uri(redirect_url)
    auth.simple.authorize(
        client_id,
        redirect_url,
        scope=scope.split(",") if scope else auth.simple.DEFAULT_SCOPE
    )


@main.command()
@click.argument("client_id")
@click.argument("redirect_url")
@click.option("--host", default="127.0.0.1")
@click.option("--port", default=auth.auto.PORT, help="Порт приложения")
@click.option("--scope", default="", help="Список разрешений/scope, по умолчанию включены все разрешения")
@click.option("--cert", default="", help="Путь до сертификата (cert.pem)")
@click.option("--key", default="", help="Путь до ключа (key.pem)")
def auto(client_id: str, redirect_url: str, host: str, port: int, scope: str, cert: str, key: str):
    check_redirect_uri(redirect_url)
    auth.auto.authorize(
        client_id,
        redirect_url,
        host=host,
        port=port,
        scope=scope.split(",") if scope else auth.auto.DEFAULT_SCOPE,
        cert=cert,
        key=key
    )


if __name__ == '__main__':
    main()
