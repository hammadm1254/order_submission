import urllib.request
from urllib.parse import urlencode
import json

json_request = '{"title":"MOs order8","user_id":null,"created_at":"2018-02-10T21:24:18.442Z","scheduled_at":"2018-02-11T16:25:00.000Z","lat":41.9135881,"lng":-87.6775337,"status":0,"id":10637129,"address":"1743 N Damen Ave, Chicago, IL 60647, USA","active_way_point_id":13036065,"started_time":null,"cancelled_at":null,"late":true,"extras":null,"external_id":"10637129","customer_id":5819944,"asap":false,"ended_time":null,"priority":10637129,"distance_traveled":null,"total_price":null,"delivery_price":15.75,"tip":null,"pre_delivery_tip":null,"post_delivery_tip_cash":null,"post_delivery_tip_credit":null,"left_to_be_paid":null,"task_cancellation_reason":null,"dispatcher_id":null,"uuid":"d0365686-88f2-45da-b90f-179877fd7b16","ready_to_execute":true,"discount":null,"tip_driver_enabled":false,"tax_price":null,"price_before_tax":null,"tag_id":"9119","group_uuid":null,"group_leader_id":null,"automatically_cancelled":0,"parent_task_id":null,"payment_method":null,"payment_type_name":null,"linked_task_id":null,"task_notes":[{"title":"09 Feb, 2018 09:24 PM, Andy Sobko","note":"16162","created_at":"2018-02-09T21:24:18.423Z","author_name":"Andy Sobko","id":11933317,"way_point_id":13036065,"url":null,"type":"TaskNote","user_id":83751,"lat":null,"lng":null}],"way_points":[{"id":13036065,"scheduled_at":"2018-02-10T16:25:00.000Z","has_to_leave_by":null,"task_id":10637129,"customer_id":5819944,"done":false,"lat":41.9135881,"lng":-87.6775337,"address":"1743 N Damen Ave, Chicago, IL 60647, USA","address_second_line":null,"zipcode":null,"position":1,"checkin_time":null,"checkout_time":null,"note":null,"find_me":null,"asap":false,"late":true,"etl":"2018-02-10T16:30:00.000Z","eta":null,"silent":false,"city":null,"borough":null,"full_address":"1743 N Damen Ave, Chicago, IL 60647, USA","automatic_checkin":false,"automatic_checkout":false,"phone":"+17735432205","email":"seankoke@gmail.com","no_later_than":null,"no_earlier_than":null,"rating":null,"checkin_lat":null,"checkin_lng":null,"checkout_lat":null,"checkout_lng":null,"district":null,"house_number":null,"company_name":null,"customer":{"id":5819944,"name":"Jack","address":"1743 N Damen Ave, Chicago, IL 60647, USA","address_second_line":null,"zipcode":null,"lat":41.9135881,"lng":-87.6775337,"phone":"+17735432205","image":"/images/avatar.png","email":"seankoke@gmail.com","merchant_id":11402,"external_id":"5819944","confirmation_code":"8781","client_version":null,"client_name":null,"mobile_type":0,"allow_login":false,"extras":null,"city":null,"borough":null,"state":null,"street":null,"business_code":null,"language":null,"customer_notes":[]}}],"shared_locations":[],"team_ids":[],"task_inventories":[],"scans":[]}'