import web_app.py

if __name__ == "__main__":
    app.run()


@app.route('/whereami')
def whereami():
    return 'UK'
