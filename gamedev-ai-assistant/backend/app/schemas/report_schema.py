from pydantic import BaseModel
class ReportView(BaseModel): projectId:str; overallScore:int
