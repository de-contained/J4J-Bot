import flask, threading, requests
import os

app = flask.Flask(__name__)
app

if True:
   @app.route('/')
   def home():
       return """
       <html>
           <style>
               center {
                        font-family: monospace;
                        font-style: monospace;
               }
           </style>
           <head>
               <title>Bongo Host</title>
           </head>
           <center>
                <h1>bongo#4444</h1>
                <p>add me on discord</p>
           </center>
       </html>
       """

class host:
      def run():
          threading.Thread(
                    target = app.run,
                    args   = (
                           '0.0.0.0',
                            8080
                    )
          ).start()
