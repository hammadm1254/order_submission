$(document).ready(function(){
    $("#submit_order").click(function(){
        var url = "https://admin-api.bringg.com/services/6f15901b/218a1520-656d-41d8-97b9-97ab36f944ed/dcc0d077-78b7-4178-a43d-297efe24574a/"
        var data = { "title": 1518389415689, "external_id": "ABC15D", "scheduled_at": "Sun Feb 11 2018 16:50:15 GMT-0600 (Central Standard Time)", "customer": { "name": "Mr. Customer", "address": "1900 Wall st, New York, NY", "phone": "0545454545", "allow_sending_sms": true, "allow_sending_email": false }, "way_points": [ { "customer": { "name": "restaurant", "phone": "0123456789", "allow_sending_sms": true, "allow_sending_email": false }, "scheduled_at": "Sun Feb 11 2018 16:50:15 GMT-0600 (Central Standard Time)", "address": "233 S Wacker Dr, Chicago, IL 60606, USA", "city": "New York" }, { "customer": { "name": "Mr. Customer", "phone": "05456974815", "allow_sending_sms": true, "allow_sending_email": false }, "scheduled_at": "Sun Feb 11 2018 16:50:15 GMT-0600 (Central Standard Time)", "address": "8400 W 31st St, Brookfield, IL 60513, USA", "delivery_confirmation_signature": "2", "note": "come to 4th floor and hand to receptionist", "inventory": [] } ], "teams": [] }

        data["title"] = Date.now();
        //data["customer"]["name"] = "Customer"+Date.now()
        //data["customer"]["address"] = "1743 N Damen Avenue, Chicago IL, 60647"
        data["way_points"][0]["address"] = $("#origin").text()
        data["way_points"][1]["address"] = $("#destination").text()
        data["delivery_price"] = $("#cost").text()
        data["scheduled_at"] = Date(Date.now())
        data["way_points"][0]["scheduled_at"]  = Date(Date.now())
        data["way_points"][1]["scheduled_at"]  = Date(Date.now())
        data["way_points"][1]["note"] = $("#instructions").text()
        //data["distance_traveled"] = $("#cost").text()+" miles"
        //data["customer_id"] =

        stringyData = JSON.stringify(data, null, 4)


        xhr = new XMLHttpRequest();
        xhr.open('POST', url, true);
        xhr.setRequestHeader("Content-type", "application/json");
        xhr.send(stringyData);


        /*
        xhr.onreadystatechange = function () {
            if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200){
                var json_response = JSON.parse(xhr.responseText);
                console.log(json_response);
            }
        }
        xhr.send(stringyData);
        */


        console.log(xhr.responseText)
        //console.log(stringyData)
        alert("Order Submitted")
        document.location.href = "/";
    });
});