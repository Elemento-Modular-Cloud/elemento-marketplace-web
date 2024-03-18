<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test PHP Page</title>
</head>
<body>
    <h1>Welcome to the Cloud fest 2024!</h1>
    <h3>Ready.Set.Cloud.</h3>

    <?php
    // Output phpinfo
    echo "<h2>PHP Info</h2>";
    phpinfo();

    // Output $_SERVER information
    echo "<h2>Server Information</h2>";
    echo "<pre>";
    print_r($_SERVER);
    echo "</pre>";
    ?>

</body>
</html>
