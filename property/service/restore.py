from postgres import connect


def execute(request):
    args = request.args
    if len(args) == 0:
        return restore_all_property()
    elif args["id"] is not None:
        return restore_property(args["id"])


def restore_property(id):
    sql = f'SELECT * FROM property WHERE id = {id};'
    header = {
        'Content-Type': 'application/json'
    }
    result = connect(sql=sql, fetch=True)
    if not result:
        return {"message": "Property is not existent."}, 404, header
    try:
        return {"body": result}, 200, header
    except Exception as err:
        raise err


def restore_all_property():
    sql = f'SELECT * FROM property;'
    header = {
        'Content-Type': 'application/json'
    }
    result = connect(sql=sql, fetch=True)
    try:
        return {"body": result}, 200, header
    except Exception as err:
        raise err
