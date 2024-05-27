from datetime import datetime
from flask_restful import Resource, abort, fields, marshal, reqparse, marshal_with
from flask import g, request
from apps.todo.models import Todo


task_post = reqparse.RequestParser()
task_post.add_argument('title', type=str, required=True)
task_post.add_argument('description', type=str, required=True)
get_resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime,
        }



class TodoResource(Resource):

    @marshal_with(get_resource_fields)
    def get(self, todo_id=None):
        if todo_id:
            todo = Todo.query.get(todo_id)
            return todo
        todo_list = Todo.query.all()
        return todo_list

    @marshal_with(get_resource_fields)
    def post(self):
        todo_request = task_post.parse_args()

        try:
            todo = Todo(
                title=todo_request['title'],
                description=todo_request['description'],
                created_at=datetime.now()
                )
            todo.save_to_db()
        except Exception as e:
            abort(400)

        return todo, 201


    @marshal_with(get_resource_fields)
    def put(self, todo_id=None):
        if not todo_id:
            return abort(404)

        todo = Todo.query.get(todo_id)

        if not todo:
            abort(404)

        todo_request = task_post.parse_args()
        try:
            todo.id = todo_id
            todo.title = todo_request['title']
            todo.description = todo_request['description']
            todo.created_at = todo.created_at
            todo.updated_at = datetime.now()
            todo.save_to_db()
        except:
            abort(400)

        return todo, 201

    def delete(self, todo_id=None):
        if not todo_id:
            return abort(404)

        todo = Todo.query.get(todo_id)

        if not todo:
            abort(404)

        todo.delete_from_db()

        return {"message": f"task id - {todo_id} deleted"}