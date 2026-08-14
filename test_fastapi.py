from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the FastAPI app instance
app = FastAPI(title="Sample API", description="A simple FastAPI project guide")

# 2. Define a Pydantic model for structured data validation
class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# 3. Create a basic GET endpoint (Root URL)
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

# 4. Create a GET endpoint with a Path Parameter and Query Parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, query_string: str | None = None):
    # FastAPI automatically validates that item_id is an integer
    return {"item_id": item_id, "search_query": query_string}

# 5. Create a POST endpoint that validates the request body against our schema
@app.post("/products/")
def create_product(product: Product):
    # The 'product' variable behaves exactly like an instance of the Product class
    discount_price = product.price * 0.9
    return {
        "status": "Product received",
        "product_name": product.name,
        "discounted_price": discount_price
    }

