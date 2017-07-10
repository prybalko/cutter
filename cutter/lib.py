from werkzeug.exceptions import abort


def get_object_or_404(model, pk):
    obj = model.query.get(pk)
    if not obj:
        abort(404)
    return obj
