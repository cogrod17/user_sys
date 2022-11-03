from fastapi import APIRouter, File, UploadFile


router = APIRouter()


@router.post('/upload')
def upload_avatar(file: UploadFile = File(descirption='this is my file')):
    return {'file': file}
