<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test PHP Page</title>
</head>
<body>
    <h1>Welcome to the Test PHP Page</h1>
    <p>This is a simple PHP page to demonstrate basic PHP usage.</p>

    <?php
    // PHP code starts here
    $name = "John";
    $age = 30;
    $city = "New York";

    // Outputting variables using echo
    echo "<p>Name: $name</p>";
    echo "<p>Age: $age</p>";
    echo "<p>City: $city</p>";

    // Simple conditional statement
    if ($age >= 18) {
        echo "<p>$name is an adult.</p>";
    } else {
        echo "<p>$name is a minor.</p>";
    }

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
