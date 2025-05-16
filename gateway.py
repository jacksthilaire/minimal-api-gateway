# To run the API gateway: uvicorn gateway:app --port 8000 --reload

from fastapi import FastAPI, Request, Response
import httpx

#BACKEND_URL_3 = "https://backend-service.com"
#BACKEND_URL_2 = "http://localhost:8003"
BACKEND_URL = "http://localhost:8001"  # or wherever your real backend lives

# Start a fastapi app
app = FastAPI()

# Generic proxy route that forwards requests to the backend service and returns the response.
@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
async def proxy_request(request: Request, full_path: str):
    async with httpx.AsyncClient() as client:
        backend_url = f"{BACKEND_URL}/{full_path}"

        # Build proxied request
        proxy_response = await client.request(
            method=request.method,
            url=backend_url,
            headers={key: value for key, value in request.headers.items() if key.lower() != "host"},
            content=await request.body(),
            params=dict(request.query_params),
        )

    # Return raw response from backend
    return Response(
        content=proxy_response.content,
        status_code=proxy_response.status_code,
        headers=dict(proxy_response.headers),
        media_type=proxy_response.headers.get("content-type")
    )




'''
# OBSELETE - Forward to specific services

# Forward /users/* to service_user (port 8001)
@app.get("/users/{user_id}")
async def proxy_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8001/users/{user_id}")
        return response.json()

# Forward /products/* to service_product (port 8002)
@app.get("/products/{product_id}")
async def proxy_product(product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8002/products/{product_id}")
        return response.json()

'''