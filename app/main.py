from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database.database import Base, engine

from app.models.customer import Customer
from app.models.policy import Policy
from app.models.claim import Claim
from app.models.user import User

from app.routes.customers import router as customer_router
from app.routes.policies import router as policy_router
from app.routes.claims import router as claim_router
from app.routes.auth import router as auth_router


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title="InsureFlow",
    description="Professional Insurance Management Platform",
    version="1.0.0"
)


# Serve CSS, JavaScript and other static files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


# Configure HTML templates
templates = Jinja2Templates(
    directory="app/templates"
)


# Register API routes
app.include_router(customer_router)
app.include_router(policy_router)
app.include_router(claim_router)
app.include_router(auth_router)


# Login page
@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "application": "InsureFlow"
        }
    )


# Registration page
@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={
            "application": "InsureFlow"
        }
    )


# Main dashboard
@app.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "application": "InsureFlow"
        }
    )


# Customers page
@app.get("/customers")
def customers_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="customers.html",
        context={
            "application": "InsureFlow"
        }
    )


# Policies page
@app.get("/policies")
def policies_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="policies.html",
        context={
            "application": "InsureFlow"
        }
    )


# Claims page
@app.get("/claims")
def claims_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="claims.html",
        context={
            "application": "InsureFlow"
        }
    )


# Analytics page
@app.get("/analytics")
def analytics_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="analytics.html",
        context={
            "application": "InsureFlow"
        }
    )


# Settings page
@app.get("/settings")
def settings_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="settings.html",
        context={
            "application": "InsureFlow"
        }
    )


# Application health check
@app.get("/health")
def health():
    return {
        "application": "InsureFlow",
        "status": "UP"
    }