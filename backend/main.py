from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import customers, templates, campaigns

# Create FastAPI App
app = FastAPI(
    title="Pasha CRM API",
    description="CRM system for managing customers and marketing campaigns for Pasha BBQ",
    version="1.0.0")


# Configure CORS (allows React to call your API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all Routers
app.include_router(customers.router, prefix="/api", tags=["customers"])
app.include_router(templates.router, prefix="/api", tags=["customers"])
app.include_router(campaigns.router, prefix="/api", tags=["customers"])


@app.get("/")
def root():
    return {
        "message": "Resturant CRM API",
        "status": "Running",
        "docs": "/docs"
    }

# Health Check Endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }