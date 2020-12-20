<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BOOGLE</title>
    <link rel="stylesheet" href="css/bootstrap.css">
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/custom.css">
</head>

<body>
    <div class="content">
        <div class="search-wrapper">
            <a href="" class="search-logo">
                <img src="logo.png">
            </a>
            <div class="search-bar">
                <div class="search-icon">
                    <i class="fa fa-search"></i>
                </div>
                <form action="parse.php" method="get">
                    <input type="text" name="cari" required>
                </form>
            </div>
        </div>
    </div>
    <script src="js/jquery.js"></script>
    <script src="js/bootstrap.js"></script>
</body>

</html>