from bson import ObjectId
from fastapi import HTTPException
def oid(value):
    if not ObjectId.is_valid(value): raise HTTPException(400,"Identificador inválido")
    return ObjectId(value)
def serialize(value):
    if isinstance(value,ObjectId): return str(value)
    if isinstance(value,list): return [serialize(x) for x in value]
    if isinstance(value,dict): return {k:serialize(v) for k,v in value.items()}
    return value
