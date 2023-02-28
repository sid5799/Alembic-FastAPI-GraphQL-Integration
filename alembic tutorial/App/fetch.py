from fastapi import FastAPI
from ariadne import ObjectType, make_executable_schema, QueryType
from ariadne.asgi import GraphQL
from ariadne import  load_schema_from_path
from App.database.database import get_db
from App.frame import School, Teacher
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
print(os.path)
type_defs = load_schema_from_path("GraphQL_Schema/")

query = QueryType()
school = ObjectType("School")
teachers = ObjectType("teachers")


@query.field("school")
async def get_school(root, info):
    db_session = next(get_db())
    try:
        sc = db_session.query(School).all()
    except Exception as e:
        return {"message": e}
    return sc


@query.field("teacher")
async def get_teachers(root, info, school_id: None):
    db_session = next(get_db())
    records = []
    try:

        sc = db_session.query(Teacher).filter_by(school_id=school_id)
        if sc is None:
            db_session.close()
            return {"message": "No record"}
        # for items in sc:
        #     records.extend(School.teachers_relationship)
    except Exception as e:
        db_session.close()
        return {"message": e}
    return sc


@teachers.field("school_id")
async def get_school_from_teachers(root, info):
    db_session = next(get_db())
    try:
        # if root.school_id == Id:
            schools = db_session.query(School).filter_by(id=root.school_id)
            return schools
    except Exception as e:
        return {"message": e}

schema = make_executable_schema(type_defs, query, school, teachers)
graph = GraphQL(schema, debug=True)

app.mount("/", graph)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_methods=['*']
# )

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8010, log_level="debug")

