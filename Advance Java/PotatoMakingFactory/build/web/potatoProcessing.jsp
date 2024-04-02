<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Potato Processing System</title>
</head>
<body>
    <h1>Potato Processing System</h1>
    <p>Status:</p>
    <ul>
        <li>Peeling: <span><%= getServletContext().getAttribute("peelingStatus") %></span></li>
        <li>Chip Cutting: <span><%= getServletContext().getAttribute("chipcuttingStatus") %></span></li>
        <li>Frying: <span><%= getServletContext().getAttribute("fryingStatus") %></span></li>
        <li>Packing: <span><%= getServletContext().getAttribute("packingStatus") %></span></li>
    </ul>
</body>
</html>
