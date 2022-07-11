from postgres import restore


def get_property(request):
    sql = f'SELECT id, name, geom_localization, create_date FROM property'
    return restore(sql)
