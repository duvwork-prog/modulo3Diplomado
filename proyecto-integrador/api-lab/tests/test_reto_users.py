

from sqlite3 import Date
from sqlite3 import Date
import time

# Contrato del recurso post: campo -> tipo esperado
CONTRATO_USERS = {"id": int, "name": str, "username": str, "email": str}


def cumple_contrato(recurso: dict, contrato: dict) -> bool:
    """Valida presencia y tipo de cada campo (el JSON Schema de la S3, versión KISS)."""
    return all(
        campo in recurso and isinstance(recurso[campo], tipo)
        for campo, tipo in contrato.items()
    )


def test_listar_gets_users_devuelve_10(api):
    respuesta = api.get("/users")

    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 10


def test_detalle_cumple_el_contrato(api):
    respuesta = api.get("/users/1")

    assert respuesta.status_code == 200
    assert cumple_contrato(respuesta.json(), CONTRATO_USERS)


def test_crear_users_devuelve_201_y_eco_del_payload(api):
    # Título único por corrida — igual que el pre-request script de Postman
    name = f"Users QA {time.time_ns()}"
    payload = {"name": name, "username": "USUARIO", "email": "user@mail.com"}

    respuesta = api.post("/users", json=payload)

    assert respuesta.status_code == 201
    creado = respuesta.json()
    assert isinstance(creado["id"], int)
    assert creado["name"] == name


def test_actualizar_users_con_put(api):
    payload = { "id": 1, "name": "Duvier Martinez", "username": "Duvwork", "email": "Duvwork@april.biz", "address": { "street": "Avenue Light", "suite": "Apt. 557", "city": "Brisbourne", "zipcode": "5598-3874", "geo": { "lat": "-37.3159", "lng": "81.1496" } }, "phone": "1-770-736-8031 x56442", "website": "hildegard.org", "company": { "name": "Romaguera-Crona", "catchPhrase": "Multi-layered client-server neural-net", "bs": "harness real-time e-markets" }}
    respuesta = api.put("/users/1", json=payload)

    assert respuesta.status_code == 200
    assert respuesta.json()["name"] == payload["name"]
    assert respuesta.json()["username"] == payload["username"]
    assert respuesta.json()["email"] == payload["email"]
    assert respuesta.json()["address"]["street"] == payload["address"]["street"]
    assert respuesta.json()["address"]["suite"] == payload["address"]["suite"]
    assert respuesta.json()["address"]["city"] == payload["address"]["city"]


def test_eliminar_user_devuelve_200_y_body_vacio(api):
    respuesta = api.delete("/users/1")

    assert respuesta.status_code == 200
    assert respuesta.json() == {}


def test_users_inexistente_devuelve_404(api):
    respuesta = api.get("/users/999999")

    assert respuesta.status_code == 404
