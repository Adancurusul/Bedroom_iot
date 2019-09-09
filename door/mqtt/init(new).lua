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


mqttConnectedFlage = 0;


tmr.alarm(3, 1000, 1, function()
    client:connect(IP, Port,ConnectSuccess,ConnectFailed)
    print("connect......");
end)

function ConnectSuccess(client)
     tmr.stop(3);
     client:subscribe(SubscribeTopic, 0, subscribeSuccess)
     print("connected")
 
     mqttConnectedFlage = 1;
end


function ConnectFailed(client,reason)
   mqttConnectedFlage = 0;
   tmr.start(3)
   print("failed reason: " .. reason)
end

function subscribeSuccess(client)
  print("subscribeSuccess")
end


client:on("message", function(client, topic, message)
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

end)


tmr.alarm(2, 1000, 1, function()
    if mqttConnectedFlage == 1 then
      client:subscribe("open_the_door", 0, function(client) print("subscribe success") end)
    end
end)


