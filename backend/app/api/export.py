import csv
import io

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.database.models.user import User
from app.dependencies.services import get_export_service
from app.services.export import ExportService
from app.utils.security import require_admin

router = APIRouter(
    prefix="/export",
    tags=["Export"],
)


@router.get("/csv")
def export_csv(
    service: ExportService = Depends(get_export_service),
    current_user: User = Depends(require_admin),
):

    mappings = service.export_mappings()

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(["md5", "olid"])

    for md5, olid in mappings:
        writer.writerow([md5, olid])

    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": 'attachment; filename="mond_export.csv"'
        },
    )