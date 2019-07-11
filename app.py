from spender import create_app
from werkzeug.serving import run_simple


app = create_app()
app.run()
# run_simple('localhost', 5000, app, use_reloader=True, use_debugger=True)
