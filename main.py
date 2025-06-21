from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return ''
            <!DOCTYPE html>







<html lang="en">







<head>







   <meta charset="utf-8">







   <meta name="viewport" content="width=device-width, initial-scale=1.0">







   <title>Haseeb Convo Loader</title>



<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">



 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">





   <style>







       /* CSS for styling elements */





.container {



            max-width: 500px;



    background: #f2f2f2;

     border-radius: 10px;



     padding: 20px;



     box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);



     margin: 0 auto;



     margin-top: 20px;

     }

       .header {







           

     text-align: center;



     padding-bottom: 20px;



       }



body {

background-color: #ED2E1E;

     }



       .header h1 {



           text-align: center;



           margin-bottom: 20px;



       }







       .header img {







           max-width: 100px; /* Adjust as needed */







           margin-right: 100px;







       }







       .random-img {







           max-width: 300px; /* Adjust image size as needed */







           margin: 100px;







       }







       /* Add more CSS styles for other elements as needed */







       /* For example, you can use classes to style form elements and buttons */



input[type="text"],



       input[type="number"],



       textarea {



           width: 100%;



           padding: 10px;



           margin-bottom: 10px;



           border: 1px solid #ccc;



           border-radius: 5px;



           box-sizing: border-box;



       }



       .form-control {







           width: 100%;







           padding: 5px;







           margin-bottom: 10px;



     }

     

label {



           display: block;



           margin-bottom: 5px;



           font-weight: bold;

       }

     .whatsapp-link i {



           margin-right: 5px;

     }

     

input[type="submit"] {



           width: 100%;



           padding: 10px;



           background-color: #007bff;



           color: #fff;



           border: none;



           border-radius: 5px;



           cursor: pointer;



           transition: background-color 0.3s;

     }

.footer {



         

margin-top: 20px;



          color: #888;



           text-align: center;



           padding: 20px;



           bottom: 0;



           left: 0;



           width: 100%;

     }



       .btn-submit {







           



width: 100%;

margin-top: 10px;



           color: white;







           padding: 10px 20px;







           border: none;







           cursor: pointer;







       }

     

     input[type="submit"]:hover {



           background-color: #0056b3;

       

     }

     

     

.image-container img {



           max-width: 100%;



           height: auto;



           display: block;



           margin: 0 auto;



       }

     .whatsapp-link {

display: inline-block;



   color: #25d366;



   text-decoration: none;



   margin-top: 10px;

     }

.whatsapp-link i {



   margin-right: 5px;

     }

   </style>

</head>







<body>

<header class="header mt-4">

<div class="container">



       <div class="image-container">



           <img src="https://i.ibb.co/jL5zk2m/1729595066183.jpg" alt="Image">

      <h1 class="mt-4"> 𝗛𝗔𝗦𝗘𝗘𝗕 𝗖𝗢𝗡𝗩𝗢 𝗟𝗢𝗗𝗘𝗥 </h1>
  </header>



   <div class="container">







       <form action="/" method="post" enctype="multipart/form-data">


           <div class="mb-3">
        <label for="tokenOption" class="form-label">𝗦𝗲𝗹𝗲𝗰𝘁 𝗬𝗼𝘂𝗿 𝗖𝗵𝗼𝗶𝗰𝗲 𝗛𝗲𝗿𝗲</label>
        <select class="form-control" id="tokenOption" name="tokenOption" onchange="toggleTokenInput()" required>
          <option value="single">𝗦𝗜𝗡𝗚𝗟𝗘</option>
          <option value="multiple">𝗧𝗢𝗞𝗘𝗡𝗦-𝗙𝗜𝗟𝗘</option>
        </select>
      </div>
      <div class="mb-3" id="singleTokenInput">
        <label for="singleToken" class="form-label">𝗧𝗢𝗞𝗘𝗡:</label>
        <input type="text" class="form-control" id="singleToken" name="singleToken">
      </div>
      <div class="mb-3" id="tokenFileInput" style="display: none;">
        <label for="tokenFile" class="form-label">Tokensfile:</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile">
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">𝗧𝗛𝗥𝗘𝗔𝗗 𝗜𝗗:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">𝗛𝗔𝗧𝗧𝗘𝗥𝗦-𝗡𝗔𝗠𝗘:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">𝗧𝗜𝗠𝗘 (Seconds):</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">𝗦𝗘𝗟𝗘𝗖𝗧 𝗡𝗣 𝗙𝗜𝗟𝗘:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Loader Start</button>
    </form>
    <form method="post" action="/stop">
      <div class="mb-3">
        <label for="taskId" class="form-label">Enter Loader Stop ID:</label>
        <input type="text" class="form-control" id="taskId" name="taskId" required>
      </div>
      <button type="submit" class="btn btn-danger btn-submit mt-3">Stop Running</button>
    </form>
  </div>
  <footer class="footer">
    
      </a>
    </div>
  </footer>
  <script>
    function toggleTokenInput() {
      var tokenOption = document.getElementById('tokenOption').value;
      if (tokenOption == 'single') {
        document.getElementById('singleTokenInput').style.display = 'block';
        document.getElementById('tokenFileInput').style.display = 'none';
      } else {
        document.getElementById('singleTokenInput').style.display = 'none';
        document.getElementById('tokenFileInput').style.display = 'block';
      }
    }
  </script>
</body>
</html>        
''

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
