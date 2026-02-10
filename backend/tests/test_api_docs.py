import pytest
from fastapi.testclient import TestClient
import re

def get_api_get_routes(client: TestClient):
    """
    Obtiene el esquema OpenAPI y extrae todas las rutas GET.
    """
    try:
        response = client.get("/openapi.json")
        response.raise_for_status()
        schema = response.json()
    except Exception as e:
        pytest.fail(f"No se pudo obtener o parsear /openapi.json: {e}")

    get_routes = [path for path, methods in schema.get("paths", {}).items() if "get" in methods]
    
    if not get_routes:
        pytest.fail("No se encontraron rutas GET en /openapi.json para probar.")

    return get_routes

def test_dynamic_get_routes_do_not_fail(client: TestClient):
    """
    Prueba cada ruta GET declarada en openapi.json para asegurarse de que no devuelve un error 5xx.
    Usa la fixture 'client' que asegura que la base de datos de prueba está configurada.
    """
    api_routes = get_api_get_routes(client)
    
    for path in api_routes:
        # Reemplaza parámetros de ruta como {param} con un valor de muestra.
        test_path = re.sub(r"\{.*?\}", "1", path)
        
        response = client.get(test_path)
        
        assert response.status_code < 500, f"Error del servidor (5xx) en la ruta GET: {test_path}"

def test_docs_ui_is_available(client: TestClient):
    """
    Verifica que la UI de la documentación (Swagger UI) esté disponible.
    """
    response = client.get("/docs")
    assert response.status_code == 200
    assert "SwaggerUIBundle" in response.text, "La respuesta de /docs no parece contener Swagger UI."