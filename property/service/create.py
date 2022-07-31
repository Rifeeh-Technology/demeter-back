from postgres import connect


def execute(request):
    return create_property(request)


def create_property(request):
    body = request.get_json()
    a = str(body['geomLocalization']).replace('\'', '"')
    name = body['name']
    sql = f"INSERT INTO property (name, geom_localization, create_date) VALUES ('{name}', '{a}', now()) "
    header = {
        'Content-Type': 'application/json'
    }
    try:
        connect(sql)
        return {"mensagem": "OK",
                "body": body}, 200, header
    except Exception as err:
        raise err
