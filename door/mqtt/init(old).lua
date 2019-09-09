ssid = "adan";
pwd="11223344";

IP = "113.124.144.24";
Port = 1883;
door_p = 2
clientid = wifi.sta.getmac()
SubscribeTopic = "open_the_door"
PublishTopic = "state"

gpio.mode(door_p,gpio.OUTPUT)
gpio.write(door_p,0)
wifi.setmode(wifi.STATIONAP)
wificonfig={}
wificonfig.ssid=ssid
wificonfig.pwd=pwd
wifi.sta.config(wificonfig)
wifi.sta.autoconnect(1)--Á¬½Ówifi


-- init mqtt client with logins, keepalive timer 120sec
m = mqtt.Client("clientid", 120, "user", "password")


m:lwt("/lwt", "offline", 0, 0)

m:on("connect", function(client) print ("connected") end)
m:on("offline", function(client) print ("offline") end)

-- on publish message receive event
m:on("message", function(client, topic, data)
  print(topic .. ":" )
  if data ~= nil then
    print(data)
	if data =="open_the_door" then
        gpio.write("door_p",1)
		print("door_open")
		client:publish("state", "door_open", 0,0)
		gpio.write(door_p,0)
  end
end)


m:connect(IP, port, 0, function(client)
  print("connected")

  client:subscribe("open_the_door", 0, function(client) print("subscribe success") end)

  client:publish("state", "ready", 0, 0, function(client) print("sent") end)
end,
function(client, reason)
  print("failed reason: " .. reason)
end)

tmr.alarm(2, 1000, 1, function()
  client:subscribe("open_the_door", 0, function(client) print("subscribe success") end)
end)