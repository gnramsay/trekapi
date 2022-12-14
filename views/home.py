"""View for the Home(Root) route."""
import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = fastapi.APIRouter()
templates = Jinja2Templates("templates")


@router.get("/", name="root_path")
def index(request: Request):
    """Define the Root path."""
    return templates.TemplateResponse("home/index.html", {"request": request})
