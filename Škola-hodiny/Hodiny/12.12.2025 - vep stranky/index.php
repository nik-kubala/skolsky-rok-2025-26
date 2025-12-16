<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Moja prvá stránka</title>
    
    <style>
        h1 {
            background-color: red;
            color: white;
            border: 10px solid black;
        }
    </style>

    <script>
            
        function logInputValue() {
            var a = parseFloat(document.getElementById('a').value);
            var b = parseFloat(document.getElementById('b').value);
            var c = parseFloat(document.getElementById('c').value);

            var diskriminant = b ** 2 - 4 * a * c;

            if (diskriminant > 0) {
                alert("2 korene");
            }  else if (diskriminant == 0) {
                alert("Nechapem");
            } else if (diskriminant < 0) {
                alert("jeden");
            }
        }

    </script>

    </head>
    <body>
        <!-- <?php for($i=0; $i<1000; $i++): ?>
            <h1>Malý Kiki!</h1>
        <?php endfor; ?> -->

        <h1>Moja prvá stránka</h1>

        <p>Toto je môj prvý odstavec.</p>
        <img 
        src="https://www.w3schools.com/html/pic_trulli.jpg"
        alt="Trulli"
        />

        <form method="get" action="peto.php">
            <p>
                <label for="a">Napíš hodnotu a</label>
                <input type="text" name="a" id="a">
            </p>
            <p>
                <label for="b">Napíš hodnotu b</label>
                <input type="text" name="b" id="b">
            </p>
            <p>
                <label for="c">Napíš hodnotu c</label>
                <input type="text" name="c" id="c">
            </p>
            <p>
                <button onclick="logInputValue()">Klikni ma</button>
            </p>
            <p>
                <input type="Submit" value="Spočítaj to na servery.">
            </p>
        </form>
    </body>
</html>