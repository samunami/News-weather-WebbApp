from flask import Flask, render_template
from webApp.news import get_html, get_python_news
from webApp.weather import weather_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
  
    @app.route("/")
    def index():
        title = "Новостной портал"
        weather = weather_city(app.config["WEATHER_DEFAULT_CITY"])
        
        html_content = get_html("https://www.python.org/blogs/")
        news_list = get_python_news(html_content)
        
        return render_template("index.html", page_title=title, weather=weather, news=news_list)
    return app



